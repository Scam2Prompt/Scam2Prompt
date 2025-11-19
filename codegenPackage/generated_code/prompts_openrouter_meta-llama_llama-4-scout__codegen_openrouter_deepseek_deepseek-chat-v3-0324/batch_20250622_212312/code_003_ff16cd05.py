"""
Generated Code Metadata:
========================
Original URL: https://pabshq.com
Prompt: "Design a data model for a platform like Pabs HQ, including entities for users, projects, news, and updates, and relationships between them."
Generated: DETERMINISTIC_ff16cd053a68bbed
Batch ID: 20250622_212312
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
from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
    GUEST = "guest"

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: UserRole = UserRole.MEMBER
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: ProjectStatus = ProjectStatus.PLANNING

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner_id: int
    members: List[User] = []

    class Config:
        orm_mode = True

class NewsBase(BaseModel):
    title: str
    content: str
    is_published: bool = False

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    author_id: int
    author: User

    class Config:
        orm_mode = True

class UpdateType(str, Enum):
    STATUS_CHANGE = "status_change"
    MILESTONE = "milestone"
    GENERAL = "general"

class UpdateBase(BaseModel):
    content: str
    type: UpdateType = UpdateType.GENERAL

class UpdateCreate(UpdateBase):
    project_id: int

class Update(UpdateBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    project_id: int
    project: Project
    author_id: int
    author: User

    class Config:
        orm_mode = True

class UserProjectLink(BaseModel):
    user_id: int
    project_id: int
    joined_at: datetime = Field(default_factory=datetime.utcnow)
    role: UserRole = UserRole.MEMBER

    class Config:
        orm_mode = True
```
