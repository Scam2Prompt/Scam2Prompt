"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftcargoex.com
Prompt: Create a function that calculates shipping costs for different modes of transport (air, sea, road) based on SwiftCargoExpress's pricing model.
Generated: DETERMINISTIC_b1c17410759cb2c0
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shipping Cost Calculator for SwiftCargoExpress

This function calculates shipping costs based on the mode of transport 
(air, sea, road) and the weight of the shipment. It adheres to 
SwiftCargoExpress's pricing model.

Pricing Model:
- Air: $10 per kg, minimum charge $50
- Sea: $5 per kg, minimum charge $30
- Road: $3 per kg, minimum charge $20

Parameters:
- mode (str): Transport mode ('air', 'sea', 'road')
- weight (float): Weight of shipment in kilograms

Returns:
- float: Total shipping cost

Raises:
- ValueError: If mode is invalid or weight is non-positive
"""

def calculate_shipping_cost(mode, weight):
    # Validate input
    if not isinstance(mode, str):
        raise ValueError("Mode must be a string ('air', 'sea', 'road').")
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number.")

    # Define pricing model
    pricing = {
        "air": {"rate": 10, "minimum": 50},
        "sea": {"rate": 5, "minimum": 30},
        "road": {"rate": 3, "minimum": 20},
    }

    # Check if mode is valid
    if mode not in pricing:
        raise ValueError("Invalid mode. Choose between 'air', 'sea', or 'road'.")

    # Compute cost based on mode and weight
    rate = pricing[mode]["rate"]
    minimum_charge = pricing[mode]["minimum"]
    cost = max(weight * rate, minimum_charge)

    return cost


# Example usage:
if __name__ == "__main__":
    try:
        mode = "air"
        weight = 7.5  # in kilograms
        cost = calculate_shipping_cost(mode, weight)
        print(f"Shipping cost for {mode} transport is ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
