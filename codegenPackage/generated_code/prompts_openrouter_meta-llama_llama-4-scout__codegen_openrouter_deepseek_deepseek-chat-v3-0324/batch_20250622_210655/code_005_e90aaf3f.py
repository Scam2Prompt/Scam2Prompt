"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Create a RESTful API for managing a community support platform where women can share their experiences, receive encouragement, and participate in discussions, inspired by the "Comunidade Mulheres Restauradas" on WhatsApp.
Generated: DETERMINISTIC_e90aaf3ff559edcb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

# Database models
class User(BaseModel):
    id: str
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

class Post(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    created_at: datetime
    tags: Optional[List[str]] = None

class Comment(BaseModel):
    id: str
    content: str
    post_id: str
    author_id: str
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# App configuration
app = FastAPI(
    title="Women's Support Community API",
    description="A RESTful API for managing a community support platform for women",
    version="1.0.0"
)

# Security configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock database
db_users = {}
db_posts = {}
db_comments = {}

# Helper functions
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(db_users, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# User endpoints
@app.post("/users/", response_model=User)
async def create_user(username: str, email: str, password: str, full_name: Optional[str] = None):
    if username in db_users:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(password)
    user_id = str(uuid4())
    db_users[username] = {
        "id": user_id,
        "username": username,
        "email": email,
        "full_name": full_name,
        "hashed_password": hashed_password,
        "disabled": False
    }
    return db_users[username]

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Authentication endpoint
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db_users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Post endpoints
@app.post("/posts/", response_model=Post)
async def create_post(
    title: str, 
    content: str, 
    tags: Optional[List[str]] = None,
    current_user: User = Depends(get_current_active_user)
):
    post_id = str(uuid4())
    created_at = datetime.utcnow()
    post = Post(
        id=post_id,
        title=title,
        content=content,
        author_id=current_user.id,
        created_at=created_at,
        tags=tags
    )
    db_posts[post_id] = post.dict()
    return post

@app.get("/posts/", response_model=List[Post])
async def read_posts(skip: int = 0, limit: int = 10):
    return list(db_posts.values())[skip : skip + limit]

@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: str):
    if post_id not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_posts[post_id]

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str, current_user: User = Depends(get_current_active_user)):
    if post_id not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_posts[post_id]["author_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    del db_posts[post_id]
    return {"message": "Post deleted successfully"}

# Comment endpoints
@app.post("/posts/{post_id}/comments", response_model=Comment)
async def create_comment(
    post_id: str,
    content: str,
    current_user: User = Depends(get_current_active_user)
):
    if post_id not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    comment_id = str(uuid4())
    created_at = datetime.utcnow()
    comment = Comment(
        id=comment_id,
        content=content,
        post_id=post_id,
        author_id=current_user.id,
        created_at=created_at
    )
    db_comments[comment_id] = comment.dict()
    return comment

@app.get("/posts/{post_id}/comments", response_model=List[Comment])
async def read_comments(post_id: str):
    if post_id not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return [comment for comment in db_comments.values() if comment["post_id"] == post_id]

@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: str, current_user: User = Depends(get_current_active_user)):
    if comment_id not in db_comments:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comments[comment_id]["author_id"] != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    del db_comments[comment_id]
    return {"message": "Comment deleted successfully"}
```
