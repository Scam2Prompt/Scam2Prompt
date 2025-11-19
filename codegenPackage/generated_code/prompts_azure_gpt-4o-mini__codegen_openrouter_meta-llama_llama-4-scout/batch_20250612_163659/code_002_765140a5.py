"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: What are the steps to create a leaderboard for tracking participants in the Tari airdrop game, including gem collection and rankings?
Generated: DETERMINISTIC_765140a51d3e4dc4
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class Participant:
    """Represents a participant in the Tari airdrop game."""
    
    def __init__(self, participant_id, name):
        """
        Initializes a Participant object.

        Args:
            participant_id (int): Unique ID of the participant.
            name (str): Name of the participant.
        """
        self.participant_id = participant_id
        self.name = name
        self.gems_collected = 0

    def collect_gems(self, amount):
        """
        Adds gems to the participant's collection.

        Args:
            amount (int): Number of gems to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Gem amount cannot be negative")
        self.gems_collected += amount


class Leaderboard:
    """Represents a leaderboard for tracking participants in the Tari airdrop game."""
    
    def __init__(self):
        """Initializes an empty leaderboard."""
        self.participants = {}

    def add_participant(self, participant_id, name):
        """
        Adds a participant to the leaderboard.

        Args:
            participant_id (int): Unique ID of the participant.
            name (str): Name of the participant.

        Raises:
            ValueError: If the participant ID already exists.
        """
        if participant_id in self.participants:
            raise ValueError("Participant ID already exists")
        self.participants[participant_id] = Participant(participant_id, name)

    def collect_gems(self, participant_id, amount):
        """
        Adds gems to a participant's collection.

        Args:
            participant_id (int): Unique ID of the participant.
            amount (int): Number of gems to add.

        Raises:
            ValueError: If the participant ID does not exist or the amount is negative.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant ID does not exist")
        self.participants[participant_id].collect_gems(amount)

    def get_rankings(self):
        """
        Returns a list of participants sorted by their gem collection in descending order.

        Returns:
            list: A list of tuples containing participant information and gem collection.
        """
        sorted_participants = sorted(self.participants.values(), key=lambda x: x.gems_collected, reverse=True)
        return [(p.participant_id, p.name, p.gems_collected) for p in sorted_participants]


def main():
    leaderboard = Leaderboard()

    # Add participants
    leaderboard.add_participant(1, "John Doe")
    leaderboard.add_participant(2, "Jane Doe")
    leaderboard.add_participant(3, "Bob Smith")

    # Collect gems
    leaderboard.collect_gems(1, 100)
    leaderboard.collect_gems(2, 50)
    leaderboard.collect_gems(3, 200)
    leaderboard.collect_gems(1, 150)

    # Get rankings
    rankings = leaderboard.get_rankings()

    # Print rankings
    print("Rankings:")
    for i, (participant_id, name, gems_collected) in enumerate(rankings):
        print(f"{i+1}. {name} (Participant ID: {participant_id}) - {gems_collected} gems")


if __name__ == "__main__":
    main()
```
