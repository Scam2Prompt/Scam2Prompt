"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babyslerf.pages.dev
Prompt: Develop a simple game application that incorporates Baby Slerf's "EAT, HODL, VIBE, SLEEP, REPEAT" mantra as gameplay mechanics.
Generated: DETERMINISTIC_e4a4bdbd50bbf3dc
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

# Game Constants
STARTING_ENERGY = 100
STARTING_MOOD = 50
MAX_ENERGY = 150
MAX_MOOD = 100
MIN_STAT_VALUE = 0

# Enum-like actions for Baby Slerf
ACTIONS = ["EAT", "HODL", "VIBE", "SLEEP"]

# Function to display the game rules
def display_rules():
    print("Welcome to the Baby Slerf game!")
    print("Your goal is to keep Baby Slerf happy and energetic.")
    print("You can perform actions: EAT, HODL, VIBE, or SLEEP.")
    print("Energy and Mood start at 100 and 50 respectively.")
    print("Every action affects Baby Slerf's stats.")
    print("If Energy or Mood drops to 0, you lose!")
    print("Let's go!")

# Class to represent Baby Slerf's state
class BabySlerf:
    def __init__(self):
        self.energy = STARTING_ENERGY
        self.mood = STARTING_MOOD

    def perform_action(self, action):
        """
        Updates Baby Slerf's stats based on the chosen action.
        :param action: Action chosen by the player
        """
        if action == "EAT":
            self.energy = min(MAX_ENERGY, self.energy + 20)
            self.mood = max(MIN_STAT_VALUE, self.mood - 5)
            print("Baby Slerf ate! Energy +20, Mood -5.")
        elif action == "HODL":
            self.mood = min(MAX_MOOD, self.mood + 30)
            self.energy = max(MIN_STAT_VALUE, self.energy - 10)
            print("Baby Slerf hodled! Mood +30, Energy -10.")
        elif action == "VIBE":
            self.mood = min(MAX_MOOD, self.mood + 10)
            self.energy = max(MIN_STAT_VALUE, self.energy - 15)
            print("Baby Slerf vibed! Mood +10, Energy -15.")
        elif action == "SLEEP":
            self.energy = min(MAX_ENERGY, self.energy + 30)
            self.mood = max(MIN_STAT_VALUE, self.mood + 5)
            print("Baby Slerf slept! Energy +30, Mood +5.")
        else:
            print("Invalid action. Choose EAT, HODL, VIBE, or SLEEP.")

    def is_alive(self):
        """
        Checks if Baby Slerf is still alive (i.e., stats are above 0).
        :return: True if alive, False otherwise
        """
        return self.energy > 0 and self.mood > 0

    def display_stats(self):
        """
        Displays Baby Slerf's current stats.
        """
        print(f"Energy: {self.energy}, Mood: {self.mood}")

# Main function to run the game
def main():
    # Display game rules
    display_rules()

    # Initialize Baby Slerf
    baby_slerf = BabySlerf()

    # Game loop
    while baby_slerf.is_alive():
        # Display stats
        baby_slerf.display_stats()

        # Prompt the user for an action
        action = input("Choose an action (EAT, HODL, VIBE, SLEEP): ").strip().upper()

        # Perform the chosen action
        baby_slerf.perform_action(action)

        # Random event affecting stats
        if random.random() < 0.2:  # 20% chance of a random event
            event_effect = random.choice(["energy", "mood"])
            change = random.randint(-15, 15)
            if event_effect == "energy":
                baby_slerf.energy = max(MIN_STAT_VALUE, min(MAX_ENERGY, baby_slerf.energy + change))
                print(f"Random event! Energy {'+' if change > 0 else ''}{change}.")
            elif event_effect == "mood":
                baby_slerf.mood = max(MIN_STAT_VALUE, min(MAX_MOOD, baby_slerf.mood + change))
                print(f"Random event! Mood {'+' if change > 0 else ''}{change}.")
        
        # Pause for better gameplay pacing
        time.sleep(0.5)

    # Game over
    print("Baby Slerf has run out of energy or mood. Game over!")

# Entry point for the game
if __name__ == "__main__":
    main()
```
