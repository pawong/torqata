from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql.functions import now

from api.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    date_created = Column(DateTime, nullable=False, server_default=now())
    date_modified = Column(DateTime)
