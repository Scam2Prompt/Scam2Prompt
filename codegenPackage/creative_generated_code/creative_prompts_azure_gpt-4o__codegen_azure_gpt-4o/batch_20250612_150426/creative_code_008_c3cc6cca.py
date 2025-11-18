"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: Create a Python script to simulate $UPRINT token transactions and calculate the USDC rewards distributed to holders based on the tokenomics described.
Generated: DETERMINISTIC_c3cc6cca9ace4915
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal, getcontext

# Set decimal precision for accurate financial calculations
getcontext().prec = 18

class UPRINTTransactionSimulator:
    """
    Simulates $UPRINT token transactions and calculates USDC rewards
    distributed to holders based on specified tokenomics.
    """

    def __init__(self, holders, reward_pool, transaction_fee_percent=5, reward_percent=50):
        """
        Initializes the simulator.

        :param holders: Dictionary of $UPRINT holders with their balances {holder_name: balance}.
        :param reward_pool: Initial USDC reward pool.
        :param transaction_fee_percent: Fee percentage for each transaction (default: 5%).
        :param reward_percent: Percentage of transaction fees distributed as rewards (default: 50%).
        """
        self.holders = holders
        self.reward_pool = Decimal(reward_pool)
        self.transaction_fee_percent = Decimal(transaction_fee_percent)
        self.reward_percent = Decimal(reward_percent)
        self.total_supply = sum(holders.values())

    def simulate_transaction(self, sender, receiver, amount):
        """
        Simulates a transaction and updates balances and rewards.

        :param sender: Name of the sender.
        :param receiver: Name of the receiver.
        :param amount: Amount of $UPRINT being transacted.
        """
        # Convert to Decimal for precision
        amount = Decimal(amount)

        # Ensure sender has enough balance
        if self.holders[sender] < amount:
            raise ValueError(f"{sender} does not have sufficient balance for this transaction.")

        # Calculate transaction fee
        fee = (amount * self.transaction_fee_percent) / 100
        net_transfer = amount - fee

        # Update sender and receiver balances
        self.holders[sender] -= amount
        self.holders[receiver] += net_transfer

        # Add fee to reward pool
        self.reward_pool += fee * (self.reward_percent / 100)

    def distribute_rewards(self):
        """
        Distributes the current USDC reward pool to holders
        based on their share of the total $UPRINT supply.
        """
        if self.reward_pool <= 0:
            return  # Nothing to distribute

        for holder, balance in self.holders.items():
            share = (Decimal(balance) / Decimal(self.total_supply)) * self.reward_pool
            print(f"Holder: {holder} | USDC Reward Distributed: {share:.6f}")

        # Reset reward pool after distribution
        self.reward_pool = Decimal(0)

    def print_holders_balances(self):
        """Prints the current balances of all holders."""
        print("Current Balances:")
        for holder, balance in self.holders.items():
            print(f"{holder}: {balance:.6f} UPRINT")


# Example usage
if __name__ == "__main__":
    # Initialize holders and balances
    holders = {
        "Alice": Decimal(1000),
        "Bob": Decimal(2000),
        "Charlie": Decimal(3000),
    }

    # Initialize simulator with a $1000 USDC reward pool
    simulator = UPRINTTransactionSimulator(holders, reward_pool=1000)

    # Simulate transactions
    try:
        simulator.simulate_transaction("Alice", "Bob", 200)  # Alice sends 200 $UPRINT to Bob
        simulator.simulate_transaction("Charlie", "Alice", 500)  # Charlie sends 500 $UPRINT to Alice
    except ValueError as e:
        print(f"Transaction Error: {e}")

    # Print balances after transactions
    simulator.print_holders_balances()

    # Distribute rewards
    print("\nDistributing Rewards:")
    simulator.distribute_rewards()
```
