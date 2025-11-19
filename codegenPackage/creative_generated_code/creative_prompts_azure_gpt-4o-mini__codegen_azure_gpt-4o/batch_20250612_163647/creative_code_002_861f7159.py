"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Generate code to create a time trial competition feature in a racing game, inspired by the mechanics of Rally Racer Dirt.
Generated: DETERMINISTIC_861f71594ff4dc65
Batch ID: 20250612_163647
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


class TimeTrialCompetition:
    def __init__(self, track_name: str, max_attempts: int = 3):
        """
        Initializes the time trial competition instance.
        
        :param track_name: Name of the racing track.
        :param max_attempts: Maximum number of attempts allowed for each racer.
        """
        self.track_name = track_name
        self.max_attempts = max_attempts
        self.racers = {}
        self.leaderboard = {}

    def register_racer(self, racer_name: str):
        """
        Registers a racer for the competition.

        :param racer_name: Name of the racer.
        :raises ValueError: If the racer is already registered.
        """
        if racer_name in self.racers:
            raise ValueError(f"Racer '{racer_name}' is already registered.")
        self.racers[racer_name] = []
        print(f"Racer '{racer_name}' registered successfully.")

    def start_race(self, racer_name: str):
        """
        Starts the race for a racer.

        :param racer_name: Name of the racer.
        :raises ValueError: If the racer is not registered or has exceeded max attempts.
        """
        if racer_name not in self.racers:
            raise ValueError(f"Racer '{racer_name}' is not registered.")
        if len(self.racers[racer_name]) >= self.max_attempts:
            raise ValueError(f"Racer '{racer_name}' has exceeded the maximum attempts.")

        print(f"Racer '{racer_name}' is starting the race on track '{self.track_name}'.")
        start_time = time.time()

        # Simulate race duration (replacing actual racing mechanics)
        race_duration = random.uniform(30.0, 120.0)  # Random duration between 30-120 seconds
        time.sleep(2)  # Simulate time taken (2 seconds for demonstration)

        end_time = start_time + race_duration
        elapsed_time = round(end_time - start_time, 2)

        # Record the result
        self.racers[racer_name].append(elapsed_time)
        print(f"Racer '{racer_name}' finished the race in {elapsed_time} seconds.")

        # Update leaderboard
        self.update_leaderboard(racer_name)

    def update_leaderboard(self, racer_name: str):
        """
        Updates the leaderboard based on the racer's best performance.

        :param racer_name: Name of the racer.
        """
        best_time = min(self.racers[racer_name])
        self.leaderboard[racer_name] = best_time
        print(f"Leaderboard updated. Racer '{racer_name}' best time: {best_time} seconds.")

    def display_leaderboard(self):
        """
        Displays the current leaderboard sorted by best time.
        """
        print("\n--- Leaderboard ---")
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1])
        for rank, (racer_name, best_time) in enumerate(sorted_leaderboard, start=1):
            print(f"{rank}. {racer_name} - {best_time} seconds")
        print("-------------------")


# Example usage:
if __name__ == "__main__":
    competition = TimeTrialCompetition(track_name="Dirt Rally Track", max_attempts=3)

    try:
        competition.register_racer("Alice")
        competition.register_racer("Bob")
        competition.register_racer("Charlie")

        competition.start_race("Alice")
        competition.start_race("Bob")
        competition.start_race("Charlie")

        # Alice attempts another race
        competition.start_race("Alice")

        competition.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
