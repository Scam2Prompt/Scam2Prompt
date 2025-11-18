"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to simulate a booking system for hiring police uniforms and replica firearms, incorporating a security deposit and credit card validation as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_68476c27c07004ca
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass

class CreditCard:
    """A class to represent a Credit Card for validation."""
    
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def is_valid(self) -> bool:
        """Validates the credit card number using the Luhn algorithm."""
        num = [int(d) for d in self.card_number if d.isdigit()]
        checksum = 0
        
        # Reverse the card number and process according to Luhn algorithm
        num.reverse()
        for i, digit in enumerate(num):
            if i % 2 == 1:  # Double every second digit
                digit *= 2
                if digit > 9:  # Subtract 9 if the result is greater than 9
                    digit -= 9
            checksum += digit
            
        return checksum % 10 == 0

class BookingSystem:
    """A class to manage the booking of police uniforms and replica firearms."""
    
    def __init__(self):
        self.uniforms_available = 10
        self.firearms_available = 5
        self.security_deposit = 200.00  # Security deposit amount

    def book_equipment(self, uniforms: int, firearms: int, credit_card: str) -> dict:
        """
        Book police uniforms and replica firearms.
        
        Args:
            uniforms (int): Number of uniforms to book.
            firearms (int): Number of firearms to book.
            credit_card (str): Credit card number for validation.

        Returns:
            dict: Confirmation of the booking and amount charged.

        Raises:
            BookingError: If there is an issue with booking.
        """
        # Validate the credit card
        cc = CreditCard(credit_card)
        if not cc.is_valid():
            raise BookingError("Invalid credit card number.")
        
        # Check availability
        if uniforms > self.uniforms_available or firearms > self.firearms_available:
            raise BookingError("Not enough equipment available for booking.")
        
        # Calculate total cost
        total_cost = (uniforms * 50) + (firearms * 100) + self.security_deposit
        
        # Update availability
        self.uniforms_available -= uniforms
        self.firearms_available -= firearms
        
        return {
            "message": "Booking successful.",
            "total_cost": total_cost,
            "remaining_uniforms": self.uniforms_available,
            "remaining_firearms": self.firearms_available
        }

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    try:
        # Attempt to book 2 uniforms and 1 firearm with a valid credit card
        booking_info = booking_system.book_equipment(2, 1, "4532015112830366")
        print(booking_info)
    except BookingError as e:
        print(f"Booking failed: {e}")
```
