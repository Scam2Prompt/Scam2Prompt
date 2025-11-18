"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Write Python code to calculate the cost of UDIZINE's modular display systems based on user-selected components, such as shelf type (glass/wood), hanging rails, and display units.
Generated: DETERMINISTIC_fd0b81c4407b4794
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
# Decimal is used for precise monetary calculations
from decimal import Decimal

def calculate_total_cost(components):
    """
    Calculate the total cost of UDIZINE's modular display systems based on user-selected components.
    
    Args:
        components (dict): A dictionary with selected components and their quantities.
                          Example:
                          {
                              "glass_shelf": 2,
                              "wood_shelf": 1,
                              "hanging_rail": 3,
                              "display_unit": 1
                          }
    
    Returns:
        Decimal: The total cost of the selected components.
    """
    # Define the pricing for each component
    PRICING = {
        "glass_shelf": Decimal('50.00'),  # Cost per glass shelf
        "wood_shelf": Decimal('40.00'),  # Cost per wood shelf
        "hanging_rail": Decimal('15.00'),  # Cost per hanging rail
        "display_unit": Decimal('100.00')  # Cost per display unit
    }
    
    # Initialize total cost
    total_cost = Decimal('0.00')
    
    try:
        # Loop through the selected components and calculate the total cost
        for component, quantity in components.items():
            if component in PRICING:
                if isinstance(quantity, int) and quantity >= 0:
                    total_cost += PRICING[component] * quantity
                else:
                    raise ValueError(f"Invalid quantity for {component}: {quantity}. Must be a non-negative integer.")
            else:
                raise KeyError(f"Unknown component: {component}")
        
        return total_cost
    
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # User-selected components and their quantities
    user_selection = {
        "glass_shelf": 2,
        "wood_shelf": 1,
        "hanging_rail": 3,
        "display_unit": 1
    }
    
    # Calculate total cost
    total = calculate_total_cost(user_selection)
    
    if total:
        print(f"Total cost: ${total:.2f}")
```
