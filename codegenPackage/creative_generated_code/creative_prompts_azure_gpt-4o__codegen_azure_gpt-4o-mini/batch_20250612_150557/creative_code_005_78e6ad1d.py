"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solak.web.app
Prompt: Create code to manage multiple wallets, including connecting, disconnecting, depositing, and withdrawing funds, as implemented on the NFT Solak platform.
Generated: DETERMINISTIC_78e6ad1df8c4ca3b
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class Wallet:
    def __init__(self, wallet_id):
        """
        Initialize a wallet with a unique ID.
        
        :param wallet_id: Unique identifier for the wallet.
        """
        self.wallet_id = wallet_id
        self.balance = 0.0  # Initialize wallet balance to zero
        self.connected = False  # Wallet is initially disconnected

    def connect(self):
        """
        Connect to the wallet.
        """
        if self.connected:
            logging.warning(f"Wallet {self.wallet_id} is already connected.")
            return
        self.connected = True
        logging.info(f"Wallet {self.wallet_id} connected successfully.")

    def disconnect(self):
        """
        Disconnect the wallet.
        """
        if not self.connected:
            logging.warning(f"Wallet {self.wallet_id} is already disconnected.")
            return
        self.connected = False
        logging.info(f"Wallet {self.wallet_id} disconnected successfully.")

    def deposit(self, amount):
        """
        Deposit funds into the wallet.
        
        :param amount: Amount of money to deposit.
        :raises ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            logging.error("Deposit amount must be non-negative.")
            raise ValueError("Deposit amount must be non-negative.")
        
        self.balance += amount
        logging.info(f"Deposited {amount} to wallet {self.wallet_id}. New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw funds from the wallet.
        
        :param amount: Amount of money to withdraw.
        :raises ValueError: If the withdrawal amount is negative or exceeds the balance.
        """
        if amount < 0:
            logging.error("Withdrawal amount must be non-negative.")
            raise ValueError("Withdrawal amount must be non-negative.")
        
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")

        self.balance -= amount
        logging.info(f"Withdrew {amount} from wallet {self.wallet_id}. New balance: {self.balance}")

    def get_balance(self):
        """
        Get the current balance of the wallet.
        
        :return: Current balance of the wallet.
        """
        return self.balance

    def to_json(self):
        """
        Convert wallet information to JSON format.
        
        :return: JSON representation of the wallet.
        """
        return json.dumps({
            'wallet_id': self.wallet_id,
            'balance': self.balance,
            'connected': self.connected
        })

class WalletManager:
    def __init__(self):
        """
        Initialize the wallet manager to handle multiple wallets.
        """
        self.wallets = {}

    def create_wallet(self, wallet_id):
        """
        Create a new wallet.
        
        :param wallet_id: Unique identifier for the new wallet.
        :raises ValueError: If the wallet ID already exists.
        """
        if wallet_id in self.wallets:
            logging.error(f"Wallet with ID {wallet_id} already exists.")
            raise ValueError("Wallet ID already exists.")
        
        self.wallets[wallet_id] = Wallet(wallet_id)
        logging.info(f"Wallet {wallet_id} created successfully.")

    def get_wallet(self, wallet_id):
        """
        Retrieve a wallet by its ID.
        
        :param wallet_id: Unique identifier of the wallet.
        :return: Wallet object.
        :raises ValueError: If the wallet ID does not exist.
        """
        if wallet_id not in self.wallets:
            logging.error(f"Wallet with ID {wallet_id} does not exist.")
            raise ValueError("Wallet ID does not exist.")
        
        return self.wallets[wallet_id]

    def list_wallets(self):
        """
        List all wallets managed by the wallet manager.
        
        :return: List of wallet IDs.
        """
        return list(self.wallets.keys())

# Example usage
if __name__ == "__main__":
    manager = WalletManager()
    try:
        manager.create_wallet("wallet1")
        wallet = manager.get_wallet("wallet1")
        
        wallet.connect()
        wallet.deposit(100)
        wallet.withdraw(50)
        
        print(wallet.to_json())
        
        wallet.disconnect()
    except ValueError as e:
        logging.error(e)
```
