"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.cvnai.org
Prompt: Generate code to implement user-friendly features for a cryptocurrency trading app, such as one-click deposit and withdrawal, inspired by 欧易交易所 functionality.
Generated: DETERMINISTIC_0a0a700dee285de1
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crypto_trading_app.py

import logging
import decimal

# Configure logging to log errors and info to a file
logging.basicConfig(filename='crypto_trading_app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptocurrencyTradingApp:
    """
    A class representing a cryptocurrency trading app with user-friendly deposit and withdrawal features.
    """

    def __init__(self):
        """
        Initialize the app with a user wallet containing default balance.
        """
        self.wallet = {'USD': decimal.Decimal('1000.00'), 'BTC': decimal.Decimal('0.05')}
        logging.info("Initialized cryptocurrency trading app with default wallet balances.")

    def view_wallet(self):
        """
        Display the current wallet balances to the user.
        """
        print("Your Wallet Balances:")
        for currency, balance in self.wallet.items():
            print(f"{currency}: {balance}")
        logging.info("Displayed wallet balances.")

    def deposit_funds(self, currency, amount):
        """
        Deposit funds into the user's wallet.
        
        Args:
            currency (str): The currency to deposit, e.g., 'USD' or 'BTC'.
            amount (Decimal): The amount to deposit.
        
        Raises:
            ValueError: If the amount is negative or invalid currency is provided.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if currency not in self.wallet:
                raise ValueError("Invalid currency.")

            self.wallet[currency] += decimal.Decimal(amount)
            print(f"Successfully deposited {amount} {currency}.")
            logging.info(f"Deposited {amount} {currency} into wallet.")
        except Exception as e:
            logging.error(f"Error during deposit: {e}")
            print(f"Error: {e}")

    def withdraw_funds(self, currency, amount):
        """
        Withdraw funds from the user's wallet.
        
        Args:
            currency (str): The currency to withdraw, e.g., 'USD' or 'BTC'.
            amount (Decimal): The amount to withdraw.
        
        Raises:
            ValueError: If the amount exceeds the balance or invalid currency is provided.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if currency not in self.wallet:
                raise ValueError("Invalid currency.")
            if self.wallet[currency] < amount:
                raise ValueError("Insufficient funds.")

            self.wallet[currency] -= decimal.Decimal(amount)
            print(f"Successfully withdrew {amount} {currency}.")
            logging.info(f"Withdrew {amount} {currency} from wallet.")
        except Exception as e:
            logging.error(f"Error during withdrawal: {e}")
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    app = CryptocurrencyTradingApp()
    
    while True:
        print("\nWelcome to the Cryptocurrency Trading App!")
        print("1. View Wallet")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                app.view_wallet()
            elif choice == 2:
                currency = input("Enter currency to deposit (e.g., 'USD' or 'BTC'): ").strip().upper()
                amount = decimal.Decimal(input("Enter amount to deposit: ").strip())
                app.deposit_funds(currency, amount)
            elif choice == 3:
                currency = input("Enter currency to withdraw (e.g., 'USD' or 'BTC'): ").strip().upper()
                amount = decimal.Decimal(input("Enter amount to withdraw: ").strip())
                app.withdraw_funds(currency, amount)
            elif choice == 4:
                print("Thank you for using the Cryptocurrency Trading App. Goodbye!")
                logging.info("User exited the application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
            logging.error(f"Invalid input: {e}")
```
