"""
Generated Code Metadata:
========================
Original URL: https://tangganglife.pages.dev
Prompt: "Write a Python code snippet to implement a leaderboard system for a guild, similar to Tang Gang's, that requires holding a specific amount of $HOA cryptocurrency."
Generated: DETERMINISTIC_fecc65d486bc6fc3
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Leaderboard:
    """
    A class to represent a leaderboard system for a guild.
    Tracks members and their $HOA cryptocurrency holdings.
    """

    def __init__(self, required_hoa: float):
        """
        Initialize the leaderboard with a required $HOA threshold.
        
        :param required_hoa: Minimum $HOA required to be listed on the leaderboard.
        """
        self.required_hoa = required_hoa
        self.members = {}  # Dictionary to store member data {name: hoa_balance}

    def add_member(self, name: str, hoa_balance: float):
        """
        Add a member to the leaderboard if they meet the $HOA requirement.
        
        :param name: Name of the guild member.
        :param hoa_balance: $HOA cryptocurrency balance of the member.
        :raises ValueError: If the $HOA balance is negative.
        """
        if hoa_balance < 0:
            raise ValueError("HOA balance cannot be negative.")
        
        self.members[name] = hoa_balance

    def get_leaderboard(self):
        """
<<<<<<< HEAD
        Get the leaderboard sorted by $HOA balance in descending order.
        Only includes members who meet the $HOA requirement.
        
        :return: List of tuples [(name, hoa_balance), ...] sorted by balance.
        """
        eligible_members = {
            name: balance for name, balance in self.members.items()
            if balance >= self.required_hoa
=======
        Get the sorted leaderboard of members who meet the $HOA requirement.
        
        :return: List of tuples (name, hoa_balance) sorted by $HOA balance in descending order.
        """
        eligible_members = {
            name: balance for name, balance in self.members.items() if balance >= self.required_hoa
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        }
        return sorted(eligible_members.items(), key=lambda x: x[1], reverse=True)

    def save_to_file(self, filename: str):
        """
        Save the leaderboard to a JSON file.
        
        :param filename: Name of the file to save the leaderboard.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.members, file, indent=4)
        except IOError as e:
            print(f"Error saving leaderboard to file: {e}")

    def load_from_file(self, filename: str):
        """
<<<<<<< HEAD
        Load member data from a JSON file.
=======
        Load the leaderboard from a JSON file.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        
        :param filename: Name of the file to load the leaderboard from.
        :raises IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                self.members = json.load(file)
        except IOError as e:
            print(f"Error loading leaderboard from file: {e}")
        except json.JSONDecodeError as e:
<<<<<<< HEAD
            print(f"Error decoding JSON data: {e}")
=======
            print(f"Error decoding JSON file: {e}")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)


# Example usage
if __name__ == "__main__":
    # Initialize leaderboard with a $HOA requirement of 100
<<<<<<< HEAD
    leaderboard = Leaderboard(required_hoa=100)

    # Add members
    leaderboard.add_member("Alice", 150)
    leaderboard.add_member("Bob", 90)
    leaderboard.add_member("Charlie", 200)

    # Display leaderboard
    print("Leaderboard:")
    for name, balance in leaderboard.get_leaderboard():
        print(f"{name}: {balance} $HOA")

    # Save leaderboard to file
    leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from file
    leaderboard.load_from_file("leaderboard.json")
    print("\nLoaded Leaderboard:")
    for name, balance in leaderboard.get_leaderboard():
=======
    guild_leaderboard = Leaderboard(required_hoa=100)

    # Add members
    guild_leaderboard.add_member("Alice", 150)
    guild_leaderboard.add_member("Bob", 90)
    guild_leaderboard.add_member("Charlie", 200)

    # Display leaderboard
    print("Leaderboard:")
    for name, balance in guild_leaderboard.get_leaderboard():
        print(f"{name}: {balance} $HOA")

    # Save leaderboard to file
    guild_leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from file
    guild_leaderboard.load_from_file("leaderboard.json")
    print("\nLoaded Leaderboard:")
    for name, balance in guild_leaderboard.get_leaderboard():
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        print(f"{name}: {balance} $HOA")
```
