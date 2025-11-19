"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Create a function that calculates the cost-effectiveness of using trailer drop services for freight forwarding, based on the operational efficiencies highlighted by Calmar Transport.
Generated: DETERMINISTIC_5ecbe218c17139bb
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_effectiveness(
    distance: float,
    fuel_cost_per_mile: float,
    driver_cost_per_mile: float,
    trailer_drop_fee: float,
    standard_delivery_time: float,
    trailer_drop_time_saving: float,
    hourly_operating_cost: float
) -> dict:
    """
    Calculate the cost-effectiveness of using trailer drop services for freight forwarding.
    
    Args:
        distance (float): Total distance of the route in miles.
        fuel_cost_per_mile (float): Fuel cost per mile in dollars.
        driver_cost_per_mile (float): Driver cost per mile in dollars.
        trailer_drop_fee (float): Fee for using trailer drop service in dollars.
        standard_delivery_time (float): Standard delivery time without trailer drop in hours.
        trailer_drop_time_saving (float): Time saved by using trailer drop in hours.
        hourly_operating_cost (float): Operating cost per hour in dollars.
        
    Returns:
        dict: Dictionary containing cost comparison and savings information.
              Keys: 'standard_cost', 'trailer_drop_cost', 'total_savings', 'time_savings_hours'
    """
    try:
        # Calculate standard delivery cost (without trailer drop)
        standard_fuel_cost = distance * fuel_cost_per_mile
        standard_driver_cost = distance * driver_cost_per_mile
        standard_operating_cost = standard_delivery_time * hourly_operating_cost
        standard_total_cost = standard_fuel_cost + standard_driver_cost + standard_operating_cost
        
        # Calculate trailer drop delivery cost
        trailer_drop_fuel_cost = distance * fuel_cost_per_mile
        trailer_drop_driver_cost = distance * driver_cost_per_mile
        trailer_drop_operating_cost = (standard_delivery_time - trailer_drop_time_saving) * hourly_operating_cost
        trailer_drop_total_cost = (trailer_drop_fuel_cost + trailer_drop_driver_cost + 
                                 trailer_drop_operating_cost + trailer_drop_fee)
        
        # Calculate savings
        total_savings = standard_total_cost - trailer_drop_total_cost
        time_savings = trailer_drop_time_saving
        
        return {
            'standard_cost': round(standard_total_cost, 2),
            'trailer_drop_cost': round(trailer_drop_total_cost, 2),
            'total_savings': round(total_savings, 2),
            'time_savings_hours': round(time_savings, 2),
            'is_cost_effective': total_savings > 0
        }
        
    except Exception as e:
        raise ValueError(f"Error calculating cost effectiveness: {str(e)}")


# Example usage (commented out for production)
# if __name__ == "__main__":
#     result = calculate_cost_effectiveness(
#         distance=500,
#         fuel_cost_per_mile=0.45,
#         driver_cost_per_mile=0.60,
#         trailer_drop_fee=200,
#         standard_delivery_time=12,
#         trailer_drop_time_saving=3,
#         hourly_operating_cost=50
#     )
#     print(result)
```
