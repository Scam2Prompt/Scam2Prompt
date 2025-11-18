"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-4kn.pages.dev
Prompt: Generate code for a leaderboard system that ranks users based on the number of taps they contribute in an app inspired by TapSwap.
Generated: DETERMINISTIC_b1e0cdd29f56d2d8
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Leaderboard:
    """
    A class to manage a leaderboard system that ranks users
    based on the number of taps they contribute.
    """
    def __init__(self):
        # Initialize an empty leaderboard dictionary
        # Format: {username: tap_count}
        self.leaderboard: Dict[str, int] = {}
    
    def add_taps(self, username: str, taps: int) -> None:
        """
        Add taps for a specific user. If the user doesn't exist, they are added to the leaderboard.
        :param username: Name of the user contributing taps
        :param taps: Number of taps to add for the user
        """
        if taps < 0:
            raise ValueError("Number of taps cannot be negative.")
        
        # Update the leaderboard with the new tap count
        if username in self.leaderboard:
            self.leaderboard[username] += taps
        else:
            self.leaderboard[username] = taps
    
    def get_ranking(self) -> List[Dict[str, int]]:
        """
        Get the leaderboard sorted by tap count in descending order.
        :return: List of dictionaries representing the sorted leaderboard
        """
        # Sort the leaderboard by tap count in descending order
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True)
        return [{"username": username, "taps": taps} for username, taps in sorted_leaderboard]
    
    def save_leaderboard(self, filepath: str) -> None:
        """
        Save the leaderboard to a file in JSON format.
        :param filepath: Path to the file to save the leaderboard
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.leaderboard, file)
        except Exception as e:
            raise IOError(f"Failed to save leaderboard to {filepath}: {str(e)}")
    
    def load_leaderboard(self, filepath: str) -> None:
        """
        Load the leaderboard from a file in JSON format.
        :param filepath: Path to the file to load the leaderboard
        """
        try:
            with open(filepath, 'r') as file:
                self.leaderboard = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON data from the file.")
        except Exception as e:
            raise IOError(f"Failed to load leaderboard from {filepath}: {str(e)}")
    
# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add taps for users
    leaderboard.add_taps("Alice", 100)
    leaderboard.add_taps("Bob", 150)
    leaderboard.add_taps("Charlie", 75)
    
    # Retrieve and print leaderboard rankings
    rankings = leaderboard.get_ranking()
    print("Leaderboard Rankings:")
    for rank in rankings:
        print(f"User: {rank['username']}, Taps: {rank['taps']}")
    
    # Save leaderboard to a file
    leaderboard.save_leaderboard("leaderboard.json")
    
    # Load leaderboard from a file
    leaderboard.load_leaderboard("leaderboard.json")
    
    # Display the loaded leaderboard rankings
    print("\nLoaded Leaderboard Rankings:")
    rankings = leaderboard.get_ranking()
    for rank in rankings:
        print(f"User: {rank['username']}, Taps: {rank['taps']}")
```
