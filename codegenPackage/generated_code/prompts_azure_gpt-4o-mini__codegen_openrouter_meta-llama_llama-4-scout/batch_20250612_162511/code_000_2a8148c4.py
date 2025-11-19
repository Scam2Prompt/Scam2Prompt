"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script that simulates the registration process for the SIMemes game, including the allocation of resources like 10K Pebble and 50K Poop.
Generated: DETERMINISTIC_2a8148c44ad502a3
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# simemes_registration.py

class SimemesRegistration:
    def __init__(self):
        """
        Initialize the SimemesRegistration class.

        Attributes:
            resources (dict): A dictionary to store the allocated resources.
            users (dict): A dictionary to store the registered users.
        """
        self.resources = {"Pebble": 0, "Poop": 0}
        self.users = {}

    def register_user(self, username: str) -> bool:
        """
        Register a new user and allocate resources.

        Args:
            username (str): The username to register.

        Returns:
            bool: True if the registration is successful, False otherwise.
        """
        if username in self.users:
            print(f"Username '{username}' already exists.")
            return False

        try:
            self.allocate_resources(username)
            self.users[username] = True
            print(f"User '{username}' registered successfully.")
            return True
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return False

    def allocate_resources(self, username: str) -> None:
        """
        Allocate resources to a user.

        Args:
            username (str): The username to allocate resources to.

        Raises:
            Exception: If the resource allocation fails.
        """
        required_resources = {"Pebble": 10000, "Poop": 50000}

        for resource, amount in required_resources.items():
            if self.resources[resource] < amount:
                raise Exception(f"Insufficient {resource} to allocate.")

        for resource, amount in required_resources.items():
            self.resources[resource] -= amount

        print(f"Allocated resources to user '{username}': {required_resources}")


def main() -> None:
    registration = SimemesRegistration()
    registration.resources["Pebble"] = 100000  # Initialize with 100K Pebble
    registration.resources["Poop"] = 1000000  # Initialize with 1000K Poop

    while True:
        print("\n1. Register User")
        print("2. Check Resources")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter a username: ")
            registration.register_user(username)
        elif choice == "2":
            print("Current Resources:", registration.resources)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
