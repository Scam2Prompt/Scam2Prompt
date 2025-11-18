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

class Game:
    def __init__(self):
        """Initialize the game with default parameters."""
        self.resources = 100
        self.population = 10
        self.happiness = 50
        self.is_game_over = False

    def display_status(self):
        """Display the current status of resources, population, and happiness."""
        print(f"Resources: {self.resources}")
        print(f"Population: {self.population}")
        print(f"Happiness: {self.happiness}")

    def gather_resources(self):
        """Simulate gathering resources based on population."""
        if self.is_game_over:
            print("Game over! No more actions can be taken.")
            return
        
        gathered = self.population * random.randint(1, 10)
        self.resources += gathered
        print(f"You gathered {gathered} resources.")

    def build_infrastructure(self):
        """Simulate building infrastructure which costs resources."""
        if self.is_game_over:
            print("Game over! No more actions can be taken.")
            return
        
        cost = 30
        if self.resources >= cost:
            self.resources -= cost
            print("Infrastructure built! Resource cost: 30")
        else:
            print("Not enough resources to build infrastructure.")

    def improve_happiness(self):
        """Simulate improving happiness."""
        if self.is_game_over:
            print("Game over! No more actions can be taken.")
            return
        
        if self.happiness < 100:
            self.happiness += 10
            print("Improved happiness by 10.")
        else:
            print("Happiness is already at maximum!")

    def check_game_over(self):
        """Check if the game is over based on the state of resources and happiness."""
        if self.resources <= 0 or self.happiness <= 0:
            self.is_game_over = True
            print("Game over! Resources or happiness dropped to zero.")

    def run_turn(self):
        """Run a turn of the game, allowing the user to choose an action."""
        while not self.is_game_over:
            self.display_status()
            action = input("Choose an action: 'gather', 'build', 'improve happiness', or 'exit': ").strip().lower()
            
            if action == 'gather':
                self.gather_resources()
            elif action == 'build':
                self.build_infrastructure()
            elif action == 'improve happiness':
                self.improve_happiness()
            elif action == 'exit':
                print("Exiting the game.")
                break
            else:
                print("Invalid action. Please choose again.")
            
            self.check_game_over()

# Entry point of the game
if __name__ == "__main__":
    game = Game()
    game.run_turn()
```
