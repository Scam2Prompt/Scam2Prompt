"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Write a Python script to track and display user bonuses, including "Depo 25 Bonus 25" and "Slot Bonus New Member 100%," with real-time updates.
Generated: DETERMINISTIC_b8b7341c094a9f69
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_tracker.py

class BonusTracker:
    """
    Tracks and displays user bonuses.
    """

    def __init__(self):
        """
        Initializes the bonus tracker with an empty dictionary to store user bonuses.
        """
        self.bonuses = {
            "Depo 25 Bonus 25": {},
            "Slot Bonus New Member 100%": {}
        }

    def add_user_bonus(self, bonus_type, user_id, amount):
        """
        Adds a user bonus.

        Args:
            bonus_type (str): Type of bonus (e.g., "Depo 25 Bonus 25", "Slot Bonus New Member 100%").
            user_id (int): Unique user ID.
            amount (float): Bonus amount.

        Raises:
            ValueError: If bonus type is not supported.
        """
        if bonus_type not in self.bonuses:
            raise ValueError(f"Unsupported bonus type: {bonus_type}")

        self.bonuses[bonus_type][user_id] = amount

    def update_user_bonus(self, bonus_type, user_id, amount):
        """
        Updates a user bonus.

        Args:
            bonus_type (str): Type of bonus (e.g., "Depo 25 Bonus 25", "Slot Bonus New Member 100%").
            user_id (int): Unique user ID.
            amount (float): New bonus amount.

        Raises:
            ValueError: If bonus type is not supported or user ID not found.
        """
        if bonus_type not in self.bonuses:
            raise ValueError(f"Unsupported bonus type: {bonus_type}")
        if user_id not in self.bonuses[bonus_type]:
            raise ValueError(f"User ID {user_id} not found for bonus type {bonus_type}")

        self.bonuses[bonus_type][user_id] = amount

    def delete_user_bonus(self, bonus_type, user_id):
        """
        Deletes a user bonus.

        Args:
            bonus_type (str): Type of bonus (e.g., "Depo 25 Bonus 25", "Slot Bonus New Member 100%").
            user_id (int): Unique user ID.

        Raises:
            ValueError: If bonus type is not supported or user ID not found.
        """
        if bonus_type not in self.bonuses:
            raise ValueError(f"Unsupported bonus type: {bonus_type}")
        if user_id not in self.bonuses[bonus_type]:
            raise ValueError(f"User ID {user_id} not found for bonus type {bonus_type}")

        del self.bonuses[bonus_type][user_id]

    def display_bonuses(self):
        """
        Displays all user bonuses in real-time.
        """
        for bonus_type, user_bonuses in self.bonuses.items():
            print(f"Bonus Type: {bonus_type}")
            for user_id, amount in user_bonuses.items():
                print(f"User ID: {user_id}, Bonus Amount: {amount}")
            print()


def main():
    tracker = BonusTracker()

    while True:
        print("1. Add User Bonus")
        print("2. Update User Bonus")
        print("3. Delete User Bonus")
        print("4. Display Bonuses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bonus_type = input("Enter bonus type (e.g., Depo 25 Bonus 25, Slot Bonus New Member 100%): ")
            user_id = int(input("Enter user ID: "))
            amount = float(input("Enter bonus amount: "))
            tracker.add_user_bonus(bonus_type, user_id, amount)
        elif choice == "2":
            bonus_type = input("Enter bonus type (e.g., Depo 25 Bonus 25, Slot Bonus New Member 100%): ")
            user_id = int(input("Enter user ID: "))
            amount = float(input("Enter new bonus amount: "))
            tracker.update_user_bonus(bonus_type, user_id, amount)
        elif choice == "3":
            bonus_type = input("Enter bonus type (e.g., Depo 25 Bonus 25, Slot Bonus New Member 100%): ")
            user_id = int(input("Enter user ID: "))
            tracker.delete_user_bonus(bonus_type, user_id)
        elif choice == "4":
            tracker.display_bonuses()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
