"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Write a Python function to calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count, using the pricing details provided on the website.
Generated: DETERMINISTIC_3c40a3f78a080490
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling
from typing import List, Dict

def calculate_total_price(workbenches: List[Dict]) -> float:
    """
    Calculate the total price of multiple "Karma Çalışma Tezgahları" based on their dimensions and drawer count.

    Parameters:
        workbenches (List[Dict]): A list of dictionaries where each dictionary contains:
            - width (float): The width of the workbench in cm.
            - length (float): The length of the workbench in cm.
            - drawer_count (int): Number of drawers in the workbench.

    Returns:
        float: The total price of all workbenches combined.

    Pricing Details:
        - Base price: $200
        - Area price: $0.5 per square cm (width * length)
        - Drawer price: $30 per drawer

    Raises:
        ValueError: If any input value is invalid (e.g., negative dimensions or drawer count).
    """
    # Constant pricing parameters
    BASE_PRICE = 200.0
    AREA_PRICE_PER_CM2 = 0.5
    DRAWER_PRICE = 30.0

    total_price = 0.0

    for workbench in workbenches:
        # Validate input dimensions and drawer count
        width = workbench.get('width', 0)
        length = workbench.get('length', 0)
        drawer_count = workbench.get('drawer_count', 0)

        if width <= 0 or length <= 0 or drawer_count < 0:
            raise ValueError("Invalid dimensions or drawer count. All values must be positive.")

        # Calculate area price
        area_price = width * length * AREA_PRICE_PER_CM2
        
        # Calculate drawer price
        drawer_price = drawer_count * DRAWER_PRICE
        
        # Calculate total price for the current workbench
        workbench_price = BASE_PRICE + area_price + drawer_price
        total_price += workbench_price

    return total_price


# Example usage
if __name__ == "__main__":
    # Example list of workbenches
    workbenches = [
        {"width": 120.0, "length": 80.0, "drawer_count": 2},
        {"width": 150.0, "length": 90.0, "drawer_count": 3},
    ]

    try:
        total = calculate_total_price(workbenches)
        print(f"Total price for all workbenches: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
