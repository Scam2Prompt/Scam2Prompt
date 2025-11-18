"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Develop a program in Python to track user activity logs, including deposits, withdrawals, and events, based on the structure provided on the webpage.
Generated: DETERMINISTIC_01083d0cb26bc564
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityLog:
    def __init__(self, filename='user_activity_log.json'):
        """
        Initializes the UserActivityLog with a specified filename.
        
        Args:
            filename (str): The name of the file where logs will be stored.
        """
        self.filename = filename
        self.activities = self.load_logs()

    def load_logs(self):
        """
        Loads existing activity logs from the specified JSON file.
        
        Returns:
            list: A list of activity logs.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning("Log file not found or is empty. Starting with an empty log.")
            return []

    def save_logs(self):
        """
        Saves the current activities to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.activities, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving logs: {e}")

    def log_activity(self, action_type, amount=0, description=''):
        """
        Records a new activity in the log.
        
        Args:
            action_type (str): The type of activity (e.g., 'deposit', 'withdrawal', 'event').
            amount (float): The amount associated with deposits or withdrawals.
            description (str): Additional information about the event.
        """
        activity = {
            'timestamp': datetime.now().isoformat(),
            'action_type': action_type,
            'amount': amount,
            'description': description
        }
        self.activities.append(activity)
        self.save_logs()
        logging.info(f"Logged activity: {activity}")

    def get_logs(self):
        """
        Retrieves all logged activities.
        
        Returns:
            list: A list of all logged activities.
        """
        return self.activities

if __name__ == '__main__':
    activity_log = UserActivityLog()
    
    # Sample activity logging
    activity_log.log_activity('deposit', amount=100.0, description='Initial deposit')
    activity_log.log_activity('withdrawal', amount=50.0, description='ATM withdrawal')
    activity_log.log_activity('event', description='User logged in')
    
    # Print all logs
    print(json.dumps(activity_log.get_logs(), indent=4))
```
