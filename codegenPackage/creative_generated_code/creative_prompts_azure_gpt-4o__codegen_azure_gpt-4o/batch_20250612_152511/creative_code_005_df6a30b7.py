"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-overlay.pages.dev
Prompt: Develop a governance voting system for Overlay Protocol contributors, incorporating Planck Cat NFTs as a mechanism for special privileges and rewards.
Generated: DETERMINISTIC_df6a30b70e33b291
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# governance_voting.py

import json
from typing import List, Dict


class VotingSystem:
    """
    A governance voting system for Overlay Protocol contributors.
    Incorporates Planck Cat NFTs for special privileges and rewards.
    """

    def __init__(self):
        # Dictionary to hold voting proposals.
        # Keys are proposal IDs, values are proposal details.
        self.proposals = {}

        # Dictionary to track votes for each proposal.
        # Keys are proposal IDs, values are dictionaries with voter details.
        self.votes = {}

        # Dictionary to track wallet addresses holding Planck Cat NFTs.
        # Keys are wallet addresses, values are boolean indicating NFT ownership.
        self.planck_cat_holders = {}

    def add_proposal(self, proposal_id: str, description: str) -> None:
        """
        Adds a new governance proposal to the system.

        :param proposal_id: Unique identifier for the proposal.
        :param description: Text description of the proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' already exists.")
        
        self.proposals[proposal_id] = {
            "description": description,
            "status": "active"  # A proposal's status can be 'active', 'passed', or 'rejected'.
        }
        self.votes[proposal_id] = {}  # Initialize empty votes for the proposal.
        print(f"Proposal '{proposal_id}' added successfully.")

    def cast_vote(self, proposal_id: str, voter_address: str, vote: str) -> None:
        """
        Casts a vote on a proposal.

        :param proposal_id: ID of the proposal to vote on.
        :param voter_address: Wallet address of the voter.
        :param vote: Vote option ('yes', 'no').
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        
        if self.proposals[proposal_id]["status"] != "active":
            raise ValueError(f"Proposal '{proposal_id}' is not active.")
        
        if vote not in ["yes", "no"]:
            raise ValueError(f"Invalid vote option '{vote}'. Choose 'yes' or 'no'.")
        
        if voter_address in self.votes[proposal_id]:
            raise ValueError(f"Voter '{voter_address}' has already voted on this proposal.")
        
        # Check for special privileges if the voter owns a Planck Cat NFT
        has_planck_cat = self.planck_cat_holders.get(voter_address, False)
        
        self.votes[proposal_id][voter_address] = {
            "vote": vote,
            "has_planck_cat": has_planck_cat
        }
        print(f"Vote cast successfully by '{voter_address}'.")

    def count_votes(self, proposal_id: str) -> Dict[str, int]:
        """
        Counts the votes for a proposal.

        :param proposal_id: ID of the proposal to count votes for.
        :return: Dictionary with the vote counts for 'yes' and 'no'.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        
        votes = self.votes.get(proposal_id, {})
        vote_counts = {"yes": 0, "no": 0}

        # Count votes and give extra weight for Planck Cat NFT holders.
        for voter, details in votes.items():
            if details["vote"] == "yes":
                vote_counts["yes"] += 2 if details["has_planck_cat"] else 1
            elif details["vote"] == "no":
                vote_counts["no"] += 2 if details["has_planck_cat"] else 1
        
        return vote_counts

    def finalize_proposal(self, proposal_id: str) -> None:
        """
        Finalizes the voting process for a proposal and updates its status.

        :param proposal_id: ID of the proposal to finalize.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        
        if self.proposals[proposal_id]["status"] != "active":
            raise ValueError(f"Proposal '{proposal_id}' is not active.")
        
        vote_counts = self.count_votes(proposal_id)
        if vote_counts["yes"] > vote_counts["no"]:
            self.proposals[proposal_id]["status"] = "passed"
        else:
            self.proposals[proposal_id]["status"] = "rejected"
        
        print(f"Proposal '{proposal_id}' finalized. Status: {self.proposals[proposal_id]['status']}")

    def add_planck_cat_holder(self, wallet_address: str) -> None:
        """
        Adds a wallet address to the list of Planck Cat NFT holders.

        :param wallet_address: Wallet address of the NFT holder.
        """
        self.planck_cat_holders[wallet_address] = True
        print(f"Wallet '{wallet_address}' added as Planck Cat NFT holder.")

    def remove_planck_cat_holder(self, wallet_address: str) -> None:
        """
        Removes a wallet address from the list of Planck Cat NFT holders.

        :param wallet_address: Wallet address of the NFT holder.
        """
        if wallet_address in self.planck_cat_holders:
            del self.planck_cat_holders[wallet_address]
            print(f"Wallet '{wallet_address}' removed as Planck Cat NFT holder.")
        else:
            print(f"Wallet '{wallet_address}' not found in Planck Cat NFT holders.")

    def save_state(self, file_path: str) -> None:
        """
        Saves the current state of the voting system to a JSON file.

        :param file_path: Path to the file where the state will be saved.
        """
        state = {
            "proposals": self.proposals,
            "votes": self.votes,
            "planck_cat_holders": self.planck_cat_holders
        }
        with open(file_path, "w") as file:
            json.dump(state, file, indent=4)
        print(f"Voting system state saved to '{file_path}'.")

    def load_state(self, file_path: str) -> None:
        """
        Loads the voting system state from a JSON file.

        :param file_path: Path to the file from which the state will be loaded.
        """
        try:
            with open(file_path, "r") as file:
                state = json.load(file)
                self.proposals = state.get("proposals", {})
                self.votes = state.get("votes", {})
                self.planck_cat_holders = state.get("planck_cat_holders", {})
            print(f"Voting system state loaded from '{file_path}'.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Unable to load state.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_path}'. Unable to load state.")


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Add some wallet addresses as Planck Cat NFT holders
    voting_system.add_planck_cat_holder("wallet1")
    voting_system.add_planck_cat_holder("wallet2")

    # Add proposals
    voting_system.add_proposal("proposal1", "Increase liquidity rewards.")
    voting_system.add_proposal("proposal2", "Reduce transaction fees.")

    # Cast votes
    voting_system.cast_vote("proposal1", "wallet1", "yes")
    voting_system.cast_vote("proposal1", "wallet3", "no")  # wallet3 does not hold Planck Cat NFT
    voting_system.cast_vote("proposal2", "wallet2", "yes")

    # Finalize proposals
    voting_system.finalize_proposal("proposal1")
    voting_system.finalize_proposal("proposal2")

    # Save and load state
    voting_system.save_state("voting_system_state.json")
    voting_system.load_state("voting_system_state.json")
```
