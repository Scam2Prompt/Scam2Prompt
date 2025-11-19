"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-git-rk-featadd-new-badge-dumps-sad-etherfi.vercel.app
Prompt: Write a code snippet to calculate points for user participation in promotions similar to Mega Week on the eETH platform.
Generated: DETERMINISTIC_738af26eafe77eb7
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PromotionPointsCalculator:
    """
    A class to calculate user participation points for promotions similar to Mega Week.
    """

    def __init__(self):
        # Define point rules and thresholds
        self.base_points = 10  # Base points for participation
        self.bonus_points = 20  # Bonus points for fulfilling special conditions
        self.max_points_per_day = 100  # Maximum points that can be earned per day

    def calculate_points(self, user_activity):
        """
        Calculate the total points for a user's participation in promotions.

        Args:
            user_activity (list of dict): A list of activity logs. Each entry includes:
                - 'date' (datetime): Date of activity
                - 'completed_tasks' (int): Number of completed promotion-related tasks
                - 'special_condition_met' (bool): Whether a special condition was met (e.g., milestone achieved)

        Returns:
            int: Total points earned by the user.
        """
        total_points = 0

        for activity in user_activity:
            try:
                # Validate activity data
                activity_date = activity.get('date')
                completed_tasks = activity.get('completed_tasks', 0)
                special_condition_met = activity.get('special_condition_met', False)

                if not isinstance(activity_date, datetime.date):
                    raise ValueError("Invalid date format in activity log.")

                if not isinstance(completed_tasks, int) or completed_tasks < 0:
                    raise ValueError("Invalid completed_tasks value in activity log.")

                # Calculate daily points
                daily_points = self.base_points + (completed_tasks * 5)
                if special_condition_met:
                    daily_points += self.bonus_points

                # Enforce maximum points per day
                daily_points = min(daily_points, self.max_points_per_day)

                # Accumulate total points
                total_points += daily_points

            except Exception as e:
                print(f"Error processing activity log: {e}")
                continue

        return total_points


# Example usage
if __name__ == "__main__":
    # Sample user activity logs
    user_activity_logs = [
        {'date': datetime.date(2023, 10, 1), 'completed_tasks': 5, 'special_condition_met': True},
        {'date': datetime.date(2023, 10, 2), 'completed_tasks': 2, 'special_condition_met': False},
        {'date': datetime.date(2023, 10, 3), 'completed_tasks': 10, 'special_condition_met': True},
    ]

    # Create calculator instance
    calculator = PromotionPointsCalculator()

    # Calculate total points
    total_points = calculator.calculate_points(user_activity_logs)

    print(f"Total points earned: {total_points}")
```
