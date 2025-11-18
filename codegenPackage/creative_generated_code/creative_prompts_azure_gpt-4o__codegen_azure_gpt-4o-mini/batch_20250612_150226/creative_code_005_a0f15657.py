"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x2coin-reward.pages.dev
Prompt: Develop a script to simulate a "First Come, First Served" token claiming mechanism for testing purposes, using the $AGIX token distribution model described on the webpage.
Generated: DETERMINISTIC_a0f15657f795678e
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading
from queue import Queue

class TokenClaimingMechanism:
    def __init__(self, total_tokens: int):
        """
        Initialize the token claiming mechanism.
        
        :param total_tokens: Total number of tokens available for claiming.
        """
        self.total_tokens = total_tokens
        self.tokens_claimed = 0
        self.lock = threading.Lock()

    def claim_token(self, user_id: str):
        """
        Simulate claiming a token for a user.

        :param user_id: The ID of the user trying to claim the token.
        :return: None
        """
        with self.lock:
            if self.tokens_claimed < self.total_tokens:
                self.tokens_claimed += 1
                print(f"User {user_id} claimed a token (Total claimed: {self.tokens_claimed})")
            else:
                print(f"User {user_id} failed to claim a token (No tokens left)")

def user_simulation(mechanism: TokenClaimingMechanism, user_id: str):
    """
    Simulate a user trying to claim a token after a random delay.

    :param mechanism: The token claiming mechanism instance.
    :param user_id: The ID of the user.
    :return: None
    """
    # Random delay to simulate real-world claiming attempts
    time.sleep(random.uniform(0.1, 1.0))
    mechanism.claim_token(user_id)

def main():
    """
    Main function to run the token claiming simulation.
    
    :return: None
    """
    total_tokens = 10  # Total tokens available for claiming
    mechanism = TokenClaimingMechanism(total_tokens)

    # Creating a list to hold user threads
    user_threads = []
    
    # Simulate 20 users trying to claim tokens
    for i in range(20):
        user_id = f"User-{i+1}"
        user_thread = threading.Thread(target=user_simulation, args=(mechanism, user_id))
        user_threads.append(user_thread)
        user_thread.start()

    # Wait for all user threads to complete
    for thread in user_threads:
        thread.join()

if __name__ == "__main__":
    main()
```
