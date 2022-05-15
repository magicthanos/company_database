from dataclasses import dataclass, field

from classes.members.roles import Role


@dataclass(slots=True)
class Salary:
    _salary: float
    _bonus: float
    _full_salary: float = field(init=False)

    def __post_init__(self):
        self._full_salary = self._salary + self._bonus

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_bonus(self):
        return self._bonus

    def set_bonus(self, bonus):
        self._bonus = bonus

    def get_full_salary(self):
        return self._full_salary


@dataclass(order=True, slots=True)
class Person:

    _sort_index: int = field(init=False, repr=False)

    _first_name: str
    _last_name: str
    _company_role: Role
    _years_of_service: int

    _salary: Salary = field(init=False)
    _full_name: str = field(init=False)

    def __post_init__(self) -> None:
        self._sort_index = self._company_role.value
        self._full_name = f'{self._last_name} {self._first_name}'
        self._salary = Salary(_salary=self._years_of_service * 1000,
                              _bonus=self._years_of_service * 100)

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str) -> None:
        self._first_name = first_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def get_company_role(self) -> Role:
        return self._company_role

    def set_company_role(self, company_role: Role) -> None:
        self._company_role = company_role

    def get_years_of_service(self) -> int:
        return self._years_of_service

    def set_years_of_service(self, years_of_service: int) -> None:
        self._years_of_service = years_of_service

    def get_salary(self) -> Salary:
        return self._salary

    def get_full_name(self) -> str:
        return self._full_name