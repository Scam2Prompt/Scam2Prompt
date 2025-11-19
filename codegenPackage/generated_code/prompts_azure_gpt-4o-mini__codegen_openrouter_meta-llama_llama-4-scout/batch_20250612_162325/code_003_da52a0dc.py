"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Create a function that calculates the rental costs for staging furniture and décor based on the pricing model of Unique Home Staging.
Generated: DETERMINISTIC_da52a0dc910ac1d2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# unique_home_staging.py

class UniqueHomeStaging:
    """
    Calculates rental costs for staging furniture and décor based on the pricing model of Unique Home Staging.
    """

    def __init__(self, 
                 furniture_rental_rate: float, 
                 decor_rental_rate: float, 
                 delivery_fee: float, 
                 installation_fee: float):
        """
        Initializes the UniqueHomeStaging calculator.

        Args:
        - furniture_rental_rate (float): The daily rental rate for furniture.
        - decor_rental_rate (float): The daily rental rate for décor.
        - delivery_fee (float): The one-time delivery fee.
        - installation_fee (float): The one-time installation fee.
        """
        self.furniture_rental_rate = furniture_rental_rate
        self.decor_rental_rate = decor_rental_rate
        self.delivery_fee = delivery_fee
        self.installation_fee = installation_fee

    def calculate_rental_cost(self, 
                              num_furniture_items: int, 
                              num_decor_items: int, 
                              rental_days: int) -> dict:
        """
        Calculates the total rental cost.

        Args:
        - num_furniture_items (int): The number of furniture items.
        - num_decor_items (int): The number of décor items.
        - rental_days (int): The number of days for rental.

        Returns:
        - dict: A dictionary containing the total rental cost and breakdown.

        Raises:
        - ValueError: If any input value is invalid (negative or zero).
        """
        if num_furniture_items < 0 or num_decor_items < 0 or rental_days < 0:
            raise ValueError("Input values must be non-negative.")

        furniture_rental_cost = num_furniture_items * self.furniture_rental_rate * rental_days
        decor_rental_cost = num_decor_items * self.decor_rental_rate * rental_days
        total_rental_cost = furniture_rental_cost + decor_rental_cost + self.delivery_fee + self.installation_fee

        return {
            "furniture_rental_cost": furniture_rental_cost,
            "decor_rental_cost": decor_rental_cost,
            "delivery_fee": self.delivery_fee,
            "installation_fee": self.installation_fee,
            "total_rental_cost": total_rental_cost
        }


def main():
    try:
        # Example usage:
        calculator = UniqueHomeStaging(
            furniture_rental_rate=50.0, 
            decor_rental_rate=20.0, 
            delivery_fee=100.0, 
            installation_fee=200.0
        )

        rental_cost_breakdown = calculator.calculate_rental_cost(
            num_furniture_items=5, 
            num_decor_items=10, 
            rental_days=14
        )

        print("Rental Cost Breakdown:")
        for key, value in rental_cost_breakdown.items():
            print(f"{key.capitalize().replace('_', ' ')}: ${value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
