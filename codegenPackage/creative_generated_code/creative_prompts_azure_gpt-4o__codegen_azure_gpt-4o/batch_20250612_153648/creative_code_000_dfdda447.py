"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Write Python code to calculate the cost of bulk orders for 3D-printed PU golf grips, factoring in customization fees, shipping costs, and discounts as described on the Longhui Golf website.
Generated: DETERMINISTIC_dfdda4472e405721
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate the cost of bulk orders for 3D-printed PU golf grips.
Factors considered:
- Base price per grip
- Customization fee per grip
- Shipping cost
- Bulk discounts (tiered pricing)
- Error handling for invalid input
"""

def calculate_bulk_order_cost(quantity, base_price, customization_fee, shipping_cost):
    """
    Calculate the total cost of a bulk order for 3D-printed PU golf grips.

    Parameters:
        quantity (int): Number of grips ordered.
        base_price (float): Base price per grip.
        customization_fee (float): Customization fee per grip.
        shipping_cost (float): Flat shipping cost for the order.

    Returns:
        float: Total cost of the order after applying discounts.
    """
    # Validate input parameters
    if quantity < 1:
        raise ValueError("Quantity must be at least 1.")
    if base_price < 0 or customization_fee < 0 or shipping_cost < 0:
        raise ValueError("Price, customization fee, and shipping cost must be non-negative.")
    
    # Calculate base cost
    total_base_cost = quantity * (base_price + customization_fee)
    
    # Apply bulk discounts based on quantity tiers
    if quantity >= 100:
        discount_rate = 0.20  # 20% discount for 100+ grips
    elif quantity >= 50:
        discount_rate = 0.10  # 10% discount for 50-99 grips
    elif quantity >= 20:
        discount_rate = 0.05  # 5% discount for 20-49 grips
    else:
        discount_rate = 0.0   # No discount for <20 grips
    
    discounted_cost = total_base_cost * (1 - discount_rate)
    
    # Calculate final total cost including shipping
    total_cost = discounted_cost + shipping_cost
    
    return round(total_cost, 2)


def main():
    """
    Main function to accept user input, calculate the bulk order cost, and display the result.
    """
    try:
        # User inputs
        quantity = int(input("Enter the quantity of grips ordered: "))
        base_price = float(input("Enter the base price per grip: "))
        customization_fee = float(input("Enter the customization fee per grip: "))
        shipping_cost = float(input("Enter the flat shipping cost for the order: "))
        
        # Calculate total cost
        total_cost = calculate_bulk_order_cost(quantity, base_price, customization_fee, shipping_cost)
        
        # Display the result
        print(f"The total cost of your order is: ${total_cost}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
