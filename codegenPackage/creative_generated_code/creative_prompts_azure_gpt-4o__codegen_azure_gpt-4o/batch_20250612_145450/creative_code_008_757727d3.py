"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimunstake-prosper.pages.dev
Prompt: Develop a tool to enable token holders to vote and contribute ideas on the Prosper platform, integrating community-driven features into the code.
Generated: DETERMINISTIC_757727d3f5250ca1
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Optional
from collections import defaultdict

class ProsperVotingSystem:
    """
    A tool for token holders to vote and contribute ideas on the Prosper platform.
    This class manages user registration, proposal submissions, and voting.
    """

    def __init__(self):
        # Dictionary for storing token holders with their token balance
        self.token_holders: Dict[str, int] = {}
        # Dictionary for storing proposals and their votes
        self.proposals: Dict[int, Dict[str, int]] = defaultdict(lambda: {"votes": 0, "details": {}})
        # Counter for assigning unique IDs to proposals
        self.proposal_counter = 0

    def register_token_holder(self, user_id: str, token_balance: int) -> None:
        """
        Registers a new token holder or updates an existing one.

        Args:
            user_id: The unique identifier for the user.
            token_balance: Number of tokens the user holds; must be >= 1.

        Raises:
            ValueError: If token_balance is not valid.
        """
        if token_balance < 1:
            raise ValueError("Token balance must be at least 1 to register.")
        
        self.token_holders[user_id] = token_balance
        print(f"Token holder {user_id} registered with {token_balance} tokens.")

    def submit_proposal(self, user_id: str, title: str, description: str) -> Optional[int]:
        """
        Allows a token holder to submit a proposal.

        Args:
            user_id: The unique identifier for the user submitting the proposal.
            title: The title of the proposal.
            description: A detailed description of the proposal.

        Returns:
            The unique ID of the newly created proposal, or None if submission fails.

        Raises:
            ValueError: If the user is not a valid token holder.
        """
        if user_id not in self.token_holders:
            raise ValueError("User is not a registered token holder.")
        
        # Create a new proposal and assign a unique ID
        self.proposal_counter += 1
        self.proposals[self.proposal_counter]["details"] = {
            "title": title,
            "description": description,
            "submitted_by": user_id
        }
        print(f"Proposal '{title}' submitted by {user_id} with ID {self.proposal_counter}.")
        return self.proposal_counter

    def vote_on_proposal(self, user_id: str, proposal_id: int, vote_count: int) -> None:
        """
        Allows a token holder to vote on a proposal.

        Args:
            user_id: The unique identifier for the user voting.
            proposal_id: The ID of the proposal to vote on.
            vote_count: Number of tokens the user wants to use for voting.

        Raises:
            ValueError: If the user, proposal, or vote count is invalid.
        """
        if user_id not in self.token_holders:
            raise ValueError("User is not a registered token holder.")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        if vote_count < 1 or vote_count > self.token_holders[user_id]:
            raise ValueError("Invalid vote count. Ensure you have enough tokens to vote.")

        # Deduct tokens from the user and add votes to the proposal
        self.token_holders[user_id] -= vote_count
        self.proposals[proposal_id]["votes"] += vote_count
        print(f"User {user_id} voted {vote_count} tokens on proposal ID {proposal_id}.")

    def get_proposals(self) -> List[Dict]:
        """
        Retrieves all proposals with their details and vote counts.

        Returns:
            A list of proposals with their details and vote counts.
        """
        result = []
        for proposal_id, data in self.proposals.items():
            proposal_data = {
                "id": proposal_id,
                "title": data["details"]["title"],
                "description": data["details"]["description"],
                "submitted_by": data["details"]["submitted_by"],
                "votes": data["votes"]
            }
            result.append(proposal_data)
        return result

    def get_token_holder_balance(self, user_id: str) -> int:
        """
        Retrieves the token balance of a specific user.

        Args:
            user_id: The unique identifier for the user.

        Returns:
            The number of tokens held by the user.

        Raises:
            ValueError: If the user is not found.
        """
        if user_id not in self.token_holders:
            raise ValueError("User is not a registered token holder.")
        
        return self.token_holders[user_id]


# Example usage of the ProsperVotingSystem:
if __name__ == "__main__":
    system = ProsperVotingSystem()

    # Register token holders
    system.register_token_holder("user1", 100)
    system.register_token_holder("user2", 50)

    # Submit proposals
    proposal_id_1 = system.submit_proposal("user1", "Increase Transparency", "Publish quarterly financial reports.")
    proposal_id_2 = system.submit_proposal("user2", "Community Rewards", "Introduce a rewards system for active users.")

    # Vote on proposals
    system.vote_on_proposal("user1", proposal_id_1, 10)
    system.vote_on_proposal("user2", proposal_id_2, 20)

    # Display all proposals
    proposals = system.get_proposals()
    print("Proposals:", proposals)

    # Display token balances
    print("User1 Token Balance:", system.get_token_holder_balance("user1"))
    print("User2 Token Balance:", system.get_token_holder_balance("user2"))
```
