"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: "Develop a community engagement strategy for an NFT marketplace, incorporating elements from LooksRare's approach to user rewards and governance."
Generated: DETERMINISTIC_49fc412346054ae1
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NFTMarketplace:
    def __init__(self):
        """
        Initializes the NFT Marketplace with default values for user rewards and governance.
        """
        self.users = {}
        self.total_rewards = 0
        self.governance_votes = {}

    def register_user(self, user_id):
        """
        Registers a new user in the marketplace.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user is already registered.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        self.users[user_id] = {'rewards': 0, 'votes': 0}
        print(f"User {user_id} registered successfully.")

    def reward_user(self, user_id, amount):
        """
        Rewards a user with a specified amount.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of rewards to be given.

        Raises:
            ValueError: If the user is not registered or amount is negative.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        if amount < 0:
            raise ValueError("Reward amount cannot be negative.")
        
        self.users[user_id]['rewards'] += amount
        self.total_rewards += amount
        print(f"User {user_id} rewarded with {amount}. Total rewards: {self.users[user_id]['rewards']}.")

    def cast_vote(self, user_id, proposal):
        """
        Allows a user to cast a vote on a governance proposal.

        Args:
            user_id (str): Unique identifier for the user.
            proposal (str): The proposal the user is voting on.

        Raises:
            ValueError: If the user is not registered or has already voted.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        if self.users[user_id]['votes'] > 0:
            raise ValueError(f"User {user_id} has already voted.")

        self.users[user_id]['votes'] += 1
        if proposal not in self.governance_votes:
            self.governance_votes[proposal] = 0
        self.governance_votes[proposal] += 1
        print(f"User {user_id} voted on proposal: {proposal}. Total votes for this proposal: {self.governance_votes[proposal]}.")

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: Total rewards for the user.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        return self.users[user_id]['rewards']

    def get_governance_results(self):
        """
        Retrieves the current results of all governance proposals.

        Returns:
            dict: A dictionary containing proposals and their respective vote counts.
        """
        return self.governance_votes


# Example usage
if __name__ == "__main__":
    marketplace = NFTMarketplace()
    
    # Register users
    try:
        marketplace.register_user("user1")
        marketplace.register_user("user2")
        
        # Reward users
        marketplace.reward_user("user1", 100)
        marketplace.reward_user("user2", 150)
        
        # Cast votes
        marketplace.cast_vote("user1", "Proposal A")
        marketplace.cast_vote("user2", "Proposal A")
        
        # Get user rewards
        print(f"User1 rewards: {marketplace.get_user_rewards('user1')}")
        
        # Get governance results
        print("Governance results:", marketplace.get_governance_results())
        
    except ValueError as e:
        print(f"Error: {e}")
```
