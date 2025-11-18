"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write Python code to calculate estimated air freight shipping times for Uniair Cargo's routes, using the provided durations for East Asia, Europe & USA, and Southeast Asia.
Generated: DETERMINISTIC_a3c9fd63e7f32c42
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define a dictionary to store shipping durations (in hours) for each region
SHIPPING_DURATIONS = {
    "East Asia": 48,        # 2 days
    "Europe & USA": 72,     # 3 days
    "Southeast Asia": 24    # 1 day
}

def calculate_shipping_time(region, departure_time):
    """
    Calculate the estimated arrival time for air freight shipping.

    Args:
        region (str): The destination region ("East Asia", "Europe & USA", or "Southeast Asia").
        departure_time (datetime.datetime): The departure time.

    Returns:
        datetime.datetime: The estimated arrival time.

    Raises:
        ValueError: If the region is not valid or departure_time is not a datetime object.
    """
    if region not in SHIPPING_DURATIONS:
        raise ValueError(f"Invalid region '{region}'. Valid regions are: {', '.join(SHIPPING_DURATIONS.keys())}")
    
    if not isinstance(departure_time, datetime.datetime):
        raise ValueError("departure_time must be a datetime.datetime object.")
    
    # Calculate the estimated arrival time by adding the shipping duration to the departure time
    shipping_duration_hours = SHIPPING_DURATIONS[region]
    estimated_arrival_time = departure_time + datetime.timedelta(hours=shipping_duration_hours)
    
    return estimated_arrival_time

def main():
    """
    Main function to demonstrate calculating shipping times.
    """
    try:
        # Example input: User-provided region and departure time
        region = "East Asia"  # Change this to test with other regions
        departure_time_str = "2023-10-01 14:00:00"  # Example departure time (YYYY-MM-DD HH:MM:SS)
        
        # Parse the user-provided departure time into a datetime object
        departure_time = datetime.datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M:%S")
        
        # Calculate the shipping time
        estimated_arrival = calculate_shipping_time(region, departure_time)
        
        # Print the result
        print(f"Estimated arrival time for region '{region}': {estimated_arrival}")
    
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```
