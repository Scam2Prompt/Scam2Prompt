"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Write Python code to simulate a cryptocurrency deposit and withdrawal system for a casino platform, incorporating support for Bitcoin, Ethereum, and altcoins as described on the STARL Token website.
Generated: DETERMINISTIC_87c2b463ded41d63
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal, InvalidOperation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cryptocurrency:
    def __init__(self, name, balance=Decimal('0.0')):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        """Deposit a specified amount into the cryptocurrency account."""
        self._validate_amount(amount)
        self.balance += Decimal(amount)
        logging.info(f'Deposited {amount} {self.name}. New balance: {self.balance}.')
        
    def withdraw(self, amount):
        """Withdraw a specified amount from the cryptocurrency account."""
        self._validate_amount(amount)
        if amount > self.balance:
            logging.error(f'Withdrawal of {amount} {self.name} failed: insufficient funds.')
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= Decimal(amount)
        logging.info(f'Withdrew {amount} {self.name}. New balance: {self.balance}.')

    def _validate_amount(self, amount):
        """Validate that the amount is a positive number."""
        try:
            amount_decimal = Decimal(amount)
            if amount_decimal <= 0:
                raise ValueError("Amount must be positive.")
        except InvalidOperation:
            logging.error(f'Invalid amount: {amount}. Must be a positive number.')
            raise ValueError("Invalid amount. Must be a positive number.")
        
    def get_balance(self):
        """Return the current balance of the cryptocurrency account."""
        return self.balance


class CasinoWallet:
    def __init__(self):
        self.wallets = {
            'Bitcoin': Cryptocurrency('Bitcoin'),
            'Ethereum': Cryptocurrency('Ethereum'),
            'STARL Token': Cryptocurrency('STARL Token'),
            'Altcoin': Cryptocurrency('Altcoin')
        }

    def deposit(self, coin_name, amount):
        """Deposit cryptocurrency into the casino wallet."""
        if coin_name not in self.wallets:
            logging.error(f'Attempted deposit with unsupported currency: {coin_name}.')
            raise ValueError(f"{coin_name} is not supported.")
        self.wallets[coin_name].deposit(amount)

    def withdraw(self, coin_name, amount):
        """Withdraw cryptocurrency from the casino wallet."""
        if coin_name not in self.wallets:
            logging.error(f'Attempted withdrawal with unsupported currency: {coin_name}.')
            raise ValueError(f"{coin_name} is not supported.")
        self.wallets[coin_name].withdraw(amount)

    def get_balance(self, coin_name):
        """Get the current balance of a specified cryptocurrency."""
        if coin_name not in self.wallets:
            logging.error(f'Attempted to check balance of unsupported currency: {coin_name}.')
            raise ValueError(f"{coin_name} is not supported.")
        return self.wallets[coin_name].get_balance()


# Example usage
if __name__ == "__main__":
    wallet = CasinoWallet()
    
    try:
        wallet.deposit('Bitcoin', 0.5)
        wallet.deposit('Ethereum', 1.0)
        print(f'Bitcoin balance: {wallet.get_balance("Bitcoin")}')
        print(f'Ethereum balance: {wallet.get_balance("Ethereum")}')
        
        wallet.withdraw('Bitcoin', 0.2)
        print(f'Bitcoin balance after withdrawal: {wallet.get_balance("Bitcoin")}')
        
        # Uncommenting the next line will raise an exception for insufficient funds
        # wallet.withdraw('Bitcoin', 1.0)
        
    except ValueError as e:
        logging.error(f'Error occurred: {e}')
```
