from enum import Enum, auto


class Role(Enum):
    MANAGER = auto()
    WORKER = auto()