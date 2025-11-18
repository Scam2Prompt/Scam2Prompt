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

class BookingSystem:
    def __init__(self):
        """Initialize the booking system with an empty list of bookings."""
        self.bookings = []

    def validate_credit_card(self, card_number):
        """
        Validate a credit card number using the Luhn algorithm.
        :param card_number: str, credit card number to validate.
        :return: bool, True if valid, False otherwise.
        """
        card_number = card_number.replace(" ", "")  # Remove spaces
        if not re.match(r"^\d{16}$", card_number):
            return False
        
        def luhn_checksum(card_num):
            """Calculate the Luhn checksum."""
            digits = [int(d) for d in card_num]
            for i in range(len(digits) - 2, -1, -2):
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9
            return sum(digits)
        
        return luhn_checksum(card_number) % 10 == 0

    def add_booking(self, name, item, deposit, credit_card):
        """
        Add a new booking to the system after validating inputs.
        :param name: str, name of the customer.
        :param item: str, item to be hired (police uniform or replica firearm).
        :param deposit: float, security deposit amount.
        :param credit_card: str, credit card number for validation.
        :return: str, success or error message.
        """
        if deposit <= 0:
            return "Error: Deposit amount must be greater than zero."
        
        if item.lower() not in ['police uniform', 'replica firearm']:
            return "Error: Item must be either 'police uniform' or 'replica firearm'."
        
        if not self.validate_credit_card(credit_card):
            return "Error: Invalid credit card number."
        
        booking = {
            "name": name,
            "item": item,
            "deposit": deposit,
            "credit_card": credit_card
        }
        self.bookings.append(booking)
        return f"Booking successful for {name}. Item: {item}, Deposit: ${deposit:.2f}"

    def view_bookings(self):
        """
        View all current bookings in the system.
        :return: list, all bookings.
        """
        return self.bookings.copy()


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Attempt to add a valid booking
    response = booking_system.add_booking(
        name="John Doe",
        item="Police Uniform",
        deposit=100.0,
        credit_card="4532015112830366"  # Example valid card number
    )
    print(response)

    # Attempt to add an invalid booking due to invalid credit card
    response = booking_system.add_booking(
        name="Jane Smith",
        item="Replica Firearm",
        deposit=50.0,
        credit_card="1234567890123456"  # Invalid card number
    )
    print(response)

    # View all bookings
    bookings = booking_system.view_bookings()
    print("Current Bookings:", bookings)
```
