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
import datetime
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, Field


class PartyTheme(str, Enum):
    """Enum representing available party themes from Wonderplanet.ee"""
    PRINCESS = "Princess Party"
    SUPERHERO = "Superhero Adventure"
    PIRATE = "Pirate Treasure Hunt"
    UNICORN = "Magical Unicorn"
    DINOSAUR = "Dinosaur Discovery"


class CharacterAppearance(str, Enum):
    """Enum representing special character appearances"""
    ELSA = "Queen Elsa"
    SPIDERMAN = "Spider-Man"
    CAPTAIN_JACK = "Captain Jack Sparrow"
    UNICORN_MASTER = "Unicorn Master"
    T_REX = "T-Rex Explorer"


class BookingRequest(BaseModel):
    """Request model for party booking"""
    customer_name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    phone: str = Field(..., min_length=5, max_length=20)
    party_date: datetime.date
    party_theme: PartyTheme
    character_appearances: List[CharacterAppearance] = []
    number_of_children: int = Field(..., gt=0, le=30)
    special_requests: Optional[str] = Field(None, max_length=500)

    @validator('party_date')
    def validate_party_date(cls, value):
        if value < datetime.date.today():
            raise ValueError("Party date cannot be in the past")
        if value > datetime.date.today() + datetime.timedelta(days=365):
            raise ValueError("Bookings can only be made up to 1 year in advance")
        return value


class BookingConfirmation(BaseModel):
    """Response model for confirmed booking"""
    booking_id: str
    customer_name: str
    party_date: datetime.date
    party_theme: PartyTheme
    character_appearances: List[CharacterAppearance]
    total_price: float
    confirmation_message: str


class BookingSystem:
    """Main booking system class for Wonderplanet.ee party services"""
    
    def __init__(self):
        self._bookings: Dict[str, BookingRequest] = {}
        self._theme_prices = {
            PartyTheme.PRINCESS: 299.99,
            PartyTheme.SUPERHERO: 349.99,
            PartyTheme.PIRATE: 279.99,
            PartyTheme.UNICORN: 329.99,
            PartyTheme.DINOSAUR: 379.99
        }
        self._character_prices = {
            CharacterAppearance.ELSA: 99.99,
            CharacterAppearance.SPIDERMAN: 119.99,
            CharacterAppearance.CAPTAIN_JACK: 109.99,
            CharacterAppearance.UNICORN_MASTER: 89.99,
            CharacterAppearance.T_REX: 129.99
        }

    def _generate_booking_id(self) -> str:
        """Generate a unique booking ID"""
        return f"WONDER-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def _calculate_total_price(self, booking: BookingRequest) -> float:
        """Calculate total price based on theme and character appearances"""
        base_price = self._theme_prices[booking.party_theme]
        character_price = sum(
            self._character_prices[character] 
            for character in booking.character_appearances
        )
        return base_price + character_price

    def create_booking(self, booking_request: BookingRequest) -> BookingConfirmation:
        """Create a new party booking"""
        booking_id = self._generate_booking_id()
        total_price = self._calculate_total_price(booking_request)
        
        self._bookings[booking_id] = booking_request
        
        return BookingConfirmation(
            booking_id=booking_id,
            customer_name=booking_request.customer_name,
            party_date=booking_request.party_date,
            party_theme=booking_request.party_theme,
            character_appearances=booking_request.character_appearances,
            total_price=total_price,
            confirmation_message=(
                f"Thank you for booking with Wonderplanet.ee! "
                f"Your {booking_request.party_theme.value} is confirmed for "
                f"{booking_request.party_date.strftime('%B %d, %Y')}. "
                f"Get ready for an unforgettable adventure!"
            )
        )

    def get_booking(self, booking_id: str) -> Optional[BookingRequest]:
        """Retrieve booking details by ID"""
        return self._bookings.get(booking_id)

    def get_available_themes(self) -> List[PartyTheme]:
        """Get list of all available party themes"""
        return list(PartyTheme)

    def get_available_characters(self) -> List[CharacterAppearance]:
        """Get list of all available character appearances"""
        return list(CharacterAppearance)


# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    
    try:
        booking_request = BookingRequest(
            customer_name="Anna Smith",
            email="anna.smith@example.com",
            phone="+3721234567",
            party_date=datetime.date.today() + datetime.timedelta(days=30),
            party_theme=PartyTheme.PRINCESS,
            character_appearances=[CharacterAppearance.ELSA],
            number_of_children=10,
            special_requests="Please include gluten-free cake options"
        )
        
        confirmation = system.create_booking(booking_request)
        print(confirmation.json(indent=2))
        
    except ValueError as e:
        print(f"Booking error: {e}")
```
