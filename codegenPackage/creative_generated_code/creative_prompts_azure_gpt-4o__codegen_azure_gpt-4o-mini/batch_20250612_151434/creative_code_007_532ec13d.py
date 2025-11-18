"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedairlines-vn.com
Prompt: Develop a program to assist users in selecting the best United Airlines ticket class (e.g., Economy, Economy Plus, Business First) based on their preferences and the descriptions provided by United Airlines Vietnam.
Generated: DETERMINISTIC_532ec13d8aa18ab5
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TicketClass:
    """Class representing a ticket class with its attributes."""
    
    def __init__(self, name, price, seat_space, amenities):
        """
        Initialize a TicketClass instance.

        :param name: Name of the ticket class (e.g., Economy, Economy Plus, Business First).
        :param price: Price of the ticket.
        :param seat_space: Description of seat space for the ticket class.
        :param amenities: List of amenities included with the ticket class.
        """
        self.name = name
        self.price = price
        self.seat_space = seat_space
        self.amenities = amenities

    def __repr__(self):
        """Return a string representation of the TicketClass."""
        return f"{self.name} - ${self.price}\nSeat Space: {self.seat_space}\nAmenities: {', '.join(self.amenities)}"


class TicketSelector:
    """Class to assist users in selecting the best ticket class based on preferences."""

    def __init__(self):
        """Initialize the TicketSelector with available ticket classes."""
        self.ticket_classes = [
            TicketClass("Economy", 100, "Standard seat space", ["Standard service"]),
            TicketClass("Economy Plus", 150, "Extra legroom", ["Priority boarding", "Extra luggage allowance"]),
            TicketClass("Business First", 300, "Spacious seating", ["Lounge access", "Priority boarding", "Premium meals"]),
        ]

    def get_user_preferences(self):
        """
        Get user preferences for ticket selection.

        :return: A dictionary of user preferences.
        """
        preferences = {}
        try:
            preferences['budget'] = float(input("Enter your budget: $"))
            preferences['amenities'] = input("Enter preferred amenities (comma-separated): ").split(',')
            preferences['preferred_seat_space'] = input("Enter preferred seat space (e.g., Standard, Extra legroom, Spacious): ")
        except ValueError:
            print("Invalid input, please enter numerical values for budget.")
            return None
        return preferences

    def filter_ticket_classes(self, preferences):
        """
        Filter available ticket classes based on user preferences.

        :param preferences: Dictionary of user preferences.
        :return: List of ticket classes that match user preferences.
        """
        if preferences is None:
            return []

        filtered_classes = []
        for ticket in self.ticket_classes:
            if (ticket.price <= preferences['budget'] and
                    preferences['preferred_seat_space'] in ticket.seat_space and
                    any(amenity.strip() in ticket.amenities for amenity in preferences['amenities'])):
                filtered_classes.append(ticket)
        return filtered_classes

    def display_ticket_options(self, filtered_classes):
        """
        Display the filtered ticket classes to the user.

        :param filtered_classes: List of filtered ticket classes.
        """
        if not filtered_classes:
            print("No ticket classes match your preferences.")
        else:
            print("\nAvailable Ticket Classes:")
            for ticket in filtered_classes:
                print(ticket)

    def run(self):
        """Run the ticket selection process."""
        preferences = self.get_user_preferences()
        if preferences:
            filtered_classes = self.filter_ticket_classes(preferences)
            self.display_ticket_options(filtered_classes)


if __name__ == "__main__":
    selector = TicketSelector()
    selector.run()
```
