import enum
from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import Enum, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.testing.schema import mapped_column, Column
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import Integer , String

class Base(DeclarativeBase):
    pass

class Accounts(Base):
    __tablename__ = "accounts"

    id : Mapped[int] = mapped_column(primary_key=True)
    account_name : Mapped[str]
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    entries: Mapped[List["Entries"]] = relationship()

    def __repr__(self) -> str:
        return f"Account {self.id , self.account_name}"

class TransactionTypes(enum.Enum):
    __tablename__ = "transaction_types"

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"

class TransactionStatus(enum.Enum):
    __tablename__ = "transaction_status"

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class Transactions(Base):
    __tablename__ = "transactions"

    id : Mapped[int] = mapped_column(primary_key=True)
    type : Mapped[str] = mapped_column(
        Enum(TransactionTypes , name="TransactionTypesEnum"),
        nullable=False
    )
    satus : Mapped[str] = mapped_column(
        Enum(TransactionStatus, name="TransactionStatusEnum"),
        nullable=False
    )
    idempotency_key : Mapped[str]
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    entries: Mapped[List["Entries"]] = relationship()

    def __repr__(self) -> str:
        return f"Transaction {self.id}"


class Entries(Base):
    __tablename__ = "entries"

    id : Mapped[int] = mapped_column(primary_key=True)
    transaction_id : Mapped[int] = mapped_column(ForeignKey("transactions.id"))
    account_id : Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    amount : Mapped[int]
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    def __repr__(self) -> str:
        return f"Entry {self.id}"
