"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Write code to calculate equipment rental costs based on attendee count, using the details provided by Parrotrans's renting services.
Generated: DETERMINISTIC_ef6181941115db3c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# equipment_rental_calculator.py

# Import necessary libraries
import math

def calculate_rental_cost(attendee_count):
    """
    Calculate equipment rental costs based on attendee count.
    
    Parrotrans's renting services details:
    1. Each equipment unit can serve up to 10 attendees.
    2. Rental cost per equipment unit is $50.
    3. A fixed service fee of $30 is applied to every order.
    
    Args:
        attendee_count (int): Number of attendees.
    
    Returns:
        float: Total rental cost.
    """
    try:
        # Validate input
        if attendee_count <= 0:
            raise ValueError("Attendee count must be a positive integer.")
        
        # Calculate equipment units needed (ceil to cover all attendees)
        equipment_units = math.ceil(attendee_count / 10)
        
        # Calculate total rental cost
        rental_cost = equipment_units * 50  # $50 per equipment unit
        service_fee = 30  # Fixed service fee
        total_cost = rental_cost + service_fee

        return total_cost
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage of the calculator
    try:
        # Prompt user for attendee count
        attendee_count = int(input("Enter the number of attendees: "))
        total_cost = calculate_rental_cost(attendee_count)

        if total_cost is not None:
            print(f"The total rental cost for {attendee_count} attendees is: ${total_cost:.2f}")
    except ValueError:
        print("Please enter a valid integer for attendee count.")
```
