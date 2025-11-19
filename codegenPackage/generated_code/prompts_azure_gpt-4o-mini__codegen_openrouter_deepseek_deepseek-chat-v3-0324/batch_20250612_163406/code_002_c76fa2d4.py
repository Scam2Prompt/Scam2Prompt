"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Write a function that calculates the monthly payment for a tire purchase based on the total price and number of installments, inspired by the pricing model on Itamarati Online.
Generated: DETERMINISTIC_c76fa2d44aa5b8e9
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_payment(total_price: float, num_installments: int) -> float:
    """
    Calculate the monthly payment for a tire purchase based on total price and number of installments.
    
    Args:
        total_price (float): The total price of the tires (must be positive).
        num_installments (int): The number of installments (must be between 1 and 12).
    
    Returns:
        float: The monthly payment amount.
    
    Raises:
        ValueError: If total_price is not positive or num_installments is not between 1 and 12.
    """
    if total_price <= 0:
        raise ValueError("Total price must be a positive number.")
    if num_installments < 1 or num_installments > 12:
        raise ValueError("Number of installments must be between 1 and 12.")
    
    # Calculate monthly payment (rounded to 2 decimal places for currency)
    monthly_payment = round(total_price / num_installments, 2)
    return monthly_payment
```
