"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Write a program to simulate gameplay mechanics for Artyfact's "Control" mode, where players secure control points to increase team scores.
Generated: DETERMINISTIC_0de33f27490119a6
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to simulate "Control" mode gameplay mechanics where players secure control points to increase team scores.

import time
import threading
import random

class ControlModeGame:
    def __init__(self, teams, control_points):
        """
        Initialize the game with teams and control points.
        
        :param teams: List of team names.
        :param control_points: List of control point names.
        """
        self.teams = {team: 0 for team in teams}  # Team scores
        self.control_points = {point: None for point in control_points}  # Control point ownership
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def capture_control_point(self, team, control_point):
        """
        Simulate a team capturing a control point.
        
        :param team: Name of the team capturing the point.
        :param control_point: Name of the control point being captured.
        """
        with self.lock:
            if control_point not in self.control_points:
                print(f"Invalid control point: {control_point}")
                return
            
            if self.control_points[control_point] != team:
                print(f"{team} is capturing {control_point}...")
                time.sleep(random.uniform(1, 3))  # Simulate capture delay
                self.control_points[control_point] = team
                print(f"{team} has secured {control_point}!")
            else:
                print(f"{control_point} is already under control of {team}.")

    def update_scores(self):
        """
        Update team scores based on control point ownership.
        """
        with self.lock:
            for control_point, team in self.control_points.items():
                if team:
                    self.teams[team] += 1

    def display_scores(self):
        """
        Display the current scores of all teams.
        """
        with self.lock:
            print("\nCurrent Scores:")
            for team, score in self.teams.items():
                print(f"{team}: {score}")
            print("\n")

    def display_control_points(self):
        """
        Display the ownership of all control points.
        """
        with self.lock:
            print("\nControl Point Ownership:")
            for control_point, team in self.control_points.items():
                status = team if team else "Unclaimed"
                print(f"{control_point}: {status}")
            print("\n")

    def simulate_gameplay(self, duration=30):
        """
        Simulate the game in real-time.
        
        :param duration: Duration of the game in seconds.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            self.update_scores()
            self.display_scores()
            self.display_control_points()
            time.sleep(5)  # Update every 5 seconds

def simulate_player_action(game, team, control_point):
    """
    Simulate a player attempting to capture a control point.
    
    :param game: Instance of ControlModeGame.
    :param team: Team name.
    :param control_point: Control point name.
    """
    while True:
        game.capture_control_point(team, control_point)
        time.sleep(random.uniform(3, 7))  # Random delay between attempts

# Main program
if __name__ == "__main__":
    # Initialize the game with two teams and three control points
    teams = ["Team A", "Team B"]
    control_points = ["Point Alpha", "Point Beta", "Point Gamma"]
    game = ControlModeGame(teams, control_points)

    # Simulate player actions using threads
    threads = [
        threading.Thread(target=simulate_player_action, args=(game, "Team A", "Point Alpha")),
        threading.Thread(target=simulate_player_action, args=(game, "Team B", "Point Alpha")),
        threading.Thread(target=simulate_player_action, args=(game, "Team A", "Point Beta")),
        threading.Thread(target=simulate_player_action, args=(game, "Team B", "Point Beta")),
        threading.Thread(target=simulate_player_action, args=(game, "Team A", "Point Gamma")),
        threading.Thread(target=simulate_player_action, args=(game, "Team B", "Point Gamma")),
    ]

    for thread in threads:
        thread.start()

    # Simulate game for 30 seconds (adjust as needed)
    game.simulate_gameplay(duration=30)

    # Stop threads after the game ends
    for thread in threads:
        thread.join()

    print("Game Over!")
    game.display_scores()
    game.display_control_points()
```
