"""
Generated Code Metadata:
========================
Original URL: https://miningbase.cloud
Prompt: Create a Python script to simulate free hashing power allocation for new users, similar to the MiningBase free GH/s feature.
Generated: DETERMINISTIC_1fecd0f2434b187c
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import random

class MiningBaseSimulator:
    """
    Simulates free hashing power allocation for new users.
    """

    def __init__(self):
        # Initialize a dictionary to store user accounts and their allocated hashing power
        self.accounts = {}

    def create_account(self, username):
        """
        Creates a new user account and allocates free hashing power.

        Args:
            username (str): The username of the new account.

        Returns:
            int: The allocated hashing power in GH/s.
        """
        if username in self.accounts:
            raise ValueError("Username already exists")

        # Allocate 1 GH/s for new users
        allocated_hashing_power = 1  # GH/s

        # Store the account and allocated hashing power in the dictionary
        self.accounts[username] = {
            "hashing_power": allocated_hashing_power,
            "last_active": time.time()
        }

        return allocated_hashing_power

    def get_account_info(self, username):
        """
        Retrieves information about a user's account.

        Args:
            username (str): The username of the account.

        Returns:
            dict: A dictionary containing the account's hashing power and last active time.
        """
        if username not in self.accounts:
            raise ValueError("Username does not exist")

        return self.accounts[username]

    def simulate_mining(self, username, block_data):
        """
        Simulates mining by hashing block data.

        Args:
            username (str): The username of the account.
            block_data (str): The data to be hashed.

        Returns:
            str: The hashed block data.
        """
        if username not in self.accounts:
            raise ValueError("Username does not exist")

        # Get the account's allocated hashing power
        allocated_hashing_power = self.accounts[username]["hashing_power"]

        # Simulate mining by hashing the block data
        # For demonstration purposes, assume 1 GH/s = 1 hash per second
        start_time = time.time()
        hashed_block_data = hashlib.sha256(block_data.encode()).hexdigest()
        end_time = time.time()

        # Update the account's last active time
        self.accounts[username]["last_active"] = end_time

        # Print the simulated mining result
        print(f"Simulated mining result: {hashed_block_data}")
        print(f"Time taken: {end_time - start_time} seconds")
        print(f"Hashing power: {allocated_hashing_power} GH/s")

        return hashed_block_data

def main():
    simulator = MiningBaseSimulator()

    while True:
        print("\n1. Create account")
        print("2. Get account info")
        print("3. Simulate mining")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter a username: ")
            try:
                allocated_hashing_power = simulator.create_account(username)
                print(f"Allocated hashing power: {allocated_hashing_power} GH/s")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            username = input("Enter a username: ")
            try:
                account_info = simulator.get_account_info(username)
                print(f"Hashing power: {account_info['hashing_power']} GH/s")
                print(f"Last active: {account_info['last_active']}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            username = input("Enter a username: ")
            block_data = str(random.randint(1, 1000000))
            try:
                simulator.simulate_mining(username, block_data)
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
