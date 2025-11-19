"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: "Design a tech support system for a computer store with a knowledgeable team, using a ticketing system and prioritization features."
Generated: DETERMINISTIC_8de377aab7e4ab46
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TicketStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class SupportAgent:
    def __init__(self, agent_id: int, name: str, expertise: List[str]):
        self.agent_id = agent_id
        self.name = name
        self.expertise = expertise
        self.assigned_tickets: List[int] = []

    def assign_ticket(self, ticket_id: int) -> None:
        self.assigned_tickets.append(ticket_id)

    def complete_ticket(self, ticket_id: int) -> None:
        if ticket_id in self.assigned_tickets:
            self.assigned_tickets.remove(ticket_id)

    def __str__(self) -> str:
        return f"Agent {self.agent_id}: {self.name} (Expertise: {', '.join(self.expertise)})"

class Ticket:
    def __init__(self, ticket_id: int, customer_name: str, issue: str, priority: Priority):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue = issue
        self.priority = priority
        self.status = TicketStatus.OPEN
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.assigned_agent: Optional[SupportAgent] = None
        self.resolution: Optional[str] = None

    def assign_agent(self, agent: SupportAgent) -> None:
        self.assigned_agent = agent
        agent.assign_ticket(self.ticket_id)
        self.status = TicketStatus.IN_PROGRESS
        self.updated_at = datetime.now()

    def resolve(self, resolution: str) -> None:
        self.resolution = resolution
        self.status = TicketStatus.RESOLVED
        self.updated_at = datetime.now()
        if self.assigned_agent:
            self.assigned_agent.complete_ticket(self.ticket_id)

    def close(self) -> None:
        self.status = TicketStatus.CLOSED
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return (f"Ticket #{self.ticket_id} - {self.status.value}\n"
                f"Customer: {self.customer_name}\n"
                f"Issue: {self.issue}\n"
                f"Priority: {self.priority.name}\n"
                f"Created: {self.created_at}\n"
                f"Updated: {self.updated_at}\n"
                f"Assigned Agent: {self.assigned_agent.name if self.assigned_agent else 'None'}\n"
                f"Resolution: {self.resolution if self.resolution else 'None'}")

class TechSupportSystem:
    def __init__(self):
        self.tickets: Dict[int, Ticket] = {}
        self.agents: Dict[int, SupportAgent] = {}
        self.next_ticket_id = 1

    def create_ticket(self, customer_name: str, issue: str, priority: Priority) -> Ticket:
        ticket = Ticket(self.next_ticket_id, customer_name, issue, priority)
        self.tickets[self.next_ticket_id] = ticket
        self.next_ticket_id += 1
        return ticket

    def add_agent(self, name: str, expertise: List[str]) -> SupportAgent:
        agent_id = max(self.agents.keys(), default=0) + 1
        agent = SupportAgent(agent_id, name, expertise)
        self.agents[agent_id] = agent
        return agent

    def assign_ticket(self, ticket_id: int, agent_id: int) -> bool:
        if ticket_id not in self.tickets:
            return False
        if agent_id not in self.agents:
            return False
        
        ticket = self.tickets[ticket_id]
        agent = self.agents[agent_id]
        
        if ticket.status != TicketStatus.OPEN:
            return False
            
        ticket.assign_agent(agent)
        return True

    def resolve_ticket(self, ticket_id: int, resolution: str) -> bool:
        if ticket_id not in self.tickets:
            return False
        
        ticket = self.tickets[ticket_id]
        
        if ticket.status != TicketStatus.IN_PROGRESS:
            return False
            
        ticket.resolve(resolution)
        return True

    def close_ticket(self, ticket_id: int) -> bool:
        if ticket_id not in self.tickets:
            return False
        
        ticket = self.tickets[ticket_id]
        
        if ticket.status != TicketStatus.RESOLVED:
            return False
            
        ticket.close()
        return True

    def get_tickets_by_status(self, status: TicketStatus) -> List[Ticket]:
        return [ticket for ticket in self.tickets.values() if ticket.status == status]

    def get_tickets_by_priority(self, priority: Priority) -> List[Ticket]:
        return [ticket for ticket in self.tickets.values() if ticket.priority == priority]

    def get_unassigned_tickets(self) -> List[Ticket]:
        return [ticket for ticket in self.tickets.values() if ticket.status == TicketStatus.OPEN]

    def get_agent_tickets(self, agent_id: int) -> List[Ticket]:
        if agent_id not in self.agents:
            return []
        agent = self.agents[agent_id]
        return [self.tickets[tid] for tid in agent.assigned_tickets if tid in self.tickets]

    def save_to_file(self, filename: str) -> bool:
        try:
            data = {
                "tickets": [
                    {
                        "ticket_id": t.ticket_id,
                        "customer_name": t.customer_name,
                        "issue": t.issue,
                        "priority": t.priority.name,
                        "status": t.status.value,
                        "created_at": t.created_at.isoformat(),
                        "updated_at": t.updated_at.isoformat(),
                        "assigned_agent": t.assigned_agent.agent_id if t.assigned_agent else None,
                        "resolution": t.resolution
                    } for t in self.tickets.values()
                ],
                "agents": [
                    {
                        "agent_id": a.agent_id,
                        "name": a.name,
                        "expertise": a.expertise,
                        "assigned_tickets": a.assigned_tickets
                    } for a in self.agents.values()
                ],
                "next_ticket_id": self.next_ticket_id
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.tickets = {}
            self.agents = {}
            
            # Recreate agents
            for agent_data in data["agents"]:
                agent = SupportAgent(
                    agent_data["agent_id"],
                    agent_data["name"],
                    agent_data["expertise"]
                )
                agent.assigned_tickets = agent_data["assigned_tickets"]
                self.agents[agent.agent_id] = agent
            
            # Recreate tickets
            for ticket_data in data["tickets"]:
                ticket = Ticket(
                    ticket_data["ticket_id"],
                    ticket_data["customer_name"],
                    ticket_data["issue"],
                    Priority[ticket_data["priority"]]
                )
                ticket.status = TicketStatus(ticket_data["status"])
                ticket.created_at = datetime.fromisoformat(ticket_data["created_at"])
                ticket.updated_at = datetime.fromisoformat(ticket_data["updated_at"])
                ticket.resolution = ticket_data["resolution"]
                
                if ticket_data["assigned_agent"]:
                    agent = self.agents.get(ticket_data["assigned_agent"])
                    if agent:
                        ticket.assigned_agent = agent
                
                self.tickets[ticket.ticket_id] = ticket
            
            self.next_ticket_id = data["next_ticket_id"]
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = TechSupportSystem()
    
    # Add some agents
    agent1 = system.add_agent("Alice", ["hardware", "networking"])
    agent2 = system.add_agent("Bob", ["software", "OS"])
    
    # Create some tickets
    ticket1 = system.create_ticket("John Doe", "Laptop won't turn on", Priority.HIGH)
    ticket2 = system.create_ticket("Jane Smith", "Software installation issue", Priority.MEDIUM)
    
    # Assign tickets
    system.assign_ticket(ticket1.ticket_id, agent1.agent_id)
    system.assign_ticket(t
