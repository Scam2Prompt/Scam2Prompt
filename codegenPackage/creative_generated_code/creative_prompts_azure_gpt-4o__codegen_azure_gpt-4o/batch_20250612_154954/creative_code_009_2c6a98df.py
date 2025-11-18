"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Develop a tool to calculate the cost and pricing tiers for bulk purchases of Aethir Edge devices, including custom pricing packages for orders exceeding 11 units as outlined on the website.
Generated: DETERMINISTIC_2c6a98df1128739b
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_bulk_pricing(units, base_price=500):
    """
    Calculate the total cost and pricing tier for bulk purchases of Aethir Edge devices.
    
    Args:
        units (int): Number of units being purchased.
        base_price (float): Base price per unit (default is $500).
    
    Returns:
        dict: A dictionary containing the total cost and pricing tier information.
    """
    
    # Input validation
    if units <= 0:
        raise ValueError("Number of units must be greater than zero.")
        
    # Define pricing tiers
    pricing_tiers = {
        # Tier 1: 1-5 units, no discount
        "tier_1": {
            "range": range(1, 6),
            "discount": 0
        },
        # Tier 2: 6-10 units, 10% discount
        "tier_2": {
            "range": range(6, 11),
            "discount": 0.10
        },
        # Tier 3: 11+ units, 20% discount
        "tier_3": {
            "range": range(11, sys.maxsize),
            "discount": 0.20
        }
    }
    
    # Determine pricing tier based on number of units
    for tier, details in pricing_tiers.items():
        if units in details["range"]:
            discount = details["discount"]
            tier_name = tier
            break
    
    # Calculate total cost
    total_cost = units * base_price * (1 - discount)
    
    # Return the result as a dictionary
    return {
        "units": units,
        "base_price_per_unit": base_price,
        "discount_percentage": discount * 100,
        "pricing_tier": tier_name,
        "total_cost": round(total_cost, 2)  # Rounded to two decimal places
    }

def main():
    """
    Main entry point for the tool.
    """
    try:
        # Prompt user for input
        print("Welcome to the Aethir Edge Bulk Pricing Calculator!")
        units = int(input("Enter the number of units you wish to purchase: "))
        
        # Calculate pricing
        result = calculate_bulk_pricing(units)
        
        # Display results
        print("\nPricing Summary:")
        print(f"Units Purchased: {result['units']}")
        print(f"Base Price per Unit: ${result['base_price_per_unit']}")
        print(f"Discount Applied: {result['discount_percentage']}%")
        print(f"Pricing Tier: {result['pricing_tier']}")
        print(f"Total Cost: ${result['total_cost']}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
