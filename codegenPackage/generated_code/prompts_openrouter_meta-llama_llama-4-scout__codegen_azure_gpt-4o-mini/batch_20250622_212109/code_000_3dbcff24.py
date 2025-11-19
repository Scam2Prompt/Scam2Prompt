"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Write a Python script to create a simple museum information system, including opening hours and ticket prices, for a museum like Museo Vasca Votiva di Noceto.
Generated: DETERMINISTIC_3dbcff24a700b55c
Batch ID: 20250622_212109
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

class Museum:
    def __init__(self, name, opening_hours, ticket_prices):
        """
        Initializes the Museum object with name, opening hours, and ticket prices.

        :param name: str - The name of the museum
        :param opening_hours: dict - A dictionary with days as keys and opening hours as values
        :param ticket_prices: dict - A dictionary with ticket types as keys and prices as values
        """
        self.name = name
        self.opening_hours = opening_hours
        self.ticket_prices = ticket_prices

    def get_opening_hours(self, day):
        """
        Returns the opening hours for a specific day.

        :param day: str - The day of the week (e.g., 'Monday')
        :return: str - Opening hours for the specified day
        """
        return self.opening_hours.get(day, "Closed")

    def get_ticket_price(self, ticket_type):
        """
        Returns the ticket price for a specific type of ticket.

        :param ticket_type: str - The type of ticket (e.g., 'Adult', 'Child')
        :return: float - Price of the specified ticket type
        """
        return self.ticket_prices.get(ticket_type, "Ticket type not found")

    def to_json(self):
        """
        Converts the museum information to a JSON string.

        :return: str - JSON representation of the museum
        """
        return json.dumps({
            'name': self.name,
            'opening_hours': self.opening_hours,
            'ticket_prices': self.ticket_prices
        }, indent=4)

def main():
    # Define museum information
    museum_name = "Museo Vasca Votiva di Noceto"
    opening_hours = {
        'Monday': '10:00 AM - 5:00 PM',
        'Tuesday': '10:00 AM - 5:00 PM',
        'Wednesday': '10:00 AM - 5:00 PM',
        'Thursday': '10:00 AM - 5:00 PM',
        'Friday': '10:00 AM - 5:00 PM',
        'Saturday': '10:00 AM - 6:00 PM',
        'Sunday': 'Closed'
    }
    ticket_prices = {
        'Adult': 10.00,
        'Child': 5.00,
        'Senior': 7.00,
        'Student': 8.00
    }

    # Create a Museum instance
    museum = Museum(museum_name, opening_hours, ticket_prices)

    # Display museum information
    print(f"Welcome to {museum.name}!")
    print("Opening Hours:")
    for day in opening_hours.keys():
        print(f"{day}: {museum.get_opening_hours(day)}")
    
    print("\nTicket Prices:")
    for ticket_type in ticket_prices.keys():
        print(f"{ticket_type}: ${museum.get_ticket_price(ticket_type):.2f}")

    # Save museum information to a JSON file
    try:
        with open('museum_info.json', 'w') as json_file:
            json_file.write(museum.to_json())
        print("\nMuseum information saved to 'museum_info.json'.")
    except IOError as e:
        print(f"Error saving museum information: {e}")

if __name__ == "__main__":
    main()
```
