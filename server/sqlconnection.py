import sqlite3

from classes.members.person import Person
from classes.members.roles import Role


class Connection:

    __slots__ = ('db', 'cur')

    def __init__(self) -> None:
        self.db = sqlite3.connect('test.db')
        print('Connection made!')

    def close(self) -> None:
        self.db.close()


class ReadWriteDB:

    def __init__(self, database: Connection) -> None:
        self.database = database

    def write(self, member: Person) -> None:
        '''Writes First Name, Last Name and Role in Workers Table'''
        cur = self.database.db.cursor()
        cur.execute(
            "INSERT INTO Workers VALUES (?, ?, ?, ?)",
            (member.get_first_name(), member.get_last_name(),
             member.get_company_role().name, member.get_years_of_service()))
        self.database.db.commit()

    def return_members(self) -> list[Person]:
        cur = self.database.db.cursor()
        person_list = [
            Person(item[0], item[1], Role.__dict__[item[2]], item[3])
            for item in cur.execute('SELECT * FROM Workers')
        ]
        return person_list
