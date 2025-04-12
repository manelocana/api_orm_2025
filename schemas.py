
### los schemas de los datos a introducir en las tablas


from pydantic import BaseModel, EmailStr 



class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str


class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr

    # convertimos los modelos de sqlalchemy a pydantic automaticamente (de DB a JSON)
    class Config:
        from_attributes=True
        # usamos from_attributes=True en los modelos de respuesta de la db


"""
Posible mejora: Podrías añadir una validación para el password, 
dependiendo de tus requisitos de seguridad (por ejemplo, longitud mínima, caracteres especiales, etc.).
con 'constr' de pydantic, por ejemplo

O encryptar el password directamente, seria lo ideal
"""