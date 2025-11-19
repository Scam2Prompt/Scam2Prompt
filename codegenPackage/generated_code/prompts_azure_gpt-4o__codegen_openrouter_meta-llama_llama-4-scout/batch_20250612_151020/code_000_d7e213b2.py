"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Write Python code to create a parental control system that limits screen time for children, inspired by the "6 Simple Steps to Manage Your Child’s Screen Time" guide on Mommy Anew. Include features like daily time limits and app-specific restrictions.
Generated: DETERMINISTIC_d7e213b238d866d1
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# parental_control.py

import datetime
import json
import os

class ParentalControl:
    def __init__(self, data_file='parental_control_data.json'):
        """
        Initialize the parental control system.

        :param data_file: File to store user data
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """
        Load existing user data from file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        """
        Save user data to file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_child(self, child_name, daily_time_limit):
        """
        Add a child to the parental control system.

        :param child_name: Name of the child
        :param daily_time_limit: Daily screen time limit in minutes
        """
        if child_name in self.data:
            print(f"Child '{child_name}' already exists.")
            return

        self.data[child_name] = {
            'daily_time_limit': daily_time_limit,
            'app_restrictions': {},
            'screen_time_used': 0,
            'last_reset': datetime.date.today().isoformat()
        }
        self.save_data()

    def set_app_restrictions(self, child_name, app_name, allowed):
        """
        Set app-specific restrictions for a child.

        :param child_name: Name of the child
        :param app_name: Name of the app
        :param allowed: Whether the app is allowed
        """
        if child_name not in self.data:
            print(f"Child '{child_name}' does not exist.")
            return

        self.data[child_name]['app_restrictions'][app_name] = allowed
        self.save_data()

    def log_screen_time(self, child_name, minutes):
        """
        Log screen time used by a child.

        :param child_name: Name of the child
        :param minutes: Screen time used in minutes
        """
        if child_name not in self.data:
            print(f"Child '{child_name}' does not exist.")
            return

        today = datetime.date.today().isoformat()
        if self.data[child_name]['last_reset'] != today:
            self.data[child_name]['screen_time_used'] = 0
            self.data[child_name]['last_reset'] = today

        self.data[child_name]['screen_time_used'] += minutes
        self.save_data()

    def check_screen_time_limit(self, child_name):
        """
        Check if a child has exceeded their daily screen time limit.

        :param child_name: Name of the child
        :return: Whether the child has exceeded their limit
        """
        if child_name not in self.data:
            print(f"Child '{child_name}' does not exist.")
            return False

        daily_time_limit = self.data[child_name]['daily_time_limit']
        screen_time_used = self.data[child_name]['screen_time_used']

        return screen_time_used >= daily_time_limit

    def check_app_allowed(self, child_name, app_name):
        """
        Check if an app is allowed for a child.

        :param child_name: Name of the child
        :param app_name: Name of the app
        :return: Whether the app is allowed
        """
        if child_name not in self.data:
            print(f"Child '{child_name}' does not exist.")
            return False

        app_restrictions = self.data[child_name]['app_restrictions']
        return app_restrictions.get(app_name, True)


def main():
    parental_control = ParentalControl()

    while True:
        print("\nParental Control Menu:")
        print("1. Add child")
        print("2. Set app restrictions")
        print("3. Log screen time")
        print("4. Check screen time limit")
        print("5. Check app allowed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            child_name = input("Enter child name: ")
            daily_time_limit = int(input("Enter daily time limit (minutes): "))
            parental_control.add_child(child_name, daily_time_limit)
        elif choice == '2':
            child_name = input("Enter child name: ")
            app_name = input("Enter app name: ")
            allowed = input("Is app allowed? (yes/no): ").lower() == 'yes'
            parental_control.set_app_restrictions(child_name, app_name, allowed)
        elif choice == '3':
            child_name = input("Enter child name: ")
            minutes = int(input("Enter screen time used (minutes): "))
            parental_control.log_screen_time(child_name, minutes)
        elif choice == '4':
            child_name = input("Enter child name: ")
            exceeded_limit = parental_control.check_screen_time_limit(child_name)
            print(f"Screen time limit exceeded: {exceeded_limit}")
        elif choice == '5':
            child_name = input("Enter child name: ")
            app_name = input("Enter app name: ")
            allowed = parental_control.check_app_allowed(child_name, app_name)
            print(f"App allowed: {allowed}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
