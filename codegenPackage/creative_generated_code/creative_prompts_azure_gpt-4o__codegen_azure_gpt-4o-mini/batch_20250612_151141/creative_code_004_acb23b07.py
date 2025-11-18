"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Implement a feature that tracks reward forfeiture, redistributing accrued revenue share among all holders if a user sells or transfers more than 300 $BANANA or their holdings drop below 50 $BANANA.
Generated: DETERMINISTIC_acb23b07c4e6d012
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal

class TokenHolder:
    """
    Class representing a holder of $BANANA tokens.
    """

    def __init__(self, address: str, balance: Decimal):
        """
        Initialize a TokenHolder with an address and a balance.

        :param address: The blockchain address of the token holder.
        :param balance: The initial balance of $BANANA tokens.
        """
        self.address = address
        self.balance = balance

class RewardTracker:
    """
    Class to track reward forfeiture and redistribute revenue shares.
    """

    def __init__(self):
        """
        Initialize the RewardTracker with an empty list of holders and total revenue.
        """
        self.holders = []
        self.total_revenue = Decimal('0.0')

    def add_holder(self, holder: TokenHolder):
        """
        Add a new holder to the tracker.

        :param holder: An instance of TokenHolder to be added.
        """
        self.holders.append(holder)

    def record_transfer(self, from_holder: TokenHolder, amount: Decimal):
        """
        Record a transfer of $BANANA tokens and handle reward forfeiture.

        :param from_holder: The TokenHolder making the transfer.
        :param amount: The amount of $BANANA tokens being transferred.
        """
        if from_holder.balance < amount:
            raise ValueError("Transfer amount exceeds holder's balance.")

        # Update holder's balance after transfer
        from_holder.balance -= amount
        
        # Check conditions for forfeiture
        if amount > Decimal('300') or from_holder.balance < Decimal('50'):
            self.redistribute_rewards()

    def redistribute_rewards(self):
        """
        Redistribute the accrued revenue share among all holders.
        """
        if not self.holders:
            print("No holders to redistribute rewards.")
            return
            
        # Calculate share per holder
        revenue_share = self.total_revenue / len(self.holders)

        # Distribute the revenue share to each holder
        for holder in self.holders:
            holder.balance += revenue_share

        # Reset total revenue after redistribution
        self.total_revenue = Decimal('0.0')

    def accrue_revenue(self, amount: Decimal):
        """
        Accrue revenue to be distributed later.

        :param amount: The amount of revenue to accrue.
        """
        if amount < Decimal('0.0'):
            raise ValueError("Revenue amount must be non-negative.")
        
        self.total_revenue += amount

# Example usage
if __name__ == "__main__":
    # Initialize reward tracker
    reward_tracker = RewardTracker()

    # Create token holders
    holder1 = TokenHolder("address_1", Decimal('500'))
    holder2 = TokenHolder("address_2", Decimal('200'))
    
    # Add holders to the tracker
    reward_tracker.add_holder(holder1)
    reward_tracker.add_holder(holder2)

    # Accrue some revenue
    reward_tracker.accrue_revenue(Decimal('1000'))

    # Simulate a transfer that triggers reward forfeiture
    try:
        reward_tracker.record_transfer(holder1, Decimal('350'))
        print(f"Holder 1 new balance: {holder1.balance}")
        print(f"Holder 2 new balance: {holder2.balance}")
    except ValueError as e:
        print(f"Error: {e}")
```
