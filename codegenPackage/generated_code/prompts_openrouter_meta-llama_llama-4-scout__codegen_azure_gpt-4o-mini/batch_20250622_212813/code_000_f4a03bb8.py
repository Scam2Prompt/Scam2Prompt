"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Explain the concept of Loud and how it utilizes trading volume to reward top contributors to discussions about a specific coin.
Generated: DETERMINISTIC_f4a03bb8f7327aaa
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Loud:
    """
    A class to represent the Loud platform that rewards contributors based on trading volume discussions.
    """

    def __init__(self):
        """
        Initializes the Loud platform with an empty list of contributors and their respective volumes.
        """
        self.contributors = {}

    def add_contributor(self, username: str, trading_volume: float):
        """
        Adds a contributor to the platform with their trading volume.

        Args:
            username (str): The username of the contributor.
            trading_volume (float): The trading volume associated with the contributor.

        Raises:
            ValueError: If trading_volume is negative or username is empty.
        """
        if trading_volume < 0:
            raise ValueError("Trading volume cannot be negative.")
        if not username:
            raise ValueError("Username cannot be empty.")

        self.contributors[username] = self.contributors.get(username, 0) + trading_volume

    def calculate_rewards(self):
        """
        Calculates rewards for each contributor based on their trading volume.

        Returns:
            dict: A dictionary with usernames as keys and their respective rewards as values.
        """
        total_volume = sum(self.contributors.values())
        if total_volume == 0:
            return {username: 0 for username in self.contributors}

        rewards = {}
        for username, volume in self.contributors.items():
            # Reward is proportional to the contributor's volume relative to the total volume
            rewards[username] = (volume / total_volume) * 100  # Example: reward as a percentage

        return rewards

    def display_rewards(self):
        """
        Displays the rewards for each contributor in a formatted manner.
        """
        rewards = self.calculate_rewards()
        for username, reward in rewards.items():
            print(f"Contributor: {username}, Reward: {reward:.2f}%")

# Example usage
if __name__ == "__main__":
    loud_platform = Loud()
    
    try:
        loud_platform.add_contributor("Alice", 1500)
        loud_platform.add_contributor("Bob", 2500)
        loud_platform.add_contributor("Charlie", 1000)

        loud_platform.display_rewards()
    except ValueError as e:
        print(f"Error: {e}")
```
