"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Develop a function that calculates the total cost for a 4-day safari tour in Ol Pejeta, including accommodation, meals, and park fees.
Generated: DETERMINISTIC_b4df901336cc8317
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SafariTour:
    def __init__(self, daily_accommodation_cost, daily_meal_cost, park_fee_per_day):
        """
        Initialize the SafariTour with costs for accommodation, meals, and park fees.

        Parameters:
            daily_accommodation_cost (float): Daily cost for accommodation.
            daily_meal_cost (float): Daily cost for meals.
            park_fee_per_day (float): Daily park fee.
        """
        self.daily_accommodation_cost = daily_accommodation_cost
        self.daily_meal_cost = daily_meal_cost
        self.park_fee_per_day = park_fee_per_day

    def calculate_total_cost(self, days=4):
        """
        Calculate the total cost of the safari tour.

        Parameters:
            days (int): Number of days for the safari tour. Default is 4.

        Returns:
            float: Total cost for the safari tour.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")

        # Calculate individual costs
        accommodation_cost = self.daily_accommodation_cost * days
        meals_cost = self.daily_meal_cost * days
        park_fees = self.park_fee_per_day * days

        # Calculate total cost
        total_cost = accommodation_cost + meals_cost + park_fees
        
        return total_cost


# Example usage
if __name__ == "__main__":
    # Define costs per day
    daily_accommodation = 100.0  # Example cost for accommodation per day
    daily_meal = 50.0             # Example cost for meals per day
    park_fee = 30.0               # Example park fee per day

    # Create a SafariTour object
    safari = SafariTour(daily_accommodation, daily_meal, park_fee)

    try:
        # Calculate total cost for a 4-day safari
        total_cost = safari.calculate_total_cost()
        print(f"Total cost for the safari tour: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
