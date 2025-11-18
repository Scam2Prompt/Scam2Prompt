"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Write a program to calculate shipping costs for air, sea, and land freight options, based on the services provided by Portline Shipping & Logistic.
Generated: DETERMINISTIC_6a72cac770c5307b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate shipping costs for air, sea, and land freight options
# based on the services provided by Portline Shipping & Logistic.

# Import necessary modules
from typing import Union

# Define shipping rates per unit weight (in USD per kg)
SHIPPING_RATES = {
    "air": 5.0,  # Air freight cost per kg
    "sea": 2.0,  # Sea freight cost per kg
    "land": 3.0  # Land freight cost per kg
}

def calculate_shipping_cost(weight: Union[int, float], method: str) -> Union[float, str]:
    """
    Calculate the shipping cost based on the freight method and weight.

    :param weight: Weight of the shipment in kilograms (must be > 0).
    :param method: Shipping method (options: "air", "sea", "land").
    :return: Shipping cost in USD or an error message if input is invalid.
    """
    try:
        # Validate input weight
        if weight <= 0:
            return "Error: Weight must be greater than 0."
        
        # Validate shipping method
        method = method.lower()  # Allow case-insensitive input
        if method not in SHIPPING_RATES:
            return f"Error: Invalid shipping method. Choose from {', '.join(SHIPPING_RATES.keys())}."
        
        # Calculate and return the shipping cost
        cost = weight * SHIPPING_RATES[method]
        return round(cost, 2)  # Return cost rounded to two decimal places
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    print("Welcome to Portline Shipping & Logistic!")
    print("Available shipping methods: air, sea, land.")
    
    try:
        # Get user input for weight
        weight = float(input("Enter the weight of your shipment in kilograms: "))
        
        # Get user input for shipping method
        method = input("Enter the desired shipping method (air, sea, land): ")
        
        # Calculate shipping cost
        result = calculate_shipping_cost(weight, method)
        
        # Display the result
        if isinstance(result, str):  # If there was an error, display the message
            print(result)
        else:  # Otherwise, display the calculated cost
            print(f"The shipping cost for {weight} kg via {method} freight is: ${result:.2f}")
    
    except ValueError:
        print("Error: Please enter a valid number for weight.")

if __name__ == "__main__":
    main()
```
