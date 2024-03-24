from enum import Enum

class UserStatus(Enum):
    INIT = "INIT"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class UserCartStatus(Enum):
    INIT = "INIT"
    IN_PROGRESS = "IN_PROGRESS"
    PAID = "PAID"

class ContractStatus(Enum):
    INIT = "INIT"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
