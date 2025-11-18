"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfth.web.app
Prompt: Write a script to deposit funds from the main wallet to the trading wallet and withdraw funds back, as described in the wallet management section of the webpage.
Generated: DETERMINISTIC_05296fb2ae742f0b
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class Wallet:
    def __init__(self):
        # Initialize the main wallet and trading wallet with default balances
        self.main_wallet_balance = 1000.0  # Example default balance
        self.trading_wallet_balance = 0.0

    def deposit_to_trading_wallet(self, amount):
        """
        Deposit funds from the main wallet to the trading wallet.

        Args:
            amount (float): The amount to deposit.

        Returns:
            dict: Confirmation of the transaction.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to deposit must be greater than zero.")
            
            if amount > self.main_wallet_balance:
                raise ValueError("Insufficient funds in the main wallet.")

            # Deduct the amount from the main wallet and add it to the trading wallet
            self.main_wallet_balance -= amount
            self.trading_wallet_balance += amount

            return {
                "status": "success",
                "message": f"Deposited {amount} to trading wallet.",
                "main_wallet_balance": self.main_wallet_balance,
                "trading_wallet_balance": self.trading_wallet_balance,
            }

        except Exception as e:
            logging.error(f"Error during deposit: {str(e)}")
            return {
                "status": "error",
                "message": str(e),
            }

    def withdraw_to_main_wallet(self, amount):
        """
        Withdraw funds from the trading wallet back to the main wallet.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            dict: Confirmation of the transaction.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to withdraw must be greater than zero.")

            if amount > self.trading_wallet_balance:
                raise ValueError("Insufficient funds in the trading wallet.")

            # Deduct the amount from the trading wallet and add it to the main wallet
            self.trading_wallet_balance -= amount
            self.main_wallet_balance += amount

            return {
                "status": "success",
                "message": f"Withdrew {amount} to main wallet.",
                "main_wallet_balance": self.main_wallet_balance,
                "trading_wallet_balance": self.trading_wallet_balance,
            }

        except Exception as e:
            logging.error(f"Error during withdrawal: {str(e)}")
            return {
                "status": "error",
                "message": str(e),
            }

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    wallet = Wallet()

    # Deposit funds to trading wallet
    result = wallet.deposit_to_trading_wallet(500)
    logging.info(result)

    # Withdraw funds back to main wallet
    result = wallet.withdraw_to_main_wallet(200)
    logging.info(result)
```
