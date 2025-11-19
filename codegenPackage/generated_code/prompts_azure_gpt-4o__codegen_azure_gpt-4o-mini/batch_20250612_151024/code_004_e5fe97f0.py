"""
Generated Code Metadata:
========================
Original URL: https://harpycoin.pages.dev
Prompt: Generate code for a contest leaderboard system that tracks and displays the highest buy contest results for HarpyCoin, including meme and shill contest submissions.
Generated: DETERMINISTIC_e5fe97f0ad3aba50
Batch ID: 20250612_151024
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

class ContestEntry:
    """Class to represent a contest entry."""
    
    def __init__(self, username: str, score: float, contest_type: str):
        self.username = username
        self.score = score
        self.contest_type = contest_type

    def to_dict(self) -> Dict[str, Any]:
        """Convert the entry to a dictionary for easy serialization."""
        return {
            "username": self.username,
            "score": self.score,
            "contest_type": self.contest_type
        }

class Leaderboard:
    """Class to manage the leaderboard for HarpyCoin contests."""
    
    def __init__(self):
        self.entries: List[ContestEntry] = []

    def add_entry(self, entry: ContestEntry) -> None:
        """Add a new entry to the leaderboard."""
        self.entries.append(entry)

    def get_top_entries(self, contest_type: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get the top entries for a specific contest type."""
        filtered_entries = [entry for entry in self.entries if entry.contest_type == contest_type]
        sorted_entries = sorted(filtered_entries, key=lambda x: x.score, reverse=True)
        return [entry.to_dict() for entry in sorted_entries[:limit]]

    def save_to_file(self, filename: str) -> None:
        """Save the leaderboard entries to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([entry.to_dict() for entry in self.entries], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load leaderboard entries from a JSON file."""
        try:
            with open(filename, 'r') as file:
                entries = json.load(file)
                for entry in entries:
                    self.add_entry(ContestEntry(entry['username'], entry['score'], entry['contest_type']))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Load existing entries from a file
    leaderboard.load_from_file('leaderboard.json')
    
    # Add new entries
    leaderboard.add_entry(ContestEntry("User1", 150.0, "meme"))
    leaderboard.add_entry(ContestEntry("User2", 200.0, "shill"))
    
    # Get top meme contest entries
    top_meme_entries = leaderboard.get_top_entries("meme")
    print("Top Meme Contest Entries:", top_meme_entries)
    
    # Get top shill contest entries
    top_shill_entries = leaderboard.get_top_entries("shill")
    print("Top Shill Contest Entries:", top_shill_entries)
    
    # Save updated leaderboard to a file
    leaderboard.save_to_file('leaderboard.json')
```
