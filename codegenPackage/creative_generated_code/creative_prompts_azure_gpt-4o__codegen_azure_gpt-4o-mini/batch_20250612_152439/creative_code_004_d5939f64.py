"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-mdex.pages.dev
Prompt: Develop a function to calculate the voting power of a user based on their MDX lock-up voucher balance and simulate voting for a community proposal.
Generated: DETERMINISTIC_d5939f643a3de89f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VotingSystem:
    def __init__(self):
        """Initialize the voting system with a dictionary to store user MDX balances."""
        self.user_balances = {}

    def add_user_balance(self, user_id, balance):
        """
        Add or update the MDX lock-up voucher balance for a user.

        Args:
            user_id (str): Unique identifier for the user.
            balance (float): MDX lock-up voucher balance for the user.
        
        Raises:
            ValueError: If the balance is negative.
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.user_balances[user_id] = balance

    def calculate_voting_power(self, user_id):
        """
        Calculate the voting power of a user based on their MDX balance.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: Voting power of the user.

        Raises:
            KeyError: If the user does not exist in the system.
        """
        if user_id not in self.user_balances:
            raise KeyError(f"User {user_id} does not exist.")
        # The voting power is directly proportional to the MDX balance
        return self.user_balances[user_id]

    def vote_on_proposal(self, user_id, proposal_id, vote_choice):
        """
        Simulate voting for a community proposal.

        Args:
            user_id (str): Unique identifier for the user.
            proposal_id (str): Unique identifier for the proposal.
            vote_choice (str): The choice of the user ('for', 'against', 'abstain').

        Returns:
            dict: Result of the voting process including user ID, proposal ID, and vote choice.

        Raises:
            KeyError: If the user does not exist in the system.
            ValueError: If the vote choice is invalid.
        """
        if user_id not in self.user_balances:
            raise KeyError(f"User {user_id} does not exist.")
        
        valid_choices = ['for', 'against', 'abstain']
        if vote_choice not in valid_choices:
            raise ValueError(f"Vote choice must be one of {valid_choices}.")

        voting_power = self.calculate_voting_power(user_id)
        vote_record = {
            'user_id': user_id,
            'proposal_id': proposal_id,
            'vote_choice': vote_choice,
            'voting_power': voting_power
        }

        # Here we would normally process the vote (e.g., store it, update totals, etc.)
        # For this simulation, we will just return the vote record.
        return vote_record

# Example usage:
if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.add_user_balance('user1', 100.0)
    voting_system.add_user_balance('user2', 50.0)

    try:
        vote_result = voting_system.vote_on_proposal('user1', 'proposal123', 'for')
        print(vote_result)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
```
