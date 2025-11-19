"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Write a Python code snippet to calculate the age of a fleet of vehicles, given their individual purchase dates, and display the average age of the fleet, similar to the "Modernidad" section on Autocares Cosme's website.
Generated: DETERMINISTIC_aac58e2ed79d3df9
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List

def calculate_vehicle_ages(purchase_dates: List[str]) -> float:
    """
    Calculate the average age of a fleet of vehicles based on their purchase dates.

    Args:
        purchase_dates (List[str]): List of purchase dates in 'YYYY-MM-DD' format.

    Returns:
        float: The average age of the fleet in years.
    """
    try:
        # Get the current date
        current_date = datetime.now()

        # Calculate ages of individual vehicles
        ages = []
        for date_str in purchase_dates:
            try:
                purchase_date = datetime.strptime(date_str, '%Y-%m-%d')
                age = (current_date - purchase_date).days / 365.25  # Convert days to years
                ages.append(age)
            except ValueError:
                print(f"Invalid date format for '{date_str}'. Expected 'YYYY-MM-DD'. Skipping...")
        
        # Ensure there are valid ages to calculate the average
        if not ages:
            raise ValueError("No valid purchase dates provided to calculate average age.")

        # Calculate and return the average age
        average_age = sum(ages) / len(ages)
        return average_age

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0.0  # Return 0.0 in case of an error

# Example usage
if __name__ == "__main__":
    # List of vehicle purchase dates
    purchase_dates = [
        "2015-06-15",
        "2018-09-20",
        "2020-01-10",
        "2012-03-05",
        "invalid-date"  # Example of an invalid date
    ]

    # Calculate and display the average age of the fleet
    average_age = calculate_vehicle_ages(purchase_dates)
    if average_age > 0:
        print(f"The average age of the fleet is {average_age:.2f} years.")
    else:
        print("Could not calculate the average age due to errors.")
```
