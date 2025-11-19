"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Create a Python script to calculate the total weight of processed EPS foam per day for the XT400 densifier, given its hourly capacity and operating hours.
Generated: DETERMINISTIC_1f8b6ab436d272c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_total_weight(hourly_capacity: float, operating_hours: float) -> float:
    """
    Calculate the total weight of processed EPS foam per day.

    Parameters:
    hourly_capacity (float): The weight of EPS foam processed per hour (in kg).
    operating_hours (float): The number of hours the densifier operates in a day.

    Returns:
    float: The total weight of processed EPS foam for the day (in kg).
    
    Raises:
    ValueError: If hourly_capacity or operating_hours is negative.
    """
    if hourly_capacity < 0:
        logging.error("Hourly capacity cannot be negative.")
        raise ValueError("Hourly capacity cannot be negative.")
    if operating_hours < 0:
        logging.error("Operating hours cannot be negative.")
        raise ValueError("Operating hours cannot be negative.")

    total_weight = hourly_capacity * operating_hours
    logging.info(f"Calculated total weight: {total_weight} kg")
    return total_weight

def main():
    """
    Main function to execute the EPS foam weight calculation.
    """
    try:
        # Example values for hourly capacity and operating hours
        hourly_capacity = 100.0  # kg per hour
        operating_hours = 8.0     # hours per day

        total_weight = calculate_total_weight(hourly_capacity, operating_hours)
        print(f"Total weight of processed EPS foam per day: {total_weight} kg")
    
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
