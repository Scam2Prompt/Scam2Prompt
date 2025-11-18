"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Develop an algorithm to estimate the cost of moving furniture based on شركة آل البيت's recommendations for budget planning and minimizing expenses.
Generated: DETERMINISTIC_12e0fa5c8d9875e1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Furniture Moving Cost Estimation Algorithm

This script provides an estimate of moving costs based on شركة آل البيت's recommendations for budget planning.
It calculates the cost based on the furniture weight, distance, and additional services requested.
"""

def estimate_moving_cost(furniture_weight, distance, additional_services=[]):
    """
    Estimate the cost of moving furniture.

    Parameters:
    - furniture_weight (float): Total weight of furniture in kilograms.
    - distance (float): Distance to be moved in kilometers.
    - additional_services (list): List of additional services requested (e.g., packing, unpacking, insurance).

    Returns:
    - float: Estimated cost of moving furniture.
    """
    try:
        # Constants based on شركة آل البيت's recommendations
        BASE_RATE_PER_KG = 0.5  # Cost per kilogram of furniture weight
        BASE_RATE_PER_KM = 1.0  # Cost per kilometer of distance
        SERVICE_COSTS = {
            'packing': 100,      # Flat rate for packing service
            'unpacking': 75,     # Flat rate for unpacking service
            'insurance': 150,    # Flat rate for insurance service
        }

        # Validate inputs
        if furniture_weight <= 0 or distance <= 0:
            raise ValueError("Furniture weight and distance must be positive values.")

        # Calculate base cost
        weight_cost = furniture_weight * BASE_RATE_PER_KG
        distance_cost = distance * BASE_RATE_PER_KM
        base_cost = weight_cost + distance_cost

        # Add costs for additional services
        additional_services_cost = sum(SERVICE_COSTS[service] for service in additional_services if service in SERVICE_COSTS)

        # Total cost calculation
        total_cost = base_cost + additional_services_cost
        return round(total_cost, 2)  # Return the total cost rounded to two decimal places

    except KeyError as ke:
        print(f"Error: Unknown service '{ke}' requested.")
        return None
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Input parameters (example values)
    furniture_weight = 120.5  # in kilograms
    distance = 25.0           # in kilometers
    additional_services = ['packing', 'insurance']  # Additional services requested

    # Estimate moving cost
    cost_estimate = estimate_moving_cost(furniture_weight, distance, additional_services)
    if cost_estimate is not None:
        print(f"The estimated moving cost is: ${cost_estimate}")
    else:
        print("Failed to estimate moving cost. Please check the input values.")
```
