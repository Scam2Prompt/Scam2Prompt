"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a Python script to calculate the total weight of processed EPS foam per day for the XT400 densifier, given its hourly capacity and operating hours.
Generated: DETERMINISTIC_1f8b6ab436d272c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total weight of processed EPS foam per day
# For the XT400 densifier, given its hourly capacity and operating hours.

def calculate_daily_weight(hourly_capacity_kg, operating_hours):
    """
    Calculate the total weight of processed EPS foam per day.

    Args:
        hourly_capacity_kg (float): The hourly capacity of the densifier in kilograms.
        operating_hours (float): The number of hours the densifier operates per day.

    Returns:
        float: The total weight of processed EPS foam in kilograms per day.
    """
    try:
        # Ensure inputs are valid
        if hourly_capacity_kg <= 0 or operating_hours <= 0:
            raise ValueError("Hourly capacity and operating hours must be positive numbers.")
        
        # Calculate the total weight
        total_weight = hourly_capacity_kg * operating_hours
        return total_weight
    except TypeError:
        raise TypeError("Both hourly_capacity_kg and operating_hours must be numbers.")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")

def main():
    """
    Main function to execute the script.
    """
    try:
        # Example hourly capacity and operating hours (replace with actual values as needed)
        hourly_capacity_kg = float(input("Enter the hourly capacity of the XT400 densifier in kilograms: "))
        operating_hours = float(input("Enter the number of operating hours per day: "))
        
        # Calculate the total weight processed in a day
        total_weight = calculate_daily_weight(hourly_capacity_kg, operating_hours)
        
        # Output the result
        print(f"The XT400 densifier processes a total of {total_weight:.2f} kg of EPS foam per day.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
