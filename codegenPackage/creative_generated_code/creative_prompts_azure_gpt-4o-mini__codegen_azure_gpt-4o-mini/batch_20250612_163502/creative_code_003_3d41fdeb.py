"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Explain how to calculate $FOMO Points based on user activity in the TOCD game and provide a sample algorithm.
Generated: DETERMINISTIC_3d41fdebeade8e50
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FOMOPointsCalculator:
    """
    A class to calculate FOMO Points based on user activity in the TOCD game.
    """

    def __init__(self):
        self.point_structure = {
            'daily_login': 10,
            'complete_mission': 50,
            'purchase_item': 20,
            'participate_event': 30,
            'invite_friend': 40
        }

    def calculate_fomo_points(self, user_activity):
        """
        Calculate the total FOMO Points for a user based on their activity.

        Parameters:
        user_activity (dict): A dictionary containing user activities and their counts.

        Returns:
        int: Total FOMO Points earned by the user.
        """
        total_points = 0

        # Iterate through the user_activity dictionary to calculate points
        for activity, count in user_activity.items():
            try:
                if activity not in self.point_structure:
                    raise ValueError(f"Unknown activity: {activity}")

                # Calculate points for the activity and add to total points
                points_for_activity = self.point_structure[activity] * count
                total_points += points_for_activity

            except ValueError as e:
                print(f"Error calculating FOMO Points: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        return total_points


# Example usage:
if __name__ == "__main__":
    # Sample user activity
    user_activity = {
        'daily_login': 5,
        'complete_mission': 2,
        'purchase_item': 3,
        'participate_event': 1,
        'invite_friend': 2
    }

    calculator = FOMOPointsCalculator()
    total_fomo_points = calculator.calculate_fomo_points(user_activity)

    print(f"Total FOMO Points earned: {total_fomo_points}")
```
