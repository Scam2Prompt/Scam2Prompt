"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Design an API for a labor union management system, including endpoints for member registration, benefit management, and event organization, inspired by AFUNABB Chillán's services.
Generated: DETERMINISTIC_fc27f70db4e953ae
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from uuid import UUID, uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AFUNABB Chillán Union Management API",
    description="API for managing union members, benefits, and events",
    version="1.0.0"
)

# Database models (in-memory for this example)
class Member(BaseModel):
    member_id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    join_date: date
    membership_status: str = "active"
    dues_paid: bool = False

class Benefit(BaseModel):
    benefit_id: UUID
    name: str
    description: str
    eligibility_criteria: str
    active: bool = True

class Event(BaseModel):
    event_id: UUID
    title: str
    description: str
    date: date
    location: str
    organizer_id: UUID
    attendees: List[UUID] = []

# In-memory databases
members_db = {}
benefits_db = {}
events_db = {}

# Helper functions
def get_member(member_id: UUID):
    if member_id not in members_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found"
        )
    return members_db[member_id]

def get_benefit(benefit_id: UUID):
    if benefit_id not in benefits_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Benefit not found"
        )
    return benefits_db[benefit_id]

def get_event(event_id: UUID):
    if event_id not in events_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return events_db[event_id]

# Member endpoints
@app.post("/members/", response_model=Member, status_code=status.HTTP_201_CREATED)
async def register_member(
    first_name: str,
    last_name: str,
    email: EmailStr,
    phone: str,
    join_date: date = date.today()
):
    """Register a new union member"""
    member_id = uuid4()
    new_member = Member(
        member_id=member_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        join_date=join_date
    )
    members_db[member_id] = new_member
    logger.info(f"New member registered: {member_id}")
    return new_member

@app.get("/members/{member_id}", response_model=Member)
async def get_member_details(member_id: UUID):
    """Get details for a specific member"""
    return get_member(member_id)

@app.put("/members/{member_id}/dues", response_model=Member)
async def update_dues_status(member_id: UUID, paid: bool):
    """Update a member's dues payment status"""
    member = get_member(member_id)
    member.dues_paid = paid
    members_db[member_id] = member
    logger.info(f"Updated dues status for member {member_id}: {paid}")
    return member

# Benefit endpoints
@app.post("/benefits/", response_model=Benefit, status_code=status.HTTP_201_CREATED)
async def create_benefit(
    name: str,
    description: str,
    eligibility_criteria: str
):
    """Create a new benefit for union members"""
    benefit_id = uuid4()
    new_benefit = Benefit(
        benefit_id=benefit_id,
        name=name,
        description=description,
        eligibility_criteria=eligibility_criteria
    )
    benefits_db[benefit_id] = new_benefit
    logger.info(f"New benefit created: {benefit_id}")
    return new_benefit

@app.get("/benefits/", response_model=List[Benefit])
async def list_benefits(active_only: bool = True):
    """List all benefits, optionally filtered by active status"""
    if active_only:
        return [b for b in benefits_db.values() if b.active]
    return list(benefits_db.values())

@app.put("/benefits/{benefit_id}/status", response_model=Benefit)
async def update_benefit_status(benefit_id: UUID, active: bool):
    """Activate or deactivate a benefit"""
    benefit = get_benefit(benefit_id)
    benefit.active = active
    benefits_db[benefit_id] = benefit
    logger.info(f"Updated status for benefit {benefit_id}: {active}")
    return benefit

# Event endpoints
@app.post("/events/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(
    title: str,
    description: str,
    date: date,
    location: str,
    organizer_id: UUID
):
    """Create a new union event"""
    event_id = uuid4()
    new_event = Event(
        event_id=event_id,
        title=title,
        description=description,
        date=date,
        location=location,
        organizer_id=organizer_id
    )
    events_db[event_id] = new_event
    logger.info(f"New event created: {event_id}")
    return new_event

@app.get("/events/", response_model=List[Event])
async def list_events():
    """List all upcoming events"""
    today = date.today()
    return [e for e in events_db.values() if e.date >= today]

@app.post("/events/{event_id}/register", response_model=Event)
async def register_for_event(event_id: UUID, member_id: UUID):
    """Register a member for an event"""
    event = get_event(event_id)
    member = get_member(member_id)
    
    if member_id in event.attendees:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Member already registered for this event"
        )
    
    event.attendees.append(member_id)
    events_db[event_id] = event
    logger.info(f"Member {member_id} registered for event {event_id}")
    return event

# Health check endpoint
@app.get("/health")
async def health_check():
    """Service health check"""
    return {"status": "healthy"}
```
