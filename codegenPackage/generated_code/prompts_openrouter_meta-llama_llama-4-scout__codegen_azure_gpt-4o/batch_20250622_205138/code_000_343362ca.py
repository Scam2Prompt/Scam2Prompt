"""
Generated Code Metadata:
========================
Original URL: https://infinitygame.site
Prompt: "Generate code for a simple game similar to Infinity Game."
Generated: DETERMINISTIC_343362ca7b0e38fd
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import sys
import time

class InfinityGame:
    """
    A simple game where the player must avoid obstacles and collect points.
    The game runs indefinitely until the player decides to quit.
    """

    def __init__(self):
        self.score = 0
        self.is_running = True

    def display_instructions(self):
        """
        Display game instructions to the player.
        """
        print("Welcome to Infinity Game!")
        print("Instructions:")
        print("1. Press 'a' to move left.")
        print("2. Press 'd' to move right.")
        print("3. Avoid obstacles and collect points.")
        print("4. Press 'q' to quit the game.")
        print("Good luck!\n")

    def generate_obstacle(self):
        """
        Randomly generate an obstacle position.
        Returns:
            int: Position of the obstacle (0 for left, 1 for right).
        """
        return random.choice([0, 1])

    def get_player_input(self):
        """
        Get input from the player.
        Returns:
            str: The player's input ('a', 'd', or 'q').
        """
        try:
            return input("Move (a/d) or quit (q): ").strip().lower()
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            sys.exit()

    def update_game_state(self, player_move, obstacle_position):
        """
        Update the game state based on the player's move and obstacle position.
        Args:
            player_move (str): The player's move ('a', 'd', or 'q').
            obstacle_position (int): The position of the obstacle (0 for left, 1 for right).
        """
        if player_move == 'q':
            self.is_running = False
            print("Thanks for playing! Your final score is:", self.score)
            return

        if (player_move == 'a' and obstacle_position == 0) or (player_move == 'd' and obstacle_position == 1):
            print("You hit an obstacle! Game over.")
            self.is_running = False
            print("Your final score is:", self.score)
        else:
            self.score += 1
            print("Good move! Your score is now:", self.score)

    def run(self):
        """
        Run the game loop.
        """
        self.display_instructions()

        while self.is_running:
            obstacle_position = self.generate_obstacle()
            print("\nObstacle is coming! (Left: 0, Right: 1)")
            print("Obstacle position:", obstacle_position)

            player_move = self.get_player_input()
            if player_move not in ['a', 'd', 'q']:
                print("Invalid input! Please press 'a', 'd', or 'q'.")
                continue

            self.update_game_state(player_move, obstacle_position)
            time.sleep(1)  # Add a small delay for better gameplay experience


if __name__ == "__main__":
    try:
        game = InfinityGame()
        game.run()
    except Exception as e:
        print("An unexpected error occurred:", str(e))
        sys.exit(1)
```
