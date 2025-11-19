"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Develop a REST API for managing customer testimonials and reviews about hot tubs, inspired by the testimonial section on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_519aec41ac2bcbd6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# Initialize FastAPI app
app = FastAPI(
    title="Hot Tub Testimonials API",
    description="REST API for managing customer testimonials and reviews about hot tubs",
    version="1.0.0"
)

# Security configurations
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database simulation (in production, use a real database)
testimonials_db = []
users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "disabled": False
    }
}

# Models
class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class TestimonialBase(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=100)
    rating: int = Field(..., ge=1, le=5)
    review_text: str = Field(..., min_length=10, max_length=1000)
    hot_tub_model: Optional[str] = Field(None, max_length=50)
    location: Optional[str] = Field(None, max_length=100)

class TestimonialCreate(TestimonialBase):
    pass

class Testimonial(TestimonialBase):
    id: str
    date_posted: datetime
    approved: bool = False

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Helper functions
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme)):
    # In production, implement proper token validation
    user = get_user(users_db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = authenticate_user(users_db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In production, generate a proper JWT token
    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/testimonials/", response_model=Testimonial, status_code=status.HTTP_201_CREATED)
async def create_testimonial(testimonial: TestimonialCreate):
    db_testimonial = {
        "id": str(uuid.uuid4()),
        "date_posted": datetime.now(),
        "approved": False,
        **testimonial.dict()
    }
    testimonials_db.append(db_testimonial)
    return db_testimonial

@app.get("/testimonials/", response_model=List[Testimonial])
async def read_testimonials(approved_only: bool = True, skip: int = 0, limit: int = 10):
    testimonials = testimonials_db
    if approved_only:
        testimonials = [t for t in testimonials if t["approved"]]
    return testimonials[skip : skip + limit]

@app.get("/testimonials/{testimonial_id}", response_model=Testimonial)
async def read_testimonial(testimonial_id: str):
    for testimonial in testimonials_db:
        if testimonial["id"] == testimonial_id:
            return testimonial
    raise HTTPException(status_code=404, detail="Testimonial not found")

@app.put("/testimonials/{testimonial_id}/approve", response_model=Testimonial)
async def approve_testimonial(testimonial_id: str, current_user: User = Depends(get_current_active_user)):
    for testimonial in testimonials_db:
        if testimonial["id"] == testimonial_id:
            testimonial["approved"] = True
            return testimonial
    raise HTTPException(status_code=404, detail="Testimonial not found")

@app.delete("/testimonials/{testimonial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_testimonial(testimonial_id: str, current_user: User = Depends(get_current_active_user)):
    for index, testimonial in enumerate(testimonials_db):
        if testimonial["id"] == testimonial_id:
            testimonials_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Testimonial not found")

@app.get("/testimonials/average-rating", response_model=float)
async def get_average_rating():
    if not testimonials_db:
        return 0.0
    approved_testimonials = [t for t in testimonials_db if t["approved"]]
    if not approved_testimonials:
        return 0.0
    total = sum(t["rating"] for t in approved_testimonials)
    return round(total / len(approved_testimonials), 2)

@app.get("/testimonials/search/", response_model=List[Testimonial])
async def search_testimonials(query: str, approved_only: bool = True):
    results = []
    for testimonial in testimonials_db:
        if approved_only and not testimonial["approved"]:
            continue
        if (query.lower() in testimonial["customer_name"].lower() or 
            query.lower() in testimonial["review_text"].lower() or
            (testimonial["hot_tub_model"] and query.lower() in testimonial["hot_tub_model"].lower())):
            results.append(testimonial)
    return results
```
