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
import uuid
from datetime import datetime
from queue import PriorityQueue

class Ticket:
    """
    Represents a support ticket in the system.
    """
    def __init__(self, customer_name, issue_description, priority):
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ticket ID
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority  # Priority: 1 (High), 2 (Medium), 3 (Low)
        self.created_at = datetime.now()  # Timestamp for ticket creation

    def __str__(self):
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Issue: {self.issue_description}\n"
                f"Priority: {self.priority}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

class TechSupportSystem:
    """
    A tech support system for managing support tickets.
    """
    def __init__(self):
        self.ticket_queue = PriorityQueue()  # Priority queue for ticket management

    def create_ticket(self, customer_name, issue_description, priority):
        """
        Creates a new support ticket and adds it to the queue.
        """
        if priority not in [1, 2, 3]:
            raise ValueError("Priority must be 1 (High), 2 (Medium), or 3 (Low).")
        
        ticket = Ticket(customer_name, issue_description, priority)
        self.ticket_queue.put((priority, ticket))  # Add ticket to queue based on priority
        print(f"Ticket created successfully:\n{ticket}")

    def resolve_ticket(self):
        """
        Resolves the highest-priority ticket in the queue.
        """
        if self.ticket_queue.empty():
            print("No tickets to resolve.")
            return
        
        _, ticket = self.ticket_queue.get()  # Get the highest-priority ticket
        print(f"Resolving ticket:\n{ticket}")

    def view_tickets(self):
        """
        Displays all tickets in the queue sorted by priority.
        """
        if self.ticket_queue.empty():
            print("No tickets in the queue.")
            return
        
        print("Tickets in the queue:")
        temp_queue = PriorityQueue()
        
        while not self.ticket_queue.empty():
            priority, ticket = self.ticket_queue.get()
            print(ticket)
            print("-" * 40)
            temp_queue.put((priority, ticket))  # Re-add ticket to temporary queue
        
        self.ticket_queue = temp_queue  # Restore original queue

# Example usage
if __name__ == "__main__":
    support_system = TechSupportSystem()
    
    # Create tickets
    support_system.create_ticket("Alice", "Computer won't start", 1)
    support_system.create_ticket("Bob", "Software installation issue", 2)
    support_system.create_ticket("Charlie", "Slow internet connection", 3)
    
    # View tickets
    support_system.view_tickets()
    
    # Resolve tickets
    support_system.resolve_ticket()
    support_system.resolve_ticket()
    
    # View remaining tickets
    support_system.view_tickets()
```
