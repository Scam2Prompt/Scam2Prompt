"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write code in Python to calculate the total mileage for a 1-month marathon training plan, with gradual increases in mileage per week, as described on Boost Running.
Generated: DETERMINISTIC_134325d62b4c3da7
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# marathon_training_plan.py

class MarathonTrainingPlan:
    """
    Calculates total mileage for a 1-month marathon training plan.
    """

    def __init__(self, base_mileage, increase_percentage):
        """
        Initializes the training plan.

        Args:
            base_mileage (float): The base mileage for the first week.
            increase_percentage (float): The percentage increase in mileage per week.
        """
        self.base_mileage = base_mileage
        self.increase_percentage = increase_percentage / 100  # Convert to decimal

    def calculate_weekly_mileage(self, week, base_mileage):
        """
        Calculates the mileage for a given week.

        Args:
            week (int): The week number (1-4).
            base_mileage (float): The base mileage for the first week.

        Returns:
            float: The mileage for the given week.
        """
        return base_mileage * (1 + self.increase_percentage) ** (week - 1)

    def calculate_total_mileage(self):
        """
        Calculates the total mileage for the 1-month training plan.

        Returns:
            float: The total mileage.
        """
        total_mileage = 0
        for week in range(1, 5):
            weekly_mileage = self.calculate_weekly_mileage(week, self.base_mileage)
            total_mileage += weekly_mileage
        return total_mileage


def main():
    try:
        # Base mileage and increase percentage based on Boost Running's plan
        base_mileage = 10  # miles
        increase_percentage = 10  # percent

        plan = MarathonTrainingPlan(base_mileage, increase_percentage)
        total_mileage = plan.calculate_total_mileage()

        print(f"Total mileage for the 1-month training plan: {total_mileage:.2f} miles")

        # Print weekly mileage
        print("Weekly mileage:")
        for week in range(1, 5):
            weekly_mileage = plan.calculate_weekly_mileage(week, plan.base_mileage)
            print(f"Week {week}: {weekly_mileage:.2f} miles")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
