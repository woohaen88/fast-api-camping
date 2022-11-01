from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from sql_app import schemas, crud

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts


@router.post("/{user_id}/posts/", response_model=schemas.Post)
def create_post_for_user(
    user_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)
):
    return crud.create_post(db, post=post, user_id=user_id)
