"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave-amber.vercel.app
Prompt: Write code to implement governance voting functionality for an Aave-like protocol.
Generated: DETERMINISTIC_9b559a92898f1c50
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List, Union

class GovernanceVoting:
    """
    A class to implement governance voting functionality for a protocol similar to Aave.
    """

    def __init__(self):
        # Store ongoing proposals and their details
        self.proposals = {}  # {proposal_id: {"description": str, "votes": {"yes": int, "no": int}, "end_time": int}}
        # Store votes by users to prevent double voting
        self.votes_by_user = {}  # {user_address: {proposal_id: "yes" or "no"}}
        self.proposal_count = 0  # Track the number of proposals

    def create_proposal(self, proposer: str, description: str, voting_duration: int) -> int:
        """
        Create a new governance proposal.

        Args:
            proposer (str): Address of the proposer.
            description (str): Description of the proposal.
            voting_duration (int): Duration of the voting period in seconds.

        Returns:
            int: Proposal ID of the newly created proposal.
        """
        # Generate a unique proposal ID
        proposal_id = self.proposal_count
        self.proposals[proposal_id] = {
            "description": description,
            "votes": {"yes": 0, "no": 0},
            "end_time": time.time() + voting_duration
        }
        self.proposal_count += 1
        return proposal_id

    def vote(self, user_address: str, proposal_id: int, vote: str) -> Union[bool, str]:
        """
        Cast a vote on a proposal.

        Args:
            user_address (str): Address of the user casting the vote.
            proposal_id (int): ID of the proposal to vote on.
            vote (str): Vote choice, must be either "yes" or "no".

        Returns:
            Union[bool, str]: True if the vote was successfully cast, otherwise an error message.
        """
        # Validate vote choice
        if vote.lower() not in ["yes", "no"]:
            return "Invalid vote choice. Must be 'yes' or 'no'."

        # Check if the proposal exists
        if proposal_id not in self.proposals:
            return "Proposal does not exist."

        # Check if the voting period is still active
        if time.time() > self.proposals[proposal_id]["end_time"]:
            return "Voting period for this proposal has ended."

        # Check if the user has already voted
        if user_address in self.votes_by_user and proposal_id in self.votes_by_user[user_address]:
            return "User has already voted on this proposal."

        # Cast the vote
        self.proposals[proposal_id]["votes"][vote.lower()] += 1
        
        # Record the user's vote
        if user_address not in self.votes_by_user:
            self.votes_by_user[user_address] = {}
        self.votes_by_user[user_address][proposal_id] = vote.lower()

        return True

    def get_proposal_status(self, proposal_id: int) -> Union[Dict[str, Union[str, int]], str]:
        """
        Retrieve the status of a proposal.

        Args:
            proposal_id (int): ID of the proposal.

        Returns:
            Union[Dict[str, Union[str, int]], str]: Proposal details if it exists, otherwise an error message.
        """
        # Check if the proposal exists
        if proposal_id not in self.proposals:
            return "Proposal does not exist."

        return self.proposals[proposal_id]

    def get_results(self, proposal_id: int) -> Union[Dict[str, Union[int, str]], str]:
        """
        Calculate and return the voting results of a proposal.

        Args:
            proposal_id (int): ID of the proposal.

        Returns:
            Union[Dict[str, Union[int, str]], str]: Voting results if the proposal exists and voting has ended,
            otherwise an error message.
        """
        # Check if the proposal exists
        if proposal_id not in self.proposals:
            return "Proposal does not exist."

        # Check if voting has ended
        if time.time() <= self.proposals[proposal_id]["end_time"]:
            return "Voting period for this proposal is still ongoing."

        votes = self.proposals[proposal_id]["votes"]
        total_votes = votes["yes"] + votes["no"]
        result = "approved" if votes["yes"] > votes["no"] else "rejected"

        return {
            "description": self.proposals[proposal_id]["description"],
            "total_votes": total_votes,
            "yes_votes": votes["yes"],
            "no_votes": votes["no"],
            "result": result
        }


# Example usage:
# governance = GovernanceVoting()
# proposal_id = governance.create_proposal("0xProposerAddress", "Increase liquidity pool rewards", 3600)
# print(governance.vote("0xUserAddress1", proposal_id, "yes"))
# print(governance.vote("0xUserAddress2", proposal_id, "no"))
# time.sleep(3600)  # Wait for voting to end
# print(governance.get_results(proposal_id))
```
