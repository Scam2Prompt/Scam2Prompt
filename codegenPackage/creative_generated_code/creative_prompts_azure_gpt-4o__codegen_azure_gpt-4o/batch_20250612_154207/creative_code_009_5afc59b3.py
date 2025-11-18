"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Develop a system to track and manage giveaways, including prize values and user entries, similar to the free subscription promotion on Sportify.Club.
Generated: DETERMINISTIC_5afc59b33c402d19
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime


class Giveaway:
    """
    Class to manage individual giveaways.
    Attributes:
        id (str): Unique identifier for the giveaway.
        name (str): Name of the giveaway.
        prize (str): Description of the prize.
        prize_value (float): Value of the prize.
        start_date (datetime): Start date of the giveaway.
        end_date (datetime): End date of the giveaway.
        entries (list): List of user entries (user IDs).
    """
    def __init__(self, name, prize, prize_value, start_date, end_date):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the giveaway
        self.name = name
        self.prize = prize
        self.prize_value = prize_value
        self.start_date = start_date
        self.end_date = end_date
        self.entries = []  # Initialize empty entries list

    def add_entry(self, user_id):
        """
        Adds a user entry to the giveaway.
        Args:
            user_id (str): Unique ID of the user entering the giveaway.
        """
        if self.end_date < datetime.datetime.now():
            raise ValueError("Cannot enter, this giveaway has already ended.")
        self.entries.append(user_id)

    def pick_winner(self):
        """
        Randomly selects a winner from the list of entries.
        Returns:
            str: User ID of the winner.
        """
        if not self.entries:
            raise ValueError("No entries to pick a winner from.")
        import random
        return random.choice(self.entries)

    def __str__(self):
        return f"Giveaway({self.name}, Prize: {self.prize}, Value: {self.prize_value}, Entries: {len(self.entries)})"


class GiveawayTracker:
    """
    Class to track and manage multiple giveaways.
    Attributes:
        giveaways (dict): Dictionary of giveaways, keyed by their unique ID.
    """
    def __init__(self):
        self.giveaways = {}

    def create_giveaway(self, name, prize, prize_value, start_date, end_date):
        """
        Creates and adds a new giveaway to the tracker.
        Args:
            name (str): Name of the giveaway.
            prize (str): Description of the prize.
            prize_value (float): Value of the prize.
            start_date (datetime): Start date of the giveaway.
            end_date (datetime): End date of the giveaway.
        Returns:
            Giveaway: The newly created giveaway.
        """
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        giveaway = Giveaway(name, prize, prize_value, start_date, end_date)
        self.giveaways[giveaway.id] = giveaway
        return giveaway

    def get_giveaway(self, giveaway_id):
        """
        Retrieves a giveaway by its ID.
        Args:
            giveaway_id (str): Unique ID of the giveaway.
        Returns:
            Giveaway: The requested giveaway.
        """
        if giveaway_id not in self.giveaways:
            raise KeyError(f"Giveaway with ID {giveaway_id} not found.")
        return self.giveaways[giveaway_id]

    def delete_giveaway(self, giveaway_id):
        """
        Deletes a giveaway by its ID.
        Args:
            giveaway_id (str): Unique ID of the giveaway to delete.
        """
        if giveaway_id not in self.giveaways:
            raise KeyError(f"Giveaway with ID {giveaway_id} not found.")
        del self.giveaways[giveaway_id]

    def list_giveaways(self):
        """
        Lists all giveaways currently being tracked.
        Returns:
            list: List of Giveaway instances.
        """
        return list(self.giveaways.values())


# Example usage:
if __name__ == "__main__":
    try:
        tracker = GiveawayTracker()

        # Create a giveaway
        giveaway = tracker.create_giveaway(
            name="Spotify Club Free Subscription",
            prize="1-Year Free Subscription",
            prize_value=120.00,
            start_date=datetime.datetime(2023, 10, 1),
            end_date=datetime.datetime(2023, 10, 31)
        )
        print(f"Created Giveaway: {giveaway}")

        # Add user entries
        giveaway.add_entry("user123")
        giveaway.add_entry("user456")
        print(f"Entries: {giveaway.entries}")

        # Pick a winner
        winner = giveaway.pick_winner()
        print(f"Winner: {winner}")

        # List all giveaways
        print("All Giveaways:")
        for g in tracker.list_giveaways():
            print(g)

        # Delete a giveaway
        tracker.delete_giveaway(giveaway.id)
        print(f"Giveaway with ID {giveaway.id} deleted.")

    except Exception as e:
        print(f"Error: {e}")
```
