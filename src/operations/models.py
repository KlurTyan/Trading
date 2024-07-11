import datetime
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from src.database import metadata

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc)),
    Column("type", String),
)
