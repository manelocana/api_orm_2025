
### los modelos de las tablas en la base de datos

from config import Base
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy import Integer, String, Text


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)

