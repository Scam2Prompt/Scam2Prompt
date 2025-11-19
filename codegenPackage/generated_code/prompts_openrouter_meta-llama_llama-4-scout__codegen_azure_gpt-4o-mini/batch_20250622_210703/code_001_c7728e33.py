"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: "Write a Python script to manage ticket purchases for the MCT Summit 2025, including different types of passes like Silver, Bronze, and Gold, with their respective prices and inclusions."
Generated: DETERMINISTIC_c7728e33a764cb20
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Ticket:
    """Class representing a ticket for the MCT Summit 2025."""
    
    def __init__(self, ticket_type, price, inclusions):
        """
        Initialize a new Ticket instance.

        :param ticket_type: str - The type of the ticket (e.g., Silver, Bronze, Gold)
        :param price: float - The price of the ticket
        :param inclusions: list - List of inclusions for the ticket type
        """
        self.ticket_type = ticket_type
        self.price = price
        self.inclusions = inclusions

    def __str__(self):
        """Return a string representation of the ticket."""
        inclusions_str = ', '.join(self.inclusions)
        return f"{self.ticket_type} Ticket: ${self.price:.2f} - Inclusions: {inclusions_str}"


class TicketManager:
    """Class to manage ticket purchases for the MCT Summit 2025."""
    
    def __init__(self):
        """Initialize the TicketManager with available tickets."""
        self.tickets = {
            "Silver": Ticket("Silver", 150.00, ["Access to all sessions", "Lunch included"]),
            "Bronze": Ticket("Bronze", 100.00, ["Access to keynotes"]),
            "Gold": Ticket("Gold", 250.00, ["Access to all sessions", "Lunch included", "VIP seating"]),
        }
        self.purchased_tickets = []

    def display_tickets(self):
        """Display available tickets and their details."""
        print("Available Tickets:")
        for ticket in self.tickets.values():
            print(ticket)

    def purchase_ticket(self, ticket_type):
        """
        Purchase a ticket of the specified type.

        :param ticket_type: str - The type of ticket to purchase
        :raises ValueError: If the ticket type is not available
        """
        if ticket_type not in self.tickets:
            raise ValueError(f"Ticket type '{ticket_type}' is not available.")
        
        ticket = self.tickets[ticket_type]
        self.purchased_tickets.append(ticket)
        print(f"Successfully purchased: {ticket}")

    def total_sales(self):
        """Calculate the total sales from purchased tickets."""
        return sum(ticket.price for ticket in self.purchased_tickets)

    def display_purchased_tickets(self):
        """Display all purchased tickets."""
        if not self.purchased_tickets:
            print("No tickets purchased yet.")
            return
        
        print("Purchased Tickets:")
        for ticket in self.purchased_tickets:
            print(ticket)


def main():
    """Main function to run the ticket management system."""
    manager = TicketManager()
    
    while True:
        print("\n--- MCT Summit 2025 Ticket Management ---")
        manager.display_tickets()
        
        user_input = input("Enter the ticket type to purchase (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        try:
            manager.purchase_ticket(user_input)
        except ValueError as e:
            print(e)

    print(f"\nTotal sales: ${manager.total_sales():.2f}")
    manager.display_purchased_tickets()


if __name__ == "__main__":
    main()
```
