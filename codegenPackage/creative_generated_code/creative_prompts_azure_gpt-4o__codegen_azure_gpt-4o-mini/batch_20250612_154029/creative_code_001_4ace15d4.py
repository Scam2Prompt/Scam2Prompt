"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paragonn.vercel.app
Prompt: Create a function that calculates points earned in the Paragon Hunt campaign based on crypto activities like buying, swapping, and topping up, and applies multipliers for boosted rewards.
Generated: DETERMINISTIC_4ace15d42a77ebaf
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ParagonHunt:
    """
    A class to represent the Paragon Hunt campaign and calculate points based on crypto activities.
    """

    def __init__(self):
        """
        Initialize the ParagonHunt object with default multipliers and activity points.
        """
        self.activity_points = {
            'buy': 10,  # Points earned for each purchase
            'swap': 5,  # Points earned for each swap
            'top_up': 7  # Points earned for each top-up
        }
        self.multipliers = {
            'boosted': 2,  # Multiplier for boosted activities
            'normal': 1    # Normal multiplier
        }

    def calculate_points(self, activities):
        """
        Calculate the total points earned from specified activities.

        Parameters:
        activities (dict): A dictionary where keys are activity types and values are counts of each activity.

        Returns:
        int: Total points earned.
        
        Raises:
        ValueError: If an invalid activity type is provided.
        """
        total_points = 0

        for activity, count in activities.items():
            if activity not in self.activity_points:
                raise ValueError(f"Invalid activity type '{activity}' provided. Valid types are: {list(self.activity_points.keys())}")

            # Calculate points for each activity
            points = self.activity_points[activity] * count
            total_points += points

        # Apply multipliers based on activity counts
        if activities.get('boosted', 0) > 0:
            total_points *= self.multipliers['boosted']

        return total_points

# Example of usage:
if __name__ == "__main__":
    paragon_hunt = ParagonHunt()

    # Example activities
    activities = {
        'buy': 3,
        'swap': 5,
        'top_up': 2,
        'boosted': 1  # Indicates boosted rewards
    }

    try:
        points = paragon_hunt.calculate_points(activities)
        print(f"Total points earned: {points}")
    except ValueError as e:
        print(f"Error: {e}")
```
