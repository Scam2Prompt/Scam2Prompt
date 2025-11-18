"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write Python code to calculate the total cost of purchasing 10 units of "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017" with a 5% discount applied, and display the cost per installment if paid in 12 interest-free payments.
Generated: DETERMINISTIC_54b8abfa95d3fc16
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Constants for the product details
PRODUCT_NAME = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
UNIT_PRICE = 0  # Set the unit price value here (in your currency)
QUANTITY = 10
DISCOUNT_RATE = 0.05  # 5% discount
INSTALLMENTS = 12

def calculate_total_cost(unit_price, quantity, discount_rate):
    """
    Calculate the total cost after applying a discount.

    Args:
        unit_price (float): The price of a single unit of the product.
        quantity (int): The number of units to purchase.
        discount_rate (float): The discount rate to apply (as a decimal).

    Returns:
        float: The total cost after discount.
    """
    try:
        # Validate inputs
        if unit_price < 0 or quantity < 0 or not (0 <= discount_rate < 1):
            raise ValueError("Invalid input: unit_price and quantity must be non-negative; discount_rate must be between 0 and 1.")

        # Calculate total cost before discount
        total_cost = unit_price * quantity
        
        # Apply the discount
        total_cost_after_discount = total_cost * (1 - discount_rate)
        
        return total_cost_after_discount
    except Exception as e:
        print(f"An error occurred while calculating total cost: {e}")
        return None

def calculate_installment_cost(total_cost, installments):
    """
    Calculate the cost per installment.

    Args:
        total_cost (float): The total cost to be paid.
        installments (int): The number of installments to divide the payment into.

    Returns:
        float: The cost per installment.
    """
    try:
        # Validate inputs
        if installments <= 0:
            raise ValueError("Invalid input: installments must be a positive integer.")
        
        # Calculate the cost per installment
        installment_cost = total_cost / installments
        
        return installment_cost
    except Exception as e:
        print(f"An error occurred while calculating installment cost: {e}")
        return None

def main():
    # Step 1: Calculate the total cost after discount
    total_cost = calculate_total_cost(UNIT_PRICE, QUANTITY, DISCOUNT_RATE)
    
    if total_cost is not None:
        # Step 2: Calculate the cost per installment
        installment_cost = calculate_installment_cost(total_cost, INSTALLMENTS)
        
        if installment_cost is not None:
            # Step 3: Display the results
            print(f"Total cost for {QUANTITY} units of '{PRODUCT_NAME}' after a {DISCOUNT_RATE * 100}% discount: {total_cost:.2f}")
            print(f"Cost per installment for {INSTALLMENTS} interest-free payments: {installment_cost:.2f}")

if __name__ == "__main__":
    main()
```

Make sure to set the `UNIT_PRICE` variable to the correct price of the product before running the code.
