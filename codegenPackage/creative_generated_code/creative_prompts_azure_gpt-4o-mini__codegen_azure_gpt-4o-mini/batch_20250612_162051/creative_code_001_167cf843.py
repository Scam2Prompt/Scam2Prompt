"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.reliableridesllc.org
Prompt: Write a function that calculates the rental price per day for a vehicle based on the model and any applicable discounts, inspired by the pricing structure of Reliable Rides LLC.
Generated: DETERMINISTIC_167cf843b1e1129e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vehicle:
    """Class representing a vehicle with a model and base rental price."""

    def __init__(self, model: str, base_price: float):
        """
        Initialize the Vehicle with the model and base rental price.

        Args:
            model (str): The model of the vehicle.
            base_price (float): The base rental price per day.
        """
        self.model = model
        self.base_price = base_price

    def calculate_rental_price_per_day(self, discount_percentage: float = 0) -> float:
        """
        Calculate the rental price per day after applying any discounts.

        Args:
            discount_percentage (float): The discount percentage to apply (default is 0).

        Returns:
            float: The final rental price per day after applying the discount.

        Raises:
            ValueError: If base price or discount percentage is negative.
        """
        if self.base_price < 0:
            raise ValueError("Base price cannot be negative.")
        if discount_percentage < 0:
            raise ValueError("Discount percentage cannot be negative.")

        # Calculate the discount amount
        discount_amount = (discount_percentage / 100) * self.base_price
        
        # Calculate final price after discount
        final_price = self.base_price - discount_amount
        
        return final_price


def main():
    """Main function to demonstrate the rental price calculation."""
    try:
        # Example vehicle models and their base prices
        vehicles = [
            Vehicle("Economy Car", 30.00),
            Vehicle("Luxury Sedan", 75.00),
            Vehicle("SUV", 50.00)
        ]

        # Calculate and display rental prices with various discounts
        for vehicle in vehicles:
            print(f"Model: {vehicle.model}")
            for discount in [0, 10, 20]:  # Testing with no discount, 10% and 20% discounts
                rental_price = vehicle.calculate_rental_price_per_day(discount)
                print(f"  Rental price with {discount}% discount: ${rental_price:.2f}")
    
    except ValueError as e:
        print(f"Error calculating rental price: {e}")


if __name__ == "__main__":
    main()
```
