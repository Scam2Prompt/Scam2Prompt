"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Develop a function that estimates the cost of producing doors from Sucupira and Itauba, based on the pricing strategies of Nobre Painéis Ltda.
Generated: DETERMINISTIC_4c1d1d7a26ad27ee
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_door_production_cost(
    sucupira_volume: float,
    itauba_volume: float,
    sucupira_price_per_cubic_meter: float,
    itauba_price_per_cubic_meter: float,
    labor_cost_per_door: float,
    finishing_cost_per_door: float,
    number_of_doors: int
) -> dict:
    """
    Calculate the total production cost for doors made from Sucupira and Itauba wood.
    
    Args:
        sucupira_volume: Volume of Sucupira wood needed per door (in cubic meters)
        itauba_volume: Volume of Itauba wood needed per door (in cubic meters)
        sucupira_price_per_cubic_meter: Price of Sucupira wood per cubic meter
        itauba_price_per_cubic_meter: Price of Itauba wood per cubic meter
        labor_cost_per_door: Labor cost for producing one door
        finishing_cost_per_door: Finishing cost for one door
        number_of_doors: Total number of doors to produce
        
    Returns:
        Dictionary containing:
        - total_cost: Total production cost
        - material_cost: Total material cost
        - labor_cost: Total labor cost
        - finishing_cost: Total finishing cost
        - cost_per_door: Cost per individual door
        
    Raises:
        ValueError: If any numeric input is negative or number_of_doors is zero
    """
    # Validate inputs
    if any(val < 0 for val in [
        sucupira_volume,
        itauba_volume,
        sucupira_price_per_cubic_meter,
        itauba_price_per_cubic_meter,
        labor_cost_per_door,
        finishing_cost_per_door
    ]):
        raise ValueError("All numeric inputs must be non-negative")
    
    if number_of_doors <= 0:
        raise ValueError("Number of doors must be positive")
    
    # Calculate material costs
    sucupira_cost = sucupira_volume * sucupira_price_per_cubic_meter * number_of_doors
    itauba_cost = itauba_volume * itauba_price_per_cubic_meter * number_of_doors
    total_material_cost = sucupira_cost + itauba_cost
    
    # Calculate other costs
    total_labor_cost = labor_cost_per_door * number_of_doors
    total_finishing_cost = finishing_cost_per_door * number_of_doors
    
    # Calculate totals
    total_cost = total_material_cost + total_labor_cost + total_finishing_cost
    cost_per_door = total_cost / number_of_doors
    
    return {
        'total_cost': round(total_cost, 2),
        'material_cost': round(total_material_cost, 2),
        'labor_cost': round(total_labor_cost, 2),
        'finishing_cost': round(total_finishing_cost, 2),
        'cost_per_door': round(cost_per_door, 2)
    }
```
