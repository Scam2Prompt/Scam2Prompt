"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Create a function that calculates the rental costs for staging furniture and décor based on the pricing model of Unique Home Staging.
Generated: DETERMINISTIC_da52a0dc910ac1d2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RentalCostCalculator:
    """
    A class to calculate the rental costs for staging furniture and décor
    based on the Unique Home Staging pricing model.
    """
    
    def __init__(self, daily_rate, minimum_rental_days):
        """
        Initializes the calculator with a daily rate and a minimum rental period.
        
        :param daily_rate: The cost of renting items per day.
        :param minimum_rental_days: The minimum number of rental days.
        """
        if daily_rate < 0:
            raise ValueError("Daily rate must be a non-negative value.")
        if minimum_rental_days < 1:
            raise ValueError("Minimum rental days must be at least 1.")
        
        self.daily_rate = daily_rate
        self.minimum_rental_days = minimum_rental_days

    def calculate_total_cost(self, rental_days):
        """
        Calculates the total rental cost based on the number of days rented.
        
        :param rental_days: The number of days the items are rented.
        :return: Total rental cost.
        """
        if rental_days < 0:
            raise ValueError("Rental days must be a non-negative value.")
        
        # Ensure the rental days meet the minimum requirement
        effective_days = max(rental_days, self.minimum_rental_days)
        total_cost = effective_days * self.daily_rate
        
        return total_cost


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the rental calculator with a daily rate of $50 and a minimum rental of 3 days
        calculator = RentalCostCalculator(daily_rate=50.0, minimum_rental_days=3)
        
        # Calculate the total cost for a rental period of 5 days
        rental_days = 5
        total_cost = calculator.calculate_total_cost(rental_days)
        print(f"Total rental cost for {rental_days} days: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
