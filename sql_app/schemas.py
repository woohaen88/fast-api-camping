from typing import List, Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True
