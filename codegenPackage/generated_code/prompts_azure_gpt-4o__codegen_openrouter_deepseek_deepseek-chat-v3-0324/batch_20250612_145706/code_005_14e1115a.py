"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Develop a function to track and display the results of active approval votes on the Agora platform, including options selected and vote counts.
Generated: DETERMINISTIC_14e1115ac4524df8
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class ApprovalVoteTracker:
    """
    A class to track and display active approval votes on the Agora platform.
    """

    def __init__(self):
        """
        Initialize the vote tracker with empty data structures.
        """
        self.active_votes: Dict[str, Dict] = {}  # {vote_id: vote_data}
        self.vote_results: Dict[str, Dict[str, int]] = {}  # {vote_id: {option: count}}
        self.voters: Dict[str, List[str]] = defaultdict(list)  # {vote_id: [voter_ids]}

    def add_vote(self, vote_id: str, title: str, description: str, options: List[str], end_time: datetime) -> bool:
        """
        Add a new active vote to be tracked.

        Args:
            vote_id: Unique identifier for the vote
            title: Title of the vote
            description: Description of the vote
            options: List of available options
            end_time: When the vote ends (datetime object)

        Returns:
            bool: True if vote was added successfully, False if vote_id already exists
        """
        if vote_id in self.active_votes:
            return False

        self.active_votes[vote_id] = {
            'title': title,
            'description': description,
            'options': options,
            'end_time': end_time,
            'created_at': datetime.now()
        }
        self.vote_results[vote_id] = {option: 0 for option in options}
        return True

    def cast_vote(self, vote_id: str, voter_id: str, selected_options: List[str]) -> Tuple[bool, Optional[str]]:
        """
        Record a voter's selected options for a vote.

        Args:
            vote_id: ID of the vote being cast
            voter_id: ID of the voter
            selected_options: List of options selected by voter

        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        if vote_id not in self.active_votes:
            return False, "Vote does not exist"

        if voter_id in self.voters[vote_id]:
            return False, "Voter has already participated in this vote"

        vote_data = self.active_votes[vote_id]
        current_time = datetime.now()

        if current_time > vote_data['end_time']:
            return False, "Voting period has ended"

        for option in selected_options:
            if option not in vote_data['options']:
                return False, f"Invalid option: {option}"

        for option in selected_options:
            self.vote_results[vote_id][option] += 1

        self.voters[vote_id].append(voter_id)
        return True, None

    def get_vote_results(self, vote_id: str) -> Tuple[Optional[Dict], Optional[str]]:
        """
        Retrieve the current results for a specific vote.

        Args:
            vote_id: ID of the vote to retrieve results for

        Returns:
            Tuple of (results: Optional[Dict], error_message: Optional[str])
        """
        if vote_id not in self.active_votes:
            return None, "Vote does not exist"

        return self.vote_results[vote_id], None

    def get_active_votes(self) -> Dict[str, Dict]:
        """
        Get all currently active votes.

        Returns:
            Dict of active votes with their metadata
        """
        current_time = datetime.now()
        active = {}
        for vote_id, vote_data in self.active_votes.items():
            if current_time <= vote_data['end_time']:
                active[vote_id] = vote_data
        return active

    def display_vote_results(self, vote_id: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Generate a formatted string displaying vote results.

        Args:
            vote_id: ID of the vote to display

        Returns:
            Tuple of (formatted_results: Optional[str], error_message: Optional[str])
        """
        if vote_id not in self.active_votes:
            return None, "Vote does not exist"

        vote_data = self.active_votes[vote_id]
        results = self.vote_results[vote_id]
        total_voters = len(self.voters[vote_id])

        output = []
        output.append(f"Vote: {vote_data['title']}")
        output.append(f"Description: {vote_data['description']}")
        output.append(f"Total participants: {total_voters}")
        output.append("\nResults:")
        
        for option, count in sorted(results.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_voters * 100) if total_voters > 0 else 0
            output.append(f"- {option}: {count} votes ({percentage:.1f}%)")

        return "\n".join(output), None

    def save_to_file(self, filename: str) -> bool:
        """
        Save the current vote data to a JSON file.

        Args:
            filename: Path to the output file

        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            data = {
                'active_votes': self.active_votes,
                'vote_results': self.vote_results,
                'voters': dict(self.voters)
            }
            # Convert datetime objects to strings
            for vote_id, vote_data in data['active_votes'].items():
                vote_data['end_time'] = vote_data['end_time'].isoformat()
                vote_data['created_at'] = vote_data['created_at'].isoformat()

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """
        Load vote data from a JSON file.

        Args:
            filename: Path to the input file

        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            # Convert string timestamps back to datetime objects
            for vote_id, vote_data in data['active_votes'].items():
                vote_data['end_time'] = datetime.fromisoformat(vote_data['end_time'])
                vote_data['created_at'] = datetime.fromisoformat(vote_data['created_at'])

            self.active_votes = data['active_votes']
            self.vote_results = data['vote_results']
            self.voters = defaultdict(list, data['voters'])
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False
```
