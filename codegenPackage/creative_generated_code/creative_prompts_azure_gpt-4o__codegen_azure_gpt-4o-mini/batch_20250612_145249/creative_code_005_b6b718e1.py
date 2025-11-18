"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrewards.com
Prompt: Write a script to simulate daily and weekly cash giveaway draws, ensuring compliance with Phantom Rewards’ membership tiers and entry rules.
Generated: DETERMINISTIC_b6b718e1848f1acb
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import defaultdict
from datetime import datetime, timedelta

class PhantomRewards:
    def __init__(self):
        # Define membership tiers and their entry rules
        self.tiers = {
            "Bronze": {"min_entries": 1, "max_entries": 5},
            "Silver": {"min_entries": 2, "max_entries": 10},
            "Gold": {"min_entries": 3, "max_entries": 15},
        }
        self.entries = defaultdict(list)

    def add_entry(self, member_id, tier):
        """
        Adds an entry for a member in the draw based on their membership tier.
        
        :param member_id: Unique identifier for the member
        :param tier: Membership tier of the member
        :raises ValueError: If the membership tier is invalid
        """
        if tier not in self.tiers:
            raise ValueError(f"Invalid membership tier: {tier}")

        # Fetch the entry limits for the given tier
        entry_limits = self.tiers[tier]
        entry_count = random.randint(entry_limits["min_entries"], entry_limits["max_entries"])
        
        # Record the entries for the member
        self.entries[member_id].extend([tier] * entry_count)

    def draw_winner(self):
        """
        Draws a random winner from the entries.
        
        :return: The member_id of the winner or None if there are no entries
        """
        if not self.entries:
            return None
        
        # Flatten the entries list and select a random winner
        all_entries = [member for members in self.entries.values() for member in members]
        return random.choice(all_entries)

    def reset_entries(self):
        """
        Resets the entries for the next draw.
        """
        self.entries.clear()

def main():
    # Simulate daily and weekly cash giveaways
    cash_giveaway = PhantomRewards()

    # Simulate adding entries for members
    try:
        members = [("member1", "Bronze"), ("member2", "Silver"), ("member3", "Gold")]
        for member_id, tier in members:
            cash_giveaway.add_entry(member_id, tier)

        daily_winner = cash_giveaway.draw_winner()
        print(f"Today's winner: {daily_winner}")

        # Simulating a weekly draw
        for _ in range(5):  # Simulates 5 draws over 5 days
            cash_giveaway.reset_entries()
            for member_id, tier in members:
                cash_giveaway.add_entry(member_id, tier)
            
            weekly_winner = cash_giveaway.draw_winner()
            print(f"Weekly winner: {weekly_winner}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
