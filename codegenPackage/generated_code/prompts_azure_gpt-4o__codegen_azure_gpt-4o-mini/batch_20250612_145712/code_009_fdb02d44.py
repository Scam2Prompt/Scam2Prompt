"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Create a function in Python to simulate the "double energy" feature, where subscribing to a sponsor channel doubles the user's energy, as described in the Khaby Lame Coin WebApp.
Generated: DETERMINISTIC_fdb02d444bb9f962
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    A class to represent a user in the Khaby Lame Coin WebApp.

    Attributes:
        username (str): The username of the user.
        energy (float): The current energy level of the user.
        is_subscribed (bool): Subscription status to the sponsor channel.
    """

    def __init__(self, username: str, initial_energy: float = 100.0):
        """
        Initializes a new user with a username and an initial energy level.

        Args:
            username (str): The username of the user.
            initial_energy (float): The initial energy level of the user. Defaults to 100.0.
        """
        self.username = username
        self.energy = initial_energy
        self.is_subscribed = False

    def subscribe_to_sponsor(self):
        """
        Subscribes the user to the sponsor channel, enabling the double energy feature.
        """
        self.is_subscribed = True
        print(f"{self.username} has subscribed to the sponsor channel.")

    def unsubscribe_from_sponsor(self):
        """
        Unsubscribes the user from the sponsor channel, disabling the double energy feature.
        """
        self.is_subscribed = False
        print(f"{self.username} has unsubscribed from the sponsor channel.")

    def simulate_double_energy(self):
        """
        Simulates the double energy feature. If the user is subscribed to the sponsor channel,
        their energy is doubled. Otherwise, an error is raised.

        Raises:
            RuntimeError: If the user is not subscribed to the sponsor channel.
        """
        if not self.is_subscribed:
            raise RuntimeError("User must be subscribed to the sponsor channel to double energy.")

        # Double the user's energy
        self.energy *= 2
        print(f"{self.username}'s energy has been doubled to {self.energy}.")

# Example usage
if __name__ == "__main__":
    try:
        user = User("KhabyLame")
        user.subscribe_to_sponsor()  # Subscribe to the sponsor channel
        user.simulate_double_energy()  # Double the energy
    except RuntimeError as e:
        print(f"Error: {e}")
```
