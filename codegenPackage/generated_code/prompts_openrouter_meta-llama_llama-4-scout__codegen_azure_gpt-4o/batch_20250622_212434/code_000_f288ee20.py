"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: "Write a Python script to calculate the cost of installing aluminum windows with thermopanel PVC in Chile, considering the company's 12-month guarantee and quality European standards."
Generated: DETERMINISTIC_f288ee204cd9cc12
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost of installing aluminum windows with thermopanel PVC in Chile.
The script considers the company's 12-month guarantee and quality European standards.
"""

# Import necessary modules
import sys

def calculate_window_cost(width, height, price_per_square_meter):
    """
    Calculate the cost of a single aluminum window with thermopanel PVC.

    Args:
        width (float): Width of the window in meters.
        height (float): Height of the window in meters.
        price_per_square_meter (float): Price per square meter in Chilean pesos.

    Returns:
        float: Total cost of the window in Chilean pesos.
    """
    try:
        # Ensure dimensions are positive
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        
        # Calculate area
        area = width * height
        
        # Calculate total cost
        total_cost = area * price_per_square_meter
        
        return total_cost
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate the cost of windows.
    """
    print("Welcome to the Aluminum Windows Cost Calculator!")
    print("This tool calculates the cost of installing aluminum windows with thermopanel PVC in Chile.")
    print("The company offers a 12-month guarantee and adheres to quality European standards.\n")
    
    try:
        # Get user input for dimensions and price
        width = float(input("Enter the width of the window (in meters): "))
        height = float(input("Enter the height of the window (in meters): "))
        price_per_square_meter = float(input("Enter the price per square meter (in Chilean pesos): "))
        
        # Calculate cost
        total_cost = calculate_window_cost(width, height, price_per_square_meter)
        
        # Display result
        print(f"\nThe total cost of the window installation is: {total_cost:.2f} Chilean pesos.")
        print("Thank you for using the Aluminum Windows Cost Calculator!")
    except ValueError:
        print("Error: Please enter valid numeric values for width, height, and price.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
