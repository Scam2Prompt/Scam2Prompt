"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Create a script to simulate raising a ticket for browser-related issues, inspired by Arcler Desk's browser support services.
Generated: DETERMINISTIC_9e0423d745fda19f
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime
from enum import Enum

class Browser(Enum):
    CHROME = "Google Chrome"
    FIREFOX = "Mozilla Firefox"
    SAFARI = "Apple Safari"
    EDGE = "Microsoft Edge"
    OPERA = "Opera"
    BRAVE = "Brave"
    OTHER = "Other"

class IssueType(Enum):
    PERFORMANCE = "Performance"
    SECURITY = "Security"
    COMPATIBILITY = "Compatibility"
    UI = "User Interface"
    CRASH = "Crash/Freeze"
    OTHER = "Other"

class TicketStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class Ticket:
    def __init__(self, name: str, email: str, browser: Browser, issue_type: IssueType, description: str):
        self.ticket_id = self._generate_ticket_id()
        self.name = name
        self.email = email
        self.browser = browser
        self.issue_type = issue_type
        self.description = description
        self.status = TicketStatus.OPEN
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def _generate_ticket_id(self) -> str:
        return f"TKT-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

    def update_status(self, new_status: TicketStatus):
        self.status = new_status
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "ticket_id": self.ticket_id,
            "name": self.name,
            "email": self.email,
            "browser": self.browser.value,
            "issue_type": self.issue_type.value,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class TicketSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, name: str, email: str, browser: Browser, issue_type: IssueType, description: str) -> Ticket:
        if not name or not email or not description:
            raise ValueError("Name, email, and description are required fields")
        
        ticket = Ticket(name, email, browser, issue_type, description)
        self.tickets.append(ticket)
        return ticket

    def get_ticket(self, ticket_id: str) -> Ticket:
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        raise ValueError(f"Ticket with ID {ticket_id} not found")

    def update_ticket_status(self, ticket_id: str, new_status: TicketStatus) -> Ticket:
        ticket = self.get_ticket(ticket_id)
        ticket.update_status(new_status)
        return ticket

    def get_all_tickets(self) -> list:
        return [ticket.to_dict() for ticket in self.tickets]

    def save_to_file(self, filename: str = "tickets.json"):
        with open(filename, "w") as f:
            json.dump([ticket.to_dict() for ticket in self.tickets], f, indent=2)

    def load_from_file(self, filename: str = "tickets.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tickets = []
                for item in data:
                    ticket = Ticket(
                        name=item["name"],
                        email=item["email"],
                        browser=Browser(item["browser"]),
                        issue_type=IssueType(item["issue_type"]),
                        description=item["description"]
                    )
                    ticket.ticket_id = item["ticket_id"]
                    ticket.status = TicketStatus(item["status"])
                    ticket.created_at = item["created_at"]
                    ticket.updated_at = item["updated_at"]
                    self.tickets.append(ticket)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty ticket system.")
        except json.JSONDecodeError:
            print(f"Error decoding {filename}. Starting with empty ticket system.")

def display_menu():
    print("\nBrowser Support Ticket System")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Update ticket status")
    print("4. Save tickets to file")
    print("5. Load tickets from file")
    print("6. Exit")

def get_browser_choice() -> Browser:
    print("\nSelect browser:")
    for i, browser in enumerate(Browser, 1):
        print(f"{i}. {browser.value}")
    choice = int(input("Enter choice (1-7): "))
    return list(Browser)[choice-1]

def get_issue_type_choice() -> IssueType:
    print("\nSelect issue type:")
    for i, issue_type in enumerate(IssueType, 1):
        print(f"{i}. {issue_type.value}")
    choice = int(input("Enter choice (1-6): "))
    return list(IssueType)[choice-1]

def get_status_choice() -> TicketStatus:
    print("\nSelect new status:")
    for i, status in enumerate(TicketStatus, 1):
        print(f"{i}. {status.value}")
    choice = int(input("Enter choice (1-4): "))
    return list(TicketStatus)[choice-1]

def main():
    ticket_system = TicketSystem()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        try:
            if choice == "1":
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                browser = get_browser_choice()
                issue_type = get_issue_type_choice()
                description = input("Describe the issue: ")
                
                ticket = ticket_system.create_ticket(name, email, browser, issue_type, description)
                print(f"\nTicket created successfully! Ticket ID: {ticket.ticket_id}")
                
            elif choice == "2":
                tickets = ticket_system.get_all_tickets()
                if not tickets:
                    print("\nNo tickets found.")
                else:
                    print("\nAll Tickets:")
                    for ticket in tickets:
                        print(json.dumps(ticket, indent=2))
                        
            elif choice == "3":
                ticket_id = input("Enter ticket ID: ")
                new_status = get_status_choice()
                ticket = ticket_system.update_ticket_status(ticket_id, new_status)
                print(f"\nTicket {ticket_id} updated to {new_status.value}")
                
            elif choice == "4":
                ticket_system.save_to_file()
                print("\nTickets saved to file successfully.")
                
            elif choice == "5":
                ticket_system.load_from_file()
                print("\nTickets loaded from file successfully.")
                
            elif choice == "6":
                print("\nExiting...")
                break
                
            else:
                print("\nInvalid choice. Please try again.")
                
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
