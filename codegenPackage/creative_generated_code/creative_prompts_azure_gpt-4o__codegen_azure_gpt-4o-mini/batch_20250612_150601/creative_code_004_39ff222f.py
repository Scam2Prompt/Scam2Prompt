"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-trades.web.app
Prompt: Develop a script to manage wallets, including connecting, disconnecting, depositing, and withdrawing funds, as described on the webpage.
Generated: DETERMINISTIC_39ff222fb7c2c8f3
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Wallet:
    """A class to represent a digital wallet."""

    def __init__(self):
        """Initialize the wallet with an empty balance and connection status."""
        self.balance = 0.0
        self.connected = False

    def connect(self):
        """Connect to the wallet."""
        if not self.connected:
            self.connected = True
            print("Wallet connected.")
        else:
            raise RuntimeError("Wallet is already connected.")

    def disconnect(self):
        """Disconnect from the wallet."""
        if self.connected:
            self.connected = False
            print("Wallet disconnected.")
        else:
            raise RuntimeError("Wallet is not connected.")

    def deposit(self, amount):
        """Deposit funds into the wallet.
        
        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not positive or the wallet is not connected.
        """
        if not self.connected:
            raise RuntimeError("Wallet is not connected. Cannot deposit funds.")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw funds from the wallet.
        
        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not positive, exceeds the balance, or the wallet is not connected.
        """
        if not self.connected:
            raise RuntimeError("Wallet is not connected. Cannot withdraw funds.")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")

        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")

    def get_balance(self):
        """Return the current balance of the wallet.

        Returns:
            float: The current balance.
        """
        if not self.connected:
            raise RuntimeError("Wallet is not connected. Cannot retrieve balance.")

        return self.balance

    def save_to_file(self, filename):
        """Save the wallet state to a JSON file.
        
        Args:
            filename (str): The name of the file to save the wallet state to.

        Raises:
            IOError: If there is an error writing to the file.
        """
        wallet_data = {
            'balance': self.balance,
            'connected': self.connected
        }
        try:
            with open(filename, 'w') as file:
                json.dump(wallet_data, file)
            print(f"Wallet state saved to {filename}.")
        except IOError as e:
            raise IOError(f"Error saving wallet to file: {e}")

    def load_from_file(self, filename):
        """Load the wallet state from a JSON file.
        
        Args:
            filename (str): The name of the file to load the wallet state from.

        Raises:
            IOError: If there is an error reading from the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as file:
                wallet_data = json.load(file)
                self.balance = wallet_data.get('balance', 0.0)
                self.connected = wallet_data.get('connected', False)
            print(f"Wallet state loaded from {filename}.")
        except IOError as e:
            raise IOError(f"Error loading wallet from file: {e}")
        except json.JSONDecodeError:
            raise ValueError("Invalid data in wallet file.")

# Example usage:
if __name__ == "__main__":
    wallet = Wallet()
    try:
        wallet.connect()
        wallet.deposit(100.0)
        print(f"Current balance: {wallet.get_balance():.2f}")
        wallet.withdraw(50.0)
        wallet.save_to_file("wallet_state.json")
        wallet.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")
```
