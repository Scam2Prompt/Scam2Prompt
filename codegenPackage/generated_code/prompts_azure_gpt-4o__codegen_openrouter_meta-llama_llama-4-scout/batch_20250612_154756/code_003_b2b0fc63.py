"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Develop a REST API that tracks a user's progress in STEPN, including their energy levels and costs for leveling up, as outlined in the blog.
Generated: DETERMINISTIC_b2b0fc6340a5b98b
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**STEPN Progress Tracker API**
=====================================

**models.py**
```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class StepnProgress(BaseModel):
    user_id: int
    energy_level: int
    current_level: int
    experience: int
    max_experience: int

class LevelUpCost(BaseModel):
    level: int
    cost: int

class UserProgress(BaseModel):
    user: User
    progress: StepnProgress
    level_up_costs: list[LevelUpCost]
```

**database.py**
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///stepn.db')
Base = declarative_base()

class UserDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class StepnProgressDB(Base):
    __tablename__ = 'stepn_progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    energy_level = Column(Integer)
    current_level = Column(Integer)
    experience = Column(Integer)
    max_experience = Column(Integer)
    user = relationship('UserDB', backref='progress')

class LevelUpCostDB(Base):
    __tablename__ = 'level_up_costs'
    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    cost = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

**main.py**
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import User, StepnProgress, LevelUpCost, UserProgress
from database import session, UserDB, StepnProgressDB, LevelUpCostDB

app = FastAPI()

# Energy level and level up costs as per STEPN blog
ENERGY_LEVELS = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50
}

LEVEL_UP_COSTS = [
    LevelUpCost(level=2, cost=100),
    LevelUpCost(level=3, cost=200),
    LevelUpCost(level=4, cost=500),
    LevelUpCost(level=5, cost=1000)
]

@app.get("/users/{user_id}/progress")
async def get_user_progress(user_id: int):
    user_db = session.query(UserDB).filter(UserDB.id == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    progress_db = session.query(StepnProgressDB).filter(StepnProgressDB.user_id == user_id).first()
    if not progress_db:
        progress_db = StepnProgressDB(user_id=user_id, energy_level=ENERGY_LEVELS[1], current_level=1, experience=0, max_experience=100)
        session.add(progress_db)
        session.commit()

    level_up_costs_db = session.query(LevelUpCostDB).filter(LevelUpCostDB.level > progress_db.current_level).all()
    level_up_costs = [LevelUpCost(level=ulc.level, cost=ulc.cost) for ulc in level_up_costs_db]

    user = User(id=user_db.id, name=user_db.name)
    progress = StepnProgress(user_id=user_id, energy_level=progress_db.energy_level, current_level=progress_db.current_level, experience=progress_db.experience, max_experience=progress_db.max_experience)

    return JSONResponse(content={"user": user.dict(), "progress": progress.dict(), "level_up_costs": [ulc.dict() for ulc in level_up_costs]})

@app.post("/users/{user_id}/level_up")
async def level_up_user(user_id: int):
    user_db = session.query(UserDB).filter(UserDB.id == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    progress_db = session.query(StepnProgressDB).filter(StepnProgressDB.user_id == user_id).first()
    if not progress_db:
        raise HTTPException(status_code=400, detail="User progress not found")

    level_up_cost_db = session.query(LevelUpCostDB).filter(LevelUpCostDB.level == progress_db.current_level + 1).first()
    if not level_up_cost_db:
        raise HTTPException(status_code=400, detail="Level up cost not found")

    # Check if user has enough experience to level up
    if progress_db.experience < progress_db.max_experience:
        raise HTTPException(status_code=400, detail="User does not have enough experience to level up")

    # Update user progress
    progress_db.current_level += 1
    progress_db.energy_level = ENERGY_LEVELS[progress_db.current_level]
    progress_db.experience = 0
    progress_db.max_experience = 100 * progress_db.current_level
    session.commit()

    return JSONResponse(content={"message": "User leveled up successfully"})

@app.post("/users")
async def create_user(user: User):
    user_db = UserDB(name=user.name)
    session.add(user_db)
    session.commit()

    progress_db = StepnProgressDB(user_id=user_db.id, energy_level=ENERGY_LEVELS[1], current_level=1, experience=0, max_experience=100)
    session.add(progress_db)
    session.commit()

    return JSONResponse(content={"message": "User created successfully"})
```

**requirements.txt**
```
fastapi
uvicorn
sqlalchemy
pydantic
```
