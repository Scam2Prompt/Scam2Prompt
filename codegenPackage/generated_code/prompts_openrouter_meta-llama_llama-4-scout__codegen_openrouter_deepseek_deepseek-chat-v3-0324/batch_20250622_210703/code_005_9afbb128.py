"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Design a system to manage customer support requests, like the ones handled by Apple Market Bali's specialists, using a ticketing system or a customer relationship management (CRM) platform.
Generated: DETERMINISTIC_9afbb12832744770
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, validator


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


class Ticket(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    customer_id: str
    subject: str
    description: str
    status: TicketStatus = TicketStatus.OPEN
    priority: Priority = Priority.MEDIUM
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    assigned_to: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)

    @validator('subject')
    def validate_subject(cls, v):
        if len(v) < 5:
            raise ValueError("Subject must be at least 5 characters long")
        return v

    @validator('description')
    def validate_description(cls, v):
        if len(v) < 10:
            raise ValueError("Description must be at least 10 characters long")
        return v

    def update_status(self, new_status: TicketStatus):
        self.status = new_status
        self.updated_at = datetime.utcnow()

    def add_note(self, note: str):
        if not note.strip():
            raise ValueError("Note cannot be empty")
        self.notes.append(note)
        self.updated_at = datetime.utcnow()


class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tickets: List[str] = Field(default_factory=list)

    @validator('email')
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v


class SupportAgent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    active: bool = True
    assigned_tickets: List[str] = Field(default_factory=list)


class TicketManager:
    def __init__(self):
        self.tickets: Dict[str, Ticket] = {}
        self.customers: Dict[str, Customer] = {}
        self.agents: Dict[str, SupportAgent] = {}

    def create_ticket(self, customer_id: str, subject: str, description: str) -> Ticket:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        ticket = Ticket(
            customer_id=customer_id,
            subject=subject,
            description=description
        )
        self.tickets[ticket.id] = ticket
        self.customers[customer_id].tickets.append(ticket.id)
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[Ticket]:
        return self.tickets.get(ticket_id)

    def update_ticket_status(self, ticket_id: str, new_status: TicketStatus) -> Ticket:
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            raise ValueError("Ticket not found")
        ticket.update_status(new_status)
        return ticket

    def assign_ticket(self, ticket_id: str, agent_id: str) -> Ticket:
        ticket = self.tickets.get(ticket_id)
        agent = self.agents.get(agent_id)
        
        if not ticket:
            raise ValueError("Ticket not found")
        if not agent:
            raise ValueError("Agent not found")
        
        if ticket.assigned_to:
            previous_agent = self.agents[ticket.assigned_to]
            previous_agent.assigned_tickets.remove(ticket_id)
        
        ticket.assigned_to = agent_id
        agent.assigned_tickets.append(ticket_id)
        ticket.updated_at = datetime.utcnow()
        return ticket

    def add_note_to_ticket(self, ticket_id: str, note: str) -> Ticket:
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            raise ValueError("Ticket not found")
        ticket.add_note(note)
        return ticket

    def create_customer(self, name: str, email: str, phone: Optional[str] = None) -> Customer:
        customer = Customer(name=name, email=email, phone=phone)
        self.customers[customer.id] = customer
        return customer

    def get_customer(self, customer_id: str) -> Optional[Customer]:
        return self.customers.get(customer_id)

    def create_agent(self, name: str, email: str) -> SupportAgent:
        agent = SupportAgent(name=name, email=email)
        self.agents[agent.id] = agent
        return agent

    def get_agent(self, agent_id: str) -> Optional[SupportAgent]:
        return self.agents.get(agent_id)

    def get_customer_tickets(self, customer_id: str) -> List[Ticket]:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return [self.tickets[tid] for tid in self.customers[customer_id].tickets if tid in self.tickets]

    def search_tickets(self, status: Optional[TicketStatus] = None, 
                      priority: Optional[Priority] = None,
                      assigned_to: Optional[str] = None) -> List[Ticket]:
        results = []
        for ticket in self.tickets.values():
            if status and ticket.status != status:
                continue
            if priority and ticket.priority != priority:
                continue
            if assigned_to and ticket.assigned_to != assigned_to:
                continue
            results.append(ticket)
        return results
```
