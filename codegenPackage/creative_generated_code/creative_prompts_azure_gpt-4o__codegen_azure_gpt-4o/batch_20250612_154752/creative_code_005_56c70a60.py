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
import datetime
from typing import List

class DirectDepositTransactionError(Exception):
    """Custom exception for direct deposit transaction errors."""
    pass

def process_direct_deposit(account_number: str, routing_number: str, amount: float, transaction_date: datetime.date) -> str:
    """
    Processes a direct deposit transaction, ensuring compliance with timing rules.
    
    Parameters:
    - account_number (str): The bank account number.
    - routing_number (str): The bank routing number.
    - amount (float): The amount to deposit.
    - transaction_date (datetime.date): The date the transaction is to be processed.
    
    Returns:
    - str: Confirmation message of the transaction.
    
    Raises:
    - DirectDepositTransactionError: If the transaction fails validation rules.
    """
    # Validate inputs
    if not account_number or not routing_number or amount <= 0:
        raise DirectDepositTransactionError("Invalid account details or deposit amount.")
    
    # Ensure transaction date is at least 2 business days from today
    today = datetime.date.today()
    if transaction_date < today + datetime.timedelta(days=2):
        raise DirectDepositTransactionError("Transaction date must be at least 2 business days from today.")
    
    # Ensure transaction date is not a weekend
    if transaction_date.weekday() > 4:  # 5 = Saturday, 6 = Sunday
        raise DirectDepositTransactionError("Transaction date cannot be on a weekend.")
    
    # Simulate transaction processing (this would typically involve integration with a payment API)
    try:
        # Placeholder for bank integration logic
        confirmation_id = f"DD-{account_number[-4:]}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Log transaction details (in production, replace with secure logging mechanisms)
        print(f"Processing deposit: Account: {account_number}, Routing: {routing_number}, Amount: {amount}, Date: {transaction_date}")
        print(f"Transaction successful. Confirmation ID: {confirmation_id}")
        
        return f"Transaction successful. Confirmation ID: {confirmation_id}"
    
    except Exception as e:
        # Catch unforeseen errors and re-raise as a custom exception
        raise DirectDepositTransactionError(f"Failed to process transaction: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        confirmation_message = process_direct_deposit(
            account_number="123456789",
            routing_number="987654321",
            amount=1500.00,
            transaction_date=datetime.date.today() + datetime.timedelta(days=3)  # Example transaction date
        )
        print(confirmation_message)
    except DirectDepositTransactionError as e:
        print(f"Error: {e}")
```
