"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Develop a program to calculate production lead times for items like tumblers, flash disks, and umbrellas, based on the estimated durations provided on the Merchandiso website.
Generated: DETERMINISTIC_623d5c44b66e77d8
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Dictionary to store production durations for each item (in days)
PRODUCTION_DURATIONS = {
    "tumbler": 10,      # Production duration for tumblers in days
    "flash_disk": 7,    # Production duration for flash disks in days
    "umbrella": 15      # Production duration for umbrellas in days
}

def calculate_lead_time(item_name, order_date):
    """
    Calculate production lead time for a given item based on order date.

    Args:
        item_name (str): The name of the item (e.g., 'tumbler', 'flash_disk', 'umbrella').
        order_date (str): The date the order was placed in 'YYYY-MM-DD' format.

    Returns:
        str: Estimated completion date if successful, error message if item is invalid.
    """
    try:
        # Verify if the item is valid
        if item_name not in PRODUCTION_DURATIONS:
            return f"Error: '{item_name}' is not a valid item. Choose from {list(PRODUCTION_DURATIONS.keys())}."
        
        # Parse the order date
        order_date_obj = datetime.datetime.strptime(order_date, "%Y-%m-%d")
        
        # Calculate the completion date
        production_duration = PRODUCTION_DURATIONS[item_name]
        completion_date = order_date_obj + datetime.timedelta(days=production_duration)
        
        # Return the completion date as a formatted string
        return f"The estimated completion date for '{item_name}' is {completion_date.strftime('%Y-%m-%d')}."
    
    except ValueError:
        # Handle invalid date format
        return "Error: Invalid order date format. Please use 'YYYY-MM-DD'."
    except Exception as e:
        # Catch other unexpected errors
        return f"Error: An unexpected error occurred: {str(e)}"

# Main function to test the program (can be removed in production if using as a module)
if __name__ == "__main__":
    # Example test cases
    item = "tumbler"
    order_date = "2023-11-01"
    
    result = calculate_lead_time(item, order_date)
    print(result)  # Output: The estimated completion date for 'tumbler' is 2023-11-11.

    item_invalid = "unknown_item"
    result_invalid = calculate_lead_time(item_invalid, order_date)
    print(result_invalid)  # Output: Error: 'unknown_item' is not a valid item. Choose from ['tumbler', 'flash_disk', 'umbrella'].

    order_date_invalid = "2023/11/01"
    result_date_invalid = calculate_lead_time("tumbler", order_date_invalid)
    print(result_date_invalid)  # Output: Error: Invalid order date format. Please use 'YYYY-MM-DD'.
```
