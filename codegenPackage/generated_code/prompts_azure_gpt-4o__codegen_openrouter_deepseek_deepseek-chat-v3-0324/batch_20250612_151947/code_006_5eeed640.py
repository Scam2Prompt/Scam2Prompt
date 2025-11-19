"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: Build a calculator tool in Python that estimates savings on furniture and appliances based on ПАНАМ's claim of reducing costs by up to 20%, and outputs the final budget.
Generated: DETERMINISTIC_5eeed640880f4089
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_savings(original_price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.
    
    Args:
        original_price (float): Original price of the item.
        discount_percentage (float): Discount percentage (0 to 20).
    
    Returns:
        float: Discounted price after applying the discount.
    """
    if discount_percentage < 0 or discount_percentage > 20:
        raise ValueError("Discount percentage must be between 0 and 20.")
    
    discount_amount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount_amount
    return discounted_price

def get_float_input(prompt):
    """
    Get a valid float input from the user.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        float: The valid float input from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the ПАНАМ Savings Calculator!")
    print("This tool estimates your savings on furniture and appliances based on ПАНАМ's claim of reducing costs by up to 20%.")
    
    try:
        # Get user inputs
        original_price = get_float_input("Enter the original price of the item: ")
        discount_percentage = get_float_input("Enter the discount percentage (0-20): ")
        
        # Validate discount percentage
        if discount_percentage < 0 or discount_percentage > 20:
            print("Error: Discount percentage must be between 0 and 20.")
            sys.exit(1)
        
        # Calculate savings
        discounted_price = calculate_savings(original_price, discount_percentage)
        savings = original_price - discounted_price
        
        # Display results
        print("\n--- Savings Calculation Results ---")
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Applied: {discount_percentage:.2f}%")
        print(f"Discounted Price: ${discounted_price:.2f}")
        print(f"Total Savings: ${savings:.2f}")
        print("----------------------------------")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
