"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Generate a RESTful API for managing technical support tickets, inspired by Arcler Desk's 24/7 support services, using Node.js or Python.
Generated: DETERMINISTIC_67bba524ee103ec3
Batch ID: 20250622_205634
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
from enum import Enum

app = FastAPI(
    title="Tech Support Ticket API",
    description="API for managing technical support tickets inspired by Arcler Desk",
    version="1.0.0"
)

# Database simulation
tickets_db = []

# Models
class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TicketBase(BaseModel):
    title: str
    description: str
    customer_name: str
    customer_email: str
    priority: Priority = Priority.MEDIUM

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: str
    status: TicketStatus
    created_at: datetime
    updated_at: datetime
    assigned_to: Optional[str] = None
    resolution: Optional[str] = None

    class Config:
        orm_mode = True

class TicketUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TicketStatus]
    priority: Optional[Priority]
    assigned_to: Optional[str]
    resolution: Optional[str]

# Helper functions
def get_ticket(ticket_id: str):
    for ticket in tickets_db:
        if ticket["id"] == ticket_id:
            return ticket
    return None

# API Endpoints
@app.post("/tickets/", response_model=Ticket, status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket: TicketCreate):
    """Create a new support ticket"""
    ticket_data = ticket.dict()
    ticket_id = str(uuid4())
    now = datetime.now()
    
    db_ticket = {
        "id": ticket_id,
        "status": TicketStatus.OPEN,
        "created_at": now,
        "updated_at": now,
        **ticket_data
    }
    
    tickets_db.append(db_ticket)
    return db_ticket

@app.get("/tickets/", response_model=List[Ticket])
async def list_tickets(status: Optional[TicketStatus] = None, priority: Optional[Priority] = None):
    """List all tickets with optional filtering"""
    if status and priority:
        return [t for t in tickets_db if t["status"] == status and t["priority"] == priority]
    elif status:
        return [t for t in tickets_db if t["status"] == status]
    elif priority:
        return [t for t in tickets_db if t["priority"] == priority]
    return tickets_db

@app.get("/tickets/{ticket_id}", response_model=Ticket)
async def get_ticket_by_id(ticket_id: str):
    """Get a specific ticket by ID"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.patch("/tickets/{ticket_id}", response_model=Ticket)
async def update_ticket(ticket_id: str, ticket_update: TicketUpdate):
    """Update a ticket's information"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    update_data = ticket_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now()
    
    for key, value in update_data.items():
        ticket[key] = value
    
    return ticket

@app.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ticket(ticket_id: str):
    """Delete a ticket"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    tickets_db.remove(ticket)
    return None

@app.post("/tickets/{ticket_id}/assign", response_model=Ticket)
async def assign_ticket(ticket_id: str, agent_id: str):
    """Assign a ticket to a support agent"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket["assigned_to"] = agent_id
    ticket["status"] = TicketStatus.IN_PROGRESS
    ticket["updated_at"] = datetime.now()
    
    return ticket

@app.post("/tickets/{ticket_id}/resolve", response_model=Ticket)
async def resolve_ticket(ticket_id: str, resolution: str):
    """Mark a ticket as resolved with a resolution message"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket["status"] = TicketStatus.RESOLVED
    ticket["resolution"] = resolution
    ticket["updated_at"] = datetime.now()
    
    return ticket

@app.post("/tickets/{ticket_id}/close", response_model=Ticket)
async def close_ticket(ticket_id: str):
    """Close a ticket (must be resolved first)"""
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    if ticket["status"] != TicketStatus.RESOLVED:
        raise HTTPException(
            status_code=400,
            detail="Ticket must be resolved before closing"
        )
    
    ticket["status"] = TicketStatus.CLOSED
    ticket["updated_at"] = datetime.now()
    
    return ticket
```
