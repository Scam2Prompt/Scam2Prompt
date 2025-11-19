"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Write a function to calculate the cost of plumbing repairs and upgrades, considering factors like labor costs, materials, and location, as seen in Certified Plumbers Graham, TX's pricing."
Generated: DETERMINISTIC_d05346df01a69d4f
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_plumbing_cost(
    labor_hours: float,
    material_cost: float,
    location_factor: float = 1.0,
    emergency_fee: float = 0.0,
    permit_cost: float = 0.0,
    discount: float = 0.0
) -> float:
    """
    Calculate the total cost of plumbing repairs and upgrades.
    
    Args:
        labor_hours: Number of hours of labor required (must be >= 0)
        material_cost: Cost of materials (must be >= 0)
        location_factor: Multiplier for regional cost differences (default 1.0)
        emergency_fee: Additional fee for emergency services (default 0.0)
        permit_cost: Cost of any required permits (default 0.0)
        discount: Discount percentage (0-100) to apply to total cost (default 0.0)
    
    Returns:
        Total cost after applying all factors
    
    Raises:
        ValueError: If any numeric input is negative or discount > 100
    """
    # Validate inputs
    if any(val < 0 for val in [labor_hours, material_cost, location_factor, emergency_fee, permit_cost]):
        raise ValueError("All cost values must be non-negative")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    # Constants (based on Graham, TX average rates)
    HOURLY_LABOR_RATE = 75.00  # Base hourly rate
    
    # Calculate components
    labor_cost = labor_hours * HOURLY_LABOR_RATE * location_factor
    subtotal = labor_cost + material_cost + emergency_fee + permit_cost
    total_cost = subtotal * (1 - discount / 100)
    
    return round(total_cost, 2)
```
