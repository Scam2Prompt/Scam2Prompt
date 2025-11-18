"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a function to calculate the cost of carpet supply and installation for rental properties, factoring in durability and affordability, as described on Perfect Melbourne Carpet's site.
Generated: DETERMINISTIC_dd149f3f227c94ab
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

def calculate_carpet_cost(room_length, room_width, carpet_price_per_sq_meter, installation_cost_per_sq_meter, durability_factor=1.0, affordability_factor=1.0):
    """
    Calculate the total cost of carpet supply and installation for a room.

    Parameters:
    - room_length (float): Length of the room in meters.
    - room_width (float): Width of the room in meters.
    - carpet_price_per_sq_meter (float): Price of carpet per square meter.
    - installation_cost_per_sq_meter (float): Installation cost per square meter.
    - durability_factor (float, optional): Multiplier for durability adjustment (default is 1.0).
    - affordability_factor (float, optional): Multiplier for affordability adjustment (default is 1.0).

    Returns:
    - total_cost (float): Total calculated cost for carpet and installation.
    """
    try:
        # Validate inputs
        if not (room_length > 0 and room_width > 0):
            raise ValueError("Room dimensions must be positive values.")
        if not (carpet_price_per_sq_meter > 0 and installation_cost_per_sq_meter > 0):
            raise ValueError("Prices must be positive values.")
        if durability_factor <= 0 or affordability_factor <= 0:
            raise ValueError("Durability and affordability factors must be positive values.")

        # Calculate the area of the room
        room_area = room_length * room_width
        
        # Calculate the base cost for carpet and installation
        base_carpet_cost = room_area * carpet_price_per_sq_meter
        base_installation_cost = room_area * installation_cost_per_sq_meter
        
        # Adjust costs for durability and affordability
        adjusted_carpet_cost = base_carpet_cost * durability_factor
        adjusted_installation_cost = base_installation_cost * affordability_factor
        
        # Calculate the total cost
        total_cost = math.ceil(adjusted_carpet_cost + adjusted_installation_cost)  # Use math.ceil to round up to the nearest integer
        
        return total_cost
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Parameters for the calculation
    length = 5.0  # in meters
    width = 4.0  # in meters
    carpet_price = 20.0  # price per square meter
    installation_cost = 10.0  # installation cost per square meter
    durability = 1.2  # durability factor
    affordability = 0.9  # affordability factor

    # Calculate the total cost
    total_carpet_cost = calculate_carpet_cost(length, width, carpet_price, installation_cost, durability, affordability)
    
    if total_carpet_cost is not None:
        print(f"The total cost for carpet supply and installation is: ${total_carpet_cost}")
```
