from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserResponse
import bcrypt



def hash_password(password:str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    return hashed_password


def verify_password(plain_password:str, hashed_password:str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))




def create_user(db: Session, user:UserCreate) -> UserResponse:
    user.email = user.email.lower()
    if db.query(User).filter(User.email == user.email).first():
        raise ValueError('email ya registrado, elige otro') 
    new_user = User(name=user.name, email=user.email, password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserResponse.model_validate(new_user)


def get_all_users(db:Session) -> list[UserResponse]:
    users = db.query(User).all()
    return [UserResponse.model_validate(user) for user in users]
    ### db.query(User) == SELECT * FROM users;


def get_user_by_email(db:Session, email:str) -> UserResponse | None:
    user = db.query(User).filter(User.email == email.lower()).first()
    return UserResponse.model_validate(user) if user else None
 

def update_user(db:Session, email:str, user_update:UserCreate) -> UserResponse | None:
    user = db.query(User).filter(User.email == email.lower()).first()
    if not user:
        return None
    
    if user_update.email.lower() != email.lower():
        if db.query(User).filter(User.email == user_update.email).first():
            raise ValueError('email ya en uso')
        user.email = user_update.email
    user.name = user_update.name    
    user.password = hash_password(user_update.password)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


def delete_user(db:Session, email:str) -> UserResponse | None:
    user = db.query(User).filter(User.email == email.lower()).first()
    if not user:
        return None
    user_deleted = UserResponse.model_validate(user)
    db.delete(user)
    db.commit()
    return user_deleted

