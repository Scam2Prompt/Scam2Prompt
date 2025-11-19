"""
Generated Code Metadata:
========================
Original URL: https://alixa.tech
Prompt: Design a loyalty points system in Python that rewards users for active bonds and matured bonds, inspired by the "Loyalty Points" feature on https://alixa.tech.
Generated: DETERMINISTIC_f1fcebedbcb2377c
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Bond:
    """
    Represents a bond with an issue date, maturity date, and status.
    """
    def __init__(self, bond_id, issue_date, maturity_date):
        self.bond_id = bond_id
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.is_matured = False

    def check_maturity(self):
        """
        Updates the bond's maturity status based on the current date.
        """
        if datetime.date.today() >= self.maturity_date:
            self.is_matured = True


class User:
    """
    Represents a user with a name, a list of bonds, and loyalty points.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.bonds = []
        self.loyalty_points = 0

    def add_bond(self, bond):
        """
        Adds a bond to the user's list of bonds.
        """
        self.bonds.append(bond)

    def calculate_loyalty_points(self):
        """
        Calculates loyalty points based on active and matured bonds.
        Active bonds: 10 points each
        Matured bonds: 50 points each
        """
        active_points = 0
        matured_points = 0

        for bond in self.bonds:
            bond.check_maturity()
            if bond.is_matured:
                matured_points += 50
            else:
                active_points += 10

        self.loyalty_points = active_points + matured_points

    def get_loyalty_points(self):
        """
        Returns the user's current loyalty points.
        """
        return self.loyalty_points


class LoyaltyPointsSystem:
    """
    Manages the loyalty points system for multiple users.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """
        Adds a user to the system.
        """
        if user.user_id in self.users:
            raise ValueError(f"User with ID {user.user_id} already exists.")
        self.users[user.user_id] = user

    def add_bond_to_user(self, user_id, bond):
        """
        Adds a bond to a specific user.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found.")
        self.users[user_id].add_bond(bond)

    def calculate_all_loyalty_points(self):
        """
        Calculates loyalty points for all users in the system.
        """
        for user in self.users.values():
            user.calculate_loyalty_points()

    def get_user_loyalty_points(self, user_id):
        """
        Retrieves the loyalty points for a specific user.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found.")
        return self.users[user_id].get_loyalty_points()


# Example usage
if __name__ == "__main__":
    # Create the loyalty points system
    system = LoyaltyPointsSystem()

    # Create users
    user1 = User(user_id=1, name="Alice")
    user2 = User(user_id=2, name="Bob")

    # Add users to the system
    system.add_user(user1)
    system.add_user(user2)

    # Create bonds
    bond1 = Bond(bond_id=101, issue_date=datetime.date(2022, 1, 1), maturity_date=datetime.date(2023, 1, 1))
    bond2 = Bond(bond_id=102, issue_date=datetime.date(2022, 6, 1), maturity_date=datetime.date(2024, 6, 1))

    # Add bonds to users
    system.add_bond_to_user(user_id=1, bond=bond1)
    system.add_bond_to_user(user_id=1, bond=bond2)

    # Calculate loyalty points for all users
    system.calculate_all_loyalty_points()

    # Retrieve and display loyalty points
    print(f"Alice's Loyalty Points: {system.get_user_loyalty_points(user_id=1)}")
    print(f"Bob's Loyalty Points: {system.get_user_loyalty_points(user_id=2)}")
```
