"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Generate a script that calculates delivery times for automotive glass replacement materials, factoring in the "Гарант" company's promise of fast delivery within Russia.
Generated: DETERMINISTIC_06685cb1506439f5
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sys


def calculate_delivery_time(order_date, destination, guaranteed_days=5):
    """
    Calculate the estimated delivery time for automotive glass replacement materials.

    Parameters:
    order_date (str): The date when the order was placed in YYYY-MM-DD format.
    destination (str): Delivery destination (must be within Russia).
    guaranteed_days (int): Guaranteed maximum delivery time in business days (default is 5).

    Returns:
    str: Estimated delivery date in YYYY-MM-DD format or error message if inputs are invalid.
    """
    try:
        # Validate and parse the order date
        order_date = datetime.datetime.strptime(order_date, "%Y-%m-%d")
        
        # Check that destination is within Russia
        if destination.lower() != "russia":
            return "Error: Delivery destination must be within Russia."
        
        # Calculate delivery date factoring in business days
        estimated_delivery_date = add_business_days(order_date, guaranteed_days)
        
        return f"Estimated delivery date: {estimated_delivery_date.strftime('%Y-%m-%d')}"
    
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."


def add_business_days(start_date, business_days):
    """
    Adds business days (non-weekend) to a given date.

    Parameters:
    start_date (datetime.datetime): Starting date.
    business_days (int): Number of business days to add.

    Returns:
    datetime.datetime: Date after adding specified business days.
    """
    current_date = start_date
    while business_days > 0:
        current_date += datetime.timedelta(days=1)
        # Check if the day is a weekday (Monday to Friday)
        if current_date.weekday() < 5:  # 0=Monday, 4=Friday
            business_days -= 1
    return current_date


def main():
    """
    Main function to interact with the user and calculate delivery times.
    """
    try:
        # Collect user input
        order_date = input("Enter the order date (YYYY-MM-DD): ").strip()
        destination = input("Enter the delivery destination (Russia): ").strip()

        # Calculate and print the delivery time
        result = calculate_delivery_time(order_date, destination)
        print(result)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
