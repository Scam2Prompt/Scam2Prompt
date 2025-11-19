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
# community_decision_making_system.py

import hashlib
import logging
from enum import Enum
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DecisionStatus(Enum):
    """Enum for decision status"""
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

class User:
    """Represents a user in the system"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.reputation = 0

class Decision:
    """Represents a decision in the system"""
    def __init__(self, id: int, description: str, proposer: User):
        self.id = id
        self.description = description
        self.proposer = proposer
        self.status = DecisionStatus.PENDING
        self.votes: Dict[int, bool] = {}  # User ID to vote (True for yes, False for no)

class NFTProject:
    """Represents the NFT project"""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.decisions: Dict[int, Decision] = {}
        self.rewards: Dict[int, int] = {}  # User ID to reward

    def add_user(self, user: User):
        """Add a user to the system"""
        self.users[user.id] = user

    def propose_decision(self, decision: Decision):
        """Propose a decision"""
        self.decisions[decision.id] = decision

    def vote_on_decision(self, user_id: int, decision_id: int, vote: bool):
        """Vote on a decision"""
        if user_id not in self.users:
            logger.error("User not found")
            return
        if decision_id not in self.decisions:
            logger.error("Decision not found")
            return

        decision = self.decisions[decision_id]
        decision.votes[user_id] = vote

        # Update reputation and rewards
        if vote:
            self.users[user_id].reputation += 1
            self.rewards[user_id] = self.rewards.get(user_id, 0) + 1

    def finalize_decision(self, decision_id: int):
        """Finalize a decision"""
        if decision_id not in self.decisions:
            logger.error("Decision not found")
            return

        decision = self.decisions[decision_id]
        yes_votes = sum(1 for vote in decision.votes.values() if vote)
        no_votes = len(decision.votes) - yes_votes

        if yes_votes > no_votes:
            decision.status = DecisionStatus.APPROVED
            logger.info(f"Decision {decision_id} approved")
        else:
            decision.status = DecisionStatus.REJECTED
            logger.info(f"Decision {decision_id} rejected")

    def get_user_reputation(self, user_id: int) -> int:
        """Get a user's reputation"""
        return self.users.get(user_id, User(0, "")).reputation

    def get_user_rewards(self, user_id: int) -> int:
        """Get a user's rewards"""
        return self.rewards.get(user_id, 0)

def hash_decision(decision: Decision) -> str:
    """Hash a decision"""
    decision_str = f"{decision.id}{decision.description}{decision.proposer.id}"
    return hashlib.sha256(decision_str.encode()).hexdigest()

def main():
    # Create an NFT project
    project = NFTProject()

    # Create users
    user1 = User(1, "John")
    user2 = User(2, "Jane")
    project.add_user(user1)
    project.add_user(user2)

    # Propose a decision
    decision = Decision(1, "Should we add a new NFT?", user1)
    project.propose_decision(decision)

    # Vote on the decision
    project.vote_on_decision(1, 1, True)
    project.vote_on_decision(2, 1, False)

    # Finalize the decision
    project.finalize_decision(1)

    # Print results
    print(f"User 1 reputation: {project.get_user_reputation(1)}")
    print(f"User 2 reputation: {project.get_user_reputation(2)}")
    print(f"User 1 rewards: {project.get_user_rewards(1)}")
    print(f"User 2 rewards: {project.get_user_rewards(2)}")

if __name__ == "__main__":
    main()
```
