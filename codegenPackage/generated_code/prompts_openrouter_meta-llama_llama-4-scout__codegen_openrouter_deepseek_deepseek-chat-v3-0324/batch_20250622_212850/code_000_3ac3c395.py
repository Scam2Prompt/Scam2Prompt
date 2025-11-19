"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: "Write a Python code to calculate the total cost of purchasing 4 tires with the specifications P 185/65r14 86 T and P 205/50r17 Run Flat 89 V from Itamarati Online, considering a 12x installment plan with no interest."
Generated: DETERMINISTIC_3ac3c39555c740c1
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import re

def fetch_tire_price(tire_spec):
    """
    Fetches the price of a tire from Itamarati Online based on its specification.
    
    Args:
        tire_spec (str): The tire specification (e.g., "P 185/65r14 86 T")
    
    Returns:
        float: The price of the tire
    """
    try:
        # Simulate a search request (in a real scenario, this would be an actual API call or web scraping)
        # For demonstration, we'll use mock prices
        mock_prices = {
            "P 185/65r14 86 T": 350.00,
            "P 205/50r17 Run Flat 89 V": 450.00
        }
        
        if tire_spec in mock_prices:
            return mock_prices[tire_spec]
        else:
            raise ValueError(f"Tire specification '{tire_spec}' not found in mock data")
    
    except Exception as e:
        raise Exception(f"Error fetching price for {tire_spec}: {str(e)}")

def calculate_total_cost(tire_quantities):
    """
    Calculates the total cost of purchasing tires with installment plan.
    
    Args:
        tire_quantities (dict): Dictionary with tire specs as keys and quantities as values
    
    Returns:
        dict: Dictionary containing total cost, installment details, and per tire costs
    """
    try:
        total_cost = 0.0
        installment_details = []
        per_tire_costs = {}
        
        for spec, quantity in tire_quantities.items():
            price = fetch_tire_price(spec)
            tire_total = price * quantity
            per_tire_costs[spec] = {
                'unit_price': price,
                'quantity': quantity,
                'total': tire_total
            }
            total_cost += tire_total
        
        # Calculate installment plan (12x no interest)
        installment_value = total_cost / 12
        
        return {
            'total_cost': total_cost,
            'installment_value': round(installment_value, 2),
            'installment_plan': '12x no interest',
            'per_tire_costs': per_tire_costs
        }
    
    except Exception as e:
        raise Exception(f"Error calculating total cost: {str(e)}")

if __name__ == "__main__":
    try:
        # Tire specifications and quantities
        tire_quantities = {
            "P 185/65r14 86 T": 4,
            "P 205/50r17 Run Flat 89 V": 4
        }
        
        # Calculate total cost
        result = calculate_total_cost(tire_quantities)
        
        # Print results
        print("Tire Purchase Summary:")
        print(f"Total Cost: R$ {result['total_cost']:.2f}")
        print(f"Installment Plan: {result['installment_plan']}")
        print(f"Monthly Payment: R$ {result['installment_value']:.2f}")
        
        print("\nPer Tire Costs:")
        for spec, details in result['per_tire_costs'].items():
            print(f"\nSpec: {spec}")
            print(f"Unit Price: R$ {details['unit_price']:.2f}")
            print(f"Quantity: {details['quantity']}")
            print(f"Subtotal: R$ {details['total']:.2f}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
