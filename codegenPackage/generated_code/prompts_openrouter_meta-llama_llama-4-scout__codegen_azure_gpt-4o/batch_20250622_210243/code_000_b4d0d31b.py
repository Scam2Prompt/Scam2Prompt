"""
Generated Code Metadata:
========================
Original URL: https://procreaition.pages.dev
Prompt: What is the purpose of the Dual-SPL-Token model in Procreation AI's ecosystem, and how do $NEURA and $PAI tokens interact?
Generated: DETERMINISTIC_b4d0d31bf124e209
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a simplified implementation of the Dual-SPL-Token model 
used in Procreation AI's ecosystem. It demonstrates the interaction between 
$NEURA and $PAI tokens, including their purpose and functionality.

$NEURA: Represents the governance token, allowing holders to vote on ecosystem decisions.
$PAI: Represents the utility token, used for transactions and accessing AI services.
"""

class DualSPLTokenModel:
    """
    A class to represent the Dual-SPL-Token model in Procreation AI's ecosystem.
    """

    def __init__(self):
        """
        Initializes the token balances and governance voting system.
        """
        self.neura_balances = {}  # Stores $NEURA token balances for each user
        self.pai_balances = {}    # Stores $PAI token balances for each user
        self.governance_votes = {}  # Tracks governance votes by $NEURA holders

    def create_account(self, user_id):
        """
        Creates a new account for a user with zero balances for both tokens.

        Args:
            user_id (str): Unique identifier for the user.
        """
        if user_id in self.neura_balances or user_id in self.pai_balances:
            raise ValueError("Account already exists.")
        self.neura_balances[user_id] = 0
        self.pai_balances[user_id] = 0

    def mint_tokens(self, user_id, token_type, amount):
        """
        Mints tokens for a user.

        Args:
            user_id (str): Unique identifier for the user.
            token_type (str): Type of token to mint ('$NEURA' or '$PAI').
            amount (float): Amount of tokens to mint.

        Raises:
            ValueError: If the token type is invalid or the amount is negative.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if token_type == "$NEURA":
            self.neura_balances[user_id] += amount
        elif token_type == "$PAI":
            self.pai_balances[user_id] += amount
        else:
            raise ValueError("Invalid token type. Use '$NEURA' or '$PAI'.")

    def transfer_tokens(self, sender_id, receiver_id, token_type, amount):
        """
        Transfers tokens from one user to another.

        Args:
            sender_id (str): Unique identifier for the sender.
            receiver_id (str): Unique identifier for the receiver.
            token_type (str): Type of token to transfer ('$NEURA' or '$PAI').
            amount (float): Amount of tokens to transfer.

        Raises:
            ValueError: If the sender has insufficient balance or the token type is invalid.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if token_type == "$NEURA":
            if self.neura_balances[sender_id] < amount:
                raise ValueError("Insufficient $NEURA balance.")
            self.neura_balances[sender_id] -= amount
            self.neura_balances[receiver_id] += amount
        elif token_type == "$PAI":
            if self.pai_balances[sender_id] < amount:
                raise ValueError("Insufficient $PAI balance.")
            self.pai_balances[sender_id] -= amount
            self.pai_balances[receiver_id] += amount
        else:
            raise ValueError("Invalid token type. Use '$NEURA' or '$PAI'.")

    def cast_vote(self, user_id, proposal_id, vote):
        """
        Allows $NEURA token holders to cast votes on governance proposals.

        Args:
            user_id (str): Unique identifier for the user.
            proposal_id (str): Unique identifier for the proposal.
            vote (str): The user's vote ('yes' or 'no').

        Raises:
            ValueError: If the user has no $NEURA tokens or the vote is invalid.
        """
        if self.neura_balances[user_id] <= 0:
            raise ValueError("User must hold $NEURA tokens to vote.")
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote. Use 'yes' or 'no'.")
        if proposal_id not in self.governance_votes:
            self.governance_votes[proposal_id] = {"yes": 0, "no": 0}
        self.governance_votes[proposal_id][vote] += self.neura_balances[user_id]

    def get_balances(self, user_id):
        """
        Retrieves the token balances for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary containing $NEURA and $PAI balances.
        """
        return {
            "$NEURA": self.neura_balances.get(user_id, 0),
            "$PAI": self.pai_balances.get(user_id, 0)
        }

    def get_governance_results(self, proposal_id):
        """
        Retrieves the results of a governance proposal.

        Args:
            proposal_id (str): Unique identifier for the proposal.

        Returns:
            dict: A dictionary containing the vote counts for 'yes' and 'no'.
        """
        return self.governance_votes.get(proposal_id, {"yes": 0, "no": 0})


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Dual-SPL-Token model
        ecosystem = DualSPLTokenModel()

        # Create user accounts
        ecosystem.create_account("user1")
        ecosystem.create_account("user2")

        # Mint tokens
        ecosystem.mint_tokens("user1", "$NEURA", 100)
        ecosystem.mint_tokens("user1", "$PAI", 50)
        ecosystem.mint_tokens("user2", "$PAI", 30)

        # Transfer tokens
        ecosystem.transfer_tokens("user1", "user2", "$PAI", 10)

        # Cast governance votes
        ecosystem.cast_vote("user1", "proposal1", "yes")

        # Retrieve balances
        print("User1 Balances:", ecosystem.get_balances("user1"))
        print("User2 Balances:", ecosystem.get_balances("user2"))

        # Retrieve governance results
        print("Governance Results for Proposal1:", ecosystem.get_governance_results("proposal1"))

    except Exception as e:
        print("Error:", e)
```
