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
# voter_delegation_system.py

class Voter:
    """
    Represents a voter in the delegation system.
    """
    def __init__(self, voter_id, name):
        """
        Initializes a voter with a unique ID and name.
        :param voter_id: Unique identifier for the voter.
        :param name: Name of the voter.
        """
        self.voter_id = voter_id
        self.name = name
        self.delegate = None  # Initially, no delegate is assigned.
        self.votes = 1  # Each voter starts with 1 vote.

    def delegate_vote(self, delegate):
        """
        Delegates the voter's vote to another voter.
        :param delegate: The voter to whom the vote is delegated.
        :raises ValueError: If delegation creates a circular delegation.
        """
        if self._creates_circular_delegation(delegate):
            raise ValueError("Circular delegation detected. Delegation not allowed.")
        
        self.delegate = delegate
        delegate.receive_votes(self.votes)
        self.votes = 0  # The voter no longer has votes after delegation.

    def receive_votes(self, votes):
        """
        Receives votes from another voter.
        :param votes: Number of votes to add.
        """
        self.votes += votes

    def _creates_circular_delegation(self, delegate):
        """
        Checks if delegating to the given delegate creates a circular delegation.
        :param delegate: The voter to check for circular delegation.
        :return: True if circular delegation is detected, False otherwise.
        """
        visited = set()
        current = delegate
        while current:
            if current == self:
                return True
            if current in visited:
                break
            visited.add(current)
            current = current.delegate
        return False

    def __str__(self):
        """
        Returns a string representation of the voter.
        """
        return f"Voter({self.voter_id}, {self.name}, Votes: {self.votes}, Delegate: {self.delegate.name if self.delegate else 'None'})"


class DelegationSystem:
    """
    Represents the voter delegation system.
    """
    def __init__(self):
        """
        Initializes the delegation system with an empty list of voters.
        """
        self.voters = {}

    def add_voter(self, voter_id, name):
        """
        Adds a new voter to the system.
        :param voter_id: Unique identifier for the voter.
        :param name: Name of the voter.
        :raises ValueError: If a voter with the same ID already exists.
        """
        if voter_id in self.voters:
            raise ValueError(f"Voter with ID {voter_id} already exists.")
        self.voters[voter_id] = Voter(voter_id, name)

    def delegate_vote(self, voter_id, delegate_id):
        """
        Delegates a voter's vote to another voter.
        :param voter_id: ID of the voter delegating their vote.
        :param delegate_id: ID of the voter receiving the delegated vote.
        :raises KeyError: If either voter ID is not found in the system.
        """
        if voter_id not in self.voters or delegate_id not in self.voters:
            raise KeyError("One or both voter IDs not found in the system.")
        
        voter = self.voters[voter_id]
        delegate = self.voters[delegate_id]
        voter.delegate_vote(delegate)

    def get_voter(self, voter_id):
        """
        Retrieves a voter by their ID.
        :param voter_id: ID of the voter to retrieve.
        :return: Voter object.
        :raises KeyError: If the voter ID is not found in the system.
        """
        if voter_id not in self.voters:
            raise KeyError(f"Voter with ID {voter_id} not found.")
        return self.voters[voter_id]

    def __str__(self):
        """
        Returns a string representation of all voters in the system.
        """
        return "\n".join(str(voter) for voter in self.voters.values())


# Example usage
if __name__ == "__main__":
    try:
        system = DelegationSystem()
        system.add_voter(1, "Alice")
        system.add_voter(2, "Bob")
        system.add_voter(3, "Charlie")

        print("Initial state:")
        print(system)

        system.delegate_vote(1, 2)  # Alice delegates to Bob
        system.delegate_vote(2, 3)  # Bob delegates to Charlie

        print("\nAfter delegation:")
        print(system)

    except Exception as e:
        print(f"Error: {e}")
```
