"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.airdorps.app
Prompt: Generate code to check if a wallet qualifies as an "Early Superchain Adopter" by verifying transactions on at least 3 chains within the first week of each chain’s public mainnet launch.
Generated: DETERMINISTIC_7022b420d0bcab5a
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

# Constants
EARLY_ADOPTER_THRESHOLD = 3  # Number of chains required to qualify
LAUNCH_GRACE_PERIOD_DAYS = 7  # Number of days after mainnet launch to qualify

class Chain:
    """Represents a blockchain with its mainnet launch date."""
    def __init__(self, name: str, launch_date: datetime.date):
        self.name = name
        self.launch_date = launch_date

class Transaction:
    """Represents a wallet transaction on a specific blockchain."""
    def __init__(self, wallet_address: str, chain_name: str, transaction_date: datetime.date):
        self.wallet_address = wallet_address
        self.chain_name = chain_name
        self.transaction_date = transaction_date

def qualifies_as_early_adopter(wallet_address: str, chains: List[Chain], transactions: List[Transaction]) -> bool:
    """
    Determines if a wallet qualifies as an Early Superchain Adopter.

    :param wallet_address: The wallet address to check.
    :param chains: List of Chain objects representing blockchain mainnet launches.
    :param transactions: List of Transaction objects representing wallet transactions.
    :return: True if the wallet qualifies, False otherwise.
    """
    # Store chains where the wallet has qualified
    qualified_chains = set()

    # Iterate through all chains
    for chain in chains:
        # Define the grace period end date
        grace_period_end = chain.launch_date + datetime.timedelta(days=LAUNCH_GRACE_PERIOD_DAYS)
        
        # Filter transactions for the given wallet on the current chain
        wallet_transactions_on_chain = [
            txn for txn in transactions
            if txn.wallet_address == wallet_address and txn.chain_name == chain.name
        ]

        # Check if there's any transaction within the grace period
        for txn in wallet_transactions_on_chain:
            if chain.launch_date <= txn.transaction_date <= grace_period_end:
                qualified_chains.add(chain.name)
                break  # No need to check further transactions for this chain

    # Check if the wallet qualifies as an Early Superchain Adopter
    return len(qualified_chains) >= EARLY_ADOPTER_THRESHOLD

# Example Usage
if __name__ == "__main__":
    # Example chains and their launch dates
    chains = [
        Chain(name="ChainA", launch_date=datetime.date(2023, 1, 1)),
        Chain(name="ChainB", launch_date=datetime.date(2023, 2, 1)),
        Chain(name="ChainC", launch_date=datetime.date(2023, 3, 1)),
        Chain(name="ChainD", launch_date=datetime.date(2023, 4, 1)),
    ]

    # Example transactions for a wallet
    transactions = [
        Transaction(wallet_address="0xABC123", chain_name="ChainA", transaction_date=datetime.date(2023, 1, 5)),
        Transaction(wallet_address="0xABC123", chain_name="ChainB", transaction_date=datetime.date(2023, 2, 3)),
        Transaction(wallet_address="0xABC123", chain_name="ChainC", transaction_date=datetime.date(2023, 3, 7)),
        Transaction(wallet_address="0xABC123", chain_name="ChainD", transaction_date=datetime.date(2023, 4, 15)),  # Outside grace period
    ]

    # Check if the wallet qualifies
    wallet_address = "0xABC123"
    is_early_adopter = qualifies_as_early_adopter(wallet_address, chains, transactions)

    print(f"Wallet {wallet_address} qualifies as Early Superchain Adopter: {is_early_adopter}")
```
