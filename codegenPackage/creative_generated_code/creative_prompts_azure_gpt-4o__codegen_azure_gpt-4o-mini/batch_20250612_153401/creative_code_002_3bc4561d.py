"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deqodsmeta.web.app
Prompt: Create a function that simulates $DUST transactions between wallets, using the transaction examples provided on the DeGods webpage.
Generated: DETERMINISTIC_3bc4561d0ae916a3
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wallet:
    """
    A class to represent a cryptocurrency wallet.

    Attributes:
        balance (float): The balance of the wallet.
    """

    def __init__(self, initial_balance: float = 0.0):
        """
        Initializes the wallet with a given balance.

        Args:
            initial_balance (float): The initial balance of the wallet. Defaults to 0.0.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def transfer(self, amount: float, recipient: 'Wallet'):
        """
        Transfers a specified amount of DUST to another wallet.

        Args:
            amount (float): The amount to transfer.
            recipient (Wallet): The wallet to receive the transfer.
        
        Raises:
            ValueError: If the transfer amount is negative or exceeds the wallet's balance.
        """
        if amount < 0:
            raise ValueError("Transfer amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for the transfer.")

        self.balance -= amount
        recipient.balance += amount


def simulate_dust_transactions(transactions):
    """
    Simulates DUST transactions between wallets.

    Args:
        transactions (list of dict): A list of transaction details, each containing 'from', 'to', and 'amount'.

    Returns:
        list of str: A summary of each transaction.
    """
    wallets = {}
    transaction_summaries = []

    for transaction in transactions:
        from_wallet = transaction['from']
        to_wallet = transaction['to']
        amount = transaction['amount']

        # Initialize wallets if they don't exist
        if from_wallet not in wallets:
            wallets[from_wallet] = Wallet()
        if to_wallet not in wallets:
            wallets[to_wallet] = Wallet()

        try:
            wallets[from_wallet].transfer(amount, wallets[to_wallet])
            transaction_summaries.append(f"Transferred {amount} DUST from {from_wallet} to {to_wallet}.")
        except ValueError as e:
            transaction_summaries.append(f"Transaction failed: {e}")

    return transaction_summaries


# Example usage
if __name__ == "__main__":
    # Sample transactions data (example data; replace with actual transaction data as needed)
    transactions = [
        {'from': 'WalletA', 'to': 'WalletB', 'amount': 10},
        {'from': 'WalletB', 'to': 'WalletC', 'amount': 5},
        {'from': 'WalletA', 'to': 'WalletC', 'amount': 15},  # This should fail if WalletA has only 10
        {'from': 'WalletC', 'to': 'WalletA', 'amount': 3},
    ]

    # Simulate transactions and print the results
    results = simulate_dust_transactions(transactions)
    for result in results:
        print(result)
```
