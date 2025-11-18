"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tektekdunk.blogspot.com
Prompt: Write a function to handle direct deposit transactions programmatically, ensuring compliance with the timing rules outlined by Intuit Payroll Services.
Generated: DETERMINISTIC_56c70a606c3e26f4
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DirectDepositError(Exception):
    """Custom exception for Direct Deposit processing errors."""
    pass

def is_business_day(date):
    """Check if the given date is a business day (Monday - Friday)."""
    return date.weekday() < 5

def next_business_day(date):
    """Return the next business day after the given date."""
    next_day = date + timedelta(days=1)
    while not is_business_day(next_day):
        next_day += timedelta(days=1)
    return next_day

def schedule_direct_deposit(transaction_date, fund_date):
    """
    Schedule a direct deposit transaction.

    Args:
        transaction_date (datetime): The date the transaction is initiated.
        fund_date (datetime): The date funds are to be deposited.

    Returns:
        datetime: The date when the direct deposit will be processed.

    Raises:
        DirectDepositError: If the transaction date is in the past or not a business day.
    """
    if transaction_date < datetime.now():
        raise DirectDepositError("Transaction date cannot be in the past.")
    
    if not is_business_day(transaction_date):
        raise DirectDepositError("Transaction date must be a business day.")

    # Compliance rules check
    if transaction_date > fund_date:
        raise DirectDepositError("Fund date must be on or after the transaction date.")

    # Determine the processing date based on rules
    processing_date = fund_date
    if not is_business_day(fund_date):
        processing_date = next_business_day(fund_date)

    logging.info(f"Direct deposit scheduled: Transaction Date: {transaction_date}, Fund Date: {fund_date}, Processing Date: {processing_date}")
    
    return processing_date

# Example usage:
if __name__ == "__main__":
    try:
        transaction_date = datetime(2023, 10, 30)  # Example transaction date
        fund_date = datetime(2023, 11, 1)           # Example fund date
        processing_date = schedule_direct_deposit(transaction_date, fund_date)
        print(f"Direct deposit will be processed on: {processing_date.date()}")
    except DirectDepositError as e:
        logging.error(e)
```
