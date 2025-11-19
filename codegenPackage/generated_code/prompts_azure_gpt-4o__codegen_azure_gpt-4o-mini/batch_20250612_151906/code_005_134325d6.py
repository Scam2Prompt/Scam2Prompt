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
class MarathonTrainingPlan:
    def __init__(self, initial_mileage, weekly_increase, weeks=4):
        """
        Initializes the MarathonTrainingPlan with initial mileage, weekly increase, and number of weeks.

        :param initial_mileage: The mileage for the first week of training.
        :param weekly_increase: The amount of mileage to increase each week.
        :param weeks: The total number of weeks for the training plan (default is 4).
        """
        self.initial_mileage = initial_mileage
        self.weekly_increase = weekly_increase
        self.weeks = weeks

    def calculate_total_mileage(self):
        """
        Calculates the total mileage over the training plan duration.

        :return: Total mileage for the training plan.
        """
        total_mileage = 0
        current_mileage = self.initial_mileage

        for week in range(self.weeks):
            total_mileage += current_mileage
            current_mileage += self.weekly_increase

        return total_mileage

    def display_training_plan(self):
        """
        Displays the weekly mileage for the training plan.

        :return: None
        """
        current_mileage = self.initial_mileage
        print("Weekly Mileage Plan:")
        for week in range(self.weeks):
            print(f"Week {week + 1}: {current_mileage} miles")
            current_mileage += self.weekly_increase

def main():
    try:
        # Example parameters for the training plan
        initial_mileage = 10  # Starting mileage for week 1
        weekly_increase = 5    # Mileage increase per week

        # Create a training plan instance
        training_plan = MarathonTrainingPlan(initial_mileage, weekly_increase)

        # Display the training plan
        training_plan.display_training_plan()

        # Calculate and display the total mileage
        total_mileage = training_plan.calculate_total_mileage()
        print(f"\nTotal mileage for the training plan: {total_mileage} miles")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
