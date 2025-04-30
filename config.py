
"""
Nota: Si utilizas root como usuario en la base de datos, asegúrate de que es una práctica segura. 
En un entorno de producción, lo ideal sería usar un usuario con permisos limitados.
"""

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


load_dotenv()
contraseña = os.getenv('contraseña')


# conexion db
engine = create_engine(f'mysql+pymysql://root:{contraseña}@localhost/api_orm_2025')


# probamos que la conexion sea ok
try:
    engine.connect()
    print('conexion DB: ok')
except Exception as e:
    print(f'error de conexion: {e}')


# manejar sesiones
    # autoflush(sube datos antes de mandarle el commit)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# definimos aqui la base para los modelos, para el ORM
class Base(DeclarativeBase):
    pass


# try:yeld - finally (yield mantiene la conexion abierta, y finally: al acabar la consulta, cierra la conexion)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
Manejo de variables de entorno para contraseñas:
Las contraseñas no deben guardarse en el código. 
Utiliza una librería como python-dotenv o las variables de entorno del sistema 
operativo para gestionar las credenciales de manera más segura.

podemos enctyptarlas con bcrypt o algo asi
"""