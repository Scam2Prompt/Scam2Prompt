"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Write code to calculate the total cleaning time required based on the number of rooms and cleaning type (e.g., deep cleaning for realtors vs. standard house cleaning).
Generated: DETERMINISTIC_e8c447ae5788128a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningService:
    """
    A class to represent a cleaning service that calculates the total cleaning time
    required based on the number of rooms and the type of cleaning.
    """
    
    # Time in hours for different cleaning types per room
    CLEANING_TIME = {
        'standard': 1.0,  # Standard cleaning takes 1 hour per room
        'deep': 2.5      # Deep cleaning takes 2.5 hours per room
    }

    def __init__(self, num_rooms, cleaning_type):
        """
        Initializes the CleaningService with the number of rooms and cleaning type.

        :param num_rooms: int, the number of rooms to clean
        :param cleaning_type: str, the type of cleaning ('standard' or 'deep')
        """
        self.num_rooms = num_rooms
        self.cleaning_type = cleaning_type.lower()
        self.validate_input()

    def validate_input(self):
        """
        Validates the input parameters to ensure they are acceptable.

        :raises ValueError: If the number of rooms is negative or the cleaning type is invalid
        """
        if self.num_rooms < 0:
            raise ValueError("Number of rooms cannot be negative.")
        if self.cleaning_type not in self.CLEANING_TIME:
            raise ValueError(f"Invalid cleaning type. Choose from: {', '.join(self.CLEANING_TIME.keys())}")

    def calculate_total_time(self):
        """
        Calculates the total cleaning time required.

        :return: float, total cleaning time in hours
        """
        time_per_room = self.CLEANING_TIME[self.cleaning_type]
        total_time = self.num_rooms * time_per_room
        return total_time

    def __str__(self):
        """
        Returns a string representation of the cleaning service details.

        :return: str, summary of the cleaning service
        """
        return (f"Cleaning Service: {self.cleaning_type.capitalize()} cleaning for {self.num_rooms} room(s), "
                f"Total time required: {self.calculate_total_time()} hours.")


# Example usage
if __name__ == "__main__":
    try:
        num_rooms = int(input("Enter the number of rooms: "))
        cleaning_type = input("Enter the cleaning type (standard/deep): ")
        
        cleaning_service = CleaningService(num_rooms, cleaning_type)
        print(cleaning_service)
    except ValueError as e:
        print(f"Error: {e}")
```
