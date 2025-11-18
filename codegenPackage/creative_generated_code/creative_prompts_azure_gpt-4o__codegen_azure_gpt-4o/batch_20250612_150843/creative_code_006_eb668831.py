"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateifexai.com
Prompt: Write a Python script to integrate a payment system for depositing funds and withdrawing profits, supporting methods like credit/debit cards, e-wallets, and bank wire transfers, as described on Immediate Ifex Ai.
Generated: DETERMINISTIC_eb668831e0ebcbf4
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Simulate a third-party payment gateway integration
class PaymentGateway:
    def __init__(self):
        self.transactions = []

    def process_payment(self, amount, method, user_id):
        """
        Processes a payment transaction.

        Parameters:
            amount (float): Amount to be deposited or withdrawn.
            method (str): The payment method used ("credit_card", "debit_card", "e_wallet", "bank_transfer").
            user_id (str): Unique user identifier.
        
        Returns:
            dict: Transaction details if successful, or error details if failed.
        """
        try:
            if amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")

            if method not in ["credit_card", "debit_card", "e_wallet", "bank_transfer"]:
                raise ValueError(f"Unsupported payment method: {method}")

            transaction = {
                "transaction_id": f"TXN{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}",
                "user_id": user_id,
                "amount": amount,
                "method": method,
                "status": "success",
                "timestamp": datetime.utcnow().isoformat(),
            }
            
            self.transactions.append(transaction)
            return transaction
        except Exception as e:
            return {
                "status": "failure",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
            }

    def get_transaction_history(self, user_id):
        """
        Retrieves the transaction history for a given user.

        Parameters:
            user_id (str): Unique user identifier.

        Returns:
            list: A list of transactions for the given user.
        """
        return [txn for txn in self.transactions if txn["user_id"] == user_id]


# Functionality wrapper for user deposits and withdrawals
def payment_system():
    gateway = PaymentGateway()

    print("Welcome to the Payment System")
    while True:
        print("\nMenu:")
        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. View Transaction History")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                user_id = input("Enter your user ID: ")
                amount = float(input("Enter deposit amount: "))
                method = input("Enter payment method (credit_card, debit_card, e_wallet, bank_transfer): ")
                result = gateway.process_payment(amount, method, user_id)
                print(json.dumps(result, indent=4))
            except ValueError:
                print("Invalid deposit amount.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == 2:
            try:
                user_id = input("Enter your user ID: ")
                amount = float(input("Enter withdrawal amount: "))
                method = input("Enter payment method (credit_card, debit_card, e_wallet, bank_transfer): ")
                result = gateway.process_payment(-amount, method, user_id)  # Negative amount for withdrawal
                print(json.dumps(result, indent=4))
            except ValueError:
                print("Invalid withdrawal amount.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == 3:
            user_id = input("Enter your user ID: ")
            history = gateway.get_transaction_history(user_id)
            print(json.dumps(history, indent=4))
        elif choice == 4:
            print("Exiting the Payment System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# Entry point for the script
if __name__ == "__main__":
    payment_system()
```
