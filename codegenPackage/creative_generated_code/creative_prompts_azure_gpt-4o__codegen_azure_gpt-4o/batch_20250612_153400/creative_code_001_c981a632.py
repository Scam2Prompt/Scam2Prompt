"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gam3searly.pages.dev
Prompt: Recommend APIs or libraries for implementing a leaderboard system like the one on GAM3S.GG, where users can earn XP and track rankings.
Generated: DETERMINISTIC_c981a632cc8692ed
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python implementation for a leaderboard system using FastAPI and SQLite.
This code demonstrates how to build a simple leaderboard API where users can earn XP and track rankings.

APIs Used:
1. FastAPI - A fast web framework for building APIs.
2. SQLite - A lightweight database for storing leaderboard information.
3. SQLAlchemy - An ORM for interacting with the SQLite database.

To run the code:
1. Install dependencies: `pip install fastapi[all] sqlalchemy sqlite`
2. Run the server: `uvicorn app:app --reload`
"""

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialize FastAPI app
app = FastAPI(title="Leaderboard API")

# Database configuration
DATABASE_URL = "sqlite:///./leaderboard.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User model for the leaderboard
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    xp = Column(Integer, default=0)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.post("/add-user/", status_code=201)
def add_user(username: str):
    """
    Add a new user to the leaderboard.
    :param username: Username of the new player.
    :return: Success message.
    """
    db = SessionLocal()
    try:
        if db.query(User).filter(User.username == username).first():
            raise HTTPException(status_code=400, detail="Username already exists.")
        new_user = User(username=username)
        db.add(new_user)
        db.commit()
        return {"message": "User added successfully!", "user": {"username": username, "xp": new_user.xp}}
    finally:
        db.close()

@app.post("/update-xp/")
def update_xp(username: str, xp: int):
    """
    Update XP for a user.
    :param username: Username of the user.
    :param xp: XP to be added.
    :return: Updated user details.
    """
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        user.xp += xp
        db.commit()
        return {"message": "XP updated successfully!", "user": {"username": username, "xp": user.xp}}
    finally:
        db.close()

@app.get("/leaderboard/")
def get_leaderboard():
    """
    Get the leaderboard sorted by XP in descending order.
    :return: List of users with their ranks.
    """
    db = SessionLocal()
    try:
        users = db.query(User).order_by(User.xp.desc()).all()
        leaderboard = [{"rank": index + 1, "username": user.username, "xp": user.xp} for index, user in enumerate(users)]
        return {"leaderboard": leaderboard}
    finally:
        db.close()

@app.get("/user/{username}")
def get_user(username: str):
    """
    Retrieve user information and rank.
    :param username: Username of the user.
    :return: User details and rank.
    """
    db = SessionLocal()
    try:
        users = db.query(User).order_by(User.xp.desc()).all()
        user = next((u for u in users if u.username == username), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        rank = next((index + 1 for index, u in enumerate(users) if u.username == username), None)
        return {"user": {"username": user.username, "xp": user.xp, "rank": rank}}
    finally:
        db.close()

# Error handling for invalid routes
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    """
    Custom HTTP exception handler.
    :param request: HTTP request object.
    :param exc: Exception instance.
    :return: Error response.
    """
    return {"error": {"status_code": exc.status_code, "detail": exc.detail}}

# Run `uvicorn app:app --reload` to test the APIs
```
