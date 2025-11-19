"""
Generated Code Metadata:
========================
Original URL: https://thegraph-the-graph.org
Prompt: "Design a system for incentivizing network participants in a decentralized data indexing protocol using a native token like GRT."
Generated: DETERMINISTIC_dc0c63188eea7ee5
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import time
from typing import Dict, List

# Define constants
INITIAL_SUPPLY = 1_000_000  # Initial token supply
REWARD_RATE = 0.01          # Reward rate per block (1%)
BLOCK_TIME = 10             # Time per block in seconds

# Define custom exceptions
class InsufficientBalanceError(Exception):
    """Raised when a participant tries to withdraw more tokens than available."""
    pass

class InvalidParticipantError(Exception):
    """Raised when an operation is attempted on a non-existent participant."""
    pass

# Token class to manage balances and transfers
class Token:
    def __init__(self, initial_supply: int):
        self.total_supply = initial_supply
        self.balances: Dict[str, float] = {}  # Participant balances

    def mint(self, participant: str, amount: float):
        """Mint new tokens to a participant."""
        self.total_supply += amount
        self.balances[participant] = self.balances.get(participant, 0) + amount

    def transfer(self, sender: str, receiver: str, amount: float):
        """Transfer tokens between participants."""
        if sender not in self.balances or self.balances[sender] < amount:
            raise InsufficientBalanceError("Sender has insufficient balance.")
        if receiver not in self.balances:
            raise InvalidParticipantError("Receiver does not exist.")
        
        self.balances[sender] -= amount
        self.balances[receiver] = self.balances.get(receiver, 0) + amount

    def get_balance(self, participant: str) -> float:
        """Get the balance of a participant."""
        return self.balances.get(participant, 0)

# Incentive system class
class IncentiveSystem:
    def __init__(self, token: Token):
        self.token = token
        self.participants: List[str] = []  # List of participants
        self.last_reward_time = time.time()

    def add_participant(self, participant: str):
        """Add a new participant to the system."""
        if participant not in self.participants:
            self.participants.append(participant)
            self.token.balances[participant] = 0  # Initialize balance

    def remove_participant(self, participant: str):
        """Remove a participant from the system."""
        if participant in self.participants:
            self.participants.remove(participant)
            self.token.balances.pop(participant, None)

    def distribute_rewards(self):
        """Distribute rewards to participants based on the reward rate."""
        current_time = time.time()
        elapsed_blocks = int((current_time - self.last_reward_time) / BLOCK_TIME)
        if elapsed_blocks > 0:
            reward_per_participant = REWARD_RATE * elapsed_blocks
            for participant in self.participants:
                self.token.mint(participant, reward_per_participant)
            self.last_reward_time = current_time

    def get_participant_balance(self, participant: str) -> float:
        """Get the balance of a participant."""
        if participant not in self.participants:
            raise InvalidParticipantError("Participant does not exist.")
        return self.token.get_balance(participant)

# Example usage
if __name__ == "__main__":
    # Initialize the token and incentive system
    token = Token(INITIAL_SUPPLY)
    incentive_system = IncentiveSystem(token)

    # Add participants
    incentive_system.add_participant("Alice")
    incentive_system.add_participant("Bob")

    # Simulate reward distribution
    time.sleep(15)  # Wait for some blocks to pass
    incentive_system.distribute_rewards()

    # Check balances
    print("Alice's balance:", incentive_system.get_participant_balance("Alice"))
    print("Bob's balance:", incentive_system.get_participant_balance("Bob"))

    # Transfer tokens
    token.transfer("Alice", "Bob", 5)
    print("Alice's balance after transfer:", incentive_system.get_participant_balance("Alice"))
    print("Bob's balance after transfer:", incentive_system.get_participant_balance("Bob"))
```
