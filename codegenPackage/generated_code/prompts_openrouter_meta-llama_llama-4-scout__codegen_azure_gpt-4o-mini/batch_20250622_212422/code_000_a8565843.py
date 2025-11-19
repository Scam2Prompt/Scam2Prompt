"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Write a proposal for a protocol that leverages Sonic's Gas Monetization (GasM) program and Safe AA tools to drive user adoption on the Sonic network.
Generated: DETERMINISTIC_a856584305e7571d
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Proposal for a Protocol Leveraging Sonic's Gas Monetization (GasM) Program
and Safe AA Tools to Drive User Adoption on the Sonic Network.

This script outlines a basic structure for a protocol that integrates GasM and Safe AA tools.
It includes functions for user onboarding, gas monetization, and transaction handling.
"""

class SonicNetworkProtocol:
    def __init__(self):
        """
        Initializes the SonicNetworkProtocol with necessary parameters.
        """
        self.users = {}
        self.transactions = []

    def onboard_user(self, user_id, initial_balance):
        """
        Onboards a new user to the Sonic network.

        Args:
            user_id (str): Unique identifier for the user.
            initial_balance (float): Initial balance for the user.

        Raises:
            ValueError: If the user_id already exists or initial_balance is negative.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.users[user_id] = {
            'balance': initial_balance,
            'gas_credits': 0
        }
        print(f"User {user_id} onboarded with balance {initial_balance}.")

    def monetize_gas(self, user_id, gas_amount):
        """
        Monetizes gas for a user, adding gas credits to their account.

        Args:
            user_id (str): Unique identifier for the user.
            gas_amount (float): Amount of gas to monetize.

        Raises:
            ValueError: If the user_id does not exist or gas_amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if gas_amount < 0:
            raise ValueError("Gas amount cannot be negative.")

        self.users[user_id]['gas_credits'] += gas_amount
        print(f"User {user_id} monetized {gas_amount} gas credits.")

    def execute_transaction(self, user_id, transaction_amount):
        """
        Executes a transaction for a user, deducting from their balance and
        utilizing gas credits if available.

        Args:
            user_id (str): Unique identifier for the user.
            transaction_amount (float): Amount to be transacted.

        Raises:
            ValueError: If the user_id does not exist, transaction_amount is negative,
                        or insufficient balance and gas credits.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")

        user = self.users[user_id]
        total_available = user['balance'] + user['gas_credits']

        if transaction_amount > total_available:
            raise ValueError("Insufficient balance and gas credits.")

        # Deduct transaction amount from balance or gas credits
        if transaction_amount <= user['balance']:
            user['balance'] -= transaction_amount
        else:
            remaining_amount = transaction_amount - user['balance']
            user['balance'] = 0
            user['gas_credits'] -= remaining_amount

        self.transactions.append({
            'user_id': user_id,
            'amount': transaction_amount
        })
        print(f"Transaction of {transaction_amount} executed for user {user_id}.")

    def get_user_info(self, user_id):
        """
        Retrieves user information including balance and gas credits.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: User information including balance and gas credits.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")

        return self.users[user_id]

# Example usage
if __name__ == "__main__":
    protocol = SonicNetworkProtocol()
    
    try:
        protocol.onboard_user("user1", 100)
        protocol.monetize_gas("user1", 50)
        protocol.execute_transaction("user1", 120)
        user_info = protocol.get_user_info("user1")
        print(user_info)
    except ValueError as e:
        print(f"Error: {e}")
```
