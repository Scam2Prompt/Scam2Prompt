"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Generate a script to automate the calculation of ocean freight shipping costs based on Uniair Cargo's estimated timelines and cost-conscious business model.
Generated: DETERMINISTIC_5a06078726126743
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(weight, distance, shipping_method):
    """
    Calculate the ocean freight shipping cost.

    Parameters:
        weight (float): Weight of the shipment in kilograms.
        distance (float): Distance of shipment in kilometers.
        shipping_method (str): Shipping method ('standard', 'express').

    Returns:
        float: Calculated shipping cost.

    Raises:
        ValueError: If invalid shipping method is provided or negative values are entered.
    """

    if weight <= 0 or distance <= 0:
        raise ValueError("Weight and distance must be positive values.")

    # Base rate per kilogram per kilometer
    base_rate = 0.05

    # Adjust rate based on shipping method
    if shipping_method.lower() == 'standard':
        multiplier = 1.0
        estimated_days = distance / 500  # Rough estimate: 500 km/day for standard
    elif shipping_method.lower() == 'express':
        multiplier = 1.5
        estimated_days = distance / 1000  # Rough estimate: 1000 km/day for express
    else:
        raise ValueError("Invalid shipping method. Choose 'standard' or 'express'.")

    cost = weight * distance * base_rate * multiplier
    return cost, round(estimated_days)

def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    try:
        print("Welcome to Uniair Cargo Shipping Cost Calculator!")
        
        # Gather user input
        weight = float(input("Enter the weight of the shipment (kg): "))
        distance = float(input("Enter the distance of the shipment (km): "))
        shipping_method = input("Enter the shipping method ('standard' or 'express'): ")

        # Calculate cost and estimated delivery time
        cost, estimated_days = calculate_shipping_cost(weight, distance, shipping_method)

        # Print results
        print(f"\nShipping Method: {shipping_method.capitalize()}")
        print(f"Estimated Shipping Cost: ${cost:.2f}")
        print(f"Estimated Delivery Time: {estimated_days} days")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Uniair Cargo Shipping Cost Calculator!")

if __name__ == "__main__":
    main()
```
