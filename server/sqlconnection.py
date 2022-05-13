import sqlite3

from classes.members.person import Person


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
            "INSERT INTO Workers VALUES (?, ?, ?)",
            (member.first_name, member.last_name, member.company_role.name))
        self.database.db.commit()
