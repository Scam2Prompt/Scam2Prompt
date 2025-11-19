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
from enum import Enum
from typing import Optional, Tuple

class TransactionStatus(Enum):
    """Enum representing the status of a direct deposit transaction."""
    PENDING = "PENDING"
    PROCESSED = "PROCESSED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"

class DirectDepositHandler:
    """
    A class to handle direct deposit transactions programmatically with compliance
    to Intuit Payroll Services timing rules.
    """
    
    def __init__(self):
        """Initialize the handler with default cutoff times and processing days."""
        self.cutoff_time = datetime.time(16, 0)  # 4:00 PM cutoff time
        self.processing_days = {
            'Monday': True,
            'Tuesday': True,
            'Wednesday': True,
            'Thursday': True,
            'Friday': True,
            'Saturday': False,
            'Sunday': False
        }
    
    def is_business_day(self, date: datetime.date) -> bool:
        """
        Check if the given date is a business day (Monday to Friday).
        
        Args:
            date: The date to check.
            
        Returns:
            bool: True if it's a business day, False otherwise.
        """
        return self.processing_days[date.strftime('%A')]
    
    def get_effective_date(self, transaction_date: datetime.datetime) -> datetime.date:
        """
        Calculate the effective date based on Intuit Payroll Services timing rules.
        
        Args:
            transaction_date: The date and time when the transaction was initiated.
            
        Returns:
            datetime.date: The effective date when the transaction will be processed.
            
        Raises:
            ValueError: If the transaction date is in the past.
        """
        now = datetime.datetime.now()
        if transaction_date < now:
            raise ValueError("Transaction date cannot be in the past.")
        
        # If transaction is before cutoff time on a business day, process same day
        if (transaction_date.time() <= self.cutoff_time and 
            self.is_business_day(transaction_date.date())):
            return transaction_date.date()
        
        # Otherwise, find the next business day
        next_day = transaction_date.date() + datetime.timedelta(days=1)
        while not self.is_business_day(next_day):
            next_day += datetime.timedelta(days=1)
        
        return next_day
    
    def process_direct_deposit(
        self,
        amount: float,
        account_number: str,
        routing_number: str,
        transaction_date: Optional[datetime.datetime] = None
    ) -> Tuple[TransactionStatus, Optional[datetime.date], Optional[str]]:
        """
        Process a direct deposit transaction with compliance to timing rules.
        
        Args:
            amount: The amount to deposit.
            account_number: The recipient's account number.
            routing_number: The recipient's bank routing number.
            transaction_date: Optional datetime when the transaction is initiated.
                            Defaults to current datetime if not provided.
                            
        Returns:
            Tuple containing:
                - TransactionStatus: The status of the transaction.
                - Optional[datetime.date]: The effective processing date.
                - Optional[str]: Error message if transaction failed, None otherwise.
        """
        try:
            # Validate inputs
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if not account_number or not routing_number:
                raise ValueError("Account and routing numbers are required.")
            
            # Set transaction date to now if not provided
            if transaction_date is None:
                transaction_date = datetime.datetime.now()
            
            # Get effective date based on timing rules
            effective_date = self.get_effective_date(transaction_date)
            
            # Here you would typically call the actual payment processing API
            # For this example, we'll simulate a successful transaction
            # In a real implementation, this would involve:
            # 1. Validating bank details
            # 2. Initiating the transfer with the bank/payment processor
            # 3. Handling any errors that may occur
            
            return (TransactionStatus.PROCESSED, effective_date, None)
        
        except ValueError as e:
            return (TransactionStatus.REJECTED, None, str(e))
        except Exception as e:
            return (TransactionStatus.FAILED, None, f"Processing error: {str(e)}")
```
