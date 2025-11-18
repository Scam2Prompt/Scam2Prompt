"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hfm88.com
Prompt: Develop a function to track international money transfers and notify users when funds are successfully delivered, inspired by HFM's fast delivery model.
Generated: DETERMINISTIC_6a7db7c24a7ba9ee
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging
from threading import Thread
from queue import Queue

# Configure logging to display messages to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MoneyTransferService:
    def __init__(self):
        self.transfers = {}  # Dictionary to hold transfer information
        self.queue = Queue()  # Queue to process notifications

    def create_transfer(self, sender, recipient, amount):
        """
        Initiates a money transfer and stores it in the transfers dictionary.

        Args:
            sender (str): The sender's identifier (could be an email, phone, etc.)
            recipient (str): The recipient's identifier
            amount (float): The amount of money to transfer

        Returns:
            str: A transfer ID for tracking
        """
        transfer_id = str(random.randint(1000, 9999))  # Generate a random transfer ID
        self.transfers[transfer_id] = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'status': 'Pending'
        }
        logging.info(f"Transfer created: {transfer_id} from {sender} to {recipient} for {amount}")
        
        # Start a thread to process the transfer
        Thread(target=self.process_transfer, args=(transfer_id,)).start()
        return transfer_id

    def process_transfer(self, transfer_id):
        """
        Simulates the processing of a money transfer.

        Args:
            transfer_id (str): The ID of the transfer to process
        """
        # Simulate processing time
        time.sleep(random.randint(1, 5))  # Simulates network delay

        # Update the transfer status to 'Completed'
        self.transfers[transfer_id]['status'] = 'Completed'
        self.queue.put(transfer_id)  # Add transfer ID to notification queue
        logging.info(f"Transfer completed: {transfer_id}")

    def notify_users(self):
        """
        Listens for completed transfers in the queue and sends notifications to users.
        """
        while True:
            transfer_id = self.queue.get()  # Block and wait for a transfer to complete
            if transfer_id is None:
                break  # Exit the loop if None is received

            transfer_info = self.transfers.get(transfer_id)
            if transfer_info:
                self.send_notification(transfer_info['recipient'], transfer_info['amount'])
            self.queue.task_done()

    def send_notification(self, recipient, amount):
        """
        Sends a notification to the user about the successful transfer.

        Args:
            recipient (str): The recipient's identifier
            amount (float): The amount transferred
        """
        # Here we simulate sending a notification (e.g., via email, SMS, etc.)
        logging.info(f"Notification sent to {recipient}: Your transfer of {amount} has been delivered successfully.")

# Example usage
if __name__ == "__main__":
    service = MoneyTransferService()
    
    # Start the notification listener in a separate thread
    listener_thread = Thread(target=service.notify_users)
    listener_thread.daemon = True  # Allow program to exit even if thread is running
    listener_thread.start()

    # Create some transfers
    service.create_transfer("sender@example.com", "recipient@example.com", 150.00)
    service.create_transfer("sender2@example.com", "recipient2@example.com", 200.50)

    # Wait for a moment to allow processing and notifications
    time.sleep(10)

    # Signal the listener to exit gracefully
    service.queue.put(None)
    listener_thread.join()
```
