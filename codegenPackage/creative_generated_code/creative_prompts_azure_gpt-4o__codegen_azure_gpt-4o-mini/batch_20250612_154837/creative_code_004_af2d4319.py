"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Develop a program to optimize customer service workflows, incorporating techniques from Master-Brain's customer service training.
Generated: DETERMINISTIC_af2d4319869d13e5
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomerServiceWorkflow:
    def __init__(self):
        self.tickets = []  # List to hold customer service tickets
        self.resolved_tickets = []  # List to hold resolved tickets

    def create_ticket(self, customer_name, issue_description):
        """
        Create a new customer service ticket.

        :param customer_name: Name of the customer
        :param issue_description: Description of the customer's issue
        """
        ticket = {
            "id": len(self.tickets) + 1,
            "customer_name": customer_name,
            "issue_description": issue_description,
            "created_at": datetime.now(),
            "status": "Open"
        }
        self.tickets.append(ticket)
        logging.info(f"Ticket created: {ticket}")

    def resolve_ticket(self, ticket_id):
        """
        Resolve a customer service ticket.

        :param ticket_id: ID of the ticket to resolve
        """
        for ticket in self.tickets:
            if ticket["id"] == ticket_id and ticket["status"] == "Open":
                ticket["status"] = "Resolved"
                ticket["resolved_at"] = datetime.now()
                self.resolved_tickets.append(ticket)
                self.tickets.remove(ticket)
                logging.info(f"Ticket resolved: {ticket}")
                return
        logging.warning(f"Ticket ID {ticket_id} not found or already resolved.")

    def get_open_tickets(self):
        """
        Return a list of open tickets.

        :return: List of open tickets
        """
        open_tickets = [ticket for ticket in self.tickets if ticket["status"] == "Open"]
        logging.info(f"Open tickets retrieved: {len(open_tickets)}")
        return open_tickets

    def get_resolved_tickets(self):
        """
        Return a list of resolved tickets.
        
        :return: List of resolved tickets
        """
        logging.info(f"Resolved tickets retrieved: {len(self.resolved_tickets)}")
        return self.resolved_tickets

    def load_tickets(self, file_path):
        """
        Load tickets from a JSON file.

        :param file_path: Path to the JSON file
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.tickets = data.get("tickets", [])
                self.resolved_tickets = data.get("resolved_tickets", [])
                logging.info("Tickets loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File {file_path} not found.")
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def save_tickets(self, file_path):
        """
        Save tickets to a JSON file.

        :param file_path: Path to the JSON file
        """
        try:
            data = {
                "tickets": self.tickets,
                "resolved_tickets": self.resolved_tickets
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, default=str)
                logging.info("Tickets saved successfully.")
        except Exception as e:
            logging.error(f"An error occurred while saving tickets: {e}")

# Example usage
if __name__ == "__main__":
    workflow = CustomerServiceWorkflow()
    workflow.create_ticket("Alice Johnson", "Issue with product delivery.")
    workflow.create_ticket("Bob Smith", "Need help with account login.")
    print(workflow.get_open_tickets())  # Display open tickets
    workflow.resolve_ticket(1)  # Resolve ticket with ID 1
    print(workflow.get_resolved_tickets())  # Display resolved tickets
    workflow.save_tickets("tickets.json")  # Save tickets to a file
    workflow.load_tickets("tickets.json")  # Load tickets from a file
```
