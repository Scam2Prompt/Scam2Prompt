"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Suggest a structure for an NGO's blog section, focusing on education and community development topics, similar to Youngistaan's blog."
Generated: DETERMINISTIC_a431c52542434103
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NGO Blog Section Structure
This module defines the structure for an NGO's blog section focusing on education and community development.
"""

from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(
    title="NGO Blog API",
    description="API for managing NGO's blog content",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BlogCategory(str, Enum):
    EDUCATION = "Education"
    COMMUNITY_DEVELOPMENT = "Community Development"
    STORIES = "Success Stories"
    NEWS = "News & Updates"
    VOLUNTEER = "Volunteer Experiences"

class BlogPost(BaseModel):
    id: str = Field(..., description="Unique identifier for the blog post")
    title: str = Field(..., max_length=100, description="Title of the blog post")
    content: str = Field(..., description="Main content of the blog post")
    author: str = Field(..., description="Author of the post")
    category: BlogCategory = Field(..., description="Category of the post")
    published_date: datetime = Field(default_factory=datetime.now, description="Publication date")
    tags: List[str] = Field(default=[], description="List of tags for the post")
    featured_image: Optional[str] = Field(None, description="URL of featured image")
    is_published: bool = Field(default=True, description="Publication status")

    @validator('title')
    def title_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty")
        return v

# In-memory database simulation
blog_db = []

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: BlogPost):
    """Create a new blog post"""
    if any(p.id == post.id for p in blog_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Post with this ID already exists"
        )
    blog_db.append(post)
    return post

@app.get("/posts/", response_model=List[BlogPost])
async def get_all_posts(category: Optional[BlogCategory] = None):
    """Get all blog posts, optionally filtered by category"""
    if category:
        return [post for post in blog_db if post.category == category]
    return blog_db

@app.get("/posts/{post_id}", response_model=BlogPost)
async def get_post(post_id: str):
    """Get a specific blog post by ID"""
    post = next((p for p in blog_db if p.id == post_id), None)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return post

@app.put("/posts/{post_id}")
async def update_post(post_id: str, updated_post: BlogPost):
    """Update an existing blog post"""
    index = next((i for i, p in enumerate(blog_db) if p.id == post_id), None)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    blog_db[index] = updated_post
    return {"message": "Post updated successfully"}

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: str):
    """Delete a blog post"""
    index = next((i for i, p in enumerate(blog_db) if p.id == post_id), None)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    blog_db.pop(index)
    return None

@app.get("/categories/", response_model=List[str])
async def get_categories():
    """Get all available blog categories"""
    return [category.value for category in BlogCategory]

@app.get("/posts/search/", response_model=List[BlogPost])
async def search_posts(query: str):
    """Search blog posts by title or content"""
    query = query.lower()
    return [
        post for post in blog_db
        if query in post.title.lower() or query in post.content.lower()
    ]
```
