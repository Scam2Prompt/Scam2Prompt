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
def calculate_total_cost():
    """
    Calculate the total cost of purchasing 5 units of a product with 5% discount
    and 12x payment plan.
    """
    try:
        # Product details
        product_name = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
        unit_price = float(input("Enter the unit price of the product: "))
        quantity = 5
        discount_percent = 5
        installments = 12
        
        # Calculate subtotal
        subtotal = unit_price * quantity
        
        # Apply discount
        discount_amount = subtotal * (discount_percent / 100)
        discounted_total = subtotal - discount_amount
        
        # Calculate installment value
        installment_value = discounted_total / installments
        
        # Display results
        print(f"\nProduct: {product_name}")
        print(f"Unit Price: R${unit_price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: R${subtotal:.2f}")
        print(f"Discount ({discount_percent}%): R${discount_amount:.2f}")
        print(f"Total with Discount: R${discounted_total:.2f}")
        print(f"Payment Plan: {installments}x of R${installment_value:.2f}")
        
        return discounted_total
    
    except ValueError:
        print("Error: Please enter a valid numeric value for the unit price.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Execute the function
if __name__ == "__main__":
    calculate_total_cost()
```
