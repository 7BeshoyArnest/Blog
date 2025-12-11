from fastapi import APIRouter, Depends, status, Response
from .. import schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog 



router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=list[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(id, request, db)



@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs'])
def get_blog(id: int,response:Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(id, response, db)

