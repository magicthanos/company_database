from dataclasses import dataclass, field

from classes.members.roles import Role


@dataclass(slots=True)
class Salary:
    salary: float
    bonus: float
    full_salary: float = field(init=False)

    def __post_init__(self):
        self.full_salary = self.salary + self.bonus


@dataclass(order=True, slots=True)
class Person:

    sort_index: int = field(init=False, repr=False)

    first_name: str
    last_name: str
    company_role: Role
    years_of_service: int

    salary: Salary = field(init=False)
    _full_name: str = field(init=False)

    def __post_init__(self) -> None:
        self.sort_index = self.company_role.value
        self._full_name = f'{self.last_name} {self.first_name}'
        self.salary = Salary(salary=self.years_of_service * 1000,
                             bonus=self.years_of_service * 100)
