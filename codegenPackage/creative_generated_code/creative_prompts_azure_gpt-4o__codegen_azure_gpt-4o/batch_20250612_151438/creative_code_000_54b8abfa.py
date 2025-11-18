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
# Python code to calculate total cost and installment payment for a product purchase

# Define the product details
product_name = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
unit_price = 120.00  # Price of a single unit in currency (e.g., USD)

# Define purchase details
quantity = 10  # Number of units to purchase
discount_rate = 0.05  # Discount rate (5%)
installments = 12  # Number of interest-free installments

# Function to calculate the total cost
def calculate_total_cost(unit_price, quantity, discount_rate):
    """
    Calculate the total cost of purchasing items after applying a discount.

    :param unit_price: Price of a single unit
    :param quantity: Number of units to purchase
    :param discount_rate: Discount rate as a decimal (e.g., 0.05 for 5%)
    :return: Total cost after discount
    """
    try:
        # Calculate the total cost before discount
        total_cost_before_discount = unit_price * quantity
        
        # Apply the discount
        discount = total_cost_before_discount * discount_rate
        total_cost_after_discount = total_cost_before_discount - discount
        
        return total_cost_after_discount
    except Exception as e:
        print(f"An error occurred while calculating total cost: {e}")
        raise

# Function to calculate installment payment
def calculate_installment(total_cost, installments):
    """
    Calculate the cost per installment for interest-free payments.

    :param total_cost: Total cost after discount
    :param installments: Number of installments
    :return: Cost per installment
    """
    try:
        # Calculate cost per installment
        installment_payment = total_cost / installments
        return installment_payment
    except ZeroDivisionError:
        print("Error: Number of installments cannot be zero.")
        raise
    except Exception as e:
        print(f"An error occurred while calculating installment payment: {e}")
        raise

# Main execution
if __name__ == "__main__":
    try:
        # Calculate total cost
        total_cost = calculate_total_cost(unit_price, quantity, discount_rate)
        
        # Calculate installment payment
        installment_payment = calculate_installment(total_cost, installments)
        
        # Display results
        print(f"Product: {product_name}")
        print(f"Unit Price: ${unit_price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Discount Rate: {discount_rate * 100:.0f}%")
        print(f"Total Cost (after discount): ${total_cost:.2f}")
        print(f"Cost Per Installment (12 interest-free payments): ${installment_payment:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
