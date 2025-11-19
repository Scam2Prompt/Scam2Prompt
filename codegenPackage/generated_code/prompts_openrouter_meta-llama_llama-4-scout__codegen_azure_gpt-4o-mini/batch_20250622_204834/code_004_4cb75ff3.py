"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Design a basic implementation of a voter delegation system in Python, inspired by Agora's delegation features for Optimism governance.
Generated: DETERMINISTIC_4cb75ff3c6636803
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Voter:
    """
    A class to represent a voter in the delegation system.
    """

    def __init__(self, voter_id):
        """
        Initializes a new voter with a unique ID.

        :param voter_id: Unique identifier for the voter
        """
        self.voter_id = voter_id
        self.delegated_to = None

    def delegate(self, delegatee):
        """
        Delegates voting power to another voter.

        :param delegatee: Voter instance to whom the voting power is delegated
        :raises ValueError: If trying to delegate to oneself
        """
        if delegatee.voter_id == self.voter_id:
            raise ValueError("A voter cannot delegate to themselves.")
        self.delegated_to = delegatee

    def revoke_delegation(self):
        """
        Revokes the current delegation, if any.
        """
        self.delegated_to = None

    def get_delegate(self):
        """
        Returns the current delegatee of the voter.

        :return: Voter instance of the delegatee or None if no delegation
        """
        return self.delegated_to


class VotingSystem:
    """
    A class to manage the voting system and voter delegations.
    """

    def __init__(self):
        """
        Initializes the voting system with an empty list of voters.
        """
        self.voters = {}

    def add_voter(self, voter_id):
        """
        Adds a new voter to the system.

        :param voter_id: Unique identifier for the voter
        :raises ValueError: If the voter already exists
        """
        if voter_id in self.voters:
            raise ValueError("Voter with this ID already exists.")
        self.voters[voter_id] = Voter(voter_id)

    def delegate_vote(self, voter_id, delegatee_id):
        """
        Delegates a voter's vote to another voter.

        :param voter_id: ID of the voter who is delegating
        :param delegatee_id: ID of the voter to whom the vote is delegated
        :raises ValueError: If either voter does not exist or if self-delegation is attempted
        """
        if voter_id not in self.voters or delegatee_id not in self.voters:
            raise ValueError("Both voters must exist in the system.")
        
        voter = self.voters[voter_id]
        delegatee = self.voters[delegatee_id]
        voter.delegate(delegatee)

    def revoke_vote_delegation(self, voter_id):
        """
        Revokes the delegation of a voter's vote.

        :param voter_id: ID of the voter who is revoking delegation
        :raises ValueError: If the voter does not exist
        """
        if voter_id not in self.voters:
            raise ValueError("Voter does not exist in the system.")
        
        voter = self.voters[voter_id]
        voter.revoke_delegation()

    def get_delegate_info(self, voter_id):
        """
        Retrieves the delegate information for a given voter.

        :param voter_id: ID of the voter
        :return: ID of the delegatee or None if no delegation
        :raises ValueError: If the voter does not exist
        """
        if voter_id not in self.voters:
            raise ValueError("Voter does not exist in the system.")
        
        voter = self.voters[voter_id]
        delegatee = voter.get_delegate()
        return delegatee.voter_id if delegatee else None


# Example usage:
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        voting_system.add_voter("voter1")
        voting_system.add_voter("voter2")
        
        # Delegate vote from voter1 to voter2
        voting_system.delegate_vote("voter1", "voter2")
        
        # Check delegate info
        print(f"Voter1 delegates to: {voting_system.get_delegate_info('voter1')}")
        
        # Revoke delegation
        voting_system.revoke_vote_delegation("voter1")
        print(f"Voter1 delegates to: {voting_system.get_delegate_info('voter1')}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
