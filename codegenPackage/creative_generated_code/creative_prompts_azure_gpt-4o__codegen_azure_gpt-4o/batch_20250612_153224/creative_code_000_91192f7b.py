"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Write Python code to calculate the cost of ordering custom metallic stickers, including options for Nickel Metal Stickers, 3D Metal Nickel Stickers, and Stainless Steel Metal Stickers, with worldwide shipping fees.
Generated: DETERMINISTIC_91192f7b0f1a7421
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Metallic Sticker Ordering - Cost Calculation Script
# This script calculates the total cost of ordering custom metallic stickers,
# including sticker type, quantity, and worldwide shipping fees.

def calculate_sticker_cost(sticker_type, quantity, shipping_fee):
    """
    Calculate the total cost for metallic stickers, including shipping.
    
    Args:
        sticker_type (str): Type of metallic sticker ('nickel', '3d_nickel', 'stainless_steel').
        quantity (int): Number of stickers to order.
        shipping_fee (float): Worldwide shipping fee.
    
    Returns:
        float: Total cost of the order.
    
    Raises:
        ValueError: If the sticker type is invalid or quantity is non-positive.
    """
    # Sticker type pricing (price per sticker)
    sticker_prices = {
        'nickel': 0.50,         # Nickel Metal Stickers: $0.50 per sticker
        '3d_nickel': 0.75,     # 3D Metal Nickel Stickers: $0.75 per sticker
        'stainless_steel': 1.00 # Stainless Steel Metal Stickers: $1.00 per sticker
    }

    # Validate sticker type
    if sticker_type not in sticker_prices:
        raise ValueError(f"Invalid sticker type: {sticker_type}. Valid types are: {', '.join(sticker_prices.keys())}")
    
    # Validate quantity
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    # Calculate sticker cost
    sticker_cost = sticker_prices[sticker_type] * quantity
    
    # Calculate total cost (sticker cost + shipping fee)
    total_cost = sticker_cost + shipping_fee
    
    return total_cost

def main():
    """
    Main function to handle user inputs and display the cost calculation.
    """
    try:
        # Get user inputs
        print("Welcome to the Metallic Sticker Ordering System!")
        sticker_type = input("Enter the sticker type ('nickel', '3d_nickel', 'stainless_steel'): ").strip().lower()
        quantity = int(input("Enter the quantity of stickers: "))
        shipping_fee = float(input("Enter worldwide shipping fee ($): "))

        # Calculate total cost
        total_cost = calculate_sticker_cost(sticker_type, quantity, shipping_fee)

        # Display the result
        print(f"\nOrder Summary:")
        print(f"Sticker Type: {sticker_type}")
        print(f"Quantity: {quantity}")
        print(f"Shipping Fee: ${shipping_fee:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point to the script
if __name__ == "__main__":
    main()
```
