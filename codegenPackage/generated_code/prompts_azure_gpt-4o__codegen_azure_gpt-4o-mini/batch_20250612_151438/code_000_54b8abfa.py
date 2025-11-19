"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write Python code to calculate the total cost of purchasing 10 units of "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017" with a 5% discount applied, and display the cost per installment if paid in 12 interest-free payments.
Generated: DETERMINISTIC_54b8abfa95d3fc16
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Constants for the product details
PRODUCT_NAME = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
UNIT_PRICE = 100.00  # Example unit price in currency
QUANTITY = 10
DISCOUNT_RATE = 0.05  # 5% discount
INSTALLMENTS = 12

def calculate_total_cost(unit_price, quantity, discount_rate):
    """
    Calculate the total cost after applying the discount.

    :param unit_price: Price of a single unit
    :param quantity: Number of units to purchase
    :param discount_rate: Discount rate to apply (as a decimal)
    :return: Total cost after discount
    """
    try:
        # Calculate total cost before discount
        total_cost = unit_price * quantity
        
        # Apply discount
        total_cost_after_discount = total_cost * (1 - discount_rate)
        
        return total_cost_after_discount
    except Exception as e:
        print(f"Error calculating total cost: {e}")
        return None

def calculate_installment_cost(total_cost, installments):
    """
    Calculate the cost per installment.

    :param total_cost: Total cost after discount
    :param installments: Number of installments
    :return: Cost per installment
    """
    try:
        if installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")
        
        # Calculate cost per installment
        installment_cost = total_cost / installments
        
        return installment_cost
    except Exception as e:
        print(f"Error calculating installment cost: {e}")
        return None

def main():
    # Calculate total cost
    total_cost = calculate_total_cost(UNIT_PRICE, QUANTITY, DISCOUNT_RATE)
    
    if total_cost is not None:
        print(f"Total cost after discount for {QUANTITY} units of '{PRODUCT_NAME}': {total_cost:.2f}")
        
        # Calculate installment cost
        installment_cost = calculate_installment_cost(total_cost, INSTALLMENTS)
        
        if installment_cost is not None:
            print(f"Cost per installment for {INSTALLMENTS} interest-free payments: {installment_cost:.2f}")

if __name__ == "__main__":
    main()
```
