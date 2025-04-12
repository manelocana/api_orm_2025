
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


"""
- INFO DE CHAT
📌 ¿Y por qué los guiones bajos?

    En Python, los atributos con doble guion bajo (__) se usan para atributos especiales o "mágicos".
    __tablename__ es un atributo especial de SQLAlchemy que no es una variable normal.
    Es una convención para evitar que los nombres choquen con otros atributos o métodos.

    Si no lo ponemos, SQLAlchemy daría un error porque no sabría cómo nombrar la tabla.


    hacemos email index,  por que vamos a usarlo como indice para buscar usuarios
"""