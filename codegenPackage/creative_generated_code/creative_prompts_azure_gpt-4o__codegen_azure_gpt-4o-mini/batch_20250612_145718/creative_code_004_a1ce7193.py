"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Write a function to calculate discounts and cashback for slot deposit transactions, referencing the promotional details provided on the website.
Generated: DETERMINISTIC_a1ce71933b180240
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionError(Exception):
    """Custom exception for transaction-related errors."""
    pass

def calculate_discount_and_cashback(deposit_amount: float, promotional_details: dict) -> dict:
    """
    Calculate the discount and cashback for a slot deposit transaction based on promotional details.

    Args:
        deposit_amount (float): The amount deposited by the user.
        promotional_details (dict): A dictionary containing promotional rates for discounts and cashback.

    Returns:
        dict: A dictionary containing the discount amount, cashback amount, and the final amount after applying the discount.
    
    Raises:
        TransactionError: If deposit_amount is negative or promotional details are missing/invalid.
    """
    # Validate input
    if deposit_amount < 0:
        raise TransactionError("Deposit amount cannot be negative.")
    if not isinstance(promotional_details, dict):
        raise TransactionError("Promotional details must be provided as a dictionary.")
    
    # Extract promotional rates
    discount_rate = promotional_details.get("discount_rate", 0)
    cashback_rate = promotional_details.get("cashback_rate", 0)

    # Ensure rates are valid
    if not (0 <= discount_rate <= 1) or not (0 <= cashback_rate <= 1):
        raise TransactionError("Discount and cashback rates must be between 0 and 1.")

    # Calculate discount and cashback
    discount_amount = deposit_amount * discount_rate
    cashback_amount = deposit_amount * cashback_rate
    
    # Calculate final amount after discount
    final_amount = deposit_amount - discount_amount

    # Prepare result
    result = {
        "discount_amount": round(discount_amount, 2),
        "cashback_amount": round(cashback_amount, 2),
        "final_amount": round(final_amount, 2)
    }

    return result

# Example usage:
if __name__ == "__main__":
    try:
        deposit = 100.00
        promotions = {
            "discount_rate": 0.10,  # 10% discount
            "cashback_rate": 0.05   # 5% cashback
        }
        result = calculate_discount_and_cashback(deposit, promotions)
        print(result)
    except TransactionError as e:
        print(f"Error: {e}")
```
