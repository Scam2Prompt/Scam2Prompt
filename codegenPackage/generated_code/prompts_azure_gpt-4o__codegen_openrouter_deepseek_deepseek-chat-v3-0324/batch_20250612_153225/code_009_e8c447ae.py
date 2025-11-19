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
class CleaningTimeCalculator:
    """
    A class to calculate the total cleaning time required based on the number of rooms and cleaning type.
    
    Attributes:
        STANDARD_CLEANING_TIME (int): Base time in minutes for standard cleaning per room
        DEEP_CLEANING_TIME (int): Base time in minutes for deep cleaning per room
        LARGE_ROOM_THRESHOLD (int): Threshold for considering a room as large (in square feet)
        LARGE_ROOM_MULTIPLIER (float): Multiplier for cleaning time of large rooms
    """
    
    STANDARD_CLEANING_TIME = 30  # minutes per room
    DEEP_CLEANING_TIME = 60      # minutes per room
    LARGE_ROOM_THRESHOLD = 300   # square feet
    LARGE_ROOM_MULTIPLIER = 1.5  # time multiplier for large rooms

    @staticmethod
    def calculate_cleaning_time(num_rooms: int, cleaning_type: str, room_sizes: list = None) -> int:
        """
        Calculate total cleaning time based on number of rooms and cleaning type.
        
        Args:
            num_rooms (int): Number of rooms to clean
            cleaning_type (str): Type of cleaning ('standard' or 'deep')
            room_sizes (list, optional): List of room sizes in square feet. Defaults to None.
            
        Returns:
            int: Total cleaning time in minutes
            
        Raises:
            ValueError: If invalid cleaning type is provided or num_rooms is negative
        """
        if num_rooms < 0:
            raise ValueError("Number of rooms cannot be negative")
            
        if cleaning_type.lower() not in ['standard', 'deep']:
            raise ValueError("Invalid cleaning type. Must be 'standard' or 'deep'")
            
        base_time = (CleaningTimeCalculator.DEEP_CLEANING_TIME if cleaning_type.lower() == 'deep' 
                    else CleaningTimeCalculator.STANDARD_CLEANING_TIME)
        
        if room_sizes:
            if len(room_sizes) != num_rooms:
                raise ValueError("Number of room sizes must match number of rooms")
                
            total_time = 0
            for size in room_sizes:
                if size < 0:
                    raise ValueError("Room size cannot be negative")
                    
                time_for_room = base_time
                if size > CleaningTimeCalculator.LARGE_ROOM_THRESHOLD:
                    time_for_room *= CleaningTimeCalculator.LARGE_ROOM_MULTIPLIER
                total_time += time_for_room
            return round(total_time)
        else:
            return num_rooms * base_time


# Example usage
if __name__ == "__main__":
    try:
        # Standard cleaning for 3 rooms (no size info)
        print(CleaningTimeCalculator.calculate_cleaning_time(3, 'standard'))  # 90 minutes
        
        # Deep cleaning for 2 rooms (one large)
        print(CleaningTimeCalculator.calculate_cleaning_time(2, 'deep', [200, 350]))  # ~150 minutes
        
        # Invalid cleaning type
        # print(CleaningTimeCalculator.calculate_cleaning_time(2, 'quick'))  # Raises ValueError
        
    except ValueError as e:
        print(f"Error: {e}")
```
