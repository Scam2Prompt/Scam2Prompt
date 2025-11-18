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
import decimal

class CryptocurrencyWallet:
    """
    A class to simulate a cryptocurrency wallet for deposit and withdrawal
    operations. Supports Bitcoin, Ethereum, and Altcoins (e.g., STARL Token).
    """
    def __init__(self):
        # Initialize balances for supported cryptocurrencies
        self.balances = {
            "Bitcoin": decimal.Decimal('0.0'),
            "Ethereum": decimal.Decimal('0.0'),
            "STARL Token": decimal.Decimal('0.0')  # Example of an altcoin
        }

    def deposit(self, currency: str, amount: float):
        """
        Handles cryptocurrency deposits.
        
        :param currency: The cryptocurrency type (e.g., "Bitcoin", "Ethereum", "STARL Token").
        :param amount: The deposit amount (must be greater than 0).
        :raises ValueError: If the currency is unsupported or the amount is invalid.
        """
        if currency not in self.balances:
            raise ValueError(f"{currency} is not supported.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Update balance after deposit
        self.balances[currency] += decimal.Decimal(amount)
        print(f"Successfully deposited {amount} {currency}.")

    def withdraw(self, currency: str, amount: float):
        """
        Handles cryptocurrency withdrawals.
        
        :param currency: The cryptocurrency type (e.g., "Bitcoin", "Ethereum", "STARL Token").
        :param amount: The withdrawal amount (must be greater than 0 and <= current balance).
        :raises ValueError: If the currency is unsupported, amount is invalid, or insufficient balance.
        """
        if currency not in self.balances:
            raise ValueError(f"{currency} is not supported.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if decimal.Decimal(amount) > self.balances[currency]:
            raise ValueError(f"Insufficient balance for {currency}.")
        
        # Update balance after withdrawal
        self.balances[currency] -= decimal.Decimal(amount)
        print(f"Successfully withdrew {amount} {currency}.")

    def get_balance(self, currency: str) -> float:
        """
        Returns the current balance for a specific cryptocurrency.
        
        :param currency: The cryptocurrency type (e.g., "Bitcoin", "Ethereum", "STARL Token").
        :return: The current balance as a float.
        :raises ValueError: If the currency is unsupported.
        """
        if currency not in self.balances:
            raise ValueError(f"{currency} is not supported.")
        return float(self.balances[currency])

    def display_balances(self):
        """
        Prints the current balances for all supported cryptocurrencies.
        """
        print("Current Wallet Balances:")
        for currency, balance in self.balances.items():
            print(f"{currency}: {balance:.8f}")


# Example usage:
if __name__ == "__main__":
    try:
        wallet = CryptocurrencyWallet()

        # Simulate deposit operations
        wallet.deposit("Bitcoin", 0.005)
        wallet.deposit("Ethereum", 1.2)
        wallet.deposit("STARL Token", 50000)

        # Display balances after deposits
        wallet.display_balances()

        # Simulate withdrawal operations
        wallet.withdraw("Bitcoin", 0.002)
        wallet.withdraw("Ethereum", 0.5)

        # Display balances after withdrawals
        wallet.display_balances()

        # Check individual balance
        starl_balance = wallet.get_balance("STARL Token")
        print(f"STARL Token Balance: {starl_balance:.8f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
