"""
Generated Code Metadata:
========================
Original URL: https://renzo.protocol-rez.org
Prompt: Write a Python script to track affiliate marketing earnings, including daily and monthly income, using a template similar to the one described on this webpage.
Generated: DETERMINISTIC_736504d2ea3dbc27
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_tracker.py

import datetime
import json
import os

class AffiliateTracker:
    def __init__(self, data_file='affiliate_data.json'):
        """
        Initialize the AffiliateTracker with a data file.

        :param data_file: The file to store affiliate data (default: 'affiliate_data.json')
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """
        Load existing affiliate data from the data file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'daily': {},
                'monthly': {}
            }

    def save_data(self):
        """
        Save affiliate data to the data file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_earnings(self, date=None, amount=0):
        """
        Add earnings for a specific date.

        :param date: The date of earnings (default: today)
        :param amount: The amount of earnings
        """
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')

        if date not in self.data['daily']:
            self.data['daily'][date] = 0

        self.data['daily'][date] += amount

        month_key = date[:7]
        if month_key not in self.data['monthly']:
            self.data['monthly'][month_key] = 0

        self.data['monthly'][month_key] += amount

        self.save_data()

    def get_daily_earnings(self, date=None):
        """
        Get daily earnings for a specific date.

        :param date: The date of earnings (default: today)
        :return: Daily earnings
        """
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')

        return self.data['daily'].get(date, 0)

    def get_monthly_earnings(self, date=None):
        """
        Get monthly earnings for a specific date.

        :param date: The date of earnings (default: today)
        :return: Monthly earnings
        """
        if date is None:
            date = datetime.date.today().strftime('%Y-%m-%d')
        month_key = date[:7]

        return self.data['monthly'].get(month_key, 0)

    def get_all_earnings(self):
        """
        Get all earnings.

        :return: Daily and monthly earnings
        """
        return {
            'daily': self.data['daily'],
            'monthly': self.data['monthly']
        }


def main():
    tracker = AffiliateTracker()

    while True:
        print("\nAffiliate Earnings Tracker")
        print("1. Add earnings")
        print("2. Get daily earnings")
        print("3. Get monthly earnings")
        print("4. Get all earnings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            if date.strip() == '':
                date = None
            else:
                try:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

            try:
                amount = float(input("Enter earnings amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            tracker.add_earnings(date, amount)
            print("Earnings added successfully.")

        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            if date.strip() == '':
                date = None
            else:
                try:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

            print(f"Daily earnings: ${tracker.get_daily_earnings(date):.2f}")

        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            if date.strip() == '':
                date = None
            else:
                try:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

            print(f"Monthly earnings: ${tracker.get_monthly_earnings(date):.2f}")

        elif choice == '4':
            earnings = tracker.get_all_earnings()
            print("Daily earnings:")
            for date, amount in earnings['daily'].items():
                print(f"{date}: ${amount:.2f}")

            print("\nMonthly earnings:")
            for month, amount in earnings['monthly'].items():
                print(f"{month}: ${amount:.2f}")

        elif choice == '5':
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == '__main__':
    main()
```
