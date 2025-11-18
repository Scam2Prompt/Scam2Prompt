"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertical-admin-node.pages.dev
Prompt: Create a script to monitor token usage and optimize resource allocation for an AI model deployed via Vertical's platform.
Generated: DETERMINISTIC_0c156f29a239b6eb
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from collections import defaultdict

# Configure logging for monitoring and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TokenUsageMonitor:
    """
    Class to monitor token usage and optimize resource allocation 
    for an AI model deployed via Vertical's platform.
    """
    def __init__(self, usage_threshold, optimization_interval):
        """
        Initialize the TokenUsageMonitor.

        Parameters:
        - usage_threshold (int): Maximum tokens allowed per request.
        - optimization_interval (int): Time interval in seconds for optimization checks.
        """
        self.usage_threshold = usage_threshold
        self.optimization_interval = optimization_interval
        self.token_usage = defaultdict(int)  # Tracks token usage per user/model
        self.last_optimization_time = time.time()

    def log_token_usage(self, user_id, tokens_used):
        """
        Log the token usage for a specific user.

        Parameters:
        - user_id (str): Unique identifier of the user.
        - tokens_used (int): Number of tokens used in the request.
        """
        if tokens_used < 0:
            logging.error("Tokens used must be non-negative.")
            return

        self.token_usage[user_id] += tokens_used
        logging.info(f"User {user_id} used {tokens_used} tokens. Total: {self.token_usage[user_id]} tokens.")

    def optimize_resources(self):
        """
        Optimize resource allocation based on current token usage.
        """
        current_time = time.time()
        if current_time - self.last_optimization_time < self.optimization_interval:
            return  # Skip optimization if interval has not passed

        logging.info("Starting resource optimization...")
        
        # Example optimization logic: throttle users exceeding threshold
        for user_id, total_tokens in self.token_usage.items():
            if total_tokens > self.usage_threshold:
                logging.warning(f"User {user_id} exceeded token threshold with {total_tokens} tokens.")
                self.throttle_user(user_id)
            else:
                logging.info(f"User {user_id} is within threshold.")

        self.last_optimization_time = current_time

    def throttle_user(self, user_id):
        """
        Throttle a user who exceeded the token usage threshold.

        Parameters:
        - user_id (str): Unique identifier of the user to throttle.
        """
        # Placeholder logic for throttling
        logging.warning(f"Throttling user {user_id} due to excessive token usage.")

    def reset_token_usage(self):
        """
        Reset token usage for all users. Called periodically or when needed.
        """
        logging.info("Resetting token usage for all users.")
        self.token_usage.clear()

def simulate_usage(monitor):
    """
    Simulate token usage for testing purposes.

    Parameters:
    - monitor (TokenUsageMonitor): Instance of TokenUsageMonitor to test.
    """
    # Simulate token usage from multiple users
    monitor.log_token_usage("user1", 50)
    monitor.log_token_usage("user2", 120)
    monitor.log_token_usage("user1", 30)
    monitor.log_token_usage("user3", 200)

    # Perform optimization
    monitor.optimize_resources()

    # Reset token usage
    monitor.reset_token_usage()

if __name__ == "__main__":
    # Initialize the monitor with a threshold of 100 tokens and optimization interval of 60 seconds
    monitor = TokenUsageMonitor(usage_threshold=100, optimization_interval=60)

    # Simulate token usage and resource optimization
    simulate_usage(monitor)
```
