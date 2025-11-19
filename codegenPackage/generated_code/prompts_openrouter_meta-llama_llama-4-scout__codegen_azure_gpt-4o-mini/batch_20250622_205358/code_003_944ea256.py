"""
Generated Code Metadata:
========================
Original URL: https://acte.now.sh
Prompt: Design a community-driven decision-making system for an NFT project, incorporating elements of gamification, rewards, and interactive storytelling, inspired by ACTE's approach.
Generated: DETERMINISTIC_944ea25642860434
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class DecisionMakingSystem:
    def __init__(self):
        """Initialize the decision-making system with empty lists for members and proposals."""
        self.members: List[str] = []
        self.proposals: List[Dict[str, Any]] = []
        self.votes: Dict[str, Dict[str, int]] = {}

    def add_member(self, member: str) -> None:
        """Add a new member to the community.

        Args:
            member (str): The name of the member to add.
        """
        if member not in self.members:
            self.members.append(member)
            print(f"Member {member} added.")
        else:
            print(f"Member {member} already exists.")

    def create_proposal(self, title: str, description: str) -> None:
        """Create a new proposal for the community to vote on.

        Args:
            title (str): The title of the proposal.
            description (str): A description of the proposal.
        """
        proposal = {
            'title': title,
            'description': description,
            'votes': {}
        }
        self.proposals.append(proposal)
        print(f"Proposal '{title}' created.")

    def vote(self, member: str, proposal_title: str, vote: str) -> None:
        """Vote on a proposal.

        Args:
            member (str): The name of the member voting.
            proposal_title (str): The title of the proposal being voted on.
            vote (str): The vote ('yes' or 'no').
        """
        if member not in self.members:
            print(f"Member {member} is not part of the community.")
            return

        proposal = next((p for p in self.proposals if p['title'] == proposal_title), None)
        if not proposal:
            print(f"Proposal '{proposal_title}' does not exist.")
            return

        if member in proposal['votes']:
            print(f"Member {member} has already voted on '{proposal_title}'.")
            return

        proposal['votes'][member] = vote
        print(f"Member {member} voted '{vote}' on proposal '{proposal_title}'.")

    def tally_votes(self, proposal_title: str) -> Dict[str, int]:
        """Tally the votes for a proposal.

        Args:
            proposal_title (str): The title of the proposal to tally votes for.

        Returns:
            Dict[str, int]: A dictionary with the vote counts.
        """
        proposal = next((p for p in self.proposals if p['title'] == proposal_title), None)
        if not proposal:
            print(f"Proposal '{proposal_title}' does not exist.")
            return {}

        yes_votes = sum(1 for vote in proposal['votes'].values() if vote == 'yes')
        no_votes = sum(1 for vote in proposal['votes'].values() if vote == 'no')
        return {'yes': yes_votes, 'no': no_votes}

    def reward_members(self) -> None:
        """Reward members based on their participation in voting."""
        for member in self.members:
            if member in self.votes:
                # Simple reward mechanism: 10 points for voting
                self.votes[member]['points'] += 10
                print(f"Member {member} rewarded with 10 points for voting.")

    def interactive_storytelling(self) -> str:
        """Generate a random story based on community decisions.

        Returns:
            str: A generated story based on the proposals and votes.
        """
        if not self.proposals:
            return "No proposals to create a story from."

        story_elements = [f"Proposal '{p['title']}' was voted on with {len(p['votes'])} votes." for p in self.proposals]
        return " ".join(story_elements)

# Example usage
if __name__ == "__main__":
    system = DecisionMakingSystem()
    system.add_member("Alice")
    system.add_member("Bob")
    system.create_proposal("Launch New NFT", "Proposal to launch a new NFT collection.")
    system.vote("Alice", "Launch New NFT", "yes")
    system.vote("Bob", "Launch New NFT", "no")
    print(system.tally_votes("Launch New NFT"))
    system.reward_members()
    print(system.interactive_storytelling())
```
