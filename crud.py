from sqlalchemy.orm import Session

import model
import schema

def getUser(db: Session, user_id:int):
    return db.query(model.UserModel).filter(model.UserModel.id ==user_id).first()

def getUserByEmail(db:Session, user_email:str):
    return db.query(model.UserModel).filter(model.UserModel.email == user_email).first()

def getUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.UserModel).offset(skip).limit(limit).all()

def createUser(db: Session, user: schema.UserCreate):
    hashed_pass = user.hashed_password +"blahblahblah"
    db_user = model.UserModel(email = user.email, hashed_password = hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def getFavorite(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.favoriteModel).offset(skip).limit(limit).all()

def createUserFavorite(db: Session, item: schema.FavoriteCreate, user_id: int):
    db_favoite = model.favoriteModel(**item.dict(), owner_id = user_id)
    db.add(db_favoite)
    db.commit()
    db.refresh(db_favoite)
    return db_favoite