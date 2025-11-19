"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Generate a code snippet to calculate the total cost of dumpster rental based on sizes and service areas mentioned on Purple Dumpster's website.
Generated: DETERMINISTIC_c5e49e4a98298f8d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_dumper_rental_cost(size, service_area):
    """
    Calculate the total cost of dumpster rental based on size and service area.
    :param size: str, the size of the dumpster (e.g., "10-yard", "20-yard", "30-yard").
    :param service_area: str, the service area for delivery (e.g., "urban", "suburban", "rural").
    :return: float, the total cost of the dumpster rental.
    """

    # Define base costs for dumpster sizes
    size_costs = {
        "10-yard": 300.00,
        "20-yard": 400.00,
        "30-yard": 500.00
    }

    # Define additional charges based on service area
    area_costs = {
        "urban": 50.00,
        "suburban": 75.00,
        "rural": 100.00
    }

    try:
        # Check if size is valid
        if size not in size_costs:
            raise ValueError(f"Invalid dumpster size: {size}. Available options are: {', '.join(size_costs.keys())}")

        # Check if service area is valid
        if service_area not in area_costs:
            raise ValueError(f"Invalid service area: {service_area}. Available options are: {', '.join(area_costs.keys())}")

        # Calculate total cost
        total_cost = size_costs[size] + area_costs[service_area]
        
        return total_cost

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

# Example usage:
if __name__ == "__main__":
    # Input: size of dumpster and service area
    dumpster_size = "20-yard"
    delivery_area = "suburban"

    # Calculate cost
    cost = calculate_dumper_rental_cost(dumpster_size, delivery_area)

    if cost is not None:
        print(f"The total cost for a {dumpster_size} dumpster delivered to a {delivery_area} area is: ${cost:.2f}")
    else:
        print("Failed to calculate the dumpster rental cost.")
```
