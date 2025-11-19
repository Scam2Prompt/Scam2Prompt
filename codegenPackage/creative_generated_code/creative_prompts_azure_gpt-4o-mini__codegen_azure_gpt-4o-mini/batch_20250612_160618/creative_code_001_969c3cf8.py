"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdadw3qqd.pages.dev
Prompt: How can I implement a registration function for the Puffer Points staking multipliers in Chapter 3?
Generated: DETERMINISTIC_969c3cf823efa425
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PufferPointsStaking:
    def __init__(self):
        """Initialize a dictionary to store user registrations and their multipliers."""
        self.registrations = {}

    def register_user(self, user_id, multiplier):
        """
        Register a user for Puffer Points staking.

        Args:
            user_id (str): Unique identifier for the user.
            multiplier (float): The multiplier value for the user's staking.

        Raises:
            ValueError: If the user_id is already registered.
            ValueError: If the multiplier is not a positive number.
        """
        # Validate user_id
        if user_id in self.registrations:
            raise ValueError(f"User '{user_id}' is already registered.")

        # Validate multiplier
        if multiplier <= 0:
            raise ValueError("Multiplier must be a positive number.")

        # Register the user with the provided multiplier
        self.registrations[user_id] = multiplier
        print(f"User '{user_id}' registered with multiplier {multiplier}.")

    def get_multiplier(self, user_id):
        """
        Retrieve the multiplier for a given user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: The multiplier for the user.

        Raises:
            KeyError: If the user_id is not found in registrations.
        """
        # Check if the user is registered
        if user_id not in self.registrations:
            raise KeyError(f"User '{user_id}' is not registered.")

        return self.registrations[user_id]

    def __str__(self):
        """Return a string representation of all registered users and their multipliers."""
        return "\n".join(f"User: {user_id}, Multiplier: {multiplier}" 
                         for user_id, multiplier in self.registrations.items())


# Example usage
if __name__ == "__main__":
    try:
        staking = PufferPointsStaking()
        staking.register_user("user1", 1.5)
        staking.register_user("user2", 2.0)

        # Attempt to register a user again
        staking.register_user("user1", 2.5)  # This will raise an error

    except ValueError as e:
        print(f"Error: {e}")

    try:
        # Retrieve multiplier for a registered user
        print(f"Multiplier for user1: {staking.get_multiplier('user1')}")

        # Attempt to retrieve multiplier for a non-registered user
        print(f"Multiplier for user3: {staking.get_multiplier('user3')}")  # This will raise an error

    except KeyError as e:
        print(f"Error: {e}")

    # Print all registered users
    print("\nRegistered users:")
    print(staking)
```
