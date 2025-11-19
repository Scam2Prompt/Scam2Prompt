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
"""
Museum Information System
This script provides information about the museum's opening hours and ticket prices.
"""

import sys

class Museum:
    def __init__(self, name, opening_hours, ticket_prices):
        """
        Initialize the Museum object.

        :param name: Name of the museum
        :param opening_hours: Dictionary containing opening hours for each day
        :param ticket_prices: Dictionary containing ticket prices for different categories
        """
        self.name = name
        self.opening_hours = opening_hours
        self.ticket_prices = ticket_prices

    def get_opening_hours(self, day):
        """
        Get the opening hours for a specific day.

        :param day: Day of the week (e.g., 'Monday')
        :return: Opening hours for the specified day or a message if the museum is closed
        """
        return self.opening_hours.get(day, "Closed")

    def get_ticket_price(self, category):
        """
        Get the ticket price for a specific category.

        :param category: Ticket category (e.g., 'Adult', 'Child', 'Senior')
        :return: Ticket price for the specified category or a message if the category is invalid
        """
        return self.ticket_prices.get(category, "Invalid ticket category")

def main():
    """
    Main function to run the Museum Information System.
    """
    # Museum data
    museum_name = "Museo Vasca Votiva di Noceto"
    opening_hours = {
        "Monday": "9:00 AM - 5:00 PM",
        "Tuesday": "9:00 AM - 5:00 PM",
        "Wednesday": "9:00 AM - 5:00 PM",
        "Thursday": "9:00 AM - 5:00 PM",
        "Friday": "9:00 AM - 5:00 PM",
        "Saturday": "10:00 AM - 6:00 PM",
        "Sunday": "10:00 AM - 6:00 PM"
    }
    ticket_prices = {
        "Adult": 15.00,
        "Child": 8.00,
        "Senior": 10.00,
        "Student": 12.00
    }

    # Create Museum object
    museum = Museum(museum_name, opening_hours, ticket_prices)

    # User interaction
    print(f"Welcome to {museum.name} Information System!")
    while True:
        print("\nOptions:")
        print("1. Check opening hours")
        print("2. Check ticket prices")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            day = input("Enter the day of the week (e.g., 'Monday'): ").capitalize()
            hours = museum.get_opening_hours(day)
            print(f"Opening hours on {day}: {hours}")
        elif choice == 2:
            category = input("Enter ticket category (e.g., 'Adult', 'Child', 'Senior', 'Student'): ").capitalize()
            price = museum.get_ticket_price(category)
            if isinstance(price, float):
                print(f"Ticket price for {category}: ${price:.2f}")
            else:
                print(price)
        elif choice == 3:
            print("Thank you for using the Museum Information System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
