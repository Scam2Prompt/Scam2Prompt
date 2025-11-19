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
from datetime import datetime
from typing import List, Dict, Optional
import heapq

class ContestEntry:
    """
    Represents a contest entry with user details and score.
    """
    def __init__(self, user_id: str, username: str, score: float, submission_type: str, timestamp: datetime):
        self.user_id = user_id
        self.username = username
        self.score = score
        self.submission_type = submission_type  # 'meme' or 'shill'
        self.timestamp = timestamp

    def __lt__(self, other: 'ContestEntry') -> bool:
        # For max heap, we want higher scores to come first
        # If scores are equal, older submissions come first
        if self.score == other.score:
            return self.timestamp < other.timestamp
        return self.score > other.score

class Leaderboard:
    """
    Manages contest entries and provides leaderboard functionality.
    """
    def __init__(self, max_entries: int = 100):
        self.max_entries = max_entries
        self.entries: List[ContestEntry] = []
        self.user_entries: Dict[str, ContestEntry] = {}  # Maps user_id to their best entry

    def add_entry(self, entry: ContestEntry) -> None:
        """
        Add a new contest entry to the leaderboard.
        """
        # Check if user already has an entry
        existing_entry = self.user_entries.get(entry.user_id)
        
        if existing_entry is None or entry.score > existing_entry.score:
            # Update user's best entry
            self.user_entries[entry.user_id] = entry
            
            # Rebuild the heap if this is a new best score for the user
            if existing_entry is not None:
                self.entries.remove(existing_entry)
                heapq.heapify(self.entries)
            
            # Add new entry to heap
            heapq.heappush(self.entries, entry)
            
            # Maintain max size
            if len(self.entries) > self.max_entries:
                removed = heapq.heappop(self.entries)
                if self.user_entries.get(removed.user_id) == removed:
                    del self.user_entries[removed.user_id]

    def get_top_entries(self, count: int, submission_type: Optional[str] = None) -> List[ContestEntry]:
        """
        Get top entries, optionally filtered by submission type.
        """
        if count <= 0:
            return []
        
        # Create a copy to avoid modifying the original heap
        temp_heap = self.entries.copy()
        heapq.heapify(temp_heap)
        
        result = []
        while temp_heap and len(result) < count:
            entry = heapq.heappop(temp_heap)
            if submission_type is None or entry.submission_type == submission_type:
                result.append(entry)
        
        return result

    def save_to_file(self, filename: str) -> None:
        """
        Save leaderboard data to a JSON file.
        """
        data = {
            'max_entries': self.max_entries,
            'entries': [
                {
                    'user_id': entry.user_id,
                    'username': entry.username,
                    'score': entry.score,
                    'submission_type': entry.submission_type,
                    'timestamp': entry.timestamp.isoformat()
                }
                for entry in self.entries
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving leaderboard: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'Leaderboard':
        """
        Load leaderboard data from a JSON file.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            leaderboard = cls(data['max_entries'])
            for entry_data in data['entries']:
                entry = ContestEntry(
                    user_id=entry_data['user_id'],
                    username=entry_data['username'],
                    score=entry_data['score'],
                    submission_type=entry_data['submission_type'],
                    timestamp=datetime.fromisoformat(entry_data['timestamp'])
                )
                leaderboard.add_entry(entry)
            
            return leaderboard
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading leaderboard: {e}")
            return cls()  # Return empty leaderboard on error

class ContestSystem:
    """
    Main system for managing HarpyCoin contests.
    """
    def __init__(self):
        self.buy_contest = Leaderboard()
        self.meme_contest = Leaderboard()
        self.shill_contest = Leaderboard()

    def add_submission(self, contest_type: str, user_id: str, username: str, score: float) -> bool:
        """
        Add a submission to the appropriate contest.
        Returns True if submission was added successfully.
        """
        if contest_type not in ['buy', 'meme', 'shill']:
            print(f"Invalid contest type: {contest_type}")
            return False
        
        entry = ContestEntry(
            user_id=user_id,
            username=username,
            score=score,
            submission_type=contest_type,
            timestamp=datetime.now()
        )
        
        if contest_type == 'buy':
            self.buy_contest.add_entry(entry)
        elif contest_type == 'meme':
            self.meme_contest.add_entry(entry)
        elif contest_type == 'shill':
            self.shill_contest.add_entry(entry)
        
        return True

    def get_leaderboard(self, contest_type: str, count: int = 10) -> List[Dict]:
        """
        Get leaderboard for a specific contest type.
        Returns a list of dictionaries with user info and scores.
        """
        if contest_type not in ['buy', 'meme', 'shill']:
            print(f"Invalid contest type: {contest_type}")
            return []
        
        leaderboard = None
        if contest_type == 'buy':
            leaderboard = self.buy_contest
        elif contest_type == 'meme':
            leaderboard = self.meme_contest
        elif contest_type == 'shill':
            leaderboard = self.shill_contest
        
        top_entries = leaderboard.get_top_entries(count)
        
        return [
            {
                'rank': i + 1,
                'user_id': entry.user_id,
                'username': entry.username,
                'score': entry.score,
                'timestamp': entry.timestamp.isoformat()
            }
            for i, entry in enumerate(top_entries)
        ]

    def save_all_contests(self, base_filename: str) -> None:
        """
        Save all contest data to files.
        """
        self.buy_contest.save_to_file(f"{base_filename}_buy.json")
        self.meme_contest.save_to_file(f"{base_filename}_meme.json")
        self.shill_contest.save_to_file(f"{base_filename}_shill.json")

    def load_all_contests(self, base_filename: str) -> None:
        """
        Load all contest data from files.
        """
        self.buy_contest = Leaderboard.load_from_file(f"{base_filename}_buy.json")
        self.meme_contest = Leaderboard.load_from_file(f"{base_filename}_meme.json")
        self.shill_contest = Leaderboard.load_from_file(f"{base_filename}_shill.json")

# Example usage
if __name__ == "__main__":
    system = ContestSystem()
    
    # Add some test submissions
    system.add_submission('buy', 'user1', 'HarpyFan1', 1500.0)
    system.add_submission('buy', 'user2', 'CoinShiller', 2000.0)
    system.add_submission('meme', 'user3', 'MemeLord', 500.0)
    system.add_submission('shill', 'user4', 'ShillMaster', 800.0)
    
    # Get and display leaderboards
    print("Buy Contest Leaderboard:")
    for entry in system.get_leaderboard('buy'):
        print(f"{entry['rank']}. {entry['username']} - {entry['score']}")
    
    print("\nMeme Contest Leaderboard:")
    for entry in system.get_leaderboard('meme'):
        print(f"{entry['rank']}. {entry['username']} - {entry['score']}")
    
    # Save and load data
    system.save_all_contests('harpycoin_contests')
    system.load_all_contests('harpycoin_contests')
```
