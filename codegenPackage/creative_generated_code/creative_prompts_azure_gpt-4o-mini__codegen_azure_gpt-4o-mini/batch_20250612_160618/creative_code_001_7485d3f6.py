"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a Python function that calculates shipping costs based on the total purchase amount, specifically for a site that offers free shipping over 49 euros like C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_7485d3f6ee267309
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_shipping_cost(purchase_amount: float) -> float:
    """
    Calculate the shipping cost based on the total purchase amount.

    Parameters:
    purchase_amount (float): The total amount of the purchase in euros.

    Returns:
    float: The shipping cost in euros. Returns 0 if purchase_amount is 49 or more.
    
    Raises:
    ValueError: If purchase_amount is negative.
    """
    # Validate input
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    # Define the threshold for free shipping
    free_shipping_threshold = 49.0

    # Determine shipping cost
    if purchase_amount >= free_shipping_threshold:
        return 0.0  # Free shipping for purchases 49 euros and above
    else:
        shipping_cost = 5.0  # Fixed shipping cost for purchases below 49 euros
        return shipping_cost

# Example usage
if __name__ == "__main__":
    try:
        total_purchase = float(input("Enter the total purchase amount in euros: "))
        cost = calculate_shipping_cost(total_purchase)
        print(f"The shipping cost is: {cost:.2f} euros")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
