"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Generate a Python script that calculates the shipping costs for orders under $200 from Tiburon Fishing Reels to a third-party shipping company.
Generated: DETERMINISTIC_8256b6a3e2d04645
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the shipping costs for orders under $200 from Tiburon Fishing Reels
to a third-party shipping company. It provides functionality for the input of order details,
calculates shipping costs based on predefined rates, and handles potential errors gracefully.
"""

# Import necessary modules
from typing import Union

# Constants
BASE_SHIPPING_COST = 10.00  # Base shipping cost in USD
ADDITIONAL_COST_PER_POUND = 1.50  # Cost per pound in USD
ORDER_COST_THRESHOLD = 200.00  # Maximum order cost for shipping calculation

def calculate_shipping_cost(order_cost: Union[float, int], package_weight: Union[float, int]) -> Union[float, str]:
    """
    Calculate the shipping cost for an order.
    
    Parameters:
        order_cost (float or int): The total cost of the order in USD.
        package_weight (float or int): The weight of the package in pounds.
    
    Returns:
        float: The total shipping cost in USD if order_cost < ORDER_COST_THRESHOLD.
        str: An error message if the input values are invalid or order_cost exceeds the threshold.
    """
    try:
        # Validate input
        if order_cost < 0 or package_weight < 0:
            return "Error: Order cost and package weight must be non-negative values."
        
        if order_cost >= ORDER_COST_THRESHOLD:
            return "Error: Shipping costs are only calculated for orders under $200."
        
        # Calculate shipping cost
        shipping_cost = BASE_SHIPPING_COST + (package_weight * ADDITIONAL_COST_PER_POUND)
        return round(shipping_cost, 2)  # Round to two decimal places for currency formatting
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"


def main():
    """
    Main function to execute the shipping cost calculation.
    """
    print("Welcome to Tiburon Fishing Reels Shipping Cost Calculator!")
    
    try:
        # Get user input
        order_cost = float(input("Enter the total cost of the order (in USD): "))
        package_weight = float(input("Enter the weight of the package (in pounds): "))
        
        # Calculate shipping cost
        result = calculate_shipping_cost(order_cost, package_weight)
        
        if isinstance(result, str):
            # Display error message
            print(result)
        else:
            # Display shipping cost
            print(f"The shipping cost for your order is: ${result}")
    except ValueError:
        print("Error: Please enter valid numeric values for order cost and package weight.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
