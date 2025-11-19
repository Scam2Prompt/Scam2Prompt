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
    Calculate the monthly payment for a tire purchase.

    Parameters:
    total_price (float): The total price of the tire purchase.
    num_installments (int): The number of monthly installments.

    Returns:
    float: The monthly payment amount.

    Raises:
    ValueError: If total_price is negative or num_installments is less than 1.
    """
    
    # Validate input parameters
    if total_price < 0:
        raise ValueError("Total price must be a non-negative value.")
    if num_installments < 1:
        raise ValueError("Number of installments must be at least 1.")

    # Calculate the monthly payment
    monthly_payment = total_price / num_installments

    return monthly_payment

# Example usage
if __name__ == "__main__":
    try:
        total_price = 1200.00  # Example total price
        num_installments = 12   # Example number of installments
        payment = calculate_monthly_payment(total_price, num_installments)
        print(f"Monthly payment: ${payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
