"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Create a script to calculate shipping costs for promotional items based on the free shipping threshold of Rp. 10,000,000 mentioned on the Merchandiso website.
Generated: DETERMINISTIC_d9bc2d30705a1acd
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(order_amount, shipping_rate, free_shipping_threshold):
    """
    Calculate the shipping cost based on the order amount,
    shipping rate, and free shipping threshold.
    
    Args:
        order_amount (float): The total amount of the order in Rp.
        shipping_rate (float): The shipping rate (cost per Rp unit).
        free_shipping_threshold (float): Minimum order amount for free shipping.
        
    Returns:
        float: Calculated shipping cost (0 if free shipping applies).
    """
    if order_amount < 0:
        raise ValueError("Order amount cannot be negative.")
    if shipping_rate < 0:
        raise ValueError("Shipping rate cannot be negative.")
    
    # Free shipping if order_amount exceeds or equals the threshold
    if order_amount >= free_shipping_threshold:
        return 0.0
    
    # Calculate the shipping cost
    shipping_cost = order_amount * shipping_rate
    return round(shipping_cost, 2)  # Rounded to two decimal places

def main():
    """
    Main function to get user input and calculate shipping cost.
    """
    try:
        # Constants
        FREE_SHIPPING_THRESHOLD = 10000000.0  # Rp. 10,000,000
        SHIPPING_RATE = 0.05  # Example rate: 5% of the order amount
        
        # Get user input
        print("Welcome to the shipping cost calculator for promotional items.")
        order_amount_input = input("Enter the total order amount in Rp: ")
        
        # Validate user input
        try:
            order_amount = float(order_amount_input)
        except ValueError:
            raise ValueError("Invalid input! Please enter a numeric value for the order amount.")
        
        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(order_amount, SHIPPING_RATE, FREE_SHIPPING_THRESHOLD)
        
        # Display results
        if shipping_cost == 0:
            print("Congratulations! You qualify for free shipping.")
        else:
            print(f"The shipping cost for your order is: Rp {shipping_cost}")
    
    # Handle errors
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
