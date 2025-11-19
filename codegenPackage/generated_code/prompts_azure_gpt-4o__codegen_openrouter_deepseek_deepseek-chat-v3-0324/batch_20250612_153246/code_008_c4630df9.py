"""
Generated Code Metadata:
========================
Original URL: https://globalhospitalitysolution.com
Prompt: Write a function to generate quotes for hotel room bookings, banquet packages, and A/V solutions, referencing the services provided by Global Hospitality Solution.
Generated: DETERMINISTIC_c4630df9a7c4a7ab
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Union

class GlobalHospitalitySolution:
    """
    A class to generate quotes for hotel room bookings, banquet packages, and A/V solutions.
    """
    
    def __init__(self):
        # Sample data for quotes
        self._room_types = [
            {"name": "Standard Room", "base_price": 150, "description": "Comfortable room with basic amenities"},
            {"name": "Deluxe Room", "base_price": 250, "description": "Spacious room with premium amenities"},
            {"name": "Suite", "base_price": 400, "description": "Luxurious suite with separate living area"}
        ]
        
        self._banquet_packages = [
            {"name": "Basic Package", "base_price": 30, "description": "Includes standard seating and basic menu"},
            {"name": "Premium Package", "base_price": 60, "description": "Includes premium seating and gourmet menu"},
            {"name": "Platinum Package", "base_price": 100, "description": "Includes VIP seating and chef's special menu"}
        ]
        
        self._av_solutions = [
            {"name": "Basic A/V Setup", "base_price": 200, "description": "Includes projector and sound system"},
            {"name": "Advanced A/V Setup", "base_price": 500, "description": "Includes HD projector, surround sound, and lighting"},
            {"name": "Full Production Setup", "base_price": 1000, "description": "Includes stage, professional lighting, and live streaming"}
        ]
        
        self._discounts = {
            "corporate": 0.15,  # 15% discount for corporate clients
            "long_stay": 0.10,  # 10% discount for stays longer than 7 days
            "bulk_event": 0.20  # 20% discount for bulk event bookings
        }
    
    def _calculate_total(self, base_price: float, quantity: int, discount_code: Optional[str] = None) -> float:
        """
        Calculate the total price after applying discounts if applicable.
        
        Args:
            base_price: The base price per unit.
            quantity: The number of units.
            discount_code: Optional discount code to apply.
            
        Returns:
            The total price after discounts.
        """
        total = base_price * quantity
        
        if discount_code and discount_code in self._discounts:
            total *= (1 - self._discounts[discount_code])
        
        return round(total, 2)
    
    def generate_room_quote(
        self,
        room_type: str,
        nights: int,
        guests: int,
        discount_code: Optional[str] = None
    ) -> Dict[str, Union[str, float]]:
        """
        Generate a quote for a hotel room booking.
        
        Args:
            room_type: Type of room (Standard, Deluxe, Suite).
            nights: Number of nights.
            guests: Number of guests.
            discount_code: Optional discount code.
            
        Returns:
            A dictionary containing quote details.
            
        Raises:
            ValueError: If room type is invalid.
        """
        room = next((r for r in self._room_types if r["name"].lower() == room_type.lower()), None)
        
        if not room:
            raise ValueError(f"Invalid room type: {room_type}")
        
        total = self._calculate_total(room["base_price"], nights, discount_code)
        
        return {
            "service": "Hotel Room Booking",
            "room_type": room["name"],
            "description": room["description"],
            "nights": nights,
            "guests": guests,
            "base_price_per_night": room["base_price"],
            "total_price": total,
            "discount_applied": discount_code if discount_code else "None"
        }
    
    def generate_banquet_quote(
        self,
        package: str,
        attendees: int,
        discount_code: Optional[str] = None
    ) -> Dict[str, Union[str, float]]:
        """
        Generate a quote for a banquet package.
        
        Args:
            package: Type of banquet package (Basic, Premium, Platinum).
            attendees: Number of attendees.
            discount_code: Optional discount code.
            
        Returns:
            A dictionary containing quote details.
            
        Raises:
            ValueError: If package is invalid.
        """
        banquet = next((b for b in self._banquet_packages if b["name"].lower() == package.lower()), None)
        
        if not banquet:
            raise ValueError(f"Invalid banquet package: {package}")
        
        total = self._calculate_total(banquet["base_price"], attendees, discount_code)
        
        return {
            "service": "Banquet Package",
            "package": banquet["name"],
            "description": banquet["description"],
            "attendees": attendees,
            "base_price_per_person": banquet["base_price"],
            "total_price": total,
            "discount_applied": discount_code if discount_code else "None"
        }
    
    def generate_av_quote(
        self,
        av_setup: str,
        hours: int,
        discount_code: Optional[str] = None
    ) -> Dict[str, Union[str, float]]:
        """
        Generate a quote for an A/V solution.
        
        Args:
            av_setup: Type of A/V setup (Basic, Advanced, Full Production).
            hours: Number of hours required.
            discount_code: Optional discount code.
            
        Returns:
            A dictionary containing quote details.
            
        Raises:
            ValueError: If A/V setup is invalid.
        """
        av = next((a for a in self._av_solutions if a["name"].lower() == av_setup.lower()), None)
        
        if not av:
            raise ValueError(f"Invalid A/V setup: {av_setup}")
        
        total = self._calculate_total(av["base_price"], hours, discount_code)
        
        return {
            "service": "A/V Solution",
            "setup": av["name"],
            "description": av["description"],
            "hours": hours,
            "base_price_per_hour": av["base_price"],
            "total_price": total,
            "discount_applied": discount_code if discount_code else "None"
        }
    
    def generate_combo_quote(
        self,
        room_type: str,
        nights: int,
        guests: int,
        package: str,
        attendees: int,
        av_setup: str,
        hours: int,
        discount_code: Optional[str] = None
    ) -> Dict[str, Union[str, float, Dict]]:
        """
        Generate a combined quote for room, banquet, and A/V services.
        
        Args:
            room_type: Type of room.
            nights: Number of nights.
            guests: Number of guests.
            package: Banquet package.
            attendees: Number of attendees.
            av_setup: A/V setup.
            hours: Number of hours.
            discount_code: Optional discount code.
            
        Returns:
            A dictionary containing combined quote details.
        """
        room_quote = self.generate_room_quote(room_type, nights, guests, discount_code)
        banquet_quote = self.generate_banquet_quote(package, attendees, discount_code)
        av_quote = self.generate_av_quote(av_setup, hours, discount_code)
        
        total = room_quote["total_price"] + banquet_quote["total_price"] + av_quote["total_price"]
        
        return {
            "service": "Combo Package",
            "room_quote": room_quote,
            "banquet_quote": banquet_quote,
            "av_quote": av_quote,
            "total_price": total,
            "discount_applied": discount_code if discount_code else "None"
        }
```
