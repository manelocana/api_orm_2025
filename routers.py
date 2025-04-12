from fastapi import APIRouter, Depends, HTTPException
import schemas, crud
from sqlalchemy.orm import Session
from config import get_db


router = APIRouter()


# le pasamos siempre a los endpoints un modelo de respuesta, desde schemas
# tanto si queremos meter datos o que los muestre

# a la funcion le pasamos los parametros 

# y llamamos a las funciones del crud, comprobando antes el none y luego el result




@router.post('/users', response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email.lower()):
        raise HTTPException(status_code=400, detail='email ya registrado')
    return crud.create_user(db, user)


@router.get('/users', response_model=list[schemas.UserResponse])
def get_all_users(db:Session = Depends(get_db)):
    return crud.get_all_users(db)


@router.get('/users/{email}', response_model=schemas.UserResponse)
def get_user(email:str, db:Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email.lower())
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    return user


@router.put('/users/{email}', response_model=schemas.UserResponse)
def update_user(email:str, user_update:schemas.UserCreate, db:Session = Depends(get_db)):
    user = crud.update_user(db, email, user_update)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    return user


@router.delete('/users/{email}', response_model=schemas.UserResponse)
def delete_user(email:str, db:Session = Depends(get_db)):
    user = crud.delete_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    return user