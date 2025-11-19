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

def calculate_refund_eligibility(purchase_date, current_date, refund_window_days=30):
    """
    Determines if a purchase is eligible for a refund based on the Nobody Mint timeline.

    Args:
        purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
        current_date (str): The current date in 'YYYY-MM-DD' format.
        refund_window_days (int): Number of days in the refund window (default is 30 days).

    Returns:
        bool: True if the purchase is eligible for a refund, False otherwise.
    """
    try:
        # Parse the input dates
        purchase_date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
        current_date_obj = datetime.strptime(current_date, '%Y-%m-%d')

        # Calculate the end date of the refund window
        refund_deadline = purchase_date_obj + timedelta(days=refund_window_days)

        # Determine eligibility
        return current_date_obj <= refund_deadline
    except ValueError as e:
        # Handle invalid date format errors
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

# Example usage:
# print(calculate_refund_eligibility("2023-09-01", "2023-09-15"))  # Should return True
# print(calculate_refund_eligibility("2023-09-01", "2023-10-02"))  # Should return False
```
