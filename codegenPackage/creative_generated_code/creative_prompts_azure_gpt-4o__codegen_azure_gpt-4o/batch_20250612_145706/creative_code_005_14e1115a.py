"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Develop a function to track and display the results of active approval votes on the Agora platform, including options selected and vote counts.
Generated: DETERMINISTIC_14e1115ac4524df8
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List

# Define a class to manage approval votes
class ApprovalVoteTracker:
    def __init__(self):
        """
        Initializes a new instance of ApprovalVoteTracker.
        Keeps track of active votes and their counts.
        """
        # Dictionary to store votes in the format:
        # {vote_id: {"options": {"option1": count1, "option2": count2}, "description": "description"}}
        self.active_votes: Dict[str, Dict] = {}

    def add_vote(self, vote_id: str, description: str, options: List[str]) -> None:
        """
        Adds a new vote to the tracker.
        
        Args:
            vote_id (str): A unique identifier for the vote.
            description (str): A description of the vote.
            options (List[str]): A list of options for the vote.
        
        Raises:
            ValueError: If the vote_id is already present.
        """
        if vote_id in self.active_votes:
            raise ValueError(f"Vote with ID '{vote_id}' already exists.")
        
        # Initialize the vote with options and zero counts
        self.active_votes[vote_id] = {
            "description": description,
            "options": {option: 0 for option in options}
        }

    def cast_vote(self, vote_id: str, option: str) -> None:
        """
        Casts a vote for a specific option.
        
        Args:
            vote_id (str): The ID of the vote to cast a vote for.
            option (str): The option being voted for.

        Raises:
            KeyError: If the vote_id is not found or option is invalid.
        """
        if vote_id not in self.active_votes:
            raise KeyError(f"No active vote found with ID '{vote_id}'.")
        if option not in self.active_votes[vote_id]["options"]:
            raise KeyError(f"Option '{option}' not found in vote '{vote_id}'.")
        
        # Increment the vote count for the specified option
        self.active_votes[vote_id]["options"][option] += 1

    def display_results(self, vote_id: str) -> None:
        """
        Displays the current results of a vote.
        
        Args:
            vote_id (str): The ID of the vote to display results for.

        Raises:
            KeyError: If the vote_id is not found.
        """
        if vote_id not in self.active_votes:
            raise KeyError(f"No active vote found with ID '{vote_id}'.")
        
        # Fetch the vote details
        vote_details = self.active_votes[vote_id]
        print(f"Vote ID: {vote_id}")
        print(f"Description: {vote_details['description']}")
        print("Results:")
        for option, count in vote_details["options"].items():
            print(f"  {option}: {count} votes")

    def remove_vote(self, vote_id: str) -> None:
        """
        Removes a vote from the tracker.
        
        Args:
            vote_id (str): The ID of the vote to remove.

        Raises:
            KeyError: If the vote_id is not found.
        """
        if vote_id not in self.active_votes:
            raise KeyError(f"No active vote found with ID '{vote_id}'.")
        
        # Remove the vote
        del self.active_votes[vote_id]


# Example usage:
if __name__ == "__main__":
    # Initialize the tracker
    tracker = ApprovalVoteTracker()

    # Add a new vote
    tracker.add_vote("vote1", "Approval for Project X", ["Approve", "Reject", "Abstain"])

    # Cast votes
    tracker.cast_vote("vote1", "Approve")
    tracker.cast_vote("vote1", "Approve")
    tracker.cast_vote("vote1", "Reject")

    # Display results
    tracker.display_results("vote1")

    # Remove the vote
    tracker.remove_vote("vote1")
```
