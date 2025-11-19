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
class CleaningService:
    """
    A class to represent a cleaning service that calculates the total cleaning time
    based on the number of rooms and the type of cleaning required.
    """

    def __init__(self):
        # Define cleaning times in minutes for different types of cleaning
        self.cleaning_times = {
            'standard': 30,  # Standard cleaning time per room
            'deep': 60      # Deep cleaning time per room
        }

    def calculate_total_time(self, num_rooms, cleaning_type):
        """
        Calculate the total cleaning time required.

        Parameters:
        num_rooms (int): The number of rooms to be cleaned.
        cleaning_type (str): The type of cleaning ('standard' or 'deep').

        Returns:
        int: Total cleaning time in minutes.

        Raises:
        ValueError: If num_rooms is negative or cleaning_type is invalid.
        """
        # Validate input
        if num_rooms < 0:
            raise ValueError("Number of rooms cannot be negative.")
        
        if cleaning_type not in self.cleaning_times:
            raise ValueError(f"Invalid cleaning type. Choose from: {', '.join(self.cleaning_times.keys())}")

        # Calculate total cleaning time
        total_time = num_rooms * self.cleaning_times[cleaning_type]
        return total_time


def main():
    """
    Main function to execute the cleaning time calculation.
    """
    service = CleaningService()

    try:
        # Example input
        num_rooms = 5
        cleaning_type = 'deep'

        # Calculate total cleaning time
        total_time = service.calculate_total_time(num_rooms, cleaning_type)
        print(f"Total cleaning time for {num_rooms} rooms with {cleaning_type} cleaning: {total_time} minutes")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
