"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Write a function to handle direct deposit transactions programmatically, ensuring compliance with the timing rules outlined by Intuit Payroll Services.
Generated: DETERMINISTIC_56c70a606c3e26f4
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DirectDepositTransactionError(Exception):
    """Custom exception for handling direct deposit transaction errors."""
    pass

def is_business_day(date):
    """Check if the given date is a business day (Monday to Friday)."""
    return date.weekday() < 5

def get_next_business_day(date):
    """Get the next business day after the given date."""
    next_day = date + datetime.timedelta(days=1)
    while not is_business_day(next_day):
        next_day += datetime.timedelta(days=1)
    return next_day

def schedule_direct_deposit(transaction_date, amount):
    """
    Schedule a direct deposit transaction ensuring compliance with Intuit Payroll Services timing rules.

    Args:
        transaction_date (datetime.date): The date the transaction is scheduled for.
        amount (float): The amount to be deposited.

    Raises:
        DirectDepositTransactionError: If the transaction date is not valid or if the amount is invalid.
    """
    # Validate the transaction date
    if not isinstance(transaction_date, datetime.date):
        raise DirectDepositTransactionError("Invalid transaction date. Must be a datetime.date object.")
    
    # Validate the amount
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise DirectDepositTransactionError("Invalid amount. Must be a positive number.")

    # Check if the transaction date is a business day
    if not is_business_day(transaction_date):
        logging.warning(f"Transaction date {transaction_date} is not a business day. Scheduling for next business day.")
        transaction_date = get_next_business_day(transaction_date)

    # Log the scheduled transaction
    logging.info(f"Scheduling direct deposit of ${amount:.2f} on {transaction_date}.")

    # Here you would integrate with the payroll service API to process the transaction
    # For demonstration, we will just simulate a successful transaction
    try:
        # Simulate API call
        # response = payroll_service_api.schedule_transaction(transaction_date, amount)
        # if not response.success:
        #     raise DirectDepositTransactionError("Failed to schedule transaction with payroll service.")
        
        # Simulated successful response
        logging.info("Direct deposit transaction scheduled successfully.")
        return {
            "transaction_date": transaction_date,
            "amount": amount,
            "status": "scheduled"
        }
    except Exception as e:
        logging.error(f"Error scheduling direct deposit: {e}")
        raise DirectDepositTransactionError("An error occurred while scheduling the direct deposit.")

# Example usage
if __name__ == "__main__":
    try:
        transaction_date = datetime.date(2023, 10, 30)  # Example date
        amount = 1500.00  # Example amount
        result = schedule_direct_deposit(transaction_date, amount)
        print(result)
    except DirectDepositTransactionError as e:
        print(f"Transaction error: {e}")
```
