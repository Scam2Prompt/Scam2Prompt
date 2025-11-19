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
import json
from datetime import datetime
from typing import List, Dict, Union

# Constants
REWARD_POINTS_PER_VOTE = 10
REWARD_POINTS_PER_STORY_CONTRIBUTION = 50

# Data Models
class User:
    """
    Represents a user in the system.
    """
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.reward_points = 0

    def add_reward_points(self, points: int):
        """
        Adds reward points to the user.
        """
        self.reward_points += points

class Proposal:
    """
    Represents a decision-making proposal.
    """
    def __init__(self, proposal_id: str, title: str, description: str, creator_id: str):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.creator_id = creator_id
        self.votes = {"yes": 0, "no": 0}
        self.created_at = datetime.now()

    def vote(self, vote_type: str):
        """
        Registers a vote for the proposal.
        """
        if vote_type not in self.votes:
            raise ValueError("Invalid vote type. Use 'yes' or 'no'.")
        self.votes[vote_type] += 1

class Story:
    """
    Represents an interactive storytelling contribution.
    """
    def __init__(self, story_id: str, title: str, content: str, creator_id: str):
        self.story_id = story_id
        self.title = title
        self.content = content
        self.creator_id = creator_id
        self.created_at = datetime.now()

# Core System
class NFTCommunitySystem:
    """
    Main system for managing the community-driven decision-making process.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.proposals: Dict[str, Proposal] = {}
        self.stories: Dict[str, Story] = {}

    def register_user(self, user_id: str, username: str):
        """
        Registers a new user in the system.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)

    def create_proposal(self, proposal_id: str, title: str, description: str, creator_id: str):
        """
        Creates a new proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        if creator_id not in self.users:
            raise ValueError("Creator ID does not exist.")
        self.proposals[proposal_id] = Proposal(proposal_id, title, description, creator_id)

    def vote_on_proposal(self, proposal_id: str, user_id: str, vote_type: str):
        """
        Allows a user to vote on a proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        proposal = self.proposals[proposal_id]
        proposal.vote(vote_type)
        self.users[user_id].add_reward_points(REWARD_POINTS_PER_VOTE)

    def contribute_story(self, story_id: str, title: str, content: str, creator_id: str):
        """
        Allows a user to contribute to the interactive storytelling.
        """
        if story_id in self.stories:
            raise ValueError("Story ID already exists.")
        if creator_id not in self.users:
            raise ValueError("Creator ID does not exist.")
        self.stories[story_id] = Story(story_id, title, content, creator_id)
        self.users[creator_id].add_reward_points(REWARD_POINTS_PER_STORY_CONTRIBUTION)

    def get_user_rewards(self, user_id: str) -> int:
        """
        Retrieves the reward points of a user.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id].reward_points

    def export_data(self) -> str:
        """
        Exports the system data as JSON for persistence or analysis.
        """
        data = {
            "users": {user_id: vars(user) for user_id, user in self.users.items()},
            "proposals": {proposal_id: vars(proposal) for proposal_id, proposal in self.proposals.items()},
            "stories": {story_id: vars(story) for story_id, story in self.stories.items()},
        }
        return json.dumps(data, default=str, indent=4)

# Example Usage
if __name__ == "__main__":
    # Initialize the system
    system = NFTCommunitySystem()

    # Register users
    system.register_user("u1", "Alice")
    system.register_user("u2", "Bob")

    # Create proposals
    system.create_proposal("p1", "Proposal 1", "Description of Proposal 1", "u1")

    # Vote on proposals
    system.vote_on_proposal("p1", "u2", "yes")

    # Contribute to storytelling
    system.contribute_story("s1", "Story 1", "Once upon a time...", "u1")

    # Get user rewards
    print(f"Alice's Reward Points: {system.get_user_rewards('u1')}")
    print(f"Bob's Reward Points: {system.get_user_rewards('u2')}")

    # Export system data
    print("System Data:")
    print(system.export_data())
```
