"""
Generated Code Metadata:
========================
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Write a Python script to create a simple voting system for a digital character event, similar to the Palio voting event described on Xterio.
Generated: DETERMINISTIC_cd00d7be68cb88e5
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class VotingSystem:
    """
    A simple voting system for digital character events.
    """
    
    def __init__(self, candidates: List[str], data_file: str = "voting_data.json"):
        """
        Initialize the voting system with candidates and data file.
        
        Args:
            candidates: List of candidate names to vote for
            data_file: File to store voting data (default: voting_data.json)
        """
        self.candidates = candidates
        self.data_file = data_file
        self.votes: Dict[str, int] = {candidate: 0 for candidate in candidates}
        self.voters: Dict[str, str] = {}  # voter_id: candidate
        
        # Load existing data if file exists
        self._load_data()
    
    def _load_data(self) -> None:
        """Load voting data from file if it exists."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.votes = data.get('votes', self.votes)
                    self.voters = data.get('voters', self.voters)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load voting data - {e}")
    
    def _save_data(self) -> None:
        """Save current voting data to file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({
                    'votes': self.votes,
                    'voters': self.voters
                }, f, indent=2)
        except IOError as e:
            print(f"Error: Could not save voting data - {e}")
    
    def vote(self, voter_id: str, candidate: str) -> bool:
        """
        Cast a vote for a candidate.
        
        Args:
            voter_id: Unique identifier for the voter
            candidate: Candidate to vote for
            
        Returns:
            bool: True if vote was successful, False otherwise
        """
        if voter_id in self.voters:
            print(f"Error: Voter {voter_id} has already voted.")
            return False
        
        if candidate not in self.votes:
            print(f"Error: Invalid candidate {candidate}.")
            return False
        
        self.votes[candidate] += 1
        self.voters[voter_id] = candidate
        self._save_data()
        return True
    
    def get_results(self) -> Dict[str, int]:
        """
        Get current voting results.
        
        Returns:
            Dict[str, int]: Dictionary of candidate names and their vote counts
        """
        return self.votes
    
    def has_voted(self, voter_id: str) -> bool:
        """
        Check if a voter has already voted.
        
        Args:
            voter_id: Unique identifier for the voter
            
        Returns:
            bool: True if voter has voted, False otherwise
        """
        return voter_id in self.voters
    
    def get_voter_choice(self, voter_id: str) -> Optional[str]:
        """
        Get the candidate a voter has voted for.
        
        Args:
            voter_id: Unique identifier for the voter
            
        Returns:
            Optional[str]: Candidate name if voter has voted, None otherwise
        """
        return self.voters.get(voter_id)


def main():
    """Example usage of the VotingSystem."""
    # Example candidates
    candidates = ["Character A", "Character B", "Character C"]
    
    # Initialize voting system
    voting_system = VotingSystem(candidates)
    
    # Example voting
    voting_system.vote("user1", "Character A")
    voting_system.vote("user2", "Character B")
    voting_system.vote("user3", "Character A")
    
    # Try duplicate vote
    voting_system.vote("user1", "Character C")  # Should fail
    
    # Get results
    results = voting_system.get_results()
    print("Current voting results:")
    for candidate, votes in results.items():
        print(f"{candidate}: {votes} votes")


if __name__ == "__main__":
    main()
```
