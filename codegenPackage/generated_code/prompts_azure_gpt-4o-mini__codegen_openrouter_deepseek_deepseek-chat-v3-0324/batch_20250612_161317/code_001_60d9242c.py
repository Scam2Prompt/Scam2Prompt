"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_air_freight_cost(weight_kg, distance_km, insurance_required=False):
    """
    Calculate the total cost of air freight forwarding based on weight, distance, and insurance.
    
    Parameters:
        weight_kg (float): Weight of the shipment in kilograms. Must be positive.
        distance_km (float): Distance of the shipment in kilometers. Must be positive.
        insurance_required (bool): Whether insurance is required for the shipment. Defaults to False.
    
    Returns:
        float: Total cost of the shipment.
    
    Raises:
        ValueError: If weight_kg or distance_km is not positive.
    """
    # Validate input parameters
    if weight_kg <= 0:
        raise ValueError("Weight must be positive.")
    if distance_km <= 0:
        raise ValueError("Distance must be positive.")
    
    # Base rate per kg per km (example rate, adjust as needed)
    base_rate_per_kg_km = 0.05
    
    # Calculate base cost
    base_cost = weight_kg * distance_km * base_rate_per_kg_km
    
    # Insurance cost (5% of base cost if required)
    insurance_cost = base_cost * 0.05 if insurance_required else 0
    
    # Total cost
    total_cost = base_cost + insurance_cost
    
    return total_cost
```
