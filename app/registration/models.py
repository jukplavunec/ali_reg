from __future__ import annotations
from sqlalchemy import JSON, Column, Integer, String, Enum, DECIMAL, Boolean
from app.database import Base
from sqlalchemy.orm import relationship, Mapped
from app.registration.enums import ContractStatus, UserStatus, UserCartStatus

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ali_user_id = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    second_name = Column(String)
    status = Column(Enum(UserStatus), nullable=False)
    registration_address = Column(String)
    monthly_income = Column(DECIMAL(precision=10, scale=2))
    phone_number = Column(String)
    email = Column(String)

    user_carts: Mapped[UserCarts] = relationship(back_populates="user", uselist=False)
    user_contracts: Mapped[UserContracts] = relationship(back_populates="user", uselist=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.id}"

class UserCarts(Base):
    __tablename__ = "user_carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    contract_id = Column(Integer)
    cart = Column(JSON)
    status = Column(Enum(UserCartStatus), nullable=False)
    total_amount = Column(DECIMAL(precision=10, scale=2))

    user: Mapped[Users] = relationship(back_populates="user_carts", uselist=True)

    def __str__(self):
        return f"user_cart_id: {self.id}, user_id: {self.user_id}"

    def __repr__(self):
        return f"user_cart_id: {self.id}, user_id: {self.user_id}"

class UserContracts(Base):
    __tablename__ = "user_contracts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    status = Column(Enum(ContractStatus), nullable=False)
    user_limit = Column(DECIMAL(precision=10, scale=2))
    contract_number = Column(String)
    assigment_of_rights = Column(Boolean, default=False)
    general_terms = Column(Boolean, default=False)
    wanted_limit = Column(DECIMAL(precision=10, scale=2))

    user: Mapped[Users] = relationship(back_populates="user_contracts", uselist=True)

    def __str__(self):
        return f"user_contract_id: {self.id}, user_id: {self.user_id}"

    def __repr__(self):
        return f"user_contract_id: {self.id}, user_id: {self.user_id}"


print(Base.metadata)
