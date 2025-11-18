"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Suggest a method to integrate a "Check Mess" feature for verifying transaction legality and communicating with an admin, as seen on admgdv.com.
Generated: DETERMINISTIC_f6a7f613b50dc8de
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Optional, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionChecker:
    def __init__(self, admin_contact: str):
        """
        Initializes the TransactionChecker with the admin contact information.
        
        :param admin_contact: Email or contact method to notify admin.
        """
        self.admin_contact = admin_contact

    def check_transaction(self, transaction_data: Dict[str, Any]) -> bool:
        """
        Verifies the legality of a transaction.
        
        :param transaction_data: A dictionary containing transaction information.
        :return: True if the transaction is legal, otherwise False.
        """
        try:
            # Implement legality checks (e.g., transaction amount, user validity)
            is_legal = self._is_transaction_legal(transaction_data)

            if not is_legal:
                self.notify_admin(transaction_data)
            
            return is_legal
        except Exception as e:
            logging.error(f"Error checking transaction: {e}")
            return False

    def _is_transaction_legal(self, transaction_data: Dict[str, Any]) -> bool:
        """
        Checks the legality of the transaction based on custom rules.
        
        :param transaction_data: A dictionary containing transaction information.
        :return: True if the transaction is deemed legal, otherwise False.
        """
        # Example legality check: ensure amount is a positive number
        if transaction_data.get('amount', 0) <= 0:
            logging.warning("Transaction amount is invalid.")
            return False
        
        # Add additional checks as necessary
        logging.info("Transaction is considered legal.")
        return True

    def notify_admin(self, transaction_data: Dict[str, Any]):
        """
        Sends a notification to the admin regarding the illegal transaction.
        
        :param transaction_data: A dictionary containing transaction information.
        """
        message = f"Illegal transaction detected: {transaction_data}"
        # Here you can implement the actual notification logic (e.g., sending an email)
        logging.info(f"Notifying admin at {self.admin_contact}: {message}")
        # Example: send_email(self.admin_contact, "Transaction Alert", message)

# Example usage
if __name__ == "__main__":
    admin_email = "admin@example.com"  # Replace with actual admin contact
    transaction_checker = TransactionChecker(admin_contact=admin_email)

    # Example transaction data
    sample_transaction = {
        "transaction_id": "12345",
        "amount": -100,  # Intentional invalid amount for testing
        "user_id": "user_678"
    }

    # Check the transaction legality
    is_valid = transaction_checker.check_transaction(sample_transaction)

    if is_valid:
        logging.info("Transaction is valid.")
    else:
        logging.info("Transaction is invalid.")
```
