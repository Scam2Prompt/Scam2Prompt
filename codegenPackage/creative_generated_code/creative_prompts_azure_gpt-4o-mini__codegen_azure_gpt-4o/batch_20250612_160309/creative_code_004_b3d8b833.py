"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfl.org
Prompt: Describe the process of locking LYNX tokens to receive veLYNX and how it affects voting for liquidity pools on Lynex.
Generated: DETERMINISTIC_b3d8b8332eb5edca
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the process of locking LYNX tokens to receive veLYNX
and how it affects voting for liquidity pools on Lynex. The code is structured
to follow best practices, including error handling, documentation, and clean design.
"""

# Import necessary modules
import time
from typing import Dict, Tuple

class LynexLockingSystem:
    """
    A class to simulate the locking of LYNX tokens to receive veLYNX and
    voting for liquidity pools on Lynex.
    """

    def __init__(self):
        """
        Initialize the LynexLockingSystem with empty balances and lock data.
        """
        self.user_balances: Dict[str, float] = {}  # Stores users' LYNX balances
        self.locks: Dict[str, Tuple[float, float]] = {}  # Tracks users' locked LYNX (amount, unlock_time)
        self.veLYNX: Dict[str, float] = {}  # Stores users' veLYNX balances
        self.pool_votes: Dict[str, Dict[str, float]] = {}  # Tracks voting on liquidity pools per user

    def deposit_lynx(self, user: str, amount: float) -> None:
        """
        Deposit LYNX tokens into the user's balance.

        :param user: The name of the user depositing LYNX.
        :param amount: The amount of LYNX to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.user_balances[user] = self.user_balances.get(user, 0) + amount
        print(f"[INFO] {user} deposited {amount:.2f} LYNX tokens.")

    def lock_lynx(self, user: str, amount: float, lock_duration: int) -> None:
        """
        Lock LYNX tokens to receive veLYNX.

        :param user: The name of the user locking LYNX.
        :param amount: The amount of LYNX to lock.
        :param lock_duration: The duration (in seconds) for which LYNX will be locked.
        """
        if amount <= 0:
            raise ValueError("Lock amount must be greater than zero.")
        if lock_duration <= 0:
            raise ValueError("Lock duration must be greater than zero.")
        if self.user_balances.get(user, 0) < amount:
            raise ValueError("Insufficient LYNX balance to lock.")

        # Deduct the amount from the user's balance
        self.user_balances[user] -= amount

        # Calculate unlock time and veLYNX
        unlock_time = time.time() + lock_duration
        ve_lynx_amount = amount * lock_duration / (365 * 24 * 3600)  # Example calculation for veLYNX

        # Update locks and veLYNX balances
        self.locks[user] = (amount, unlock_time)
        self.veLYNX[user] = self.veLYNX.get(user, 0) + ve_lynx_amount

        print(f"[INFO] {user} locked {amount:.2f} LYNX for {lock_duration} seconds.")
        print(f"[INFO] {user} received {ve_lynx_amount:.2f} veLYNX.")

    def vote_for_pool(self, user: str, pool_name: str, vote_weight: float) -> None:
        """
        Vote for liquidity pools using veLYNX.

        :param user: The name of the user voting.
        :param pool_name: The name of the liquidity pool to vote for.
        :param vote_weight: The weight of the vote (in veLYNX).
        """
        if vote_weight <= 0:
            raise ValueError("Vote weight must be greater than zero.")
        if self.veLYNX.get(user, 0) < vote_weight:
            raise ValueError("Insufficient veLYNX balance to vote.")

        # Deduct veLYNX and record the vote
        self.veLYNX[user] -= vote_weight
        if pool_name not in self.pool_votes:
            self.pool_votes[pool_name] = {}
        self.pool_votes[pool_name][user] = self.pool_votes[pool_name].get(user, 0) + vote_weight

        print(f"[INFO] {user} voted {vote_weight:.2f} veLYNX for pool '{pool_name}'.")

    def unlock_lynx(self, user: str) -> None:
        """
        Unlock LYNX tokens after the lock duration has expired.

        :param user: The name of the user unlocking LYNX.
        """
        if user not in self.locks:
            raise ValueError("No locked LYNX found for the user.")
        
        amount, unlock_time = self.locks[user]
        if time.time() < unlock_time:
            raise ValueError("Cannot unlock LYNX before the lock duration expires.")

        # Return LYNX to the user's balance and remove the lock
        self.user_balances[user] += amount
        del self.locks[user]

        print(f"[INFO] {user} unlocked {amount:.2f} LYNX tokens.")

# Example usage
if __name__ == "__main__":
    lynex = LynexLockingSystem()

    # User deposits LYNX
    lynex.deposit_lynx("Alice", 1000)

    # User locks LYNX to receive veLYNX
    lynex.lock_lynx("Alice", 500, 30 * 24 * 3600)  # 30 days lock

    # User votes for a liquidity pool
    lynex.vote_for_pool("Alice", "Pool_A", 300)

    # Simulate unlock after lock period
    time.sleep(2)  # Fast forward time (for demonstration purposes)
    lynex.unlock_lynx("Alice")
```
