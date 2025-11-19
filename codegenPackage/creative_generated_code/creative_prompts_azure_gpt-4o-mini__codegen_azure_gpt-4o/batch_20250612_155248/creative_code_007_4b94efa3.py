"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invest-destreams.web.app
Prompt: Generate a code snippet for a voting mechanism that allows token holders to propose changes in a decentralized streaming platform like DeeStream.
Generated: DETERMINISTIC_4b94efa38f461fb4
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, List, Optional

class VotingSystem:
    """
    A class representing a voting mechanism for token holders to propose and vote on changes.
    """

    def __init__(self):
        # Dictionary to store proposals with their details
        self.proposals: Dict[int, Dict] = {}
        # Counter for proposal IDs
        self.proposal_id_counter = 0

    def create_proposal(self, proposer: str, title: str, description: str, deadline: datetime.datetime) -> int:
        """
        Allows a token holder to create a new proposal.
        
        Args:
            proposer (str): The address or ID of the proposer.
            title (str): Title of the proposal.
            description (str): Details of the proposal.
            deadline (datetime.datetime): Voting deadline for the proposal.

        Returns:
            int: Unique ID of the created proposal.
        """
        if deadline <= datetime.datetime.now():
            raise ValueError("Deadline must be in the future.")

        self.proposal_id_counter += 1
        self.proposals[self.proposal_id_counter] = {
            "proposer": proposer,
            "title": title,
            "description": description,
            "deadline": deadline,
            "votes": {"yes": 0, "no": 0},
            "voters": set()  # To prevent double voting
        }

        return self.proposal_id_counter

    def vote(self, proposal_id: int, voter: str, vote: str) -> str:
        """
        Allows a token holder to cast a vote.

        Args:
            proposal_id (int): ID of the proposal to vote on.
            voter (str): The address or ID of the voter.
            vote (str): The vote cast by the voter ('yes' or 'no').

        Returns:
            str: Confirmation message upon successful voting.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        proposal = self.proposals[proposal_id]

        if datetime.datetime.now() > proposal["deadline"]:
            raise ValueError("Voting period has ended.")
        
        if voter in proposal["voters"]:
            raise ValueError("Voter has already cast a vote.")
        
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote. Must be 'yes' or 'no'.")

        # Register the vote
        proposal["votes"][vote] += 1
        proposal["voters"].add(voter)

        return f"Vote '{vote}' successfully cast for proposal ID {proposal_id}."

    def get_proposal_result(self, proposal_id: int) -> Dict[str, Optional[str]]:
        """
        Retrieves the result of a proposal.

        Args:
            proposal_id (int): ID of the proposal.

        Returns:
            Dict[str, Optional[str]]: A dictionary with the results of the proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id]

        if datetime.datetime.now() <= proposal["deadline"]:
            return {"result": None, "message": "Voting is still ongoing."}

        # Determine the result
        yes_votes = proposal["votes"]["yes"]
        no_votes = proposal["votes"]["no"]

        if yes_votes > no_votes:
            result = "Accepted"
        elif no_votes > yes_votes:
            result = "Rejected"
        else:
            result = "Tie"

        return {
            "title": proposal["title"],
            "description": proposal["description"],
            "result": result,
            "yes_votes": yes_votes,
            "no_votes": no_votes
        }

# Example usage (this section should not be included in production code):
if __name__ == "__main__":
    voting_system = VotingSystem()
    
    try:
        proposal_id = voting_system.create_proposal(
            proposer="0x123TokenHolder",
            title="Reduce Streaming Fees",
            description="Proposal to reduce streaming fees by 10%.",
            deadline=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        print(f"Proposal created with ID: {proposal_id}")
        
        print(voting_system.vote(proposal_id, voter="0x456Voter", vote="yes"))
        print(voting_system.vote(proposal_id, voter="0x789Voter", vote="no"))
        
        results = voting_system.get_proposal_result(proposal_id)
        print("Proposal Results:", results)
    except Exception as e:
        print(f"Error: {e}")
```
