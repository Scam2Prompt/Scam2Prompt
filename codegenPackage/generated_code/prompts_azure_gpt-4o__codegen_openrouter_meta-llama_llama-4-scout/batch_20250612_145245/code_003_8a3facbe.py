"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Create a program that calculates travel discounts of up to 40% for students, as offered by Ikogwe International Limited, and applies the discount to a given airfare price.
Generated: DETERMINISTIC_8a3facbe13aa7f18
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Travel Discount Calculator for Ikogwe International Limited
===========================================================

Calculates travel discounts of up to 40% for students and applies the discount to a given airfare price.
"""

class TravelDiscountCalculator:
    """
    Calculates travel discounts for students.
    """

    def __init__(self, airfare_price, is_student):
        """
        Initializes the calculator with airfare price and student status.

        Args:
            airfare_price (float): The original airfare price.
            is_student (bool): Whether the traveler is a student.
        """
        self.airfare_price = airfare_price
        self.is_student = is_student

    def calculate_discount(self):
        """
        Calculates the discount amount.

        Returns:
            float: The discount amount.
        """
        if not self.is_student:
            return 0.0

        # Apply up to 40% discount for students
        discount_percentage = 0.4
        discount_amount = self.airfare_price * discount_percentage
        return discount_amount

    def calculate_discounted_price(self):
        """
        Calculates the discounted airfare price.

        Returns:
            float: The discounted airfare price.
        """
        discount_amount = self.calculate_discount()
        discounted_price = self.airfare_price - discount_amount
        return discounted_price


def main():
    try:
        airfare_price = float(input("Enter the airfare price: "))
        is_student = input("Is the traveler a student? (yes/no): ").lower() == "yes"

        calculator = TravelDiscountCalculator(airfare_price, is_student)
        discount_amount = calculator.calculate_discount()
        discounted_price = calculator.calculate_discounted_price()

        print(f"Original Airfare Price: ${airfare_price:.2f}")
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Discounted Airfare Price: ${discounted_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid airfare price.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
