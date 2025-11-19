"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Create a function to filter and display leaderboard rankings from MANTRA Zone based on specific criteria such as wallet address, rank range, or KARMA thresholds.
Generated: DETERMINISTIC_238fb56a1025df75
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class LeaderboardEntry:
    """Class to represent a single entry in the leaderboard."""
    def __init__(self, wallet_address: str, rank: int, karma: float):
        self.wallet_address = wallet_address
        self.rank = rank
        self.karma = karma

    def to_dict(self) -> Dict[str, Any]:
        """Convert the leaderboard entry to a dictionary."""
        return {
            "wallet_address": self.wallet_address,
            "rank": self.rank,
            "karma": self.karma
        }

def load_leaderboard(file_path: str) -> List[LeaderboardEntry]:
    """Load leaderboard data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing leaderboard data.

    Returns:
        List[LeaderboardEntry]: A list of leaderboard entries.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [LeaderboardEntry(entry['wallet_address'], entry['rank'], entry['karma']) for entry in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError("Error: The file content is not valid JSON.") from e

def filter_leaderboard(entries: List[LeaderboardEntry], 
                       wallet_address: str = None, 
                       rank_range: tuple = None, 
                       karma_threshold: float = None) -> List[LeaderboardEntry]:
    """Filter leaderboard entries based on specified criteria.

    Args:
        entries (List[LeaderboardEntry]): The list of leaderboard entries to filter.
        wallet_address (str, optional): The wallet address to filter by.
        rank_range (tuple, optional): A tuple specifying the min and max rank (inclusive).
        karma_threshold (float, optional): The minimum karma threshold.

    Returns:
        List[LeaderboardEntry]: A list of filtered leaderboard entries.
    """
    filtered_entries = entries

    if wallet_address:
        filtered_entries = [entry for entry in filtered_entries if entry.wallet_address == wallet_address]

    if rank_range:
        min_rank, max_rank = rank_range
        filtered_entries = [entry for entry in filtered_entries if min_rank <= entry.rank <= max_rank]

    if karma_threshold is not None:
        filtered_entries = [entry for entry in filtered_entries if entry.karma >= karma_threshold]

    return filtered_entries

def display_leaderboard(entries: List[LeaderboardEntry]) -> None:
    """Display the leaderboard entries in a formatted manner.

    Args:
        entries (List[LeaderboardEntry]): The list of leaderboard entries to display.
    """
    if not entries:
        print("No entries to display.")
        return

    print(f"{'Rank':<10} {'Wallet Address':<42} {'Karma':<10}")
    print("=" * 62)
    for entry in entries:
        print(f"{entry.rank:<10} {entry.wallet_address:<42} {entry.karma:<10.2f}")

def main():
    """Main function to load, filter, and display the leaderboard."""
    file_path = 'leaderboard.json'  # Path to the leaderboard JSON file

    try:
        leaderboard_entries = load_leaderboard(file_path)
        filtered_entries = filter_leaderboard(leaderboard_entries, rank_range=(1, 10), karma_threshold=50.0)
        display_leaderboard(filtered_entries)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
