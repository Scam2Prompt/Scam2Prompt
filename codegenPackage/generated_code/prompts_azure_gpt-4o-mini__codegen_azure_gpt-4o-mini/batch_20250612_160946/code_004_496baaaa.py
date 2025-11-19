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
import os
from datetime import datetime

class DailyLogger:
    """A class to log daily thoughts and rants to a text file."""

    def __init__(self, log_file='daily_log.txt'):
        """
        Initializes the DailyLogger with a specified log file.

        Args:
            log_file (str): The name of the file where logs will be stored.
        """
        self.log_file = log_file
        self.ensure_log_file_exists()

    def ensure_log_file_exists(self):
        """Checks if the log file exists; if not, creates it."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("Daily Thoughts and Rants Log\n")
                f.write("=" * 40 + "\n")

    def log_thought(self, thought):
        """
        Logs a thought or rant to the log file with a timestamp.

        Args:
            thought (str): The thought or rant to log.
        """
        if not thought:
            raise ValueError("Thought cannot be empty.")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - {thought}\n"

        try:
            with open(self.log_file, 'a') as f:
                f.write(entry)
        except IOError as e:
            print(f"Error writing to log file: {e}")

    def read_logs(self):
        """Reads and returns the contents of the log file."""
        try:
            with open(self.log_file, 'r') as f:
                return f.read()
        except IOError as e:
            print(f"Error reading log file: {e}")
            return None

def main():
    """Main function to run the DailyLogger."""
    logger = DailyLogger()

    while True:
        user_input = input("Enter your thought or rant (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the logger. Goodbye!")
            break
        try:
            logger.log_thought(user_input)
            print("Your thought has been logged.")
        except ValueError as ve:
            print(ve)

    # Optionally, read and display all logs at the end
    print("\nHere are all your logged thoughts and rants:")
    logs = logger.read_logs()
    if logs:
        print(logs)

if __name__ == "__main__":
    main()
```
