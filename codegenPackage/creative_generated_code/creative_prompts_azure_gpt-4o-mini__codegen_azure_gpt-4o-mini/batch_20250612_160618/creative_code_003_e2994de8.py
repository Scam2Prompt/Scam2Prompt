"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdadw3qqd.pages.dev
Prompt: Create a function that calculates the total Puffer Points earned based on the registration for Chapter 3 rewards.
Generated: DETERMINISTIC_e2994de81de01a3c
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PufferPointCalculator:
    def __init__(self):
        # Initialize the base Puffer Points
        self.base_points = 100  # Base points for registration
        self.bonus_percentage = 0.1  # Bonus percentage for additional criteria

    def calculate_total_points(self, registrations, bonus_criteria_met):
        """
        Calculate the total Puffer Points earned based on registrations and bonus criteria.

        :param registrations: int - Number of registrations
        :param bonus_criteria_met: bool - Whether bonus criteria are met
        :return: float - Total Puffer Points earned
        :raises ValueError: If the number of registrations is negative
        """
        # Validate inputs
        if registrations < 0:
            raise ValueError("Number of registrations cannot be negative.")

        # Calculate base points from registrations
        total_points = self.base_points * registrations

        # Calculate bonus points if criteria are met
        if bonus_criteria_met:
            total_points += total_points * self.bonus_percentage

        return total_points


if __name__ == "__main__":
    # Example usage of the PufferPointCalculator class
    try:
        calculator = PufferPointCalculator()
        registrations = 5  # Example number of registrations
        bonus_criteria_met = True  # Example condition for bonus

        total_points = calculator.calculate_total_points(registrations, bonus_criteria_met)
        print(f"Total Puffer Points earned: {total_points:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
