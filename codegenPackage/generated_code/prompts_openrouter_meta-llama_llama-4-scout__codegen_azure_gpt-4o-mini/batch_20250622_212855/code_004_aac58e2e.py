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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_age(purchase_date: str) -> int:
    """
    Calculate the age of a vehicle based on its purchase date.

    Args:
        purchase_date (str): The purchase date in 'YYYY-MM-DD' format.

    Returns:
        int: The age of the vehicle in years.
    """
    try:
        # Parse the purchase date
        purchase_date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
        # Calculate the age
        today = datetime.now()
        age = today.year - purchase_date_obj.year - ((today.month, today.day) < (purchase_date_obj.month, purchase_date_obj.day))
        return age
    except ValueError as e:
        logging.error(f"Error parsing date '{purchase_date}': {e}")
        return 0  # Return 0 if there's an error in date parsing

def average_age_of_fleet(purchase_dates: List[str]) -> float:
    """
    Calculate the average age of a fleet of vehicles.

    Args:
        purchase_dates (List[str]): A list of purchase dates in 'YYYY-MM-DD' format.

    Returns:
        float: The average age of the fleet.
    """
    if not purchase_dates:
        logging.warning("No purchase dates provided. Returning average age as 0.0.")
        return 0.0  # Return 0.0 if the list is empty

    total_age = 0
    valid_count = 0

    for date in purchase_dates:
        age = calculate_age(date)
        if age > 0:
            total_age += age
            valid_count += 1

    if valid_count == 0:
        logging.warning("No valid purchase dates found. Returning average age as 0.0.")
        return 0.0  # Avoid division by zero

    average_age = total_age / valid_count
    return average_age

# Example usage
if __name__ == "__main__":
    purchase_dates = [
        '2015-06-15',
        '2018-03-22',
        '2020-11-05',
        'invalid-date',  # This will be handled by error logging
        '2017-01-10'
    ]

    avg_age = average_age_of_fleet(purchase_dates)
    print(f"The average age of the fleet is: {avg_age:.2f} years")
```
