"""
Generated Code Metadata:
========================
Original URL: https://bafybeibpiht7izgwflj7ruju4tcwrl7b45xmoifhhch7hi47n5ip5du4c4.ipfs.dweb.link
Prompt: Illustrate how to implement a community voting system for a cryptocurrency project, taking cues from the SharkCat community ownership model.
Generated: DETERMINISTIC_d28eb38d48f1e1df
Batch ID: 20250612_161035
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

class VotingSystem:
    """
    A community voting system for a cryptocurrency project.
    """

    def __init__(self):
        """
        Initialize the voting system with an empty list of proposals and votes.
        """
        self.proposals = {}  # Dictionary to store proposals and their details
        self.votes = {}      # Dictionary to store votes for each proposal

    def create_proposal(self, proposal_id, title, description, creator):
        """
        Create a new proposal for voting.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            title (str): Title of the proposal.
            description (str): Detailed description of the proposal.
            creator (str): Address or identifier of the proposal creator.

        Returns:
            dict: The created proposal details.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")

        proposal = {
            "proposal_id": proposal_id,
            "title": title,
            "description": description,
            "creator": creator,
            "created_at": datetime.now().isoformat(),
            "votes": {"yes": 0, "no": 0}
        }
        self.proposals[proposal_id] = proposal
        self.votes[proposal_id] = {}
        return proposal

    def cast_vote(self, proposal_id, voter_id, vote):
        """
        Cast a vote for a proposal.

        Args:
            proposal_id (str): The ID of the proposal to vote on.
            voter_id (str): Unique identifier for the voter.
            vote (str): Vote choice, either "yes" or "no".

        Returns:
            str: Confirmation message.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")

        if voter_id in self.votes[proposal_id]:
            raise ValueError("Voter has already cast a vote for this proposal.")

        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote. Must be 'yes' or 'no'.")

        # Record the vote
        self.votes[proposal_id][voter_id] = vote
        self.proposals[proposal_id]["votes"][vote] += 1
        return f"Vote '{vote}' cast successfully by voter '{voter_id}' for proposal '{proposal_id}'."

    def get_proposal_results(self, proposal_id):
        """
        Get the voting results for a proposal.

        Args:
            proposal_id (str): The ID of the proposal.

        Returns:
            dict: Voting results for the proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")

        return {
            "proposal_id": proposal_id,
            "title": self.proposals[proposal_id]["title"],
            "votes": self.proposals[proposal_id]["votes"]
        }

    def export_data(self, file_path):
        """
        Export all proposals and votes to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.

        Returns:
            str: Confirmation message.
        """
        data = {
            "proposals": self.proposals,
            "votes": self.votes
        }
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            return f"Data successfully exported to {file_path}."
        except Exception as e:
            raise IOError(f"Failed to export data: {e}")

    def import_data(self, file_path):
        """
        Import proposals and votes from a JSON file.

        Args:
            file_path (str): Path to the file containing data.

        Returns:
            str: Confirmation message.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.proposals = data.get("proposals", {})
                self.votes = data.get("votes", {})
            return f"Data successfully imported from {file_path}."
        except Exception as e:
            raise IOError(f"Failed to import data: {e}")


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Create a proposal
    proposal = voting_system.create_proposal(
        proposal_id="proposal_1",
        title="Increase Staking Rewards",
        description="Proposal to increase staking rewards by 10%.",
        creator="creator_address_123"
    )
    print("Proposal Created:", proposal)

    # Cast votes
    try:
        print(voting_system.cast_vote("proposal_1", "voter_1", "yes"))
        print(voting_system.cast_vote("proposal_1", "voter_2", "no"))
    except ValueError as e:
        print("Error:", e)

    # Get proposal results
    results = voting_system.get_proposal_results("proposal_1")
    print("Proposal Results:", results)

    # Export data
    try:
        print(voting_system.export_data("voting_data.json"))
    except IOError as e:
        print("Error:", e)

    # Import data
    try:
        print(voting_system.import_data("voting_data.json"))
    except IOError as e:
        print("Error:", e)
```
