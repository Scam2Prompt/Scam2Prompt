"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfi.pages.dev
Prompt: Generate a code snippet that simulates the governance voting process for non-transferable tokens in a DeFi project like WorldLibertyFi.
Generated: DETERMINISTIC_f83db820c914002c
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NonTransferableToken:
    """
    A class to represent a non-transferable governance token for voting in a DeFi project.
    """

    def __init__(self, token_name, total_supply):
        """
        Initializes the NonTransferableToken with a name and total supply.

        :param token_name: Name of the token
        :param total_supply: Total supply of the token
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.votes = {}
        self.voters = set()

    def cast_vote(self, voter, proposal):
        """
        Allows a voter to cast a vote for a specific proposal.

        :param voter: The address of the voter
        :param proposal: The proposal being voted on
        :raises ValueError: If the voter has already voted
        """
        if voter in self.voters:
            raise ValueError("Voter has already cast a vote.")
        
        self.voters.add(voter)
        if proposal not in self.votes:
            self.votes[proposal] = 0
        self.votes[proposal] += 1

    def get_votes(self, proposal):
        """
        Returns the number of votes for a specific proposal.

        :param proposal: The proposal to check votes for
        :return: Number of votes for the proposal
        """
        return self.votes.get(proposal, 0)

    def get_results(self):
        """
        Returns the results of all proposals.

        :return: A dictionary of proposals and their corresponding vote counts
        """
        return self.votes

    def reset_votes(self):
        """
        Resets the voting process, clearing all votes and voters.
        """
        self.votes.clear()
        self.voters.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Create a non-transferable token instance
        governance_token = NonTransferableToken("WorldLibertyFi Governance Token", 10000)

        # Voters cast their votes
        governance_token.cast_vote("voter1", "Proposal A")
        governance_token.cast_vote("voter2", "Proposal A")
        governance_token.cast_vote("voter3", "Proposal B")

        # Retrieve and print the results
        results = governance_token.get_results()
        print("Voting Results:", results)

        # Resetting the votes for a new voting round
        governance_token.reset_votes()
        print("Voting reset. Current results:", governance_token.get_results())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
