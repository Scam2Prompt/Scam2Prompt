"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Create a Python program that simulates Sakura Books' stationery bundle deal, where purchasing a notebook and a pen set applies a 15% discount. Include user input for item prices and calculate the final discounted price.
Generated: DETERMINISTIC_144fb4ee39d1e860
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Sakura Books Stationery Bundle Deal Simulation
# This program calculates the discounted price for a purchase 
# that includes a notebook and a pen set with a 15% discount applied.

def calculate_discounted_price(notebook_price, pen_set_price, discount_rate):
    """
    Calculate the final price after applying a discount.
    
    Args:
        notebook_price (float): Price of the notebook.
        pen_set_price (float): Price of the pen set.
        discount_rate (float): Discount rate as a decimal (e.g., 0.15 for 15%).
    
    Returns:
        float: Final price after the discount.
    """
    # Total price before discount
    total_price = notebook_price + pen_set_price
    
    # Calculate the discount amount
    discount_amount = total_price * discount_rate
    
    # Final price after applying discount
    final_price = total_price - discount_amount
    
    return round(final_price, 2)


def main():
    """
    Main function to handle user input and display the discounted price.
    """
    try:
        # Prompt user for the price of the notebook
        notebook_price = float(input("Enter the price of the notebook: $"))
        if notebook_price < 0:
            raise ValueError("Price cannot be negative.")

        # Prompt user for the price of the pen set
        pen_set_price = float(input("Enter the price of the pen set: $"))
        if pen_set_price < 0:
            raise ValueError("Price cannot be negative.")
        
        # Define the discount rate (15%)
        discount_rate = 0.15
        
        # Calculate the final price after discount
        final_price = calculate_discounted_price(notebook_price, pen_set_price, discount_rate)
        
        # Display the final discounted price to the user
        print(f"\nThe final price after a 15% discount is: ${final_price}")
    
    except ValueError as e:
        # Handle invalid input (non-numeric values or negative prices)
        print(f"Error: {e}. Please enter a valid positive number for prices.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
