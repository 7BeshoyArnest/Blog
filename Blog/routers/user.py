from fastapi import APIRouter, Depends, status, Response
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user 

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,  db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    return user.get_user(id, response, db)
