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
import threading
import time
from queue import Queue

class TokenDistributor:
    """
    A class to simulate First Come, First Served token claiming mechanism.
    """
    def __init__(self, total_tokens, token_symbol='AGIX'):
        """
        Initializes the TokenDistributor object.
        
        Args:
            total_tokens (int): Total number of tokens available for distribution.
            token_symbol (str): Symbol of the token being distributed.
        """
        self.total_tokens = total_tokens
        self.token_symbol = token_symbol
        self.claimed_tokens = 0
        self.lock = threading.Lock()  # Ensures thread-safe access to the token counter.

    def claim_token(self, user_id):
        """
        Simulates a single user attempting to claim a token.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            str: Result of the token claim attempt.
        """
        with self.lock:  # Lock ensures only one thread can access this section at a time.
            if self.claimed_tokens < self.total_tokens:
                self.claimed_tokens += 1
                return f"User {user_id} successfully claimed 1 {self.token_symbol} token."
            else:
                return f"User {user_id} failed to claim a token. All tokens have been distributed."

def simulate_token_claiming(total_users, total_tokens):
    """
    Simulates the token claiming process for multiple users.
    
    Args:
        total_users (int): Number of users trying to claim tokens.
        total_tokens (int): Total number of tokens available for distribution.
    """
    distributor = TokenDistributor(total_tokens)
    user_queue = Queue()

    # Add user IDs to the queue
    for i in range(1, total_users + 1):
        user_queue.put(f'User-{i}')

    def user_claim():
        """
        Simulates each user attempting to claim a token.
        """
        while not user_queue.empty():
            user_id = user_queue.get()
            result = distributor.claim_token(user_id)
            print(result)
            user_queue.task_done()

    # Spawn multiple threads for concurrent token claiming
    threads = []
    for _ in range(10):  # Number of threads can be adjusted
        t = threading.Thread(target=user_claim)
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    # Configuration for the simulation
    TOTAL_USERS = 100  # Number of users attempting to claim tokens
    TOTAL_TOKENS = 50  # Total tokens to distribute

    print(f"Starting simulation: {TOTAL_USERS} users competing for {TOTAL_TOKENS} tokens.")
    simulate_token_claiming(TOTAL_USERS, TOTAL_TOKENS)
    print("Simulation completed.")
```
