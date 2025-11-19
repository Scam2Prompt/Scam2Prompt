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
from datetime import datetime, date

def calculate_vehicle_age(purchase_date):
    """
    Calculate the age of a vehicle given its purchase date.

    Args:
        purchase_date (str): The purchase date of the vehicle in YYYY-MM-DD format.

    Returns:
        int: The age of the vehicle in years.
    """
    try:
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - purchase_date.year - ((today.month, today.day) < (purchase_date.month, purchase_date.day))
        return age
    except ValueError:
        raise ValueError("Invalid purchase date format. Please use YYYY-MM-DD.")

def calculate_fleet_age(purchase_dates):
    """
    Calculate the average age of a fleet of vehicles given their individual purchase dates.

    Args:
        purchase_dates (list): A list of purchase dates in YYYY-MM-DD format.

    Returns:
        float: The average age of the fleet in years.
    """
    try:
        ages = [calculate_vehicle_age(date) for date in purchase_dates]
        average_age = sum(ages) / len(ages)
        return average_age
    except ZeroDivisionError:
        raise ValueError("Cannot calculate average age of an empty fleet.")
    except Exception as e:
        raise Exception("An error occurred: " + str(e))

def main():
    # Example usage:
    purchase_dates = ["2018-01-01", "2020-06-01", "2015-03-01"]
    try:
        ages = [calculate_vehicle_age(date) for date in purchase_dates]
        average_age = calculate_fleet_age(purchase_dates)

        print("Vehicle Ages:")
        for i, (date, age) in enumerate(zip(purchase_dates, ages)):
            print(f"Vehicle {i+1} (Purchased: {date}): {age} years")

        print(f"\nAverage Fleet Age: {average_age:.2f} years")
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":
    main()
```
