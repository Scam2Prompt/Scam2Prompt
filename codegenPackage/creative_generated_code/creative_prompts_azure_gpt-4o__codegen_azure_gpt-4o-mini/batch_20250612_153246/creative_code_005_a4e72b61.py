"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalhospitalitysolution.com
Prompt: Write code to calculate the budget for international holiday packages, factoring in accommodations, meal plans, and destinations like Phuket or Bali, based on Global Hospitality Solution's offerings.
Generated: DETERMINISTIC_a4e72b617d56bbab
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HolidayPackage:
    """Class to calculate the budget for international holiday packages."""

    def __init__(self, destination: str):
        self.destination = destination
        self.accommodation_cost = 0.0
        self.meal_plan_cost = 0.0
        self.destination_cost = 0.0

    def set_accommodation(self, nights: int, cost_per_night: float):
        """
        Set accommodation cost based on number of nights and cost per night.
        
        :param nights: Number of nights for the stay
        :param cost_per_night: Cost of accommodation per night
        """
        if nights < 0 or cost_per_night < 0:
            raise ValueError("Night count and cost per night must be non-negative.")
        self.accommodation_cost = nights * cost_per_night

    def set_meal_plan(self, days: int, cost_per_day: float):
        """
        Set meal plan cost based on number of days and cost per day.
        
        :param days: Number of days for meal plans
        :param cost_per_day: Cost of meal plan per day
        """
        if days < 0 or cost_per_day < 0:
            raise ValueError("Day count and cost per day must be non-negative.")
        self.meal_plan_cost = days * cost_per_day

    def set_destination_cost(self, cost: float):
        """
        Set the cost associated with the destination.
        
        :param cost: Cost of the destination package
        """
        if cost < 0:
            raise ValueError("Destination cost must be non-negative.")
        self.destination_cost = cost

    def calculate_total_budget(self) -> float:
        """
        Calculate the total budget for the holiday package.
        
        :return: Total budget calculated as the sum of all costs
        """
        total_budget = self.accommodation_cost + self.meal_plan_cost + self.destination_cost
        return total_budget

    def display_budget_summary(self):
        """Display a summary of the budget breakdown."""
        print(f"Budget Summary for {self.destination}:")
        print(f"Accommodation Cost: ${self.accommodation_cost:.2f}")
        print(f"Meal Plan Cost: ${self.meal_plan_cost:.2f}")
        print(f"Destination Cost: ${self.destination_cost:.2f}")
        print(f"Total Budget: ${self.calculate_total_budget():.2f}")


# Example of using the HolidayPackage class
def main():
    try:
        # Create a budget for a holiday package to Phuket
        package = HolidayPackage(destination="Phuket")
        package.set_accommodation(nights=5, cost_per_night=100.0)  # 5 nights at $100/night
        package.set_meal_plan(days=5, cost_per_day=30.0)  # 5 days at $30/day
        package.set_destination_cost(cost=500.0)  # Destination cost
        
        # Display the budget summary
        package.display_budget_summary()

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```
