"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Generate code to calculate the total puff capacity for a wholesale order of Elfworld vape devices, including PB45000 (45000 puffs), AI22000 (22000 puffs), and Big-B (100000 puffs).
Generated: DETERMINISTIC_4b135e3598a59f42
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
# For scalability, we might want to handle JSON import/export or database integration
import sys

def calculate_total_puff_capacity(order):
    """
    Calculate the total puff capacity for a given order of vape devices.

    Args:
        order (dict): A dictionary representing the quantity of each vape model.

    Returns:
        int: Total puff capacity for the wholesale order.
    """
    # Vape models with their respective puff capacities
    vape_models = {
        "PB45000": 45000,  # PB45000 offers 45000 puffs per unit
        "AI22000": 22000,  # AI22000 offers 22000 puffs per unit
        "Big-B": 100000    # Big-B offers 100000 puffs per unit
    }

    total_puffs = 0

    try:
        # Iterate through the order and calculate total puffs
        for model, quantity in order.items():
            if model in vape_models:
                total_puffs += vape_models[model] * quantity
            else:
                print(f"Warning: '{model}' is not a recognized vape device model.")
        return total_puffs
    except Exception as e:
        print(f"An error occurred while calculating total puff capacity: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example wholesale order
    # Adjust quantities as needed for real-world orders
    order_example = {
        "PB45000": 10,  # 10 units of PB45000
        "AI22000": 5,   # 5 units of AI22000
        "Big-B": 2,     # 2 units of Big-B
        "UnknownModel": 4  # Example of an invalid model for demonstration
    }

    # Calculate and display the total puff capacity
    total_capacity = calculate_total_puff_capacity(order_example)
    print(f"Total puff capacity for the wholesale order: {total_capacity}")
```
