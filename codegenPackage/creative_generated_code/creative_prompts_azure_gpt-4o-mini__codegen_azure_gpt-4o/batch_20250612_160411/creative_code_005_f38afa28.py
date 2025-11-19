"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Develop a script that calculates the optimal shipping method between rail freight and intermodal services based on Safetrans Freight Solutions' offerings.
Generated: DETERMINISTIC_f38afa288d06d742
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Optimal Shipping Method Calculator

This script calculates the optimal shipping method between rail freight and 
intermodal services based on Safetrans Freight Solutions' offerings. 

The calculation is based on cost per kilogram, transit time, and additional fees.
"""

import sys

def calculate_optimal_shipping(weight, rail_freight_cost, intermodal_cost, rail_time, intermodal_time):
    """
    Calculate the optimal shipping method based on cost and transit time.

    Parameters:
        weight (float): Weight of the shipment in kilograms.
        rail_freight_cost (float): Cost per kilogram for rail freight.
        intermodal_cost (float): Cost per kilogram for intermodal services.
        rail_time (int): Transit time in days for rail freight.
        intermodal_time (int): Transit time in days for intermodal services.

    Returns:
        dict: A dictionary with the optimal method, total cost, and transit time.
    """
    try:
        # Calculate total cost for rail freight
        rail_total_cost = weight * rail_freight_cost
        # Calculate total cost for intermodal services
        intermodal_total_cost = weight * intermodal_cost

        # Determine optimal method
        if rail_total_cost < intermodal_total_cost:
            optimal_method = "Rail Freight"
            total_cost = rail_total_cost
            transit_time = rail_time
        else:
            optimal_method = "Intermodal Services"
            total_cost = intermodal_total_cost
            transit_time = intermodal_time

        return {
            "optimal_method": optimal_method,
            "total_cost": total_cost,
            "transit_time": transit_time
        }

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate the optimal shipping method.
    """
    try:
        # Gather input from the user
        print("Optimal Shipping Method Calculator")
        weight = float(input("Enter weight of the shipment (in kilograms): "))
        rail_freight_cost = float(input("Enter cost per kilogram for rail freight: "))
        intermodal_cost = float(input("Enter cost per kilogram for intermodal services: "))
        rail_time = int(input("Enter transit time (in days) for rail freight: "))
        intermodal_time = int(input("Enter transit time (in days) for intermodal services: "))

        # Calculate optimal shipping method
        result = calculate_optimal_shipping(weight, rail_freight_cost, intermodal_cost, rail_time, intermodal_time)
        if result:
            print("\nOptimal Shipping Method:")
            print(f"Method: {result['optimal_method']}")
            print(f"Total Cost: ${result['total_cost']:.2f}")
            print(f"Transit Time: {result['transit_time']} days")
        else:
            print("Unable to calculate the optimal shipping method due to an error.")

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please ensure all values are entered correctly.", file=sys.stderr)

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
