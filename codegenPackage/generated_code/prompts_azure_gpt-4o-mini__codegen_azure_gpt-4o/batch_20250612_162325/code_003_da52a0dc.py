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
class RentalCostCalculator:
    """
    A class to calculate rental costs for staging furniture and décor
    based on the pricing model of Unique Home Staging.
    """

    def __init__(self, base_rental_rate, daily_rate, damage_fee_rate=0.05):
        """
        Initialize the calculator with pricing details.

        :param base_rental_rate: The base rental rate (flat fee) in dollars.
        :param daily_rate: The daily rental rate in dollars.
        :param damage_fee_rate: The percentage of the total cost charged as a damage fee (default is 5%).
        """
        self.base_rental_rate = base_rental_rate
        self.daily_rate = daily_rate
        self.damage_fee_rate = damage_fee_rate

    def calculate_rental_cost(self, num_items, rental_days, apply_damage_fee=False):
        """
        Calculate the total rental cost.

        :param num_items: The number of items being rented.
        :param rental_days: The number of days the items are rented for.
        :param apply_damage_fee: Whether to apply the damage fee (default is False).
        :return: The total rental cost in dollars.
        """
        if num_items <= 0:
            raise ValueError("Number of items must be greater than zero.")
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        # Calculate the base cost and daily rental cost
        base_cost = self.base_rental_rate * num_items
        daily_cost = self.daily_rate * num_items * rental_days

        # Calculate the total cost
        total_cost = base_cost + daily_cost

        # Apply damage fee if applicable
        if apply_damage_fee:
            damage_fee = total_cost * self.damage_fee_rate
            total_cost += damage_fee

        return round(total_cost, 2)  # Round to 2 decimal places for currency

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with pricing details
        calculator = RentalCostCalculator(base_rental_rate=50, daily_rate=10)

        # Calculate rental cost
        total_cost = calculator.calculate_rental_cost(num_items=5, rental_days=7, apply_damage_fee=True)
        print(f"Total Rental Cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
