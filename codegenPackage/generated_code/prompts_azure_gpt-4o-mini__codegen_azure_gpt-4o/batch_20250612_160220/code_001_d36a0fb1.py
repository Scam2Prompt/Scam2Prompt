"""
Generated Code Metadata:
========================
Original URL: https://clais.pages.dev
Prompt: Write a code snippet to create a first-come, first-served airdrop claim system similar to the one described for $BROCK.
Generated: DETERMINISTIC_d36a0fb1610b5b4f
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from threading import Lock

class AirdropSystem:
    """
    AirdropSystem: A first-come, first-served airdrop claim system.
    """

    def __init__(self, total_tokens, max_claim_per_user):
        """
        Initialize the airdrop system.

        :param total_tokens: Total tokens available for the airdrop.
        :param max_claim_per_user: Maximum tokens a single user can claim.
        """
        self.total_tokens = total_tokens
        self.max_claim_per_user = max_claim_per_user
        self.claimed_tokens = 0
        self.lock = Lock()  # Thread-safe lock for concurrent access
        self.claimed_users = set()  # Track users who have already claimed

    def claim_tokens(self, user_id):
        """
        Allow a user to claim tokens if tokens are still available.

        :param user_id: Unique identifier for the user.
        :return: A message indicating the claim status.
        """
        with self.lock:  # Ensure thread-safe access
            # Check if the user has already claimed
            if user_id in self.claimed_users:
                return f"User {user_id} has already claimed tokens."

            # Check if there are enough tokens left for the claim
            if self.claimed_tokens + self.max_claim_per_user > self.total_tokens:
                return "Airdrop has ended. No tokens left to claim."

            # Process the claim
            self.claimed_tokens += self.max_claim_per_user
            self.claimed_users.add(user_id)
            return f"User {user_id} successfully claimed {self.max_claim_per_user} tokens."

    def get_remaining_tokens(self):
        """
        Get the number of remaining tokens in the airdrop.

        :return: Number of remaining tokens.
        """
        with self.lock:
            return self.total_tokens - self.claimed_tokens


# Example usage
if __name__ == "__main__":
    # Initialize the airdrop system with 100 tokens and a max claim of 10 tokens per user
    airdrop = AirdropSystem(total_tokens=100, max_claim_per_user=10)

    # Simulate users claiming tokens
    print(airdrop.claim_tokens("user1"))  # User 1 claims tokens
    print(airdrop.claim_tokens("user2"))  # User 2 claims tokens
    print(airdrop.claim_tokens("user1"))  # User 1 tries to claim again
    print(f"Remaining tokens: {airdrop.get_remaining_tokens()}")  # Check remaining tokens
```
