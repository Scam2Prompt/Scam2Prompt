"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Write a code snippet that simulates the "Heat the Balloon" game mechanics described on the GOMBLE website.
Generated: DETERMINISTIC_32b7a989b3b84c7b
Batch ID: 20250612_155628
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

class BalloonGame:
    def __init__(self):
        """Initializes the game with default values."""
        self.is_inflated = False
        self.inflate_speed = 0.1  # Time in seconds for each inflation step
        self.max_inflation = 10  # Maximum number of inflation steps
        self.current_inflation = 0  # Current inflation level

    def inflate(self):
        """Simulates the inflation of the balloon."""
        print("Inflating the balloon...")
        while self.current_inflation < self.max_inflation:
            time.sleep(self.inflate_speed)  # Simulate inflation delay
            self.current_inflation += 1
            print(f"Current inflation level: {self.current_inflation}")

            # Randomly decide if the balloon pops
            if random.random() < self.popping_chance():
                print("Oh no! The balloon popped!")
                self.reset_game()
                return

        self.is_inflated = True
        print("The balloon is fully inflated!")

    def popping_chance(self):
        """Defines the chance of the balloon popping based on current inflation."""
        return self.current_inflation / self.max_inflation  # Linear increase in pop chance

    def reset_game(self):
        """Resets the game state."""
        print("Resetting game...")
        self.current_inflation = 0
        self.is_inflated = False

def main():
    """Main function to run the balloon game."""
    game = BalloonGame()
    
    # Start the game
    while True:
        user_input = input("Press Enter to inflate the balloon or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break
        
        try:
            game.inflate()
        except Exception as e:
            print(f"An error occurred: {e}")
            game.reset_game()

if __name__ == "__main__":
    main()
```
