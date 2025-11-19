"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Write a function in Python to track and log the frequency of 1-minute training sessions for a dog, ensuring consistency as emphasized by the "1 Minute Dog Training" method.
Generated: DETERMINISTIC_51cdf1d458e1defd
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import datetime
import json
import os

# Set up logging configuration
logging.basicConfig(filename='dog_training.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DogTrainingTracker:
    def __init__(self, log_file='dog_training.json'):
        """
        Initialize the DogTrainingTracker with a log file.

        Args:
            log_file (str): The file path to store the training log.
        """
        self.log_file = log_file
        self.training_log = self.load_log()

    def load_log(self):
        """
        Load the existing training log from the log file.

        Returns:
            dict: A dictionary containing the training log.
        """
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_log(self):
        """
        Save the training log to the log file.
        """
        with open(self.log_file, 'w') as f:
            json.dump(self.training_log, f, indent=4)

    def log_session(self, date=None, session_duration=1):
        """
        Log a 1-minute training session for a dog.

        Args:
            date (str): The date of the training session (YYYY-MM-DD). Defaults to today.
            session_duration (int): The duration of the training session in minutes. Defaults to 1.

        Raises:
            ValueError: If the session duration is not 1 minute.
        """
        if session_duration != 1:
            raise ValueError("Session duration must be 1 minute")

        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')

        if date not in self.training_log:
            self.training_log[date] = []

        self.training_log[date].append(datetime.datetime.now().strftime('%H:%M'))
        self.save_log()

        logging.info(f"Logged 1-minute training session on {date} at {datetime.datetime.now().strftime('%H:%M')}")

    def get_session_frequency(self, date=None):
        """
        Get the frequency of training sessions for a dog on a specific date.

        Args:
            date (str): The date to retrieve the session frequency for (YYYY-MM-DD). Defaults to today.

        Returns:
            int: The number of training sessions on the specified date.
        """
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')

        if date in self.training_log:
            return len(self.training_log[date])
        else:
            return 0


def main():
    tracker = DogTrainingTracker()

    while True:
        print("\n1. Log a training session")
        print("2. Get session frequency")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                tracker.log_session()
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            date = input("Enter a date (YYYY-MM-DD), or leave blank for today: ")
            if date.strip() == "":
                date = None
            print(f"Session frequency on {date or 'today'}: {tracker.get_session_frequency(date)}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
