"""
Generated Code Metadata:
========================
Original URL: https://matrica17.vercel.app
Prompt: Generate a script that allows users to select between Solana, Ethereum, and Polygon networks during login.
Generated: DETERMINISTIC_c7088d9651f88e9b
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum

class Network(Enum):
    """Enum representing supported blockchain networks."""
    SOLANA = "Solana"
    ETHEREUM = "Ethereum"
    POLYGON = "Polygon"

class User:
    """Class representing a user with network selection capability."""
    def __init__(self, username: str, network: Network = None):
        self.username = username
        self.network = network

    def set_network(self, network: Network):
        """Set the user's preferred network."""
        if not isinstance(network, Network):
            raise ValueError("Invalid network type. Must be a Network enum.")
        self.network = network

    def to_dict(self):
        """Convert user object to dictionary for serialization."""
        return {
            "username": self.username,
            "network": self.network.value if self.network else None
        }

def display_network_options():
    """Display available network options to the user."""
    print("\nAvailable Networks:")
    for i, network in enumerate(Network, 1):
        print(f"{i}. {network.value}")

def get_network_choice() -> Network:
    """Get and validate user's network choice."""
    while True:
        try:
            choice = int(input("Select a network (1-3): "))
            if 1 <= choice <= len(Network):
                return list(Network)[choice - 1]
            print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def login():
    """Handle user login and network selection."""
    print("Welcome to the Blockchain Login System")
    
    # Get username
    username = input("Enter your username: ").strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    
    # Network selection
    display_network_options()
    selected_network = get_network_choice()
    
    # Create user
    user = User(username, selected_network)
    print(f"\nWelcome, {user.username}! You've selected {user.network.value} network.")
    
    return user

def save_user_session(user: User, filename: str = "user_session.json"):
    """Save user session to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(user.to_dict(), f)
    except IOError as e:
        print(f"Error saving session: {e}")

def main():
    """Main program entry point."""
    try:
        user = login()
        save_user_session(user)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
