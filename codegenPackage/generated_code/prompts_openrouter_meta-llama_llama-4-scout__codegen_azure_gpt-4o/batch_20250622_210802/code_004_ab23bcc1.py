"""
Generated Code Metadata:
========================
Original URL: https://anyinuairdrop.pages.dev
Prompt: Develop a community governance system for a cryptocurrency project, incorporating features like voting, proposals, and community engagement, inspired by Any Inu's community-driven approach.
Generated: DETERMINISTIC_ab23bcc18aa21931
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_governance.py

import json
from datetime import datetime, timedelta

class CommunityGovernance:
    """
    A class to manage community governance for a cryptocurrency project.
    Features include proposal creation, voting, and community engagement.
    """

    def __init__(self):
        """
        Initializes the governance system with empty proposals and members.
        """
        self.proposals = {}  # Dictionary to store proposals
        self.members = set()  # Set to store community members

    def add_member(self, member_id):
        """
        Adds a new member to the community.
        :param member_id: Unique identifier for the member (e.g., wallet address).
        """
        if member_id in self.members:
            raise ValueError("Member already exists.")
        self.members.add(member_id)

    def create_proposal(self, proposal_id, title, description, creator_id, duration_days=7):
        """
        Creates a new proposal for voting.
        :param proposal_id: Unique identifier for the proposal.
        :param title: Title of the proposal.
        :param description: Detailed description of the proposal.
        :param creator_id: ID of the member creating the proposal.
        :param duration_days: Duration of the voting period in days (default is 7 days).
        """
        if creator_id not in self.members:
            raise ValueError("Creator must be a registered member.")
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        
        end_time = datetime.now() + timedelta(days=duration_days)
        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "creator_id": creator_id,
            "votes": {"yes": 0, "no": 0},
            "end_time": end_time,
            "voters": set()  # Track who has voted
        }

    def vote(self, proposal_id, member_id, vote_choice):
        """
        Casts a vote on a proposal.
        :param proposal_id: ID of the proposal to vote on.
        :param member_id: ID of the member casting the vote.
        :param vote_choice: Choice of vote ("yes" or "no").
        """
        if member_id not in self.members:
            raise ValueError("Member must be registered to vote.")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        if datetime.now() > proposal["end_time"]:
            raise ValueError("Voting period has ended.")
        if member_id in proposal["voters"]:
            raise ValueError("Member has already voted on this proposal.")
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Invalid vote choice. Use 'yes' or 'no'.")
        
        proposal["votes"][vote_choice] += 1
        proposal["voters"].add(member_id)

    def get_proposal_results(self, proposal_id):
        """
        Retrieves the results of a proposal.
        :param proposal_id: ID of the proposal to retrieve results for.
        :return: Dictionary containing the proposal details and voting results.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        if datetime.now() <= proposal["end_time"]:
            raise ValueError("Voting period is still ongoing.")
        
        return {
            "title": proposal["title"],
            "description": proposal["description"],
            "creator_id": proposal["creator_id"],
            "votes": proposal["votes"],
            "end_time": proposal["end_time"].strftime("%Y-%m-%d %H:%M:%S")
        }

    def list_proposals(self):
        """
        Lists all proposals in the system.
        :return: List of proposals with basic details.
        """
        return [
            {
                "proposal_id": proposal_id,
                "title": proposal["title"],
                "description": proposal["description"],
                "end_time": proposal["end_time"].strftime("%Y-%m-%d %H:%M:%S"),
                "votes": proposal["votes"]
            }
            for proposal_id, proposal in self.proposals.items()
        ]

# Example usage
if __name__ == "__main__":
    try:
        governance = CommunityGovernance()
        
        # Add members
        governance.add_member("member1")
        governance.add_member("member2")
        
        # Create a proposal
        governance.create_proposal(
            proposal_id="proposal1",
            title="Increase Staking Rewards",
            description="Proposal to increase staking rewards by 10%.",
            creator_id="member1"
        )
        
        # Cast votes
        governance.vote("proposal1", "member1", "yes")
        governance.vote("proposal1", "member2", "no")
        
        # List proposals
        print(json.dumps(governance.list_proposals(), indent=4))
        
        # Get proposal results (after voting period ends)
        # Uncomment the line below after the voting period ends
        # print(json.dumps(governance.get_proposal_results("proposal1"), indent=4))
    except Exception as e:
        print(f"Error: {e}")
```
