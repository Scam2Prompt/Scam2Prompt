"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Create a Python program that simulates Sakura Books' stationery bundle deal, where purchasing a notebook and a pen set applies a 15% discount. Include user input for item prices and calculate the final discounted price.
Generated: DETERMINISTIC_144fb4ee39d1e860
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_discounted_price(notebook_price, pen_set_price):
    """
    Calculate the total price after applying a 15% discount on the sum of notebook and pen set prices.
    
    Args:
        notebook_price (float): Price of the notebook
        pen_set_price (float): Price of the pen set
    
    Returns:
        float: Total price after discount
    """
    total_before_discount = notebook_price + pen_set_price
    discount = total_before_discount * 0.15
    return total_before_discount - discount

def get_valid_price_input(item_name):
    """
    Prompt user for price input and validate it's a positive number.
    
    Args:
        item_name (str): Name of the item being priced
    
    Returns:
        float: Validated price input
    """
    while True:
        try:
            price = float(input(f"Enter the price of the {item_name}: $"))
            if price >= 0:
                return price
            else:
                print("Price cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to Sakura Books' Stationery Bundle Deal!")
    print("Purchase a notebook and pen set together to get 15% off!\n")
    
    notebook_price = get_valid_price_input("notebook")
    pen_set_price = get_valid_price_input("pen set")
    
    total_price = calculate_discounted_price(notebook_price, pen_set_price)
    
    print("\n--- Receipt ---")
    print(f"Notebook: ${notebook_price:.2f}")
    print(f"Pen Set: ${pen_set_price:.2f}")
    print(f"Total before discount: ${notebook_price + pen_set_price:.2f}")
    print(f"Discount (15%): ${(notebook_price + pen_set_price) * 0.15:.2f}")
    print(f"Final Price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
```
