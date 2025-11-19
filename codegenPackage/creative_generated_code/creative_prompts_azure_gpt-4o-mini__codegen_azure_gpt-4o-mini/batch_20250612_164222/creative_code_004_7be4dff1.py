"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Construct a script that validates user input for booking a rental car, ensuring it checks for a valid driving license and credit card, as required by Agoda RentACar.
Generated: DETERMINISTIC_7be4dff16a12a0fd
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RentalCarBooking:
    def __init__(self):
        self.license_pattern = r'^[A-Za-z0-9]{5,20}$'  # Example pattern for a valid driving license
        self.credit_card_pattern = r'^\\d{4}-\\d{4}-\\d{4}-\\d{4}$'  # Example pattern for a valid credit card

    def validate_driving_license(self, license_number):
        """
        Validate the user's driving license.

        Parameters:
            license_number (str): The driving license number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if re.match(self.license_pattern, license_number):
            return True
        return False

    def validate_credit_card(self, credit_card_number):
        """
        Validate the user's credit card number.

        Parameters:
            credit_card_number (str): The credit card number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if re.match(self.credit_card_pattern, credit_card_number):
            return True
        return False

    def book_rental_car(self, license_number, credit_card_number):
        """
        Book a rental car after validating user input.

        Parameters:
            license_number (str): The driving license number.
            credit_card_number (str): The credit card number.

        Returns:
            str: Confirmation message if booking is successful, or an error message.
        """
        try:
            if not self.validate_driving_license(license_number):
                return "Error: Invalid driving license number."
            if not self.validate_credit_card(credit_card_number):
                return "Error: Invalid credit card number."
            # Proceed with booking logic (omitted for brevity)
            return "Booking successful! Your rental car is confirmed."
        except Exception as e:
            return f"An error occurred during the booking process: {str(e)}"

if __name__ == "__main__":
    booking = RentalCarBooking()
    # Sample user input (these would ideally come from a user interface)
    user_license = input("Enter your driving license number: ")
    user_credit_card = input("Enter your credit card number (format: XXXX-XXXX-XXXX-XXXX): ")

    # Attempt the booking
    result = booking.book_rental_car(user_license, user_credit_card)
    print(result)
```
