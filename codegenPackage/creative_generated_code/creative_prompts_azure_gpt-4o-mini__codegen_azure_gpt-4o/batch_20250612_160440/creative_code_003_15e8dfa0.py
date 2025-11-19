"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: How can I implement a voting system for $DOG token holders to decide on upcoming rewards in the Doge ecosystem?
Generated: DETERMINISTIC_15e8dfa07d3bac9d
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VotingSystem:
    """
    A class to implement a token-based voting system for DOG token holders
    to decide on upcoming rewards in the Doge ecosystem.
    """

    def __init__(self):
        """
        Initializes the voting system.
        - `proposals`: A dictionary to hold proposals with their votes.
        - `voters`: A set to track addresses that have already voted.
        """
        self.proposals = {}  # Stores proposals and associated vote counts
        self.voters = set()  # Tracks addresses that have voted

    def add_proposal(self, proposal_id, description):
        """
        Adds a new proposal to the system.

        Args:
            proposal_id (str): Unique identifier of the proposal.
            description (str): Text describing the proposal.

        Raises:
            ValueError: If the proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' already exists.")
        self.proposals[proposal_id] = {"description": description, "votes": 0}

    def vote(self, voter_address, proposal_id, token_balance):
        """
        Registers a vote for a proposal.

        Args:
            voter_address (str): Address of the voter.
            proposal_id (str): ID of the proposal to vote for.
            token_balance (int): Number of DOG tokens the voter holds.

        Raises:
            ValueError: If the voter has already voted.
            KeyError: If the proposal ID does not exist.
        """
        if voter_address in self.voters:
            raise ValueError("This voter has already cast their vote.")

        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal ID '{proposal_id}' does not exist.")

        if token_balance <= 0:
            raise ValueError("Token balance must be greater than 0 to vote.")

        # Update votes based on token balance
        self.proposals[proposal_id]["votes"] += token_balance

        # Mark voter as having voted
        self.voters.add(voter_address)

    def get_results(self):
        """
        Returns the current voting results.

        Returns:
            dict: A dictionary with proposal IDs as keys and their vote counts as values.
        """
        return {proposal_id: data["votes"] for proposal_id, data in self.proposals.items()}

    def save_state(self, filepath):
        """
        Saves the current state of the voting system to a JSON file.

        Args:
            filepath (str): Path to the file where state will be saved.
        """
        with open(filepath, "w") as file:
            json.dump({"proposals": self.proposals, "voters": list(self.voters)}, file, indent=4)

    def load_state(self, filepath):
        """
        Loads the state of the voting system from a JSON file.

        Args:
            filepath (str): Path to the file from which state will be loaded.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                self.proposals = data["proposals"]
                self.voters = set(data["voters"])
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filepath}' not found.")

# Example usage:
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Add proposals
    voting_system.add_proposal("proposal_1", "Increase staking rewards by 20%")
    voting_system.add_proposal("proposal_2", "Introduce weekly community events")

    # Cast votes
    try:
        voting_system.vote("address_1", "proposal_1", 100)  # 100 DOG tokens
        voting_system.vote("address_2", "proposal_2", 150)  # 150 DOG tokens

        # Uncomment below to see error handling in action:
        # voting_system.vote("address_1", "proposal_1", 50)  # This would raise an error (already voted)
        # voting_system.vote("address_3", "proposal_3", 50)  # This would raise an error (invalid proposal)

        # Print the results
        print("Voting Results:", voting_system.get_results())

        # Save and load state
        voting_system.save_state("voting_system_state.json")
        voting_system.load_state("voting_system_state.json")
        print("Loaded Voting System State:", voting_system.get_results())

    except (ValueError, KeyError, FileNotFoundError) as e:
        print("Error:", e)
```
