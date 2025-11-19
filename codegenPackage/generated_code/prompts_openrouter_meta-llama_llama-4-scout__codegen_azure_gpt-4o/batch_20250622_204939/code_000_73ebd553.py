"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a Python code snippet to calculate the total cost of purchasing 5 units of the `Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017` product with 5% discount and 12x payment plan.
Generated: DETERMINISTIC_73ebd55386b232a0
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the total cost of purchasing 5 units of a product
# with a 5% discount and a 12x payment plan.

def calculate_total_cost(unit_price, quantity, discount_rate, payment_plan):
    """
    Calculate the total cost of purchasing a product with a discount and payment plan.

    Args:
        unit_price (float): Price of a single unit of the product.
        quantity (int): Number of units to purchase.
        discount_rate (float): Discount rate as a percentage (e.g., 5 for 5%).
        payment_plan (int): Number of installments for payment.

    Returns:
        dict: A dictionary containing the total cost after discount and installment details.
    """
    try:
        # Calculate the total price before discount
        total_price = unit_price * quantity

        # Apply the discount
        discount_amount = total_price * (discount_rate / 100)
        total_price_after_discount = total_price - discount_amount

        # Calculate installment amount
        installment_amount = total_price_after_discount / payment_plan

        # Return the results
        return {
            "total_price_after_discount": round(total_price_after_discount, 2),
            "installment_amount": round(installment_amount, 2),
            "payment_plan": payment_plan
        }
    except Exception as e:
        # Handle any unexpected errors
        return {"error": str(e)}


# Product details
unit_price = 59.99  # Price of a single unit of the product
quantity = 5        # Number of units to purchase
discount_rate = 5   # Discount rate in percentage
payment_plan = 12   # Number of installments

# Calculate the total cost
result = calculate_total_cost(unit_price, quantity, discount_rate, payment_plan)

# Display the results
if "error" in result:
    print(f"An error occurred: {result['error']}")
else:
    print(f"Total price after discount: ${result['total_price_after_discount']}")
    print(f"Installment amount (12x): ${result['installment_amount']} per month")
```
