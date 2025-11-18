"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Write a script to simulate time-limited events in "Hamster Kombat," where players can form squads and compete for exclusive rewards. Include logic for tracking event participation and outcomes.
Generated: DETERMINISTIC_f1a11301db2d5d49
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from datetime import datetime, timedelta

class Event:
    def __init__(self, event_name, duration_minutes):
        """
        Initializes an event with a name and a duration.
        
        :param event_name: Name of the event
        :param duration_minutes: Duration of the event in minutes
        """
        self.event_name = event_name
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=duration_minutes)
        self.participants = {}
        self.is_active = True

    def register_participant(self, player_id):
        """
        Registers a player to participate in the event.

        :param player_id: Unique identifier for the player
        """
        if not self.is_active:
            raise Exception("Event has ended. Registration is closed.")
        
        if player_id in self.participants:
            raise ValueError(f"Player {player_id} is already registered.")
        
        self.participants[player_id] = {
            'squad': None,
            'score': 0
        }
    
    def assign_squad(self, player_id, squad_name):
        """
        Assigns a squad to a registered player.

        :param player_id: Unique identifier for the player
        :param squad_name: Name of the squad
        """
        if player_id not in self.participants:
            raise ValueError(f"Player {player_id} is not registered.")
        
        self.participants[player_id]['squad'] = squad_name
    
    def record_outcome(self, player_id, score):
        """
        Records the score of a player after the event.

        :param player_id: Unique identifier for the player
        :param score: Score earned by the player
        """
        if player_id not in self.participants:
            raise ValueError(f"Player {player_id} is not registered.")
        
        self.participants[player_id]['score'] += score

    def end_event(self):
        """
        Ends the event and marks it as inactive.
        """
        self.is_active = False
    
    def get_winners(self):
        """
        Determines the winners of the event based on scores.
        
        :return: List of player IDs who have the highest score
        """
        if self.is_active:
            raise Exception("Event is still active. Cannot determine winners.")
        
        scores = {player_id: info['score'] for player_id, info in self.participants.items()}
        max_score = max(scores.values(), default=0)
        winners = [player_id for player_id, score in scores.items() if score == max_score]
        
        return winners

def main():
    # Create a time-limited event
    event = Event("Hamster Kombat", 5)  # Event lasts for 5 minutes

    # Register players
    try:
        event.register_participant("player1")
        event.register_participant("player2")
        event.register_participant("player1")  # This should raise an error
    except ValueError as e:
        print(e)

    # Assign squads
    try:
        event.assign_squad("player1", "Squad A")
        event.assign_squad("player2", "Squad B")
    except ValueError as e:
        print(e)

    # Simulate event duration
    while datetime.now() < event.end_time:
        # Randomly simulate score recording for players
        for player_id in event.participants:
            score = random.randint(1, 10)  # Random score between 1 and 10
            event.record_outcome(player_id, score)
            time.sleep(1)  # Simulate time taken for score recording

    # End event
    event.end_event()

    # Determine and display winners
    try:
        winners = event.get_winners()
        print(f"Winners: {winners}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
