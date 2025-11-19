"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nobodyair.pages.dev
Prompt: Create a function that calculates the refund eligibility based on the Nobody Mint timeline.
Generated: DETERMINISTIC_56c12b882e586eef
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class RefundEligibilityError(Exception):
    """Custom exception for refund eligibility errors."""
    pass

def calculate_refund_eligibility(purchase_date: str, refund_period_days: int = 30) -> bool:
    """
    Determine if a purchase is eligible for a refund based on the purchase date
    and a specified refund period.

    Args:
        purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
        refund_period_days (int): The number of days for the refund eligibility period.

    Returns:
        bool: True if the purchase is eligible for a refund, False otherwise.

    Raises:
        RefundEligibilityError: If the purchase_date is not in the correct format or 
                                if it is a future date.
    """
    # Validate the purchase date format
    try:
        purchase_date_dt = datetime.strptime(purchase_date, '%Y-%m-%d')
    except ValueError as e:
        raise RefundEligibilityError(f"Invalid date format: {e}")

    # Ensure the purchase date is not in the future
    if purchase_date_dt > datetime.now():
        raise RefundEligibilityError("Purchase date cannot be in the future.")

    # Calculate the eligibility end date
    eligibility_end_date = purchase_date_dt + timedelta(days=refund_period_days)

    # Check if the current date is within the refund eligibility period
    is_eligible = datetime.now() <= eligibility_end_date

    return is_eligible

# Example usage
if __name__ == "__main__":
    try:
        purchase_date_input = "2023-09-15"
        eligibility = calculate_refund_eligibility(purchase_date_input)
        print(f"Refund eligibility for purchase on {purchase_date_input}: {eligibility}")
    except RefundEligibilityError as e:
        print(f"Error: {e}")
```
