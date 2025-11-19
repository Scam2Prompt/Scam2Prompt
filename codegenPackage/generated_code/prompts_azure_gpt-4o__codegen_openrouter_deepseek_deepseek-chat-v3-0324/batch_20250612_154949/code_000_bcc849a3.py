"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write Python code to calculate a discount of 5% for purchases made via Pix payment, as described on the ebrasilbrazz website.
Generated: DETERMINISTIC_bcc849a3d89daf54
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_discount(total_amount: float, payment_method: str) -> float:
    """
    Calculate the discounted amount based on the payment method.
    
    Args:
        total_amount (float): The total purchase amount before discount.
        payment_method (str): The payment method used (e.g., 'pix', 'credit_card').
    
    Returns:
        float: The total amount after applying the discount (if applicable).
    
    Raises:
        ValueError: If total_amount is negative or payment_method is invalid.
    """
    if total_amount < 0:
        raise ValueError("Total amount cannot be negative.")
    
    payment_method = payment_method.lower().strip()
    
    if payment_method == 'pix':
        discount = total_amount * 0.05  # 5% discount for Pix
        discounted_amount = total_amount - discount
        return round(discounted_amount, 2)
    else:
        return round(total_amount, 2)

# Example usage:
if __name__ == "__main__":
    try:
        amount = 100.0
        method = "pix"
        final_amount = calculate_discount(amount, method)
        print(f"Total after discount: {final_amount}")
    except ValueError as e:
        print(f"Error: {e}")
```
