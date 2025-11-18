"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidmmx6ovrkgb7pb5l6vt5iccg5zig3n4kdoo3t6qc7oswvkxckfy4.ipfs.dweb.link
Prompt: Generate code to calculate quarterly points multipliers for users with consecutive trading activity, based on the rules mentioned on the Blitz platform.
Generated: DETERMINISTIC_2d438f10b68da468
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TradingActivity:
    """
    A class to represent trading activity for a user.

    Attributes:
        user_id (int): The ID of the user.
        activity_dates (list of datetime.date): Dates of trading activities.
    """

    def __init__(self, user_id, activity_dates):
        """
        Initializes a TradingActivity instance.

        Args:
            user_id (int): The ID of the user.
            activity_dates (list of datetime.date): Dates of trading activities.
        """
        self.user_id = user_id
        self.activity_dates = activity_dates

    def calculate_quarterly_multiplier(self):
        """
        Calculates the quarterly points multiplier based on consecutive trading activity.

        Returns:
            float: The points multiplier for the quarter.
        """
        try:
            # Ensure activity dates are valid and sorted
            if not self.activity_dates or not all(isinstance(d, datetime.date) for d in self.activity_dates):
                raise ValueError("Invalid activity dates provided.")

            # Sort dates in ascending order for processing
            self.activity_dates.sort()

            # Initialize variables
            consecutive_days = 0
            max_consecutive_days = 0

            # Iterate through activity dates and calculate consecutive days
            for i in range(len(self.activity_dates)):
                if i == 0:
                    consecutive_days = 1  # First activity day
                else:
                    # Check if the current date is consecutive from the previous date
                    if (self.activity_dates[i] - self.activity_dates[i - 1]).days == 1:
                        consecutive_days += 1
                    else:
                        # Reset consecutive days count
                        max_consecutive_days = max(max_consecutive_days, consecutive_days)
                        consecutive_days = 1

            # Update max consecutive days for the last sequence
            max_consecutive_days = max(max_consecutive_days, consecutive_days)

            # Determine points multiplier based on Blitz platform rules
            if max_consecutive_days >= 90:
                return 2.5  # Top multiplier for sustained activity
            elif max_consecutive_days >= 60:
                return 2.0  # High multiplier
            elif max_consecutive_days >= 30:
                return 1.5  # Medium multiplier
            else:
                return 1.0  # Default multiplier for limited activity

        except Exception as e:
            # Log error message to console (or replace with logging framework in production environments)
            print(f"Error calculating multiplier for user {self.user_id}: {e}")
            return 1.0  # Fallback multiplier in case of error


# Example usage
if __name__ == "__main__":
    # Example data: User trading activity for the quarter
    user_id = 12345
    activity_dates = [
        datetime.date(2023, 7, 1),
        datetime.date(2023, 7, 2),
        datetime.date(2023, 7, 3),
        datetime.date(2023, 7, 5),  # Skipped a day
        datetime.date(2023, 7, 6),
        datetime.date(2023, 7, 7),
        datetime.date(2023, 7, 8),  # Consecutive days activity resumes
    ]

    trading_activity = TradingActivity(user_id, activity_dates)
    multiplier = trading_activity.calculate_quarterly_multiplier()

    print(f"User {user_id} points multiplier for the quarter: {multiplier}")
```
