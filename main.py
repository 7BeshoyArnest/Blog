from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

# @app.get('/')
# def index():
#     return {"data":"blog list"}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # fetech published blogs with limit
    if published:
        return {"data":f'{limit} published blogs from db'}
    else:
        return {"data":f'{limit} blogs from db'}


@app.get('/blog/unpublished')
#fetech unpublished blogs
def unpublished():
    return {"data": "all unpublished blogs"}



@app.get('/blog/{id}')
#fetech blog with id=id
def show(id: int):
    return {"data": id}



@app.get('/blog/{id}/comments')
#fetech comments of blog with id=id
def comments(id: int):
    return {"data": {"1", "2"}}


# request body
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
# create a new blog 
def create_blog(blog: Blog):
    
    return {"data": f"blog is created with title as {blog.title}"}      


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000)