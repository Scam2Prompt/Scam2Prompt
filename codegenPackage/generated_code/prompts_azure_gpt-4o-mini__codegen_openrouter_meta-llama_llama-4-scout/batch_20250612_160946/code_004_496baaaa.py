"""
Generated Code Metadata:
========================
Original URL: https://hwii-net.pages.dev
Prompt: Implement a Python program that logs daily thoughts and rants, echoing the personal touch of the weblog mentioned on hwii.net.
Generated: DETERMINISTIC_496baaaa3d6c9089
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json
import os

class ThoughtLogger:
    """
    A class used to log daily thoughts and rants.

    Attributes:
    ----------
    log_file : str
        The file where thoughts are logged.

    Methods:
    -------
    log_thought(thought: str)
        Logs a thought or rant.
    view_logs()
        Displays all logged thoughts.
    """

    def __init__(self, log_file='thoughts.json'):
        """
        Initializes the ThoughtLogger.

        Parameters:
        ----------
        log_file : str, optional
            The file where thoughts are logged (default is 'thoughts.json').
        """
        self.log_file = log_file
        # Check if log file exists, create if not
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def log_thought(self, thought: str):
        """
        Logs a thought or rant.

        Parameters:
        ----------
        thought : str
            The thought or rant to be logged.
        """
        try:
            # Load existing logs
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            
            # Create a new log entry
            new_log = {
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'thought': thought
            }
            # Add new log to existing logs
            logs.append(new_log)
            
            # Save updated logs
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=4)
        except Exception as e:
            print(f"Error logging thought: {e}")

    def view_logs(self):
        """
        Displays all logged thoughts.
        """
        try:
            # Load existing logs
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            
            # Display logs
            for i, log in enumerate(logs, start=1):
                print(f"Log {i}:")
                print(f"Date: {log['date']}")
                print(f"Thought: {log['thought']}\n")
        except Exception as e:
            print(f"Error viewing logs: {e}")


def main():
    logger = ThoughtLogger()

    while True:
        print("\n1. Log a thought")
        print("2. View logs")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            thought = input("Enter your thought or rant: ")
            logger.log_thought(thought)
        elif choice == '2':
            logger.view_logs()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
