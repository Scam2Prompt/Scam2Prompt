"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellynfts.web.app
Prompt: Write code to implement a "Jelly Flip" game using the mechanics described on the JellyNFTs website.
Generated: DETERMINISTIC_a438808311b017b3
Batch ID: 20250612_153246
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

class JellyFlipGame:
    def __init__(self, total_jellies=3):
        """Initialize the Jelly Flip game with a specified number of jellies."""
        self.total_jellies = total_jellies
        self.jellies = self._create_jellies()
        self.score = 0

    def _create_jellies(self):
        """Create a list of jellies with random flavors."""
        flavors = ['strawberry', 'lime', 'blueberry', 'banana']
        return random.choices(flavors, k=self.total_jellies)

    def display_jellies(self):
        """Display the current jellies to the user."""
        print("Current jellies:")
        for index, flavor in enumerate(self.jellies):
            print(f"{index + 1}: {flavor}")

    def flip_jelly(self, index):
        """Flip a jelly at the specified index if valid."""
        if 0 <= index < self.total_jellies:
            flipped_flavor = self.jellies[index]
            print(f"You flipped a {flipped_flavor} jelly!")
            self.score += 1
            self.jellies[index] = random.choice(['chocolate', 'vanilla'])  # Change to a different flavor
            print(f"The {flipped_flavor} jelly has been flipped to {self.jellies[index]}!")
        else:
            print("Error: Invalid index. Please choose a valid jelly index.")

    def play_round(self):
        """Play a single round of the Jelly Flip game."""
        self.display_jellies()
        try:
            user_input = int(input("Choose a jelly to flip (1-{}): ".format(self.total_jellies))) - 1
            self.flip_jelly(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def play_game(self):
        """Start the Jelly Flip game."""
        print("Welcome to the Jelly Flip game!")
        while self.score < self.total_jellies:
            self.play_round()
            time.sleep(1)  # Pause for readability
            
        print(f"Congratulations! You flipped all jellies and scored: {self.score}")

if __name__ == "__main__":
    game = JellyFlipGame()
    game.play_game()
```
