"""
Generated Code Metadata:
========================
Original URL: https://aero-4dm.pages.dev
Prompt: "What are the benefits of using Aerodrome Finance's liquidity incentive engine and vote-lock governance model for a decentralized finance (DeFi) project? Provide a detailed explanation."
Generated: DETERMINISTIC_ca7cfc556472426d
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AerodromeFinance:
    """
    A class to represent the Aerodrome Finance liquidity incentive engine and vote-lock governance model.
    """

    def __init__(self):
        """
        Initializes the Aerodrome Finance model with default parameters.
        """
        self.liquidity_incentives = []
        self.vote_lock_period = 0  # in days
        self.governance_votes = {}

    def add_liquidity_incentive(self, incentive: str):
        """
        Adds a liquidity incentive to the engine.

        Parameters:
        incentive (str): Description of the liquidity incentive.

        Raises:
        ValueError: If the incentive is empty.
        """
        if not incentive:
            raise ValueError("Incentive cannot be empty.")
        self.liquidity_incentives.append(incentive)

    def set_vote_lock_period(self, days: int):
        """
        Sets the vote-lock period for governance.

        Parameters:
        days (int): The number of days for the vote-lock period.

        Raises:
        ValueError: If the number of days is negative.
        """
        if days < 0:
            raise ValueError("Vote-lock period cannot be negative.")
        self.vote_lock_period = days

    def cast_vote(self, user: str, proposal: str, vote: bool):
        """
        Casts a vote for a governance proposal.

        Parameters:
        user (str): The user casting the vote.
        proposal (str): The proposal being voted on.
        vote (bool): The vote (True for yes, False for no).

        Raises:
        ValueError: If the user has not locked their votes.
        """
        if user not in self.governance_votes:
            raise ValueError("User has not locked their votes.")
        self.governance_votes[user][proposal] = vote

    def lock_votes(self, user: str):
        """
        Locks the user's votes for the specified vote-lock period.

        Parameters:
        user (str): The user locking their votes.

        Raises:
        ValueError: If the user is already locked.
        """
        if user in self.governance_votes:
            raise ValueError("User has already locked their votes.")
        self.governance_votes[user] = {}

    def get_liquidity_incentives(self):
        """
        Returns the list of liquidity incentives.

        Returns:
        list: A list of liquidity incentives.
        """
        return self.liquidity_incentives

    def get_vote_lock_period(self):
        """
        Returns the current vote-lock period.

        Returns:
        int: The vote-lock period in days.
        """
        return self.vote_lock_period

    def get_user_votes(self, user: str):
        """
        Returns the votes cast by a user.

        Parameters:
        user (str): The user whose votes are to be retrieved.

        Returns:
        dict: A dictionary of proposals and their corresponding votes.

        Raises:
        ValueError: If the user has not locked their votes.
        """
        if user not in self.governance_votes:
            raise ValueError("User has not locked their votes.")
        return self.governance_votes[user]


# Example usage
if __name__ == "__main__":
    try:
        aerodrome = AerodromeFinance()
        aerodrome.add_liquidity_incentive("Liquidity Mining Rewards")
        aerodrome.set_vote_lock_period(30)
        aerodrome.lock_votes("user1")
        aerodrome.cast_vote("user1", "Proposal A", True)

        print("Liquidity Incentives:", aerodrome.get_liquidity_incentives())
        print("Vote Lock Period:", aerodrome.get_vote_lock_period())
        print("User Votes:", aerodrome.get_user_votes("user1"))

    except ValueError as e:
        print(f"Error: {e}")
```
