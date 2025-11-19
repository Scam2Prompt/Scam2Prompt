"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tektekdunk.blogspot.com
Prompt: Create a function to handle ACH transaction cancellations and notify users based on Intuit's guidelines.
Generated: DETERMINISTIC_3f4aaf4d0a2cf5a8
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cancel_ach_transaction(transaction_id, user_email):
    """
    Cancels an ACH transaction and notifies the user.

    Args:
        transaction_id (str): The unique identifier of the ACH transaction.
        user_email (str): The email address of the user to notify.

    Returns:
        dict: A dictionary containing the cancellation status and message.
    """
    try:
        # Input validation
        if not isinstance(transaction_id, str) or not isinstance(user_email, str):
            raise ValueError("Invalid input: 'transaction_id' and 'user_email' must be strings")

        # Simulate transaction lookup and cancellation
        transaction = get_transaction_by_id(transaction_id)  # Fetch transaction details
        if not transaction:
            raise ValueError(f"No transaction found with ID: {transaction_id}")

        if transaction['status'] == 'Cancelled':
            return {
                "status": "Error",
                "message": "Transaction is already cancelled"
            }

        # Simulate cancellation logic
        transaction['status'] = 'Cancelled'
        save_transaction(transaction)  # Persist the cancellation

        # Notify user
        notification_status = send_notification(user_email, f"Transaction {transaction_id} has been cancelled.")
        if not notification_status:
            raise RuntimeError("Failed to send notification to the user")

        logging.info(f"Transaction {transaction_id} successfully cancelled and user notified.")

        return {
            "status": "Success",
            "message": f"Transaction {transaction_id} successfully cancelled"
        }

    except ValueError as ve:
        logging.error(f"ValueError occurred: {str(ve)}")
        return {
            "status": "Error",
            "message": str(ve)
        }

    except RuntimeError as re:
        logging.error(f"RuntimeError occurred: {str(re)}")
        return {
            "status": "Error",
            "message": str(re)
        }

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return {
            "status": "Error",
            "message": "An unexpected error occurred. Please try again later."
        }

# Helper functions (mock implementations)
def get_transaction_by_id(transaction_id):
    """
    Mock function to fetch a transaction by its ID.
    """
    # Example transaction data
    mock_transactions = {
        "txn001": {"status": "Pending"},
        "txn002": {"status": "Completed"},
        "txn003": {"status": "Cancelled"},
    }
    return mock_transactions.get(transaction_id)

def save_transaction(transaction):
    """
    Mock function to save transaction details.
    """
    # In a real-world application, this would involve saving the updated transaction to a database.
    logging.info(f"Transaction saved: {transaction}")

def send_notification(email, message):
    """
    Mock function to send a notification to a user.
    """
    # Simulate notification success
    logging.info(f"Notification sent to {email}: {message}")
    return True
```
