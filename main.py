import tkinter as tk

from classes.members.person import Person
from classes.members.roles import Role
from server.sqlconnection import Connection, ReadWriteDB

root = tk.Tk()
root.title('Company members')

frame1 = tk.LabelFrame(root)
frame1.grid(row=0, column=0)
frame2 = tk.LabelFrame(root)
frame2.grid(row=1, column=0)
frame3 = tk.LabelFrame(root)
frame3.grid(row=2, column=0)
frame4 = tk.LabelFrame(root)
frame4.grid(row=3, column=0)


def make_connection() -> None:
    global sql
    sql = Connection()
    server_write_button.config(state='active')
    server_close_button.config(state='active')
    server_connect_button.config(state='disabled')
    read_members_button.config(state='active')
    display_member_info_button.config(state='active')


def close_connection() -> None:
    global sql
    sql.close()
    server_write_button.config(state='disabled')
    server_close_button.config(state='disabled')
    server_connect_button.config(state='active')
    read_members_button.config(state='disabled')
    display_member_info_button.config(state='disabled')


def write_person(role: str, last_name: str, first_name: str,
                 years_of_service: str) -> None:

    #check if the string is empty
    if is_empty_string(last_name):
        return
    if is_empty_string(first_name):
        return
    if is_empty_string(years_of_service) or not years_of_service.isdigit():
        return
    if role not in Role.__dict__:
        return

    global sql
    temp_person = Person(first_name, last_name, Role.__dict__[role],
                         int(years_of_service))
    print(temp_person)
    temp_writer = ReadWriteDB(sql)
    temp_writer.write(temp_person)


def is_empty_string(string: str) -> bool:
    return string.strip() == ''


def get_company_members() -> list[Person]:
    temp_reader = ReadWriteDB(sql)
    return temp_reader.return_members()


def display_members(listbox: tk.Listbox):
    listbox.delete(0, 'end')
    for key, item in enumerate(get_company_members()):
        listbox.insert(
            key, f'{item.get_full_name()} {item.get_company_role().name}')
    print(get_company_members())


def show_member_info(members_listbox: tk.Listbox):
    try:
        index = members_listbox.curselection()[0]
        print(get_company_members()[index])
    except:
        pass


first_name_label = tk.Label(frame1, text='First Name', font=('', 10))
first_name_entry = tk.Entry(frame1, font=('', 10))

last_name_label = tk.Label(frame1, text='Last Name', font=('', 10))
last_name_entry = tk.Entry(frame1, font=('', 10))

years_of_service_label = tk.Label(frame1,
                                  text='Years of Service',
                                  font=('', 10))
years_of_service_entry = tk.Entry(frame1, font=('', 10))

clicked = tk.StringVar()
clicked.set('Select Role')
roles_list = {role.name for role in Role}

role_label = tk.Label(frame1, text='Role', font=('', 10))
role_menu = tk.OptionMenu(frame1, clicked, *(roles_list))

company_members = tk.Listbox(frame3, selectmode='SINGLE', width=50, height=10)

read_members_button = tk.Button(
    frame4,
    text='Read',
    command=lambda: display_members(company_members),
    state='disabled')
display_member_info_button = tk.Button(
    frame4,
    text='Display',
    state='disabled',
    command=lambda: show_member_info(company_members))
server_connect_button = tk.Button(
    frame2,
    text='Connect',
    command=lambda: make_connection(),
    padx=10,
    pady=10,
)

server_write_button = tk.Button(
    frame2,
    text='Write',
    command=lambda: write_person(clicked.get(), last_name_entry.get(
    ), first_name_entry.get(), years_of_service_entry.get()),
    padx=10,
    pady=10,
    state='disabled')

server_close_button = tk.Button(frame2,
                                text='Close',
                                command=lambda: close_connection(),
                                padx=10,
                                pady=10,
                                state='disabled')

#griding
first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=1, column=0)

last_name_label.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)

years_of_service_label.grid(row=0, column=2)
years_of_service_entry.grid(row=1, column=2)

role_label.grid(row=0, column=3)
role_menu.grid(row=1, column=3)

server_connect_button.grid(row=0, column=0)
server_write_button.grid(row=0, column=1)
server_close_button.grid(row=0, column=2)

company_members.grid(row=0, column=0)
read_members_button.grid(row=1, column=0)
display_member_info_button.grid(row=1, column=1)

tk.mainloop()
