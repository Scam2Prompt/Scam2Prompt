"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--grsklippare-m8a.se
Prompt: Write a code snippet to filter lawn mowers by price and type, similar to the sorting options on Gräsklippare.se.
Generated: DETERMINISTIC_252037a0fb7b8bb6
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LawnMower:
    def __init__(self, model, price, mower_type):
        self.model = model
        self.price = price
        self.mower_type = mower_type

    def __repr__(self):
        return f"{self.model} | Price: {self.price} | Type: {self.mower_type}"

def filter_lawn_mowers(mowers, max_price=None, mower_type=None):
    """
    Filters the list of lawn mowers based on price and type.

    Parameters:
        mowers (list): List of LawnMower objects to filter.
        max_price (float): Maximum price for filtering.
        mower_type (str): The type of mower to filter.

    Returns:
        list: A list of filtered LawnMower objects.
    """
    # Validate input
    if not isinstance(mowers, list):
        raise ValueError("Invalid input: mowers should be a list.")
    
    filtered_mowers = []
    
    for mower in mowers:
        # Check if the mower meets the price criteria
        if max_price is not None and mower.price > max_price:
            continue
        
        # Check if the mower meets the type criteria
        if mower_type is not None and mower.mower_type.lower() != mower_type.lower():
            continue
        
        filtered_mowers.append(mower)

    return filtered_mowers

# Example usage
if __name__ == "__main__":
    # Sample data
    mowers = [
        LawnMower("Model A", 300, "Electric"),
        LawnMower("Model B", 400, "Gas"),
        LawnMower("Model C", 250, "Electric"),
        LawnMower("Model D", 500, "Gas"),
    ]
    
    try:
        # Filter mowers under 400 that are Electric
        result = filter_lawn_mowers(mowers, max_price=400, mower_type="Electric")
        print("Filtered Lawn Mowers:")
        for mower in result:
            print(mower)
    except ValueError as e:
        print(f"Error: {e}")
```
