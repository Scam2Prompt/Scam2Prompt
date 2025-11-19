"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-rk-featadd-new-badge-dumps-sad-etherfi.vercel.app
Prompt: Write a code snippet to calculate points for user participation in promotions similar to Mega Week on the eETH platform.
Generated: DETERMINISTIC_738af26eafe77eb7
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class PromotionCalculator:
    def __init__(self, start_time: datetime, end_time: datetime, 
                 base_points_per_hour: int, bonus_points_per_hour: int, 
                 bonus_threshold: timedelta):
        """
        Initialize the PromotionCalculator.

        Args:
        - start_time (datetime): The start time of the promotion.
        - end_time (datetime): The end time of the promotion.
        - base_points_per_hour (int): The base points awarded per hour of participation.
        - bonus_points_per_hour (int): The bonus points awarded per hour of participation after the bonus threshold.
        - bonus_threshold (timedelta): The time threshold after which bonus points are awarded.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.base_points_per_hour = base_points_per_hour
        self.bonus_points_per_hour = bonus_points_per_hour
        self.bonus_threshold = bonus_threshold

    def calculate_points(self, user_participation: List[Dict[str, datetime]]) -> int:
        """
        Calculate the points for a user's participation in the promotion.

        Args:
        - user_participation (List[Dict[str, datetime]]): A list of dictionaries containing the start and end times of the user's participation.

        Returns:
        - int: The total points earned by the user.
        """
        total_points = 0
        for participation in user_participation:
            participation_start = participation['start']
            participation_end = participation['end']

            # Check if participation overlaps with the promotion period
            if participation_start < self.end_time and participation_end > self.start_time:
                # Calculate the overlap period
                overlap_start = max(self.start_time, participation_start)
                overlap_end = min(self.end_time, participation_end)

                # Calculate the duration of the overlap
                overlap_duration = overlap_end - overlap_start

                # Calculate the base points
                base_points = self.calculate_base_points(overlap_duration)

                # Calculate the bonus points
                bonus_points = self.calculate_bonus_points(overlap_duration)

                # Add the points to the total
                total_points += base_points + bonus_points

        return total_points

    def calculate_base_points(self, duration: timedelta) -> int:
        """
        Calculate the base points for a given duration.

        Args:
        - duration (timedelta): The duration of participation.

        Returns:
        - int: The base points earned.
        """
        hours = duration.total_seconds() / 3600
        return int(hours * self.base_points_per_hour)

    def calculate_bonus_points(self, duration: timedelta) -> int:
        """
        Calculate the bonus points for a given duration.

        Args:
        - duration (timedelta): The duration of participation.

        Returns:
        - int: The bonus points earned.
        """
        if duration > self.bonus_threshold:
            bonus_duration = duration - self.bonus_threshold
            hours = bonus_duration.total_seconds() / 3600
            return int(hours * self.bonus_points_per_hour)
        else:
            return 0


def main():
    # Example usage
    start_time = datetime(2024, 9, 16, 0, 0, 0)
    end_time = datetime(2024, 9, 23, 0, 0, 0)
    base_points_per_hour = 10
    bonus_points_per_hour = 20
    bonus_threshold = timedelta(hours=2)

    calculator = PromotionCalculator(start_time, end_time, base_points_per_hour, bonus_points_per_hour, bonus_threshold)

    user_participation = [
        {'start': datetime(2024, 9, 16, 1, 0, 0), 'end': datetime(2024, 9, 16, 4, 0, 0)},
        {'start': datetime(2024, 9, 20, 10, 0, 0), 'end': datetime(2024, 9, 20, 12, 0, 0)},
    ]

    points = calculator.calculate_points(user_participation)
    print(f"Total points: {points}")


if __name__ == "__main__":
    main()
```
