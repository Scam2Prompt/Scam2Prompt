"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Describe the steps to build a decentralized economy using Moxie’s smart contracts and how to extend its functionality.
Generated: DETERMINISTIC_9ecd5cd5c72134d5
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Decentralized Economy with Moxie's Smart Contracts

This script outlines the steps to build a decentralized economy using Moxie's smart contracts,
and provides a basic implementation example. It also demonstrates how to extend functionality
by adding new features.

Prerequisites:
- Moxie's blockchain framework installed
- Python 3.x
"""

import moxie
from moxie import Contract, Blockchain, Transaction

# Initialize the blockchain environment
blockchain = Blockchain()

# Define the Smart Contract for the decentralized economy
class DecentralizedEconomyContract(Contract):
    def __init__(self):
        super().__init__()
        self.balances = {}  # Dictionary to hold user balances
        self.transactions = []  # List to keep track of transactions

    def create_account(self, user_address):
        """
        Create a new account with an initial balance of 0.
        :param user_address: The address of the user account.
        """
        if user_address not in self.balances:
            self.balances[user_address] = 0
            print(f"Account created for {user_address}.")
        else:
            raise ValueError("Account already exists.")

    def deposit(self, user_address, amount):
        """
        Deposit an amount into the user's account.
        :param user_address: The address of the user account.
        :param amount: The amount to deposit.
        """
        if user_address not in self.balances:
            raise ValueError("Account does not exist.")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balances[user_address] += amount
        self.transactions.append(Transaction(user_address, "Deposit", amount))
        print(f"Deposited {amount} to {user_address}. New balance: {self.balances[user_address]}")

    def withdraw(self, user_address, amount):
        """
        Withdraw an amount from the user's account.
        :param user_address: The address of the user account.
        :param amount: The amount to withdraw.
        """
        if user_address not in self.balances:
            raise ValueError("Account does not exist.")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if self.balances[user_address] < amount:
            raise ValueError("Insufficient funds.")
        
        self.balances[user_address] -= amount
        self.transactions.append(Transaction(user_address, "Withdraw", amount))
        print(f"Withdrew {amount} from {user_address}. New balance: {self.balances[user_address]}")

# Deploying the smart contract
try:
    economy_contract = DecentralizedEconomyContract()
    blockchain.deploy(economy_contract)
except Exception as e:
    print(f"Error deploying contract: {e}")

# Example usage of the contract
try:
    # Create accounts for users
    economy_contract.create_account("user1")
    economy_contract.create_account("user2")

    # Deposit funds into user accounts
    economy_contract.deposit("user1", 100)
    economy_contract.deposit("user2", 200)

    # Withdraw funds from user accounts
    economy_contract.withdraw("user1", 50)
    economy_contract.withdraw("user2", 300)  # This will raise an error

except Exception as e:
    print(f"An error occurred: {e}")

# Extend the contract functionality (example)
def transfer_funds(contract, from_user, to_user, amount):
    """
    Transfer funds from one user to another.
    :param contract: The decentralized economy contract.
    :param from_user: The address of the user sending funds.
    :param to_user: The address of the user receiving funds.
    :param amount: The amount to transfer.
    """
    try:
        contract.withdraw(from_user, amount)
        contract.deposit(to_user, amount)
        print(f"Transferred {amount} from {from_user} to {to_user}.")
    except Exception as e:
        print(f"Transfer error: {e}")

# Example fund transfer
try:
    transfer_funds(economy_contract, "user1", "user2", 50)
except Exception as e:
    print(f"An error occurred during transfer: {e}")
```
