"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Create a program that calculates travel discounts of up to 40% for students, as offered by Ikogwe International Limited, and applies the discount to a given airfare price.
Generated: DETERMINISTIC_8a3facbe13aa7f18
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TravelDiscountCalculator:
    """
    A class to calculate travel discounts for students offered by Ikogwe International Limited.
    The maximum discount available is 40%.
    """

    def __init__(self, airfare_price: float):
        """
        Initializes the TravelDiscountCalculator with the airfare price.

        :param airfare_price: The original price of the airfare.
        """
        if airfare_price < 0:
            raise ValueError("Airfare price must be non-negative.")
        self.airfare_price = airfare_price

    def calculate_discount(self, discount_percentage: float) -> float:
        """
        Calculates the discount based on the provided discount percentage.

        :param discount_percentage: The discount percentage to apply (max 40%).
        :return: The discounted price.
        """
        if discount_percentage < 0 or discount_percentage > 40:
            raise ValueError("Discount percentage must be between 0 and 40.")
        
        discount_amount = (discount_percentage / 100) * self.airfare_price
        discounted_price = self.airfare_price - discount_amount
        return discounted_price

    def apply_student_discount(self) -> float:
        """
        Applies the maximum student discount of 40% to the airfare price.

        :return: The price after applying the student discount.
        """
        return self.calculate_discount(40)


def main():
    """
    Main function to demonstrate the discount calculation.
    """
    try:
        # Example airfare price
        airfare_price = float(input("Enter the airfare price: $"))
        
        # Create an instance of TravelDiscountCalculator
        discount_calculator = TravelDiscountCalculator(airfare_price)
        
        # Calculate the discounted price
        discounted_price = discount_calculator.apply_student_discount()
        
        # Display the results
        print(f"Original Airfare Price: ${airfare_price:.2f}")
        print(f"Discounted Airfare Price for Students: ${discounted_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
