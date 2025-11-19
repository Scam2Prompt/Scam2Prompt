"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Create a function that calculates the cost of printing various items like wedding cards and business cards, based on the pricing model described by Ram Digi.
Generated: DETERMINISTIC_9dd2a66dfa13f270
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python Code: Function to calculate the cost of printing items based on a pricing model

def calculate_printing_cost(item_type, quantity):
    """
    Calculate the cost of printing items based on the pricing model.

    Parameters:
        item_type (str): Type of item to print ('wedding_card', 'business_card').
        quantity (int): Number of items to print.

    Returns:
        float: Total cost of printing the items.

    Raises:
        ValueError: If the item_type is invalid or quantity is not positive.
    """
    # Pricing model (cost per item)
    pricing_model = {
        'wedding_card': 2.50,  # Cost per wedding card
        'business_card': 0.10  # Cost per business card
    }

    # Validate input
    if item_type not in pricing_model:
        raise ValueError(f"Invalid item type: {item_type}. Valid types are: {', '.join(pricing_model.keys())}")
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    # Calculate total cost
    cost_per_item = pricing_model[item_type]
    total_cost = cost_per_item * quantity

    return total_cost


# Example usage:
if __name__ == "__main__":
    try:
        # Test cases
        print("Cost of 100 wedding cards:", calculate_printing_cost('wedding_card', 100))  # Expected: 250.0
        print("Cost of 500 business cards:", calculate_printing_cost('business_card', 500))  # Expected: 50.0
    except ValueError as e:
        print("Error:", e)
```
