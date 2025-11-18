"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Generate code for a community-based voting system to manage decisions for a cryptocurrency token, inspired by the decentralized nature of "Rich Pepe."
Generated: DETERMINISTIC_52dd473feb1d03dd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Community Voting System for Cryptocurrency Token
Inspired by decentralized decision-making.
"""

import json
from datetime import datetime, timedelta


class VotingSystem:
    """
    A class to manage a community-based voting system.
    """

    def __init__(self, duration_in_days=7):
        """
        Initializes the voting system.

        :param duration_in_days: Voting duration in days (default: 7 days)
        """
        self.proposals = {}  # Dictionary to store proposals
        self.duration = timedelta(days=duration_in_days)  # Voting duration

    def create_proposal(self, proposal_id, title, description, creator):
        """
        Creates a new proposal for voting.

        :param proposal_id: Unique ID for the proposal
        :param title: Title of the proposal
        :param description: Description of the proposal
        :param creator: Creator's name or wallet address
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal with ID {proposal_id} already exists.")

        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "creator": creator,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + self.duration,
            "votes": {"yes": 0, "no": 0},
        }

    def vote(self, proposal_id, vote_type):
        """
        Cast a vote on a proposal.

        :param proposal_id: ID of the proposal to vote on
        :param vote_type: Type of vote ('yes' or 'no')
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal with ID {proposal_id} does not exist.")

        proposal = self.proposals[proposal_id]

        if datetime.now() > proposal["expires_at"]:
            raise ValueError("Voting has expired for this proposal.")

        if vote_type not in ["yes", "no"]:
            raise ValueError("Invalid vote type. Use 'yes' or 'no'.")

        proposal["votes"][vote_type] += 1

    def get_results(self, proposal_id):
        """
        Retrieves the results of a proposal's vote.

        :param proposal_id: ID of the proposal to retrieve results for
        :return: Results dictionary containing votes and decision status
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal with ID {proposal_id} does not exist.")

        proposal = self.proposals[proposal_id]

        if datetime.now() <= proposal["expires_at"]:
            raise ValueError("Voting is still ongoing for this proposal.")

        # Determine the decision
        if proposal["votes"]["yes"] > proposal["votes"]["no"]:
            decision = "Approved"
        elif proposal["votes"]["no"] > proposal["votes"]["yes"]:
            decision = "Rejected"
        else:
            decision = "Tied"

        return {
            "title": proposal["title"],
            "description": proposal["description"],
            "votes": proposal["votes"],
            "decision": decision,
        }

    def save_proposals_to_file(self, file_path):
        """
        Saves all proposals to a file in JSON format.

        :param file_path: Path to the file where proposals will be saved
        """
        with open(file_path, "w") as file:
            json.dump(self.proposals, file, default=str, indent=4)

    def load_proposals_from_file(self, file_path):
        """
        Loads proposals from a file in JSON format.

        :param file_path: Path to the file to load proposals from
        """
        with open(file_path, "r") as file:
            self.proposals = json.load(file)


# Example usage:
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()

        # Create a proposal
        voting_system.create_proposal(
            proposal_id="P001",
            title="Increase Block Size",
            description="Proposal to increase the block size from 1MB to 2MB.",
            creator="User123",
        )

        # Cast votes
        voting_system.vote(proposal_id="P001", vote_type="yes")
        voting_system.vote(proposal_id="P001", vote_type="no")
        voting_system.vote(proposal_id="P001", vote_type="yes")

        # Wait for voting to expire (simulate by changing duration or time)
        # Retrieve results
        results = voting_system.get_results(proposal_id="P001")
        print("Voting Results:", results)

        # Save and load proposals for persistence
        voting_system.save_proposals_to_file("proposals.json")
        voting_system.load_proposals_from_file("proposals.json")

    except Exception as e:
        print("Error:", str(e))
```
