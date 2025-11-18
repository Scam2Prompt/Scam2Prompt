"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.projectortechnology.gr
Prompt: Create a program to track and log the usage of interactive kits in an educational setting, referencing the interactive education products offered by Projector Technology.
Generated: DETERMINISTIC_1b4da32dd5c136c7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os


class KitUsageTracker:
    """
    A class to track and log the usage of interactive education kits.
    """

    def __init__(self, log_file="kit_usage_log.json"):
        """
        Initializes the KitUsageTracker instance.

        :param log_file: Path to the log file where usage data will be stored.
        """
        self.log_file = log_file
        self.kits = ["Interactive Projector", "Digital Whiteboard", "AR Learning Kit", "VR Education Kit"]
        
        # Ensure log file exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def log_usage(self, kit_name, user_name):
        """
        Logs the usage of a kit.

        :param kit_name: Name of the kit used.
        :param user_name: Name of the user using the kit.
        """
        if kit_name not in self.kits:
            raise ValueError(f"Invalid kit name: {kit_name}. Available kits are: {', '.join(self.kits)}")

        usage_entry = {
            "kit_name": kit_name,
            "user_name": user_name,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Append the new entry to the log file
        try:
            with open(self.log_file, 'r') as f:
                log_data = json.load(f)

            log_data.append(usage_entry)

            with open(self.log_file, 'w') as f:
                json.dump(log_data, f, indent=4)

            print(f"Usage logged successfully: {usage_entry}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error logging usage: {e}")
            raise

    def get_usage_logs(self):
        """
        Retrieves all usage logs from the log file.

        :return: List of usage logs.
        """
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error retrieving logs: {e}")
            raise

    def display_available_kits(self):
        """
        Displays the list of available kits.
        """
        print("Available kits:")
        for kit in self.kits:
            print(f"- {kit}")


# Main execution flow
if __name__ == "__main__":
    tracker = KitUsageTracker()

    print("Welcome to the Interactive Education Kit Tracker!")
    tracker.display_available_kits()

    while True:
        print("\nChoose an option:")
        print("1. Log kit usage")
        print("2. View usage logs")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                kit_name = input("Enter the name of the kit used: ").strip()
                user_name = input("Enter the name of the user: ").strip()
                tracker.log_usage(kit_name, user_name)
            elif choice == 2:
                logs = tracker.get_usage_logs()
                print("\nUsage Logs:")
                for log in logs:
                    print(log)
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
```
