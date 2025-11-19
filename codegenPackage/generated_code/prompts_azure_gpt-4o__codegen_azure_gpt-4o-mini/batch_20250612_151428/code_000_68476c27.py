"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to simulate a booking system for hiring police uniforms and replica firearms, incorporating a security deposit and credit card validation as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_68476c27c07004ca
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class CreditCard:
    """Class to represent a credit card and validate its number."""
    
    def __init__(self, card_number: str):
        self.card_number = card_number
        if not self.validate_card():
            raise BookingError("Invalid credit card number.")

    def validate_card(self) -> bool:
        """Validate the credit card number using the Luhn algorithm."""
        card_number = self.card_number.replace(" ", "")
        if not re.match(r'^\d{13,19}$', card_number):
            return False
        
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:  # Double every second digit
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

class Booking:
    """Class to handle the booking of police uniforms and replica firearms."""
    
    def __init__(self, customer_name: str, credit_card: CreditCard, deposit: float):
        self.customer_name = customer_name
        self.credit_card = credit_card
        self.deposit = deposit
        self.is_booked = False

    def book(self):
        """Simulate the booking process."""
        if self.is_booked:
            raise BookingError("This booking has already been made.")
        
        # Simulate booking logic (e.g., checking availability)
        if self.deposit < 100.0:
            raise BookingError("Deposit must be at least $100.")
        
        # Here you would typically check inventory and confirm the booking
        self.is_booked = True
        return f"Booking confirmed for {self.customer_name} with a deposit of ${self.deposit}."

def main():
    """Main function to run the booking system."""
    try:
        # Example customer details
        customer_name = "John Doe"
        credit_card_number = "4111 1111 1111 1111"  # Example valid card number
        deposit_amount = 150.0  # Example deposit
        
        # Create a credit card instance
        credit_card = CreditCard(credit_card_number)
        
        # Create a booking instance
        booking = Booking(customer_name, credit_card, deposit_amount)
        
        # Attempt to book
        confirmation = booking.book()
        print(confirmation)
        
    except BookingError as e:
        print(f"Booking failed: {e}")

if __name__ == "__main__":
    main()
```
