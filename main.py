import tkinter as tk
from server.sqlconnection import Connection
from classes.members.person import Person
from classes.members.roles import Role

root = tk.Tk()
root.title('Company members')

frame1 = tk.LabelFrame(root)
frame1.grid(row=0, column=0)
frame2 = tk.LabelFrame(root)
frame2.grid(row=1, column=0)

sql = None


def make_connection():
    global sql
    sql = Connection()
    server_write_button.config(state='active')
    server_close_button.config(state='active')


def close_connection():
    global sql
    sql.close()
    server_write_button.config(state='disabled')
    server_close_button.config(state='disabled')


def write_person(last_name, first_name, role):

    #check if the string is empty
    if last_name.strip() == '':
        return
    if first_name.strip() == '':
        return
    if role not in Role.__dict__:
        return

    global sql
    temp = Person(Role.__dict__[role], last_name, first_name)
    print(temp)
    sql.write(temp)


last_name_label = tk.Label(frame1, text='Last Name', font=('', 10))
first_name_label = tk.Label(frame1, text='First Name', font=('', 10))
last_name_entry = tk.Entry(frame1, font=('', 10))
first_name_entry = tk.Entry(frame1, font=('', 10))

clicked = tk.StringVar()
clicked.set('Select Role')
roles_list = {role.name: role.value for role in Role}

role_label = tk.Label(frame1, text='Role', font=('', 10))
role_menu = tk.OptionMenu(frame1, clicked, *roles_list)

server_connect_button = tk.Button(frame2,
                                  text='Connect',
                                  command=lambda: make_connection(),
                                  padx=10,
                                  pady=10)

server_write_button = tk.Button(
    frame2,
    text='Write',
    command=lambda: write_person(last_name_entry.get(), first_name_entry.get(),
                                 clicked.get()),
    padx=10,
    pady=10,
    state='disabled')

server_close_button = tk.Button(frame2,
                                text='Close',
                                command=lambda: close_connection(),
                                padx=10,
                                pady=10,
                                state='disabled')

last_name_label.grid(row=0, column=0)
first_name_label.grid(row=0, column=1)
last_name_entry.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
role_label.grid(row=0, column=2)
role_menu.grid(row=1, column=2)

server_connect_button.grid(row=0, column=0)
server_write_button.grid(row=0, column=1)
server_close_button.grid(row=0, column=2)

tk.mainloop()