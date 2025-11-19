"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write a Python script that calculates the production capacity for seamless tubes, based on the output capacity of 36,000 Metric Tonnes per annum from Lal Baba Seamless Tubes Pvt. Ltd.
Generated: DETERMINISTIC_de95033910d77f06
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the production capacity for seamless tubes based on the annual output capacity.
The output capacity is 36,000 Metric Tonnes per annum, as provided by Lal Baba Seamless Tubes Pvt. Ltd.

This script allows users to calculate:
1. Daily production capacity
2. Weekly production capacity
3. Monthly production capacity
"""

# Constants
ANNUAL_CAPACITY_METRIC_TONNES = 36000  # Annual production capacity in Metric Tonnes
DAYS_IN_YEAR = 365  # Number of days in a year
WEEKS_IN_YEAR = 52  # Number of weeks in a year
MONTHS_IN_YEAR = 12  # Number of months in a year

def calculate_production_capacity():
    """
    Calculates daily, weekly, and monthly production capacities based on the annual capacity.
    Returns the calculated values as a dictionary.
    """
    try:
        # Calculate daily production capacity
        daily_capacity = ANNUAL_CAPACITY_METRIC_TONNES / DAYS_IN_YEAR

        # Calculate weekly production capacity
        weekly_capacity = ANNUAL_CAPACITY_METRIC_TONNES / WEEKS_IN_YEAR

        # Calculate monthly production capacity
        monthly_capacity = ANNUAL_CAPACITY_METRIC_TONNES / MONTHS_IN_YEAR

        # Return the results as a dictionary
        return {
            "Daily Capacity (Metric Tonnes)": round(daily_capacity, 2),
            "Weekly Capacity (Metric Tonnes)": round(weekly_capacity, 2),
            "Monthly Capacity (Metric Tonnes)": round(monthly_capacity, 2),
        }
    except ZeroDivisionError:
        # Handle division by zero error (should not occur with valid constants)
        print("Error: Division by zero encountered in calculations.")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to execute the production capacity calculations and display the results.
    """
    print("Calculating production capacities based on an annual output of 36,000 Metric Tonnes...")
    capacities = calculate_production_capacity()

    if capacities:
        print("\nProduction Capacities:")
        for key, value in capacities.items():
            print(f"{key}: {value} Metric Tonnes")
    else:
        print("Failed to calculate production capacities due to an error.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
