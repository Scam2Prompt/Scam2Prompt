"""
Generated Code Metadata:
========================
Original URL: https://napamerch.com
Prompt: Create a Python script to calculate the total cost of an order for NAPA T-shirts, considering factors like shirt size, quantity, and shipping costs.
Generated: DETERMINISTIC_b97ec6e05dcd8660
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the total cost of an order for NAPA T-shirts

# Constants for shirt prices based on size
SHIRT_PRICES = {
    "S": 15.00,  # Small size price
    "M": 17.50,  # Medium size price
    "L": 20.00,  # Large size price
    "XL": 22.50  # Extra Large size price
}

# Flat shipping cost
SHIPPING_COST = 5.00

def calculate_order_cost(size, quantity):
    """
    Calculate the total cost of an order for NAPA T-shirts.

    Args:
        size (str): The size of the T-shirt ('S', 'M', 'L', 'XL').
        quantity (int): The number of T-shirts ordered.

    Returns:
        float: The total cost of the order, including shipping.
    """
    try:
        # Validate size
        if size not in SHIRT_PRICES:
            raise ValueError(f"Invalid shirt size '{size}'. Valid sizes are: {', '.join(SHIRT_PRICES.keys())}")
        
        # Validate quantity
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Calculate cost of shirts
        shirt_cost = SHIRT_PRICES[size] * quantity
        
        # Calculate total cost including shipping
        total_cost = shirt_cost + SHIPPING_COST
        
        return total_cost
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate the order cost.
    """
    print("Welcome to the NAPA T-shirt Order Calculator!")
    
    try:
        # Get user input for shirt size
        size = input("Enter the shirt size (S, M, L, XL): ").strip().upper()
        
        # Get user input for quantity
        quantity = int(input("Enter the quantity of shirts: "))
        
        # Calculate total cost
        total_cost = calculate_order_cost(size, quantity)
        
        if total_cost is not None:
            print(f"The total cost of your order is: ${total_cost:.2f}")
        else:
            print("Failed to calculate the order cost due to invalid input.")
    
    except ValueError:
        # Handle invalid input for quantity
        print("Error: Quantity must be a valid integer.")

if __name__ == "__main__":
    main()
```
