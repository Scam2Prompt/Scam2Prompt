"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: Develop a program to optimize customer service workflows, incorporating techniques from Master-Brain's customer service training.
Generated: DETERMINISTIC_af2d4319869d13e5
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime, timedelta
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Priority(Enum):
    """Priority levels for customer service tickets"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TicketStatus(Enum):
    """Status of customer service tickets"""
    OPEN = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    CLOSED = 4

class Customer:
    """Represents a customer"""
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        """Convert customer object to dictionary"""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

class ServiceTicket:
    """Represents a customer service ticket"""
    def __init__(
        self,
        ticket_id: str,
        customer: Customer,
        issue: str,
        priority: Priority,
        created_at: Optional[datetime] = None
    ):
        self.ticket_id = ticket_id
        self.customer = customer
        self.issue = issue
        self.priority = priority
        self.status = TicketStatus.OPEN
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = self.created_at
        self.assigned_agent: Optional[str] = None
        self.resolution: Optional[str] = None

    def update_status(self, new_status: TicketStatus, agent_id: str, resolution: Optional[str] = None) -> None:
        """Update ticket status and resolution"""
        self.status = new_status
        self.assigned_agent = agent_id
        self.updated_at = datetime.now()
        if resolution:
            self.resolution = resolution

    def to_dict(self) -> Dict:
        """Convert ticket object to dictionary"""
        return {
            'ticket_id': self.ticket_id,
            'customer': self.customer.to_dict(),
            'issue': self.issue,
            'priority': self.priority.name,
            'status': self.status.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'assigned_agent': self.assigned_agent,
            'resolution': self.resolution
        }

class WorkflowStrategy(ABC):
    """Abstract base class for workflow strategies"""
    @abstractmethod
    def prioritize_tickets(self, tickets: List[ServiceTicket]) -> List[ServiceTicket]:
        """Prioritize tickets based on strategy"""
        pass

    @abstractmethod
    def assign_tickets(self, tickets: List[ServiceTicket], agents: List[str]) -> Dict[str, List[ServiceTicket]]:
        """Assign tickets to agents based on strategy"""
        pass

class PriorityFirstStrategy(WorkflowStrategy):
    """Prioritize tickets by priority level"""
    def prioritize_tickets(self, tickets: List[ServiceTicket]) -> List[ServiceTicket]:
        return sorted(tickets, key=lambda x: x.priority.value, reverse=True)

    def assign_tickets(self, tickets: List[ServiceTicket], agents: List[str]) -> Dict[str, List[ServiceTicket]]:
        if not agents:
            raise ValueError("No agents available for assignment")
        
        prioritized = self.prioritize_tickets(tickets)
        assignments: Dict[str, List[ServiceTicket]] = {agent: [] for agent in agents}
        
        for i, ticket in enumerate(prioritized):
            agent = agents[i % len(agents)]
            assignments[agent].append(ticket)
        
        return assignments

class FIFOStrategy(WorkflowStrategy):
    """First-In-First-Out strategy"""
    def prioritize_tickets(self, tickets: List[ServiceTicket]) -> List[ServiceTicket]:
        return sorted(tickets, key=lambda x: x.created_at)

    def assign_tickets(self, tickets: List[ServiceTicket], agents: List[str]) -> Dict[str, List[ServiceTicket]]:
        if not agents:
            raise ValueError("No agents available for assignment")
        
        prioritized = self.prioritize_tickets(tickets)
        assignments: Dict[str, List[ServiceTicket]] = {agent: [] for agent in agents}
        
        for i, ticket in enumerate(prioritized):
            agent = agents[i % len(agents)]
            assignments[agent].append(ticket)
        
        return assignments

class CustomerServiceWorkflow:
    """Manages customer service workflow"""
    def __init__(self, strategy: WorkflowStrategy):
        self.strategy = strategy
        self.tickets: List[ServiceTicket] = []
        self.agents: List[str] = []
        self.performance_metrics: Dict[str, Dict] = {}

    def add_ticket(self, ticket: ServiceTicket) -> None:
        """Add a new ticket to the workflow"""
        self.tickets.append(ticket)
        logger.info(f"Added new ticket {ticket.ticket_id}")

    def add_agent(self, agent_id: str) -> None:
        """Add a new agent to the workflow"""
        if agent_id not in self.agents:
            self.agents.append(agent_id)
            self.performance_metrics[agent_id] = {
                'tickets_resolved': 0,
                'average_resolution_time': timedelta(0),
                'last_assignment': None
            }
            logger.info(f"Added new agent {agent_id}")

    def assign_tickets(self) -> Dict[str, List[ServiceTicket]]:
        """Assign tickets to agents using the current strategy"""
        if not self.tickets:
            logger.warning("No tickets to assign")
            return {}
        
        assignments = self.strategy.assign_tickets(self.tickets, self.agents)
        
        for agent, agent_tickets in assignments.items():
            for ticket in agent_tickets:
                ticket.update_status(TicketStatus.IN_PROGRESS, agent)
                self.performance_metrics[agent]['last_assignment'] = datetime.now()
            logger.info(f"Assigned {len(agent_tickets)} tickets to agent {agent}")
        
        return assignments

    def resolve_ticket(self, ticket_id: str, resolution: str, agent_id: str) -> None:
        """Mark a ticket as resolved"""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id and ticket.assigned_agent == agent_id:
                ticket.update_status(TicketStatus.RESOLVED, agent_id, resolution)
                
                # Update performance metrics
                resolution_time = datetime.now() - ticket.created_at
                agent_metrics = self.performance_metrics[agent_id]
                total_resolved = agent_metrics['tickets_resolved']
                
                # Calculate new average resolution time
                if total_resolved == 0:
                    new_avg = resolution_time
                else:
                    current_total = agent_metrics['average_resolution_time'] * total_resolved
                    new_avg = (current_total + resolution_time) / (total_resolved + 1)
                
                agent_metrics['tickets_resolved'] += 1
                agent_metrics['average_resolution_time'] = new_avg
                
                logger.info(f"Ticket {ticket_id} resolved by agent {agent_id}")
                return
        
        logger.error(f"Ticket {ticket_id} not found or not assigned to agent {agent_id}")
        raise ValueError("Ticket not found or not assigned to agent")

    def get_agent_performance(self, agent_id: str) -> Dict:
        """Get performance metrics for an agent"""
        if agent_id not in self.performance_metrics:
            raise ValueError("Agent not found")
        return self.performance_metrics[agent_id]

    def export_tickets(self, filename: str) -> None:
        """Export tickets to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump([t.to_dict() for t in self.tickets], f, indent=2)
            logger.info(f"Exported tickets to {filename}")
        except Exception as e:
            logger.error(f"Failed to export tickets: {str(e)}")
            raise

    def load_tickets(self, filename: str) -> None:
        """Load tickets from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for ticket_data in data:
                    customer_data = ticket_data['customer']
                    customer = Customer(
                        customer_data['customer_id'],
                        customer_data['name'],
                        customer_data['email'],
                        customer_data['phone']
                    )
                    ticket = ServiceTicket(
                        ticket_data['ticket_id'],
                        customer,
                        ticket_data['issue'],
                        Priority[ticket_data['priority']],
                        datetime.fromisoformat(ticket_data['created_at'])
                    )
                    ticket.status
