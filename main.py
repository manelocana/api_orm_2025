from config import Base, engine
from fastapi import FastAPI
from routers import router



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
1

# añadir health_check()
# crear tablas solo en entornos de produccion? 