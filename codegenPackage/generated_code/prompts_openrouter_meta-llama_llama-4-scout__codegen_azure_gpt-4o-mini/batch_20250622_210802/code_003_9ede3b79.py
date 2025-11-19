"""
Generated Code Metadata:
========================
Original URL: https://singularity2.pages.dev
Prompt: "Describe the role of the AGIX token in the SingularityNET ecosystem, including its use in transactions, governance, and staking."
Generated: DETERMINISTIC_9ede3b79fbecd33d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AGIXToken:
    """
    A class to represent the AGIX token in the SingularityNET ecosystem.

    Attributes
    ----------
    total_supply : float
        The total supply of AGIX tokens.
    balance : dict
        A dictionary to hold the balance of each user.
    governance_votes : dict
        A dictionary to hold the governance votes of each user.

    Methods
    -------
    transfer(sender, receiver, amount):
        Transfers AGIX tokens from one user to another.
    stake(user, amount):
        Allows a user to stake their AGIX tokens.
    vote(user, proposal_id):
        Allows a user to vote on governance proposals.
    """
    
    def __init__(self, total_supply):
        """
        Initializes the AGIX token with a total supply and empty balances.

        Parameters
        ----------
        total_supply : float
            The total supply of AGIX tokens.
        """
        self.total_supply = total_supply
        self.balance = {}
        self.governance_votes = {}

    def transfer(self, sender, receiver, amount):
        """
        Transfers AGIX tokens from one user to another.

        Parameters
        ----------
        sender : str
            The user sending the tokens.
        receiver : str
            The user receiving the tokens.
        amount : float
            The amount of tokens to transfer.

        Raises
        ------
        ValueError
            If the sender has insufficient balance or if the amount is negative.
        """
        if amount < 0:
            raise ValueError("Transfer amount must be positive.")
        if sender not in self.balance or self.balance[sender] < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        # Perform the transfer
        self.balance[sender] -= amount
        if receiver not in self.balance:
            self.balance[receiver] = 0
        self.balance[receiver] += amount

    def stake(self, user, amount):
        """
        Allows a user to stake their AGIX tokens.

        Parameters
        ----------
        user : str
            The user staking the tokens.
        amount : float
            The amount of tokens to stake.

        Raises
        ------
        ValueError
            If the user has insufficient balance or if the amount is negative.
        """
        if amount < 0:
            raise ValueError("Stake amount must be positive.")
        if user not in self.balance or self.balance[user] < amount:
            raise ValueError("Insufficient balance for staking.")
        
        # Deduct the staked amount from the user's balance
        self.balance[user] -= amount
        # Here you would typically add the staked amount to a staking pool

    def vote(self, user, proposal_id):
        """
        Allows a user to vote on governance proposals.

        Parameters
        ----------
        user : str
            The user casting the vote.
        proposal_id : str
            The ID of the proposal being voted on.

        Raises
        ------
        ValueError
            If the user has not staked tokens or if the user has already voted.
        """
        if user not in self.balance or self.balance[user] <= 0:
            raise ValueError("User must stake tokens to vote.")
        if user in self.governance_votes:
            raise ValueError("User has already voted on this proposal.")
        
        # Record the user's vote
        self.governance_votes[user] = proposal_id
        # Here you would typically update the proposal's vote count

# Example usage
if __name__ == "__main__":
    try:
        agix = AGIXToken(total_supply=1_000_000_000)
        agix.balance['Alice'] = 1000
        agix.balance['Bob'] = 500

        agix.transfer('Alice', 'Bob', 200)
        agix.stake('Alice', 300)
        agix.vote('Alice', 'Proposal_1')

        print("Transfer, staking, and voting executed successfully.")
    except ValueError as e:
        print(f"Error: {e}")
```
