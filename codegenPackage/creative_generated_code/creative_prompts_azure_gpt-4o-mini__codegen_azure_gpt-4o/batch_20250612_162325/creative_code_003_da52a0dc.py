"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Create a function that calculates the rental costs for staging furniture and décor based on the pricing model of Unique Home Staging.
Generated: DETERMINISTIC_da52a0dc910ac1d2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_rental_cost(item_list, rental_duration_days):
    """
    Calculate the rental cost for staging furniture and décor based on the pricing model.

    Parameters:
        item_list (list of dict): A list of items where each item is represented as a dictionary
                                  with 'name', 'daily_rate', and 'quantity' keys.
                                  Example: [{'name': 'Sofa', 'daily_rate': 25.0, 'quantity': 2}, ...]
        rental_duration_days (int): The number of days the items will be rented.

    Returns:
        float: The total rental cost for all items.
    """
    # Validate input parameters
    if not isinstance(item_list, list) or not all(isinstance(item, dict) for item in item_list):
        raise ValueError("item_list must be a list of dictionaries representing the items.")
    if not isinstance(rental_duration_days, int) or rental_duration_days <= 0:
        raise ValueError("rental_duration_days must be a positive integer.")

    total_cost = 0.0

    for item in item_list:
        # Validate item data
        if 'name' not in item or 'daily_rate' not in item or 'quantity' not in item:
            raise ValueError("Each item must have 'name', 'daily_rate', and 'quantity' keys.")
        if not isinstance(item['daily_rate'], (int, float)) or item['daily_rate'] < 0:
            raise ValueError(f"Invalid daily_rate for item '{item.get('name', 'Unknown')}'.")
        if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
            raise ValueError(f"Invalid quantity for item '{item.get('name', 'Unknown')}'.")

        # Calculate cost for the current item
        item_cost = item['daily_rate'] * item['quantity'] * rental_duration_days
        total_cost += item_cost

    return total_cost


# Example usage of the function:
if __name__ == "__main__":
    try:
        items = [
            {'name': 'Sofa', 'daily_rate': 25.0, 'quantity': 2},
            {'name': 'Dining Table', 'daily_rate': 40.0, 'quantity': 1},
            {'name': 'Chair', 'daily_rate': 10.0, 'quantity': 4}
        ]
        days = 5
        total = calculate_rental_cost(items, days)
        print(f"Total Rental Cost: ${total:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
