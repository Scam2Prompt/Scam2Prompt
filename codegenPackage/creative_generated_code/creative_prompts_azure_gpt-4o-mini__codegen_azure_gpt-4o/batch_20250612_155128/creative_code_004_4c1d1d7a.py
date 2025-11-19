"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary modules
from typing import Dict, Union

def estimate_door_cost(material: str, height: float, width: float, num_doors: int) -> Union[float, str]:
    """
    Estimates the cost of producing doors made from Sucupira or Itauba wood.
    
    Nobre Painéis Ltda Pricing Strategy:
    - Sucupira: $150 per square meter
    - Itauba: $180 per square meter
    
    Args:
        material (str): The type of wood ("Sucupira" or "Itauba").
        height (float): The height of the door in meters.
        width (float): The width of the door in meters.
        num_doors (int): The number of doors to be produced.
    
    Returns:
        float: The total estimated cost of producing the doors.
        str: Error message if invalid input is provided.
    """
    
    # Pricing per square meter for each type of wood
    pricing: Dict[str, float] = {
        "Sucupira": 150.0,
        "Itauba": 180.0
    }
    
    # Input validation
    if material not in pricing:
        return "Error: Invalid material. Please choose 'Sucupira' or 'Itauba'."
    if height <= 0 or width <= 0:
        return "Error: Height and width must be positive values."
    if num_doors <= 0:
        return "Error: Number of doors must be a positive integer."
    
    try:
        # Calculate the area of one door (height * width)
        area_per_door = height * width
        
        # Calculate the total area (area of one door multiplied by the number of doors)
        total_area = area_per_door * num_doors
        
        # Calculate the total cost based on material pricing
        cost_per_square_meter = pricing[material]
        total_cost = total_area * cost_per_square_meter
        
        return round(total_cost, 2)  # Return cost rounded to 2 decimal places
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Example usage:
# cost = estimate_door_cost("Sucupira", 2.0, 0.8, 5)
# print(cost)  # Output: 1200.0
```
