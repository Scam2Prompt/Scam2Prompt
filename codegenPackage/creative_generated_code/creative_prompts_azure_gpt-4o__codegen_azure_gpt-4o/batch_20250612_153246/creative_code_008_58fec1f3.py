"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idgfiber.com
Prompt: Write code to calculate the total weight of purchased fiberglass products, assuming weight data is available for items like Ceramic Fiber and Carbon Fiber Chopped.
Generated: DETERMINISTIC_58fec1f347c11ea7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate the total weight of purchased fiberglass products

def calculate_total_weight(purchased_items, weights):
    """
    Calculate the total weight of purchased fiberglass products.

    Args:
        purchased_items (dict): A dictionary where keys are product names and values are quantities purchased.
                                Example: {'Ceramic Fiber': 5, 'Carbon Fiber Chopped': 3}
        weights (dict): A dictionary where keys are product names and values are weights per unit.
                        Example: {'Ceramic Fiber': 2.5, 'Carbon Fiber Chopped': 1.2}

    Returns:
        float: Total weight of all purchased products.

    Raises:
        ValueError: If the purchased item is not found in the weights dictionary.
    """
    try:
        total_weight = 0.0
        for item, quantity in purchased_items.items():
            if item not in weights:
                raise ValueError(f"Weight data for '{item}' not found.")
            # Calculate weight for the current item
            total_weight += weights[item] * quantity
        return total_weight
    except Exception as e:
        # Log the error (print in this example; replace with proper logging in production)
        print(f"Error calculating total weight: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define weight data
    weights_data = {
        'Ceramic Fiber': 2.5,  # weight per unit in kilograms
        'Carbon Fiber Chopped': 1.2,  # weight per unit in kilograms
    }

    # Define purchased items
    purchased_items_data = {
        'Ceramic Fiber': 5,  # quantity purchased
        'Carbon Fiber Chopped': 3,  # quantity purchased
    }

    # Calculate the total weight
    total_weight = calculate_total_weight(purchased_items_data, weights_data)
    if total_weight is not None:
        print(f"Total weight of purchased fiberglass products: {total_weight:.2f} kg")
```
