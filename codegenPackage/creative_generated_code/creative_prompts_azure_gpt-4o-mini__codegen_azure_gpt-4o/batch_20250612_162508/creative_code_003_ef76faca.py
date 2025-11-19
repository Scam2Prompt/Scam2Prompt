"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Generate a function that calculates the probability of winning for different items in the Degen Toy Machine inventory.
Generated: DETERMINISTIC_ef76faca17b60913
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_win_probability(inventory):
    """
    Calculates the probability of winning for each item in the Degen Toy Machine inventory.

    Parameters:
    inventory (dict): A dictionary where keys are item names and values are their weights 
                      (higher weights correspond to higher chances of winning).

    Returns:
    dict: A dictionary where keys are item names and values are the winning probabilities 
          (as percentages) for each item.
    """
    # Error handling: Ensure inventory is a non-empty dictionary
    if not isinstance(inventory, dict) or not inventory:
        raise ValueError("Inventory must be a non-empty dictionary.")

    # Error handling: Ensure weights are positive numbers
    if any(value <= 0 for value in inventory.values()):
        raise ValueError("All weights in the inventory must be positive numbers.")

    # Calculate the total weight of all items
    total_weight = sum(inventory.values())
    
    # Error handling: Ensure total weight is valid
    if total_weight <= 0:
        raise ValueError("Total weight must be greater than zero.")

    # Create a dictionary to store winning probabilities
    probabilities = {}

    for item, weight in inventory.items():
        # Calculate probability as a percentage
        probabilities[item] = (weight / total_weight) * 100

    return probabilities

# Example usage
if __name__ == "__main__":
    try:
        # Degen Toy Machine inventory (example data)
        toy_inventory = {
            "Rare Doll": 10,
            "Mini Robot": 30,
            "Plastic Dinosaur": 20,
            "Rubber Duck": 40
        }

        # Calculate and display win probabilities
        win_probabilities = calculate_win_probability(toy_inventory)
        for item, probability in win_probabilities.items():
            print(f"{item}: {probability:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
