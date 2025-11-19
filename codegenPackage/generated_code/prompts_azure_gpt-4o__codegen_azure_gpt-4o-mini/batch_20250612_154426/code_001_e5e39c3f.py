"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Generate a script to simulate identity theft detection and prevention mechanisms, incorporating features mentioned in Genesis Investment Credit Union's "Cyberscout" resources.
Generated: DETERMINISTIC_e5e39c3f4ee29d0c
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IdentityTheftDetector:
    def __init__(self):
        self.suspicious_activity_threshold = 5  # Number of suspicious activities to trigger an alert
        self.suspicious_activities = []
        self.user_data = {}  # Store user data for simulation

    def generate_fake_user_data(self, user_id):
        """Generate fake user data for simulation."""
        self.user_data[user_id] = {
            'name': f'User{user_id}',
            'email': f'user{user_id}@example.com',
            'transactions': []
        }

    def log_transaction(self, user_id, amount):
        """Log a transaction for a user."""
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} not found.")
            return
        
        transaction = {
            'amount': amount,
            'timestamp': datetime.now()
        }
        self.user_data[user_id]['transactions'].append(transaction)
        logging.info(f"Transaction logged for {user_id}: {transaction}")

    def detect_suspicious_activity(self, user_id):
        """Detect suspicious activity based on transaction patterns."""
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} not found.")
            return
        
        transactions = self.user_data[user_id]['transactions']
        if len(transactions) < self.suspicious_activity_threshold:
            return  # Not enough data to determine suspicious activity

        # Check for rapid transactions
        recent_transactions = [t for t in transactions if t['timestamp'] > datetime.now() - timedelta(minutes=5)]
        if len(recent_transactions) >= self.suspicious_activity_threshold:
            self.suspicious_activities.append(user_id)
            logging.warning(f"Suspicious activity detected for {user_id}: {len(recent_transactions)} transactions in the last 5 minutes.")

    def alert_user(self, user_id):
        """Send an alert to the user about suspicious activity."""
        if user_id not in self.user_data:
            logging.error(f"User ID {user_id} not found.")
            return
        
        logging.info(f"Alert sent to {self.user_data[user_id]['email']} regarding suspicious activity.")

    def simulate_activity(self, user_id):
        """Simulate user activity for testing purposes."""
        self.generate_fake_user_data(user_id)
        
        # Simulate random transactions
        for _ in range(random.randint(1, 10)):
            amount = random.uniform(10, 500)  # Random transaction amount
            self.log_transaction(user_id, amount)
            self.detect_suspicious_activity(user_id)

        # If suspicious activity detected, alert the user
        if user_id in self.suspicious_activities:
            self.alert_user(user_id)

if __name__ == "__main__":
    detector = IdentityTheftDetector()
    
    # Simulate activity for multiple users
    for user_id in range(1, 6):
        detector.simulate_activity(user_id)
```
