"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Write a code example that integrates a booking system for party services, referencing the unique offerings of Wonderplanet.ee, including themed parties and special character appearances.
Generated: DETERMINISTIC_a016b2b208ad2bc4
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# party_booking_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class PartyTheme(Enum):
    """Enum for party themes"""
    SPACE_ADVENTURE = "Space Adventure"
    FAIRY_TALE = "Fairy Tale"
    SUPERHERO = "Superhero"

class CharacterAppearance(Enum):
    """Enum for character appearances"""
    ALIEN = "Alien"
    PRINCESS = "Princess"
    SUPERHERO = "Superhero"

class PartyService:
    """Class representing a party service"""
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

class BookingSystem:
    """Class representing a booking system"""
    def __init__(self):
        self.party_services: Dict[str, PartyService] = {}
        self.bookings: List[Dict] = []

    def add_party_service(self, service: PartyService):
        """Add a party service to the system"""
        self.party_services[service.name] = service

    def book_party(self, customer_name: str, party_theme: PartyTheme, 
                    character_appearance: CharacterAppearance, 
                    date: datetime, num_guests: int):
        """Book a party with the given details"""
        try:
            if party_theme not in [theme for theme in PartyTheme]:
                raise ValueError("Invalid party theme")
            if character_appearance not in [appearance for appearance in CharacterAppearance]:
                raise ValueError("Invalid character appearance")

            party_service = PartyService(
                f"{party_theme.value} with {character_appearance.value}",
                f"Themed party with {character_appearance.value} appearance",
                100.0  # default price
            )

            booking = {
                "customer_name": customer_name,
                "party_theme": party_theme.value,
                "character_appearance": character_appearance.value,
                "date": date,
                "num_guests": num_guests,
                "party_service": party_service.name,
                "total_price": party_service.price * num_guests
            }

            self.bookings.append(booking)
            return booking

        except Exception as e:
            print(f"Error booking party: {str(e)}")
            return None

    def get_bookings(self):
        """Get all bookings"""
        return self.bookings

def main():
    booking_system = BookingSystem()

    # Add party services
    booking_system.add_party_service(PartyService("Themed Party", "Themed party with decorations", 50.0))
    booking_system.add_party_service(PartyService("Character Appearance", "Character appearance with photo opportunity", 75.0))

    # Book a party
    customer_name = "John Doe"
    party_theme = PartyTheme.SPACE_ADVENTURE
    character_appearance = CharacterAppearance.ALIEN
    date = datetime(2024, 9, 17, 14, 0, 0)
    num_guests = 10

    booking = booking_system.book_party(customer_name, party_theme, character_appearance, date, num_guests)

    # Print bookings
    if booking:
        print("Booking successful:")
        print(f"Customer Name: {booking['customer_name']}")
        print(f"Party Theme: {booking['party_theme']}")
        print(f"Character Appearance: {booking['character_appearance']}")
        print(f"Date: {booking['date']}")
        print(f"Number of Guests: {booking['num_guests']}")
        print(f"Party Service: {booking['party_service']}")
        print(f"Total Price: ${booking['total_price']:.2f}")

    print("\nAll Bookings:")
    for booking in booking_system.get_bookings():
        print(f"Customer Name: {booking['customer_name']}")
        print(f"Party Theme: {booking['party_theme']}")
        print(f"Character Appearance: {booking['character_appearance']}")
        print(f"Date: {booking['date']}")
        print(f"Number of Guests: {booking['num_guests']}")
        print(f"Party Service: {booking['party_service']}")
        print(f"Total Price: ${booking['total_price']:.2f}")
        print("")

if __name__ == "__main__":
    main()
```
