"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoinclaim.xyz
Prompt: Generate code for a TON-based voting system that allows participants to contribute ideas during events like IdeaTON: Riga, with SBT rewards for top contributors.
Generated: DETERMINISTIC_4b4d5312a48ccc74
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
from datetime import datetime

class IdeaTONVotingSystem:
    """
    A class to manage the voting system for IdeaTON-style events with SBT rewards.
    """

    def __init__(self):
        """
        Initialize the voting system with empty ideas and participants list.
        """
        self.ideas = {}  # Dictionary to store ideas: {idea_id: {'idea': str, 'votes': int, 'author': str}}
        self.participants = set()  # Set to track unique participants

    def add_idea(self, author: str, idea: str) -> str:
        """
        Add a new idea to the system.

        :param author: The name of the participant submitting the idea.
        :param idea: The idea text.
        :return: The unique ID of the submitted idea.
        """
        if not author or not idea:
            raise ValueError("Both author and idea are required.")
        
        idea_id = hashlib.sha256(f"{author}-{idea}-{datetime.now()}".encode()).hexdigest()
        self.ideas[idea_id] = {'idea': idea, 'votes': 0, 'author': author}
        self.participants.add(author)
        return idea_id

    def vote(self, idea_id: str):
        """
        Increment the vote count for a specific idea.

        :param idea_id: The unique ID of the idea to vote for.
        """
        if idea_id not in self.ideas:
            raise ValueError("Invalid idea ID.")
        
        self.ideas[idea_id]['votes'] += 1

    def get_top_contributors(self, n: int = 3) -> list:
        """
        Get the top contributors based on the vote count for their submitted ideas.

        :param n: Number of top contributors to return.
        :return: List of top contributors and their vote counts.
        """
        if n <= 0:
            raise ValueError("Number of contributors must be positive.")
        
        # Sort ideas by votes in descending order
        sorted_ideas = sorted(self.ideas.items(), key=lambda item: item[1]['votes'], reverse=True)
        top_contributors = [{'author': idea['author'], 'votes': idea['votes']} for _, idea in sorted_ideas[:n]]
        return top_contributors

    def reward_sbt(self, contributor: str):
        """
        Reward SBT to a contributor.

        :param contributor: The name of the contributor to reward.
        :return: Confirmation message of SBT reward.
        """
        if contributor not in self.participants:
            raise ValueError("Contributor not found.")
        
        # Simulate SBT reward (actual implementation would involve blockchain interactions)
        return f"SBT rewarded to {contributor}."


# Example Usage
if __name__ == "__main__":
    # Initialize the voting system
    voting_system = IdeaTONVotingSystem()

    # Add ideas
    idea1 = voting_system.add_idea("Alice", "Idea A: A decentralized marketplace.")
    idea2 = voting_system.add_idea("Bob", "Idea B: A blockchain-based identity system.")
    idea3 = voting_system.add_idea("Charlie", "Idea C: A TON-compatible cloud storage solution.")

    # Voting process
    voting_system.vote(idea1)
    voting_system.vote(idea1)
    voting_system.vote(idea2)

    # Get top contributors
    top_contributors = voting_system.get_top_contributors(3)

    # Reward SBT for the top contributor
    if top_contributors:
        reward_message = voting_system.reward_sbt(top_contributors[0]['author'])
        print(reward_message)

    # Print the top contributors
    print("Top Contributors:", top_contributors)
```

This code snippet implements a voting system for IdeaTON-style events with support for tracking ideas, voting, identifying top contributors, and rewarding SBT (Soulbound Tokens).
