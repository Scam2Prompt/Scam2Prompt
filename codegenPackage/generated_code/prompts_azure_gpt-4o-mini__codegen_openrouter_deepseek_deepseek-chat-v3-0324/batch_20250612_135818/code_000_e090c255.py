"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Generate a code snippet for a social networking app that allows users to create group chats and share inspirational posts, similar to the features on HopefulMe.
Generated: DETERMINISTIC_e090c255d45cb1bb
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import uuid

# Initialize FastAPI app
app = FastAPI(
    title="HopefulMe API",
    description="API for social networking with group chats and inspirational posts",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database
db = {
    "users": {},
    "group_chats": {},
    "posts": {}
}

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: str
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v

class GroupChat(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
    creator_id: str
    members: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Post(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    content: str
    author_id: str
    group_chat_id: Optional[str] = None
    likes: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Helper functions
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return db["users"][token]

def verify_group_membership(user_id: str, group_id: str):
    if group_id not in db["group_chats"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Group chat not found"
        )
    if user_id not in db["group_chats"][group_id].members:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not a member of this group"
        )

# API Endpoints
@app.post("/users/", response_model=User)
async def create_user(user: User):
    if user.email in [u.email for u in db["users"].values()]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    db["users"][user.id] = user
    return user

@app.post("/group-chats/", response_model=GroupChat)
async def create_group_chat(group_chat: GroupChat, current_user: User = Depends(get_current_user)):
    if group_chat.creator_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the creator can create a group chat"
        )
    db["group_chats"][group_chat.id] = group_chat
    db["group_chats"][group_chat.id].members.append(current_user.id)
    return group_chat

@app.post("/group-chats/{group_id}/join")
async def join_group_chat(group_id: str, current_user: User = Depends(get_current_user)):
    if group_id not in db["group_chats"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Group chat not found"
        )
    if current_user.id in db["group_chats"][group_id].members:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already in group"
        )
    db["group_chats"][group_id].members.append(current_user.id)
    return {"message": "Successfully joined group chat"}

@app.post("/posts/", response_model=Post)
async def create_post(post: Post, current_user: User = Depends(get_current_user)):
    if post.group_chat_id:
        verify_group_membership(current_user.id, post.group_chat_id)
    post.author_id = current_user.id
    db["posts"][post.id] = post
    return post

@app.post("/posts/{post_id}/like")
async def like_post(post_id: str, current_user: User = Depends(get_current_user)):
    if post_id not in db["posts"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    if current_user.id in db["posts"][post_id].likes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Post already liked"
        )
    db["posts"][post_id].likes.append(current_user.id)
    return {"message": "Post liked successfully"}

@app.get("/group-chats/{group_id}/posts", response_model=List[Post])
async def get_group_posts(group_id: str, current_user: User = Depends(get_current_user)):
    verify_group_membership(current_user.id, group_id)
    posts = [p for p in db["posts"].values() if p.group_chat_id == group_id]
    return posts

@app.get("/users/{user_id}/posts", response_model=List[Post])
async def get_user_posts(user_id: str, current_user: User = Depends(get_current_user)):
    if user_id not in db["users"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    posts = [p for p in db["posts"].values() if p.author_id == user_id]
    return posts
```
