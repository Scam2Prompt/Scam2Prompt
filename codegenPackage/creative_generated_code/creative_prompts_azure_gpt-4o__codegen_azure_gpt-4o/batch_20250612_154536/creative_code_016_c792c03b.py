"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Write a Python function to calculate missed flight penalties for airlines like Alaska Airlines and Qatar Airways, using missed flight policies from Airlines Manage Booking.
Generated: DETERMINISTIC_c792c03b541838fc
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime, timedelta

# Define a dictionary to store the missed flight penalties for airlines
MISSED_FLIGHT_PENALTIES = {
    "Alaska Airlines": {
        "penalty_fee": 150,  # Base fee for missing a flight
        "grace_period": 2,  # Grace period in hours
        "cancellation_fee": 200  # Fee for cancellation without rebooking
    },
    "Qatar Airways": {
        "penalty_fee": 300,  # Base fee for missing a flight
        "grace_period": 4,  # Grace period in hours
        "cancellation_fee": 500  # Fee for cancellation without rebooking
    }
}

def calculate_missed_flight_penalty(airline, missed_flight_time, current_time=None, rebooked=False):
    """
    Calculate the penalty for missing a flight based on airline policies.

    Args:
        airline (str): The name of the airline (e.g., "Alaska Airlines", "Qatar Airways").
        missed_flight_time (str): The time of the missed flight in "YYYY-MM-DD HH:MM" format.
        current_time (str or None): The current time in "YYYY-MM-DD HH:MM" format.
                                    If None, the function uses the system's current time.
        rebooked (bool): Whether the passenger has rebooked the flight.

    Returns:
        int: The penalty amount to be charged.
    """
    try:
        # Ensure the airline is supported
        if airline not in MISSED_FLIGHT_PENALTIES:
            raise ValueError(f"Unsupported airline: {airline}. Supported airlines are: {', '.join(MISSED_FLIGHT_PENALTIES.keys())}")
        
        # Parse missed flight time and current time
        missed_flight_datetime = datetime.strptime(missed_flight_time, "%Y-%m-%d %H:%M")
        current_datetime = datetime.strptime(current_time, "%Y-%m-%d %H:%M") if current_time else datetime.now()
        
        # Get airline-specific policy details
        policy = MISSED_FLIGHT_PENALTIES[airline]
        grace_period = timedelta(hours=policy["grace_period"])
        
        # Check if the passenger missed the flight within the grace period
        if current_datetime <= missed_flight_datetime + grace_period:
            return 0  # No penalty within the grace period
        
        # Calculate the appropriate penalty based on rebooking status
        if rebooked:
            return policy["penalty_fee"]  # Rebooking incurs only the base penalty fee
        else:
            return policy["cancellation_fee"]  # No rebooking incurs a higher cancellation fee
    
    except ValueError as e:
        print(f"Error: {e}")  # Handle errors related to invalid input
        return -1  # Return -1 to indicate an error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1  # Return -1 to indicate an unexpected error

# Example usage:
# penalty = calculate_missed_flight_penalty("Alaska Airlines", "2023-10-01 14:00", "2023-10-01 18:00", rebooked=False)
# print(f"Missed flight penalty: ${penalty}")
```
