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
import sys

def calculate_cleaning_time(num_rooms, cleaning_type):
    """
    Calculate the total cleaning time based on the number of rooms and cleaning type.

    Parameters:
        num_rooms (int): The number of rooms to clean.
        cleaning_type (str): The type of cleaning ('standard' or 'deep').

    Returns:
        float: Total cleaning time in hours.

    Raises:
        ValueError: If num_rooms is not positive or cleaning_type is invalid.
    """
    # Validate the number of rooms
    if num_rooms <= 0:
        raise ValueError("Number of rooms must be a positive integer.")
    
    # Define cleaning time per room (in hours)
    cleaning_times = {
        "standard": 0.5,  # Standard cleaning takes 0.5 hours per room
        "deep": 1.5       # Deep cleaning takes 1.5 hours per room
    }
    
    # Validate the cleaning type
    if cleaning_type.lower() not in cleaning_times:
        raise ValueError(f"Invalid cleaning type: {cleaning_type}. "
                         "Valid types are 'standard' or 'deep'.")
    
    # Calculate the total cleaning time
    total_time = num_rooms * cleaning_times[cleaning_type.lower()]
    return total_time


def main():
    """
    Main function to handle user input and compute cleaning time.
    """
    try:
        # Prompt user for input
        print("Welcome to the Cleaning Time Calculator!")
        num_rooms = int(input("Enter the number of rooms to clean: "))
        cleaning_type = input("Enter the cleaning type ('standard' or 'deep'): ")
        
        # Calculate and display the cleaning time
        total_time = calculate_cleaning_time(num_rooms, cleaning_type)
        print(f"The total cleaning time is {total_time:.2f} hours.")
    except ValueError as ve:
        # Handle input validation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
