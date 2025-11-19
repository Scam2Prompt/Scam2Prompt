"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Provide code to calculate the monthly installment amount for purchasing "04 X Junção Branca Sanfonada P/ Luminaria Circular (redonda)" with a 5% discount and 12 interest-free payments.
Generated: DETERMINISTIC_39f961a7245abaac
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_installment(item_name, price, discount_percentage, installments):
    """
    Calculate the monthly installment amount for a purchase with discount and interest-free installments.
    
    Args:
        item_name (str): Name of the item being purchased
        price (float): Original price of the item
        discount_percentage (float): Discount percentage (0-100)
        installments (int): Number of interest-free installments
        
    Returns:
        dict: Dictionary containing original price, discounted price, and installment amount
    """
    try:
        # Validate inputs
        if not isinstance(item_name, str):
            raise ValueError("Item name must be a string")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        if installments <= 0:
            raise ValueError("Number of installments must be greater than 0")
        
        # Calculate discounted price
        discount_amount = price * (discount_percentage / 100)
        discounted_price = price - discount_amount
        
        # Calculate installment amount
        installment_amount = discounted_price / installments
        
        return {
            "item_name": item_name,
            "original_price": price,
            "discount_percentage": discount_percentage,
            "discounted_price": round(discounted_price, 2),
            "installments": installments,
            "installment_amount": round(installment_amount, 2)
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to calculate installment"
        }

# Example usage
if __name__ == "__main__":
    item_name = "04 X Junção Branca Sanfonada P/ Luminaria Circular (redonda)"
    price = 100.00  # Assuming a base price of 100 for example
    discount_percentage = 5
    installments = 12
    
    result = calculate_monthly_installment(item_name, price, discount_percentage, installments)
    print(result)
```
