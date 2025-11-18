"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-pepe.xyz
Prompt: Generate code for a weekly giveaway system that distributes 1,000,000 $BPEP tokens to active community members, as described in Bitcoin Pepe's campaign.
Generated: DETERMINISTIC_aea8b4f4aaef5047
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class GiveawaySystem:
    """
    A class to represent a weekly giveaway system for distributing $BPEP tokens.
    """

    def __init__(self, total_tokens: int, active_members: List[str]):
        """
        Initializes the GiveawaySystem with the total tokens and active community members.

        Args:
            total_tokens (int): The total number of tokens to distribute.
            active_members (List[str]): A list of active community member IDs.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        
        if not active_members:
            raise ValueError("Active members list cannot be empty.")
        
        self.total_tokens = total_tokens
        self.active_members = active_members

    def distribute_tokens(self) -> Dict[str, int]:
        """
        Distributes the total tokens randomly among active community members.

        Returns:
            Dict[str, int]: A dictionary mapping member IDs to the number of tokens they received.
        """
        tokens_distribution = {member: 0 for member in self.active_members}
        remaining_tokens = self.total_tokens
        
        # Randomly distribute tokens until all tokens are allocated
        while remaining_tokens > 0:
            # Choose a random active member
            member = random.choice(self.active_members)
            # Randomly assign tokens to the chosen member
            tokens_to_assign = random.randint(1, remaining_tokens)
            tokens_distribution[member] += tokens_to_assign
            remaining_tokens -= tokens_to_assign
        
        return tokens_distribution

def main():
    """
    Main function to execute the giveaway system.
    """
    # Constants
    TOTAL_TOKENS = 1_000_000
    ACTIVE_MEMBERS = ["member1", "member2", "member3", "member4", "member5"]

    try:
        # Create a GiveawaySystem instance
        giveaway = GiveawaySystem(TOTAL_TOKENS, ACTIVE_MEMBERS)

        # Distribute tokens and print the results
        distribution = giveaway.distribute_tokens()
        for member, tokens in distribution.items():
            print(f"{member} received {tokens} $BPEP tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
