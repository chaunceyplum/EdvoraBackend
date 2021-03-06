

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database


class UserModel(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    

    favorite = relationship("favoriteModel", back_populates="owner")

class favoriteModel(database.Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id =Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserModel", back_populates="favorite")