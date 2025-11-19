"""
Generated Code Metadata:
========================
Original URL: https://questn-rewards.web.app
Prompt: Design a basic API structure for a platform that offers quests, events, and rewards, similar to QuestN's features.
Generated: DETERMINISTIC_3f54bda9c80b97e4
Batch ID: 20250622_205230
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
from uuid import UUID, uuid4

app = FastAPI(
    title="Quest Platform API",
    description="API for managing quests, events, and rewards",
    version="1.0.0"
)

# Database models (in-memory for this example)
class User(BaseModel):
    id: UUID
    username: str
    email: str
    points: int = 0

class Quest(BaseModel):
    id: UUID
    title: str
    description: str
    points: int
    start_date: datetime
    end_date: datetime
    is_active: bool = True

class Event(BaseModel):
    id: UUID
    title: str
    description: str
    location: str
    start_time: datetime
    end_time: datetime
    max_participants: int

class Reward(BaseModel):
    id: UUID
    name: str
    description: str
    cost: int
    stock: int

# In-memory databases
users_db: List[User] = []
quests_db: List[Quest] = []
events_db: List[Event] = []
rewards_db: List[Reward] = []

# Dependency to get current user (simplified for example)
def get_current_user(user_id: UUID):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(username: str, email: str):
    user = User(id=uuid4(), username=username, email=email)
    users_db.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID):
    return get_current_user(user_id)

# Quest endpoints
@app.post("/quests/", response_model=Quest, status_code=status.HTTP_201_CREATED)
def create_quest(
    title: str,
    description: str,
    points: int,
    start_date: datetime,
    end_date: datetime
):
    quest = Quest(
        id=uuid4(),
        title=title,
        description=description,
        points=points,
        start_date=start_date,
        end_date=end_date
    )
    quests_db.append(quest)
    return quest

@app.get("/quests/", response_model=List[Quest])
def get_quests(is_active: Optional[bool] = None):
    if is_active is None:
        return quests_db
    return [q for q in quests_db if q.is_active == is_active]

@app.post("/quests/{quest_id}/complete", response_model=User)
def complete_quest(quest_id: UUID, user_id: UUID):
    user = get_current_user(user_id)
    quest = next((q for q in quests_db if q.id == quest_id), None)
    
    if not quest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quest not found"
        )
    
    if not quest.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quest is not active"
        )
    
    user.points += quest.points
    return user

# Event endpoints
@app.post("/events/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(
    title: str,
    description: str,
    location: str,
    start_time: datetime,
    end_time: datetime,
    max_participants: int
):
    event = Event(
        id=uuid4(),
        title=title,
        description=description,
        location=location,
        start_time=start_time,
        end_time=end_time,
        max_participants=max_participants
    )
    events_db.append(event)
    return event

@app.get("/events/", response_model=List[Event])
def get_events():
    return events_db

# Reward endpoints
@app.post("/rewards/", response_model=Reward, status_code=status.HTTP_201_CREATED)
def create_reward(
    name: str,
    description: str,
    cost: int,
    stock: int
):
    reward = Reward(
        id=uuid4(),
        name=name,
        description=description,
        cost=cost,
        stock=stock
    )
    rewards_db.append(reward)
    return reward

@app.get("/rewards/", response_model=List[Reward])
def get_rewards():
    return rewards_db

@app.post("/rewards/{reward_id}/redeem", response_model=User)
def redeem_reward(reward_id: UUID, user_id: UUID):
    user = get_current_user(user_id)
    reward = next((r for r in rewards_db if r.id == reward_id), None)
    
    if not reward:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reward not found"
        )
    
    if user.points < reward.cost:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough points"
        )
    
    if reward.stock <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Reward out of stock"
        )
    
    user.points -= reward.cost
    reward.stock -= 1
    return user
```
