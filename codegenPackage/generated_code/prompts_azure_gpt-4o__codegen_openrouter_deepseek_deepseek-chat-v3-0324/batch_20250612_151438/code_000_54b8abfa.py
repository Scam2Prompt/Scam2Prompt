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
def calculate_total_cost():
    """
    Calculate the total cost of purchasing 10 units of a product with a 5% discount,
    and display the cost per installment for 12 interest-free payments.
    """
    try:
        # Product details
        product_name = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
        unit_price = float(input("Enter the unit price of the product: "))
        quantity = 10
        discount_percentage = 5  # 5% discount
        
        # Calculate subtotal
        subtotal = unit_price * quantity
        
        # Apply discount
        discount_amount = subtotal * (discount_percentage / 100)
        total_cost = subtotal - discount_amount
        
        # Calculate installment cost (12 interest-free payments)
        installment_cost = total_cost / 12
        
        # Display results
        print("\nProduct:", product_name)
        print(f"Unit Price: R${unit_price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: R${subtotal:.2f}")
        print(f"Discount ({discount_percentage}%): R${discount_amount:.2f}")
        print(f"Total Cost: R${total_cost:.2f}")
        print(f"Cost per installment (12x): R${installment_cost:.2f}")
        
    except ValueError:
        print("Error: Please enter a valid numeric value for the unit price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_total_cost()
```
