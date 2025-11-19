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

class HeatTheBalloonGame:
    """
    A class to simulate the 'Heat the Balloon' game mechanics.

    Players heat a virtual balloon until it pops. Each player takes turns,
    and each heat action has a risk factor that increases over time.
    """
    def __init__(self, max_heat=100):
        """
        Initializes the game with default or specified max heat level.

        :param max_heat: The maximum heat level before the balloon pops.
        """
        self.current_heat = 0
        self.max_heat = max_heat
        self.balloon_popped = False

    def heat_balloon(self, heat_increment):
        """
        Heats the balloon by the specified increment and checks if it pops.

        :param heat_increment: The amount of heat to add to the balloon.
        :return: True if the balloon pops, False otherwise.
        """
        try:
            if self.balloon_popped:
                raise ValueError("The balloon has already popped. Start a new game.")

            self.current_heat += heat_increment

            # Check if the balloon pops
            if self.current_heat >= self.max_heat:
                self.balloon_popped = True
                return True
            return False
        except Exception as e:
            print(f"Error during heat increment: {e}")
            return False

    def reset_game(self):
        """
        Resets the game to its initial state.
        """
        self.current_heat = 0
        self.balloon_popped = False

    def display_status(self):
        """
        Displays the current heat level and game status.
        """
        status = "Popped" if self.balloon_popped else "Intact"
        print(f"Balloon Status: {status} | Current Heat: {self.current_heat}/{self.max_heat}")


def play_game():
    """
    Simulates a single session of the 'Heat the Balloon' game.
    """
    # Initialize game instance
    game = HeatTheBalloonGame(max_heat=100)

    print("Welcome to 'Heat the Balloon'!")

    while not game.balloon_popped:
        try:
            game.display_status()
            
            # Get user input for heat increment
            heat_input = input("Enter heat increment (1-20): ")
            
            # Validate input
            if not heat_input.isdigit():
                print("Invalid input. Please enter a number between 1 and 20.")
                continue
            
            heat_increment = int(heat_input)
            
            if heat_increment < 1 or heat_increment > 20:
                print("Invalid range. Heat increment must be between 1 and 20.")
                continue
            
            # Apply heat increment
            if game.heat_balloon(heat_increment):
                print("The balloon popped!")
                break
            
            # Add random risk factor (chance for spontaneous pop)
            spontaneous_pop_chance = random.randint(1, 100)
            if spontaneous_pop_chance <= game.current_heat:  # Higher heat increases risk
                game.balloon_popped = True
                print("The balloon popped spontaneously!")
                break

        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    game.display_status()
    print("Game Over. Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
```
