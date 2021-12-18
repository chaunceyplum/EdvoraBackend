from typing import List, Optional

from pydantic import BaseModel



class FavoriteBase(BaseModel):
    title:str

    class Config:
        orm_mode =True

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: int
    owner_id:int

    class Config:
        orm_mode = True

class UserBase(BaseModel):

    email:str
    
    class Config:
        orm_mode =True

class UserCreate(UserBase):
    hashed_password:str

    class Config:
        orm_mode =True

class User(UserBase):
    id:int
    is_active: bool
    favorites:List[Favorite] = []

    class Config:
        orm_mode =True