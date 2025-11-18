"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Develop a simulation where user input dynamically influences game outcomes, inspired by the AI-powered "Parallel Colony" experience described on the website.
Generated: DETERMINISTIC_67033bda73f2eb19
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ParallelColonySimulation:
    """
    A simulation inspired by the AI-powered "Parallel Colony" experience.
    Users dynamically influence game outcomes via input choices.
    """
    
    def __init__(self):
        # Initialize colony state
        self.resources = 100  # Starting resources
        self.population = 50  # Starting population
        self.morale = 75      # Starting morale (scale: 0-100)
        self.turn = 0         # Track the number of turns

    def display_status(self):
        """
        Displays the current status of the colony.
        """
        print("\n--- Colony Status ---")
        print(f"Turn: {self.turn}")
        print(f"Resources: {self.resources}")
        print(f"Population: {self.population}")
        print(f"Morale: {self.morale}/100")
        print("---------------------\n")

    def user_choice(self):
        """
        Prompts the user to make a decision that affects the colony.
        """
        print("Choose an action:")
        print("1. Expand territory (High risk, high reward)")
        print("2. Focus on resource gathering")
        print("3. Hold a festival to boost morale")
        print("4. Conduct research to improve future outcomes")
        print("5. Do nothing (passive turn)")
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice not in range(1, 6):
                raise ValueError("Invalid choice. Please select a number between 1 and 5.")
            return choice
        except ValueError as e:
            print(f"Error: {e}")
            return self.user_choice()  # Retry on invalid input

    def process_choice(self, choice):
        """
        Updates the colony's state based on the user's choice.
        """
        event_outcome = random.randint(-20, 20)  # Random factor affecting outcomes
        
        if choice == 1:
            # Expanding territory (High risk, high reward)
            print("You chose to expand territory...")
            self.resources += event_outcome * 2
            self.morale += event_outcome
            self.population += event_outcome

        elif choice == 2:
            # Resource gathering (Moderate risk, moderate reward)
            print("You chose to gather resources...")
            self.resources += event_outcome + 10
            self.morale += event_outcome // 2

        elif choice == 3:
            # Festival (Improves morale at the cost of resources)
            print("You chose to hold a festival...")
            self.resources -= 10
            self.morale += 15 + event_outcome

        elif choice == 4:
            # Research (Long-term benefit)
            print("You chose to conduct research...")
            self.resources -= 5
            self.morale += event_outcome // 2
            print("Your colony's future now looks brighter!")

        elif choice == 5:
            # Passing the turn (No immediate effect)
            print("You chose to do nothing...")
            self.morale += event_outcome // 3

        # Ensure values stay within boundaries
        self.resources = max(0, self.resources)
        self.morale = max(0, min(100, self.morale))
        self.population = max(0, self.population)

    def check_game_over(self):
        """
        Checks if the simulation has reached a game-over state.
        """
        if self.resources <= 0:
            print("Game Over: Your colony has run out of resources!")
            return True
        if self.population <= 0:
            print("Game Over: Your colony's population has fallen to zero!")
            return True
        if self.morale <= 0:
            print("Game Over: Your colony's morale has collapsed!")
            return True
        return False

    def simulate(self):
        """
        Starts the simulation loop.
        """
        print("Welcome to Parallel Colony Simulation!")
        while True:
            self.turn += 1
            self.display_status()
            choice = self.user_choice()
            self.process_choice(choice)

            if self.check_game_over():
                print(f"Simulation ended on Turn {self.turn}.")
                break

        print("Thank you for playing!")

# Entry point for the simulation
if __name__ == "__main__":
    simulation = ParallelColonySimulation()
    simulation.simulate()
```
