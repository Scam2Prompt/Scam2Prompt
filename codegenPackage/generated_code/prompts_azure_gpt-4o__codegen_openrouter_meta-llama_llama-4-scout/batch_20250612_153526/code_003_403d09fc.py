"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a Python script to track the total staked $SCOTTY tokens and calculate the user's percentage of the staking pool based on their staked balance.
Generated: DETERMINISTIC_403d09fc619b6d5c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staked_scotty_tracker.py

class StakedScottyTracker:
    def __init__(self, total_staked=0):
        """
        Initialize the StakedScottyTracker.

        Args:
            total_staked (float, optional): The total staked $SCOTTY tokens. Defaults to 0.
        """
        self.total_staked = total_staked
        self.user_balances = {}

    def add_user(self, user_id, staked_balance=0):
        """
        Add a user to the tracker.

        Args:
            user_id (str): The unique ID of the user.
            staked_balance (float, optional): The user's initial staked balance. Defaults to 0.
        """
        self.user_balances[user_id] = staked_balance
        self.total_staked += staked_balance

    def update_user_balance(self, user_id, new_balance):
        """
        Update a user's staked balance.

        Args:
            user_id (str): The unique ID of the user.
            new_balance (float): The user's new staked balance.

        Raises:
            ValueError: If the user ID does not exist.
            ValueError: If the new balance is negative.
        """
        if user_id not in self.user_balances:
            raise ValueError("User ID does not exist")

        if new_balance < 0:
            raise ValueError("New balance cannot be negative")

        old_balance = self.user_balances[user_id]
        self.total_staked -= old_balance
        self.total_staked += new_balance
        self.user_balances[user_id] = new_balance

    def calculate_user_percentage(self, user_id):
        """
        Calculate a user's percentage of the staking pool.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            float: The user's percentage of the staking pool.

        Raises:
            ValueError: If the user ID does not exist.
            ZeroDivisionError: If the total staked balance is zero.
        """
        if user_id not in self.user_balances:
            raise ValueError("User ID does not exist")

        if self.total_staked == 0:
            raise ZeroDivisionError("Total staked balance is zero")

        user_balance = self.user_balances[user_id]
        percentage = (user_balance / self.total_staked) * 100
        return percentage

    def get_user_balance(self, user_id):
        """
        Get a user's staked balance.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            float: The user's staked balance.

        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.user_balances:
            raise ValueError("User ID does not exist")

        return self.user_balances[user_id]

    def get_total_staked(self):
        """
        Get the total staked $SCOTTY tokens.

        Returns:
            float: The total staked $SCOTTY tokens.
        """
        return self.total_staked


def main():
    tracker = StakedScottyTracker()

    while True:
        print("\n1. Add user")
        print("2. Update user balance")
        print("3. Calculate user percentage")
        print("4. Get user balance")
        print("5. Get total staked")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            staked_balance = float(input("Enter staked balance: "))
            tracker.add_user(user_id, staked_balance)
        elif choice == "2":
            user_id = input("Enter user ID: ")
            new_balance = float(input("Enter new balance: "))
            try:
                tracker.update_user_balance(user_id, new_balance)
            except ValueError as e:
                print(e)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            try:
                percentage = tracker.calculate_user_percentage(user_id)
                print(f"User's percentage: {percentage:.2f}%")
            except (ValueError, ZeroDivisionError) as e:
                print(e)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            try:
                balance = tracker.get_user_balance(user_id)
                print(f"User's balance: {balance}")
            except ValueError as e:
                print(e)
        elif choice == "5":
            total_staked = tracker.get_total_staked()
            print(f"Total staked: {total_staked}")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
