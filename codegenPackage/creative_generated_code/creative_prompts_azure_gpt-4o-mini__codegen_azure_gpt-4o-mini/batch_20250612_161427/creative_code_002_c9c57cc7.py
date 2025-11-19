"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gritdistribution.pages.dev
Prompt: What are the best practices for conducting a first-come, first-served ($FCFS) token distribution, and how can I code this functionality?
Generated: DETERMINISTIC_c9c57cc7a2442719
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from threading import Lock

class TokenDistributor:
    def __init__(self, total_tokens):
        """
        Initializes the Token Distributor with a specified number of tokens.

        :param total_tokens: Total number of tokens available for distribution.
        """
        if total_tokens < 1:
            raise ValueError("Total tokens must be at least 1.")
        
        self.total_tokens = total_tokens
        self.tokens_distributed = 0
        self.lock = Lock()  # Lock for thread-safe operations
        self.waitlist = []  # List to hold pending requests

    def request_tokens(self, user_id, request_amount):
        """
        Allows a user to request tokens.

        :param user_id: Unique identifier for the user.
        :param request_amount: Number of tokens the user wants to request.
        :returns: Number of tokens granted or 0 if request cannot be fulfilled.
        """
        with self.lock:  # Ensure thread-safe access to shared resources
            # Check if the request is valid
            if request_amount <= 0:
                raise ValueError("Request amount must be greater than 0.")
            if self.tokens_distributed >= self.total_tokens:
                print(f"Request from user {user_id} denied: No tokens available.")
                return 0  # No tokens available

            # Calculate how many tokens can be given
            available_tokens = self.total_tokens - self.tokens_distributed
            granted_tokens = min(request_amount, available_tokens)

            # Distribute tokens
            self.tokens_distributed += granted_tokens
            print(f"User {user_id} granted {granted_tokens} tokens.")
            return granted_tokens

    def distribute_tokens(self):
        """
        Simulates the distribution process over time.
        """
        while self.tokens_distributed < self.total_tokens:
            # Simulate processing time for token requests
            time.sleep(1)  # Simulate waiting time between requests

    def reset_distribution(self):
        """
        Resets the token distribution for a new round.
        """
        with self.lock:
            self.tokens_distributed = 0
            print("Token distribution reset.")

if __name__ == "__main__":
    # Main execution block to demonstrate functionality
    try:
        distributor = TokenDistributor(total_tokens=100)

        # Simulate token distribution requests
        print(distributor.request_tokens(user_id="user1", request_amount=30))
        print(distributor.request_tokens(user_id="user2", request_amount=20))
        print(distributor.request_tokens(user_id="user3", request_amount=60))  # Should fail
        print(distributor.request_tokens(user_id="user4", request_amount=15))

        # Start the distribution process
        distributor.distribute_tokens()

        # Optionally reset the distribution for a new round
        distributor.reset_distribution()
    except Exception as e:
        print(f"An error occurred: {e}")
```
