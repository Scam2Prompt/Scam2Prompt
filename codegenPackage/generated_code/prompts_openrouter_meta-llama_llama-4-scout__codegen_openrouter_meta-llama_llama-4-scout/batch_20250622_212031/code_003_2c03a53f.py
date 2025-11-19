"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Design a basic online banking system, like Grand Chase's platform, that allows users to create accounts, transfer money, and view transaction history, using a suitable programming language.
Generated: DETERMINISTIC_2c03a53fd78e6f00
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# banking_system.py

class User:
    """Represents a bank user."""
    
    def __init__(self, user_id, username, password):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique user ID.
            username (str): Username chosen by the user.
            password (str): Password chosen by the user.
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.accounts = {}

class Account:
    """Represents a bank account."""
    
    def __init__(self, account_id, user_id, balance=0.0):
        """
        Initializes an Account object.

        Args:
            account_id (int): Unique account ID.
            user_id (int): ID of the account owner.
            balance (float, optional): Initial account balance. Defaults to 0.0.
        """
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance
        self.transaction_history = []

class BankingSystem:
    """Represents the online banking system."""
    
    def __init__(self):
        """Initializes the banking system."""
        self.users = {}
        self.accounts = {}
        self.user_id_counter = 1
        self.account_id_counter = 1

    def create_user(self, username, password):
        """
        Creates a new user.

        Args:
            username (str): Username chosen by the user.
            password (str): Password chosen by the user.

        Returns:
            int: The ID of the newly created user.
        """
        user_id = self.user_id_counter
        self.users[user_id] = User(user_id, username, password)
        self.user_id_counter += 1
        return user_id

    def create_account(self, user_id, initial_balance=0.0):
        """
        Creates a new account for a user.

        Args:
            user_id (int): ID of the account owner.
            initial_balance (float, optional): Initial account balance. Defaults to 0.0.

        Returns:
            int: The ID of the newly created account.
        """
        if user_id not in self.users:
            raise ValueError("User not found")

        account_id = self.account_id_counter
        self.accounts[account_id] = Account(account_id, user_id, initial_balance)
        self.users[user_id].accounts[account_id] = self.accounts[account_id]
        self.account_id_counter += 1
        return account_id

    def transfer(self, from_account_id, to_account_id, amount):
        """
        Transfers money between accounts.

        Args:
            from_account_id (int): ID of the account to transfer from.
            to_account_id (int): ID of the account to transfer to.
            amount (float): The amount to transfer.

        Raises:
            ValueError: If either account is not found or if the transfer amount is invalid.
        """
        if from_account_id not in self.accounts or to_account_id not in self.accounts:
            raise ValueError("One or both accounts not found")

        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]

        if amount <= 0:
            raise ValueError("Invalid transfer amount")

        if from_account.balance < amount:
            raise ValueError("Insufficient funds")

        from_account.balance -= amount
        to_account.balance += amount

        from_account.transaction_history.append(f"Transferred ${amount:.2f} to account {to_account_id}")
        to_account.transaction_history.append(f"Received ${amount:.2f} from account {from_account_id}")

    def get_transaction_history(self, account_id):
        """
        Retrieves the transaction history for an account.

        Args:
            account_id (int): ID of the account.

        Returns:
            list: A list of transaction history entries.

        Raises:
            ValueError: If the account is not found.
        """
        if account_id not in self.accounts:
            raise ValueError("Account not found")

        return self.accounts[account_id].transaction_history

def main():
    banking_system = BankingSystem()

    # Create users
    user1_id = banking_system.create_user("user1", "password1")
    user2_id = banking_system.create_user("user2", "password2")

    # Create accounts
    account1_id = banking_system.create_account(user1_id, 1000.0)
    account2_id = banking_system.create_account(user2_id, 500.0)

    # Transfer money
    banking_system.transfer(account1_id, account2_id, 200.0)

    # Get transaction history
    print("Account 1 transaction history:")
    for entry in banking_system.get_transaction_history(account1_id):
        print(entry)

    print("\nAccount 2 transaction history:")
    for entry in banking_system.get_transaction_history(account2_id):
        print(entry)

if __name__ == "__main__":
    main()
```
