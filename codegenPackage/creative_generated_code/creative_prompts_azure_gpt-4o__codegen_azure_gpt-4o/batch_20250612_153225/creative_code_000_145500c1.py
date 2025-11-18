"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Write a Python script to calculate the cost of bulk uniform production, including accessories like hats and belts, based on the pricing model described by Real Garment Konveksi Seragam in Surabaya.
Generated: DETERMINISTIC_145500c14ca58846
Batch ID: 20250612_153225
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

def calculate_uniform_cost(quantity, uniform_price, hat_price=None, belt_price=None):
    """
    Calculate the total cost for bulk uniform production, including optional accessories.

    Args:
        quantity (int): Number of uniforms to produce.
        uniform_price (float): Price per uniform.
        hat_price (float, optional): Price per hat, if included.
        belt_price (float, optional): Price per belt, if included.

    Returns:
        float: Total cost for the bulk production.
    """
    try:
        # Ensure all inputs are valid
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if uniform_price < 0:
            raise ValueError("Uniform price cannot be negative.")
        if hat_price is not None and hat_price < 0:
            raise ValueError("Hat price cannot be negative.")
        if belt_price is not None and belt_price < 0:
            raise ValueError("Belt price cannot be negative.")
        
        # Calculate total cost
        total_cost = quantity * uniform_price
        
        # Add costs for accessories if included
        if hat_price is not None:
            total_cost += quantity * hat_price
        if belt_price is not None:
            total_cost += quantity * belt_price
        
        return total_cost
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function for user interaction and calculating uniform production costs.
    """
    print("Welcome to the Bulk Uniform Cost Calculator!")
    try:
        # Input for number of uniforms
        quantity = int(input("Enter the number of uniforms to produce: "))
        
        # Input for uniform price
        uniform_price = float(input("Enter the price per uniform: "))
        
        # Input for accessory costs (optional)
        include_hat = input("Include hats? (yes/no): ").strip().lower() == "yes"
        hat_price = float(input("Enter the price per hat: ")) if include_hat else None
        
        include_belt = input("Include belts? (yes/no): ").strip().lower() == "yes"
        belt_price = float(input("Enter the price per belt: ")) if include_belt else None
        
        # Calculate total cost
        total_cost = calculate_uniform_cost(quantity, uniform_price, hat_price, belt_price)
        
        if total_cost is not None:
            print(f"The total cost for producing {quantity} uniforms is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the total cost due to invalid inputs.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numbers for quantity and prices.", file=sys.stderr)

if __name__ == "__main__":
    main()
```
