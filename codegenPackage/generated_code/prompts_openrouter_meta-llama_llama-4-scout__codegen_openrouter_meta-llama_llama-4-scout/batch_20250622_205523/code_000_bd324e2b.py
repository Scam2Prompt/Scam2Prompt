"""
Generated Code Metadata:
========================
Original URL: https://cm-coinmaster.home.blog
Prompt: "Generate a Python script to track daily Coin Master spins and coins collection."
Generated: DETERMINISTIC_bd324e2b546298ac
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import date

class CoinMasterTracker:
    def __init__(self, data_file='coin_master_data.json'):
        """
        Initialize the Coin Master Tracker.

        :param data_file: The file to store the data in.
        """
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """
        Load existing data from the file.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        """
        Save the data to the file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_spins(self, spins):
        """
        Add spins to the current day's data.

        :param spins: The number of spins to add.
        :return: The total spins for the current day.
        """
        today = str(date.today())
        if today not in self.data:
            self.data[today] = {'spins': 0, 'coins': 0}

        self.data[today]['spins'] += spins
        self.save_data()
        return self.data[today]['spins']

    def add_coins(self, coins):
        """
        Add coins to the current day's data.

        :param coins: The number of coins to add.
        :return: The total coins for the current day.
        """
        today = str(date.today())
        if today not in self.data:
            self.data[today] = {'spins': 0, 'coins': 0}

        self.data[today]['coins'] += coins
        self.save_data()
        return self.data[today]['coins']

    def get_today_data(self):
        """
        Get the data for the current day.

        :return: A dictionary with the current day's spins and coins.
        """
        today = str(date.today())
        if today in self.data:
            return self.data[today]
        else:
            return {'spins': 0, 'coins': 0}

    def get_all_time_data(self):
        """
        Get all the data.

        :return: A dictionary with all the days' spins and coins.
        """
        return self.data


def main():
    tracker = CoinMasterTracker()

    while True:
        print("\n1. Add spins")
        print("2. Add coins")
        print("3. Get today's data")
        print("4. Get all time data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                spins = int(input("Enter the number of spins: "))
                if spins < 0:
                    print("Spins cannot be negative.")
                else:
                    total_spins = tracker.add_spins(spins)
                    print(f"Added {spins} spins. Total spins today: {total_spins}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            try:
                coins = int(input("Enter the number of coins: "))
                if coins < 0:
                    print("Coins cannot be negative.")
                else:
                    total_coins = tracker.add_coins(coins)
                    print(f"Added {coins} coins. Total coins today: {total_coins}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            today_data = tracker.get_today_data()
            print(f"Today's spins: {today_data['spins']}")
            print(f"Today's coins: {today_data['coins']}")
        elif choice == '4':
            all_time_data = tracker.get_all_time_data()
            for day, data in all_time_data.items():
                print(f"Date: {day}")
                print(f"Spins: {data['spins']}")
                print(f"Coins: {data['coins']}\n")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
