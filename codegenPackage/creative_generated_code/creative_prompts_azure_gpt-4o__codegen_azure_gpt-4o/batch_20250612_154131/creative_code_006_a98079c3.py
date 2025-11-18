"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Write a program to manage IT systems for small businesses, ensuring satisfaction and tailored customer service as guaranteed by uuip-hualdlugeen.
Generated: DETERMINISTIC_a98079c302d6d4b3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
IT System Management Program for Small Businesses
This program manages IT systems for small businesses, ensuring customer satisfaction and tailored services.
Features:
- Customer and system tracking
- Ticket management for IT issues
- Reporting tools for system health
"""

import json


class ITSystemManagement:
    def __init__(self):
        """
        Initialize ITSystemManagement with empty data structures for customers and tickets.
        """
        self.customers = {}  # Dictionary to store customer details
        self.tickets = {}  # Dictionary to store tickets for IT issues

    def add_customer(self, customer_id, name, email, contact_number):
        """
        Add a new customer to the system.

        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Customer's name.
            email (str): Customer's email address.
            contact_number (str): Customer's contact number.
        """
        if customer_id in self.customers:
            print(f"Error: Customer with ID {customer_id} already exists.")
            return

        self.customers[customer_id] = {
            "name": name,
            "email": email,
            "contact_number": contact_number,
        }
        print(f"Customer {name} with ID {customer_id} added successfully.")

    def create_ticket(self, ticket_id, customer_id, issue_description):
        """
        Create a new ticket for an IT issue.

        Args:
            ticket_id (str): Unique identifier for the ticket.
            customer_id (str): ID of the customer reporting the issue.
            issue_description (str): Description of the IT issue.
        """
        if ticket_id in self.tickets:
            print(f"Error: Ticket with ID {ticket_id} already exists.")
            return

        if customer_id not in self.customers:
            print(f"Error: No customer found with ID {customer_id}.")
            return

        self.tickets[ticket_id] = {
            "customer_id": customer_id,
            "issue_description": issue_description,
            "status": "Open",
        }
        print(f"Ticket {ticket_id} created successfully for customer ID {customer_id}.")

    def resolve_ticket(self, ticket_id):
        """
        Resolve an existing ticket.

        Args:
            ticket_id (str): Unique identifier for the ticket.
        """
        if ticket_id not in self.tickets:
            print(f"Error: No ticket found with ID {ticket_id}.")
            return

        self.tickets[ticket_id]["status"] = "Resolved"
        print(f"Ticket {ticket_id} resolved successfully.")

    def generate_report(self):
        """
        Generate a report of customers and tickets in the system.
        """
        print("\n--- IT System Report ---")
        print("\nCustomers:")
        for customer_id, details in self.customers.items():
            print(f"ID: {customer_id}, Name: {details['name']}, Email: {details['email']}, Contact: {details['contact_number']}")

        print("\nTickets:")
        for ticket_id, details in self.tickets.items():
            print(f"ID: {ticket_id}, Customer ID: {details['customer_id']}, Issue: {details['issue_description']}, Status: {details['status']}")


def main():
    """
    Main function to run the IT System Management program.
    """
    system = ITSystemManagement()

    # Adding customers
    system.add_customer("C001", "Alice Johnson", "alice@example.com", "555-1234")
    system.add_customer("C002", "Bob Smith", "bob@example.com", "555-5678")

    # Creating and resolving tickets
    system.create_ticket("T001", "C001", "Cannot connect to the internet.")
    system.create_ticket("T002", "C002", "Printer not working.")
    system.resolve_ticket("T001")

    # Generate system report
    system.generate_report()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
