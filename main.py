from config import Base, engine
from fastapi import FastAPI
from routers import router

"""
📌 3. Paso a paso: Seguridad en tu API

1️⃣ Guardar contraseñas encriptadas con bcrypt (esto ya lo discutimos, ¿lo tienes listo?)

2️⃣ Proteger los endpoints para que solo usuarios autenticados puedan usarlos (JWT Tokens, lo veremos después)

3️⃣ Validar bien los datos de entrada para evitar inyecciones SQL y errores

4️⃣ Implementar permisos y roles en la API
"""

# creamos las tablas en db (si no existen, con create_all())
Base.metadata.create_all(engine)


# pasamos parametros a fastapi
app = FastAPI(title='primera_api_2025', 
              description="conexion mediante sqlAlchemy", 
              version='0.1.1')

 
# incluimos el router, es donde tenemos los endpoints o llamadas http
app.include_router(router)


# este me gusta hacerlo de prueba, para ver que el servidor corre bien
@app.get('/')
async def home():
    return {'hola': 'perro'}


# añadir health_check()
# crear tablas solo en entornos de produccion? 