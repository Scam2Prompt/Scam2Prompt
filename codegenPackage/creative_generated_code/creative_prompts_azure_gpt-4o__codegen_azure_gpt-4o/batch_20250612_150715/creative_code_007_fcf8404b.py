"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notcoin-46x.pages.dev
Prompt: Provide an example of code to simulate a "first to claim, first to receive" logic for $NOT vouchers using the Notcoin airdrop system.
Generated: DETERMINISTIC_fcf8404bef543ac8
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading

class NotcoinAirdrop:
    def __init__(self, total_vouchers):
        """
        Initialize the Notcoin Airdrop system.

        Args:
            total_vouchers (int): The total number of $NOT vouchers available for claiming.
        """
        self.vouchers = total_vouchers
        self.lock = threading.Lock()

    def claim_voucher(self, user_id):
        """
        Simulate the claiming of a $NOT voucher by a user.

        Args:
            user_id (str): The ID of the user attempting to claim a voucher.

        Returns:
            str: A message indicating whether the claim was successful or not.
        """
        with self.lock:  # Ensure thread-safe access to vouchers
            if self.vouchers > 0:
                self.vouchers -= 1
                return f"Success: User {user_id} claimed a voucher! Remaining vouchers: {self.vouchers}"
            else:
                return f"Failed: User {user_id} tried to claim a voucher, but none are left."

def simulate_airdrop():
    """
    Simulates the first-to-claim $NOT voucher airdrop process with multiple users.
    """
    # Initialize the airdrop system with 5 vouchers
    airdrop = NotcoinAirdrop(total_vouchers=5)

    # List of users attempting to claim vouchers
    users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7"]

    # Function for each user to attempt to claim a voucher
    def user_attempt(user_id):
        print(airdrop.claim_voucher(user_id))

    # Create threads for each user
    threads = [threading.Thread(target=user_attempt, args=(user,)) for user in users]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Run the airdrop simulation
    simulate_airdrop()
```
