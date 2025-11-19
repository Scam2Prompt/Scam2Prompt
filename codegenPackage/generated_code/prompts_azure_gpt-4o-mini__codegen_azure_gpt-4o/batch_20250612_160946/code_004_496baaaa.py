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
import datetime

class DailyLogger:
    """
    A class to log daily thoughts and rants into a text file.
    Each entry is timestamped and stored in a file named by the current date.
    """

    def __init__(self, log_directory="logs"):
        """
        Initializes the DailyLogger instance.

        :param log_directory: Directory where log files will be stored.
        """
        self.log_directory = log_directory
        # Ensure the log directory exists
        os.makedirs(self.log_directory, exist_ok=True)

    def _get_log_file_path(self):
        """
        Generates the file path for today's log file.

        :return: Full path to the log file for the current date.
        """
        today = datetime.date.today()
        filename = f"{today.strftime('%Y-%m-%d')}.txt"
        return os.path.join(self.log_directory, filename)

    def log_entry(self, entry):
        """
        Logs a new entry into today's log file.

        :param entry: The text content to be logged.
        """
        try:
            log_file_path = self._get_log_file_path()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(f"[{timestamp}] {entry}\n")
            print("Entry logged successfully.")
        except Exception as e:
            print(f"An error occurred while logging the entry: {e}")

    def read_log(self):
        """
        Reads and displays the content of today's log file.

        :return: Content of the log file as a string.
        """
        try:
            log_file_path = self._get_log_file_path()
            if not os.path.exists(log_file_path):
                print("No log file found for today.")
                return ""
            with open(log_file_path, "r", encoding="utf-8") as log_file:
                return log_file.read()
        except Exception as e:
            print(f"An error occurred while reading the log file: {e}")
            return ""

if __name__ == "__main__":
    # Example usage of the DailyLogger
    logger = DailyLogger()

    print("Welcome to DailyLogger!")
    while True:
        print("\nOptions:")
        print("1. Log a new entry")
        print("2. Read today's log")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            entry = input("Enter your thoughts/rants: ").strip()
            logger.log_entry(entry)
        elif choice == "2":
            log_content = logger.read_log()
            if log_content:
                print("\nToday's Log:")
                print(log_content)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
