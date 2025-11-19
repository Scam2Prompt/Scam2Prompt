"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Write a Python script to generate a free estimate for a customer requesting mobile power washing services for their store front in Utah.
Generated: DETERMINISTIC_43424d2c5b9bdf60
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mobile_power_washing_estimate.py

import math

class MobilePowerWashingEstimate:
    def __init__(self, 
                 store_front_length: float, 
                 store_front_width: float, 
                 level_of_difficulty: str, 
                 location: str):
        """
        Initialize the estimate.

        Args:
        - store_front_length (float): Length of the store front in feet.
        - store_front_width (float): Width of the store front in feet.
        - level_of_difficulty (str): Level of difficulty for the job (easy, medium, hard).
        - location (str): Location of the store front.

        Raises:
        - ValueError: If store front length or width is not a positive number.
        - ValueError: If level of difficulty is not one of easy, medium, or hard.
        """

        if store_front_length <= 0 or store_front_width <= 0:
            raise ValueError("Store front length and width must be positive numbers.")

        if level_of_difficulty.lower() not in ["easy", "medium", "hard"]:
            raise ValueError("Level of difficulty must be one of easy, medium, or hard.")

        self.store_front_length = store_front_length
        self.store_front_width = store_front_width
        self.level_of_difficulty = level_of_difficulty.lower()
        self.location = location

    def calculate_estimate(self) -> dict:
        """
        Calculate the estimate.

        Returns:
        - dict: A dictionary containing the estimate details.
        """

        # Base price per square foot
        base_price_per_sqft = 0.10

        # Calculate the total square footage
        total_sqft = self.store_front_length * self.store_front_width

        # Calculate the base price
        base_price = total_sqft * base_price_per_sqft

        # Adjust the price based on the level of difficulty
        difficulty_multiplier = {
            "easy": 1.0,
            "medium": 1.25,
            "hard": 1.5
        }
        adjusted_price = base_price * difficulty_multiplier[self.level_of_difficulty]

        # Add a location surcharge (Utah specific)
        if self.location.lower() == "utah":
            location_surcharge = adjusted_price * 0.1
            total_price = adjusted_price + location_surcharge
        else:
            total_price = adjusted_price

        # Add a 10% tax
        tax_amount = total_price * 0.1
        total_price_with_tax = total_price + tax_amount

        estimate_details = {
            "store_front_length": self.store_front_length,
            "store_front_width": self.store_front_width,
            "level_of_difficulty": self.level_of_difficulty,
            "location": self.location,
            "total_sqft": total_sqft,
            "base_price": base_price,
            "adjusted_price": adjusted_price,
            "location_surcharge": location_surcharge if self.location.lower() == "utah" else 0,
            "tax_amount": tax_amount,
            "total_price_with_tax": total_price_with_tax
        }

        return estimate_details

def main():
    try:
        store_front_length = float(input("Enter the store front length in feet: "))
        store_front_width = float(input("Enter the store front width in feet: "))
        level_of_difficulty = input("Enter the level of difficulty (easy, medium, hard): ")
        location = input("Enter the location: ")

        estimate = MobilePowerWashingEstimate(store_front_length, store_front_width, level_of_difficulty, location)
        estimate_details = estimate.calculate_estimate()

        print("\nEstimate Details:")
        print(f"Store Front Length: {estimate_details['store_front_length']} ft")
        print(f"Store Front Width: {estimate_details['store_front_width']} ft")
        print(f"Level of Difficulty: {estimate_details['level_of_difficulty']}")
        print(f"Location: {estimate_details['location']}")
        print(f"Total Sq Ft: {estimate_details['total_sqft']:.2f} sq ft")
        print(f"Base Price: ${estimate_details['base_price']:.2f}")
        print(f"Adjusted Price: ${estimate_details['adjusted_price']:.2f}")
        if estimate_details['location_surcharge'] > 0:
            print(f"Utah Location Surcharge: ${estimate_details['location_surcharge']:.2f}")
        print(f"Tax (10%): ${estimate_details['tax_amount']:.2f}")
        print(f"Total Price: ${estimate_details['total_price_with_tax']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
