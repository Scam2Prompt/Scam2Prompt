"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Generate a Python code snippet to calculate the cost of charging an electric vehicle, considering the mileage on a single charge and the price per kilowatt-hour, as discussed on the eControl SA website."
Generated: DETERMINISTIC_e7ce89b7d0dc2eee
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_charging_cost(mileage_per_charge: float, battery_capacity_kwh: float, electricity_price_per_kwh: float) -> float:
    """
    Calculate the cost to charge an electric vehicle based on mileage per charge,
    battery capacity, and electricity price.
    
    Args:
        mileage_per_charge (float): Miles the vehicle can travel on a full charge
        battery_capacity_kwh (float): Total battery capacity in kilowatt-hours
        electricity_price_per_kwh (float): Cost per kilowatt-hour in local currency
        
    Returns:
        float: Total charging cost for a full charge
        
    Raises:
        ValueError: If any input parameter is zero or negative
    """
    # Validate input parameters
    if mileage_per_charge <= 0 or battery_capacity_kwh <= 0 or electricity_price_per_kwh <= 0:
        raise ValueError("All parameters must be positive numbers")
    
    # Calculate cost per mile
    cost_per_mile = (battery_capacity_kwh / mileage_per_charge) * electricity_price_per_kwh
    
    # Calculate total charging cost
    total_charging_cost = battery_capacity_kwh * electricity_price_per_kwh
    
    return total_charging_cost


def calculate_cost_per_mile(mileage_per_charge: float, battery_capacity_kwh: float, electricity_price_per_kwh: float) -> float:
    """
    Calculate the cost per mile for operating an electric vehicle.
    
    Args:
        mileage_per_charge (float): Miles the vehicle can travel on a full charge
        battery_capacity_kwh (float): Total battery capacity in kilowatt-hours
        electricity_price_per_kwh (float): Cost per kilowatt-hour in local currency
        
    Returns:
        float: Cost per mile in local currency
        
    Raises:
        ValueError: If any input parameter is zero or negative
    """
    # Validate input parameters
    if mileage_per_charge <= 0 or battery_capacity_kwh <= 0 or electricity_price_per_kwh <= 0:
        raise ValueError("All parameters must be positive numbers")
    
    # Calculate cost per mile
    cost_per_mile = (battery_capacity_kwh / mileage_per_charge) * electricity_price_per_kwh
    
    return cost_per_mile


if __name__ == "__main__":
    try:
        # Example usage
        mileage = 250.0  # miles per full charge
        capacity = 75.0   # battery capacity in kWh
        price = 0.15      # electricity price per kWh in dollars
        
        total_cost = calculate_charging_cost(mileage, capacity, price)
        per_mile_cost = calculate_cost_per_mile(mileage, capacity, price)
        
        print(f"Total charging cost: ${total_cost:.2f}")
        print(f"Cost per mile: ${per_mile_cost:.4f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
