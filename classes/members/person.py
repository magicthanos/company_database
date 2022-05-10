from dataclasses import dataclass, field
from classes.members.roles import Role


@dataclass(order=True, slots=True)
class Person:

    sort_index: int = field(init=False, repr=False)
    company_role: Role

    last_name: str
    first_name: str
    _full_name: str = field(init=False)

    def __post_init__(self) -> None:
        self.sort_index = self.company_role.value
        self._full_name = f'{self.last_name} {self.first_name}'

    def __repr__(self) -> str:
        return f'(Full name: {self._full_name}, Role: {self.company_role.name})'