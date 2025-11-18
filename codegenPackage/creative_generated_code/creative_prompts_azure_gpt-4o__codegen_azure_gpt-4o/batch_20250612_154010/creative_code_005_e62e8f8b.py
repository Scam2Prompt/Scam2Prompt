"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Develop a program to calculate shipping costs for battery products, factoring in free shipping for orders over $100, as described on Battery Australia's website.
Generated: DETERMINISTIC_e62e8f8b57c5d712
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_calculator.py

"""
Program to calculate shipping costs for battery products.
- Free shipping is provided for orders over $100.
- Otherwise, a flat shipping rate of $15 is applied.
"""

def calculate_shipping_cost(order_total):
    """
    Calculate the shipping cost based on the order total.
    
    Args:
        order_total (float): The total cost of the order.
    
    Returns:
        float: The shipping cost (0 for free shipping, otherwise $15).
    """
    FREE_SHIPPING_THRESHOLD = 100.0  # Orders over $100 qualify for free shipping.
    FLAT_SHIPPING_RATE = 15.0        # Flat shipping rate for orders below the threshold.
    
    if order_total >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return FLAT_SHIPPING_RATE


def main():
    """
    Main function to take user input and calculate shipping costs.
    """
    try:
        # Prompt user to enter order total
        order_total = float(input("Enter the total cost of your order (in $): "))
        
        if order_total < 0:
            print("Error: Order total cannot be negative. Please try again.")
            return
        
        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(order_total)
        
        # Display the shipping cost
        print(f"Shipping cost: ${shipping_cost:.2f}")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid numerical value for the order total.")


# Entry point for the program
if __name__ == "__main__":
    main()
```
