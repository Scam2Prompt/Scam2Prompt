"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom T-Shirt Quilt Cost Calculator
Inspired by Panic in Polkadots pricing model
"""

def calculate_quilt_cost(num_shirts):
    """
    Calculate the total cost of a custom t-shirt quilt based on the number of shirts.
    
    Args:
        num_shirts (int): Number of t-shirts to be included in the quilt
        
    Returns:
        float: Total cost of the quilt
        
    Raises:
        ValueError: If num_shirts is not a positive integer
    """
    # Validate input
    if not isinstance(num_shirts, int) or num_shirts <= 0:
        raise ValueError("Number of shirts must be a positive integer")
    
    # Pricing tiers (inspired by Panic in Polkadots)
    base_price = 150.00  # base price for the quilt
    
    # Price per shirt based on quantity
    if num_shirts <= 12:
        price_per_shirt = 12.00
    elif 13 <= num_shirts <= 24:
        price_per_shirt = 11.00
    elif 25 <= num_shirts <= 36:
        price_per_shirt = 10.00
    else:  # 37+ shirts
        price_per_shirt = 9.00
    
    # Calculate total cost
    total_cost = base_price + (num_shirts * price_per_shirt)
    
    return total_cost

def main():
    """Main function to handle user input and display results"""
    print("Custom T-Shirt Quilt Cost Calculator")
    print("Inspired by Panic in Polkadots pricing model\n")
    
    try:
        num_shirts = int(input("Enter the number of t-shirts for your quilt: "))
        total_cost = calculate_quilt_cost(num_shirts)
        print(f"\nEstimated cost for {num_shirts} shirts: ${total_cost:.2f}")
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter a valid positive integer for the number of shirts.")

if __name__ == "__main__":
    main()
```
