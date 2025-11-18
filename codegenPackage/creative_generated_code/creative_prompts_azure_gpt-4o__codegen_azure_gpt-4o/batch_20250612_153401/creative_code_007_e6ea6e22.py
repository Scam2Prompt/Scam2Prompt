"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundfa.com
Prompt: Create a function to simulate the account purchasing process and trading exam participation for SDF Prop Firm, referencing the steps outlined on Fundfa.
Generated: DETERMINISTIC_e6ea6e221fdafdca
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Initialize logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def purchase_account(account_type, payment_method):
    """
    Simulates purchasing an account from SDF Prop Firm.

    Args:
        account_type (str): The type of account to purchase (e.g., "Starter", "Pro").
        payment_method (str): The payment method for the purchase (e.g., "Credit Card", "PayPal").
    
    Returns:
        dict: A dictionary containing purchase status and account details.
    """
    try:
        # Validate input
        if account_type not in ["Starter", "Pro"]:
            raise ValueError("Invalid account type. Choose 'Starter' or 'Pro'.")
        
        if payment_method not in ["Credit Card", "PayPal", "Crypto"]:
            raise ValueError("Invalid payment method. Choose 'Credit Card', 'PayPal', or 'Crypto'.")

        # Simulate purchase process
        logging.info(f"Processing purchase for {account_type} account using {payment_method}...")
        account_details = {
            "account_type": account_type,
            "payment_method": payment_method,
            "purchase_status": "Success",
            "account_id": "SDF-" + str(hash(account_type + payment_method))[:8]
        }

        logging.info("Account purchase successful.")
        return account_details

    except Exception as e:
        logging.error(f"An error occurred during account purchase: {e}")
        return {"error": str(e)}


def participate_in_trading_exam(account_id):
    """
    Simulates participation in the trading exam at SDF Prop Firm.

    Args:
        account_id (str): Unique identifier for the purchased account.
    
    Returns:
        dict: A dictionary containing the exam participation status and results.
    """
    try:
        # Validate input
        if not account_id:
            raise ValueError("Account ID is required to participate in the trading exam.")
        
        # Simulate exam participation
        logging.info(f"Starting trading exam for account ID {account_id}...")
        exam_results = {
            "account_id": account_id,
            "exam_status": "Completed",
            "exam_score": 85,  # Example fixed score
            "passed": True if 85 >= 80 else False  # Assuming passing score is ≥ 80
        }

        logging.info(f"Trading exam completed. Results: {exam_results}")
        return exam_results

    except Exception as e:
        logging.error(f"An error occurred during the trading exam: {e}")
        return {"error": str(e)}


# Example usage:
if __name__ == "__main__":
    # Purchase an account
    account = purchase_account("Pro", "Credit Card")
    if "error" not in account:
        # Participate in trading exam
        exam_results = participate_in_trading_exam(account["account_id"])
        print(f"Exam Results: {exam_results}")
```
