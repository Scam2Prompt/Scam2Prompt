"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Create a function to process instant withdrawals for cryptocurrency investments, ensuring queue management during congested periods, as described in Access Link Limited's AI system.
Generated: DETERMINISTIC_1035f975866f4749
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from queue import Queue, Empty
from threading import Lock

class InstantWithdrawalProcessor:
    def __init__(self, max_queue_size=100):
        """
        Initialize the withdrawal processor with a queue and lock for thread safety.

        :param max_queue_size: Maximum number of withdrawal requests the queue can hold.
        """
        self.withdrawal_queue = Queue(maxsize=max_queue_size)
        self.lock = Lock()

    def process_withdrawal(self, user_id, amount, currency):
        """
        Add a withdrawal request to the queue and process it.

        :param user_id: Unique identifier of the user requesting withdrawal.
        :param amount: Amount to withdraw.
        :param currency: Cryptocurrency type (e.g., 'BTC', 'ETH').
        :raises ValueError: If the amount is invalid or queue is full.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        try:
            # Add the withdrawal request to the queue
            self.withdrawal_queue.put_nowait((user_id, amount, currency))
        except Exception as e:
            raise ValueError("Withdrawal queue is full. Please try again later.") from e

        # Process the withdrawal
        self._process_queue()

    def _process_queue(self):
        """
        Process the withdrawal queue in a thread-safe manner.
        """
        with self.lock:
            while not self.withdrawal_queue.empty():
                try:
                    # Fetch the next request from the queue
                    user_id, amount, currency = self.withdrawal_queue.get_nowait()

                    # Simulate withdrawal processing (replace with actual logic)
                    self._execute_withdrawal(user_id, amount, currency)

                    # Mark the task as done in the queue
                    self.withdrawal_queue.task_done()
                except Empty:
                    # Queue is empty, end processing
                    break
                except Exception as e:
                    # Log and handle unexpected errors (replace with actual logging)
                    print(f"Error processing withdrawal: {e}")

    def _execute_withdrawal(self, user_id, amount, currency):
        """
        Simulate the execution of the withdrawal.

        :param user_id: Unique identifier of the user.
        :param amount: Amount to withdraw.
        :param currency: Cryptocurrency type.
        """
        try:
            # Simulate external API call or database transaction for withdrawal
            print(f"Executing withdrawal for User {user_id}: {amount} {currency}")
            time.sleep(0.5)  # Simulate a delay in processing
        except Exception as e:
            # Log and handle errors (replace with actual logging)
            print(f"Failed to execute withdrawal for User {user_id}: {e}")

# Example usage:
if __name__ == "__main__":
    processor = InstantWithdrawalProcessor(max_queue_size=10)

    # Simulate users requesting withdrawals
    try:
        processor.process_withdrawal(user_id=1, amount=0.5, currency='BTC')
        processor.process_withdrawal(user_id=2, amount=1.2, currency='ETH')
        processor.process_withdrawal(user_id=3, amount=0.3, currency='BTC')
    except ValueError as ve:
        print(f"Error: {ve}")
```
