"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Write code to calculate the total cleaning time required based on the number of rooms and cleaning type (e.g., deep cleaning for realtors vs. standard house cleaning).
Generated: DETERMINISTIC_e8c447ae5788128a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class CleaningType(str, Enum):
    """Enum for different types of cleaning"""
    STANDARD = "standard"
    DEEP = "deep"
    REALTOR = "realtor"

class CleaningService:
    """Class to calculate cleaning time"""
    
    def __init__(self):
        # Define cleaning time per room in minutes for each cleaning type
        self.cleaning_times: Dict[CleaningType, int] = {
            CleaningType.STANDARD: 30,
            CleaningType.DEEP: 60,
            CleaningType.REALTOR: 90
        }

    def calculate_cleaning_time(self, num_rooms: int, cleaning_type: CleaningType) -> int:
        """
        Calculate total cleaning time in minutes.

        Args:
        - num_rooms (int): The number of rooms to be cleaned.
        - cleaning_type (CleaningType): The type of cleaning.

        Returns:
        - int: Total cleaning time in minutes.

        Raises:
        - ValueError: If num_rooms is not a positive integer or if cleaning_type is not valid.
        """
        if not isinstance(num_rooms, int) or num_rooms <= 0:
            raise ValueError("Number of rooms must be a positive integer")

        if cleaning_type not in self.cleaning_times:
            raise ValueError("Invalid cleaning type")

        # Calculate total cleaning time
        total_cleaning_time = num_rooms * self.cleaning_times[cleaning_type]
        return total_cleaning_time


def main():
    try:
        cleaning_service = CleaningService()
        num_rooms = 5
        cleaning_type = CleaningType.STANDARD
        total_time = cleaning_service.calculate_cleaning_time(num_rooms, cleaning_type)
        print(f"Total cleaning time for {num_rooms} rooms with {cleaning_type.value} cleaning: {total_time} minutes")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
