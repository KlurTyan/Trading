import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Boolean,
    MetaData,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
    JSON,
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    String,
    Integer,
)

from fastapi_users.db import SQLAlchemyBaseUserTable

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),  # nullable - Не может быть пустым
    Column("permission", JSON),
)

# Императивный способ

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column(
        "registered_at", TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc)
    ),
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class Base(DeclarativeBase):
    pass


# Декларативный способ


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
