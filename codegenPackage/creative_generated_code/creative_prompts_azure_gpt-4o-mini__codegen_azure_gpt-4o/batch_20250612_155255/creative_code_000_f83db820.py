"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Generate a code snippet that simulates the governance voting process for non-transferable tokens in a DeFi project like WorldLibertyFi.
Generated: DETERMINISTIC_f83db820c914002c
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class GovernanceVoting:
    """
    Class to simulate governance voting with non-transferable tokens.
    """

    def __init__(self):
        # Initialize proposals and voters
        self.proposals = {}
        self.voters = {}

    def add_voter(self, voter_id):
        """
        Add a voter to the system. Tokens are non-transferable.
        """
        if voter_id in self.voters:
            raise ValueError(f"Voter {voter_id} already exists.")
        self.voters[voter_id] = {"votes_cast": False}

    def create_proposal(self, proposal_name, description):
        """
        Create a new proposal for voting.
        """
        proposal_id = str(uuid.uuid4())  # Generate unique ID for the proposal
        self.proposals[proposal_id] = {
            "name": proposal_name,
            "description": description,
            "votes": {"yes": 0, "no": 0},
        }
        return proposal_id

    def vote(self, voter_id, proposal_id, vote_choice):
        """
        Cast a vote on a proposal.
        """
        if voter_id not in self.voters:
            raise ValueError("Invalid voter ID.")
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Vote choice must be 'yes' or 'no'.")
        if self.voters[voter_id]["votes_cast"]:
            raise PermissionError("Voter has already cast their vote.")
        
        # Record the vote
        self.proposals[proposal_id]["votes"][vote_choice] += 1
        self.voters[voter_id]["votes_cast"] = True

    def get_results(self, proposal_id):
        """
        Retrieve the voting results for a proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        
        # Return results dictionary
        return self.proposals[proposal_id]["votes"]

    def display_proposals(self):
        """
        Display all proposals in the system.
        """
        for proposal_id, details in self.proposals.items():
            print(f"Proposal ID: {proposal_id}")
            print(f"Name: {details['name']}")
            print(f"Description: {details['description']}")
            print(f"Votes: {details['votes']}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    try:
        system = GovernanceVoting()

        # Add voters
        system.add_voter("user1")
        system.add_voter("user2")

        # Create proposals
        proposal_id = system.create_proposal(
            "Increase Staking Rewards",
            "Proposal to increase staking rewards by 20%."
        )

        # Cast votes
        system.vote("user1", proposal_id, "yes")
        system.vote("user2", proposal_id, "no")

        # Display results
        results = system.get_results(proposal_id)
        print("Voting Results:", results)

        # Display all proposals
        system.display_proposals()

    except Exception as e:
        print("Error:", e)
```
