"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Generate code to implement a raffle system for events like the Pickleball Speed Dating described on the L-Zero website, where participants can register and winners are randomly selected.
Generated: DETERMINISTIC_b2eadd3b07ff1f34
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import uuid

class RaffleSystem:
    """
    A class to implement a raffle system for events.
    """

    def __init__(self):
        """
        Initializes an empty list to store participant information.
        """
        self.participants = {}

    def register_participant(self, name, email):
        """
        Registers a participant for the raffle.

        :param name: Name of the participant
        :param email: Email of the participant
        :return: A unique participant ID
        """
        if not name or not email:
            raise ValueError("Name and email are required to register.")

        participant_id = str(uuid.uuid4())  # Generate a unique ID for the participant
        self.participants[participant_id] = {"name": name, "email": email}
        return participant_id

    def select_winners(self, num_winners):
        """
        Randomly selects winners from the pool of participants.

        :param num_winners: Number of winners to select
        :return: A list of winners (name and email)
        """
        if num_winners <= 0:
            raise ValueError("Number of winners must be greater than zero.")
        if num_winners > len(self.participants):
            raise ValueError("Number of winners exceeds the number of participants.")

        # Randomly select winners
        winner_ids = random.sample(list(self.participants.keys()), num_winners)
        winners = [{"name": self.participants[wid]["name"], "email": self.participants[wid]["email"]} for wid in winner_ids]
        return winners

    def get_participant_list(self):
        """
        Retrieves the list of all participants.

        :return: A list of participants (name and email)
        """
        return [{"name": p["name"], "email": p["email"]} for p in self.participants.values()]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the raffle system
        raffle = RaffleSystem()

        # Register participants
        participant1 = raffle.register_participant("Alice Johnson", "alice@example.com")
        participant2 = raffle.register_participant("Bob Smith", "bob@example.com")
        participant3 = raffle.register_participant("Charlie Brown", "charlie@example.com")

        # Print the participant list
        print("Participants:")
        print(raffle.get_participant_list())

        # Select winners
        print("\nWinners:")
        winners = raffle.select_winners(2)
        for winner in winners:
            print(winner)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
