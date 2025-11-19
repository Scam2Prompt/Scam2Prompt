"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clais.pages.dev
Prompt: Write a code snippet to create a first-come, first-served airdrop claim system similar to the one described for $BROCK.
Generated: DETERMINISTIC_d36a0fb1610b5b4f
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time

class AirdropSystem:
    def __init__(self, token_amount, max_claims):
        """
        Initialize the airdrop system.

        Args:
            token_amount (int): Total tokens available for airdrop.
            max_claims (int): Maximum claims allowed.
        """
        self.token_amount = token_amount
        self.max_claims = max_claims
        self.claimed = 0
        self.lock = threading.Lock()  # To ensure thread-safe operations.
    
    def claim_tokens(self, user_id):
        """
        Allow a user to claim tokens if the airdrop is still available.

        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            str: Success or failure message.
        """
        with self.lock:  # Ensure thread-safe access.
            if self.claimed >= self.max_claims or self.token_amount <= 0:
                return f"Claim failed for User {user_id}: Airdrop ended or tokens exhausted."
            
            self.claimed += 1
            self.token_amount -= 1
            return f"Claim successful for User {user_id}: You received 1 token. Remaining tokens: {self.token_amount}."

    def get_airdrop_status(self):
        """
        Get the current status of the airdrop.

        Returns:
            dict: Airdrop status information.
        """
        with self.lock:
            return {
                "total_tokens": self.token_amount,
                "claimed": self.claimed,
                "remaining_claims": max(0, self.max_claims - self.claimed),
            }

# Example usage:
if __name__ == "__main__":
    # Initialize the airdrop system with 100 tokens and a maximum of 50 claims.
    airdrop = AirdropSystem(token_amount=100, max_claims=50)
    
    def simulate_user_claim(user_id):
        """
        Simulates a user trying to claim tokens.
        """
        result = airdrop.claim_tokens(user_id)
        print(result)
    
    # Simulate airdrop claiming by multiple users using threads.
    threads = []
    for i in range(60):  # Simulate 60 users attempting to claim.
        user_thread = threading.Thread(target=simulate_user_claim, args=(f"User-{i+1}",))
        threads.append(user_thread)
        user_thread.start()
    
    for thread in threads:
        thread.join()

    # Print the final status of the airdrop.
    final_status = airdrop.get_airdrop_status()
    print("Final Airdrop Status:", final_status)
```
