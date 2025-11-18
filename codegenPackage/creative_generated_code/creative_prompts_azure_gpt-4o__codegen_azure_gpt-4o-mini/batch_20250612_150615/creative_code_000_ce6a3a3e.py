"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Write Python code to simulate a gacha game reward system, incorporating tips from Argo App's article on avoiding addiction to gacha games.
Generated: DETERMINISTIC_ce6a3a3e55564677
Batch ID: 20250612_150615
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

class GachaGame:
    def __init__(self, user_budget=100, max_draws=10):
        """
        Initializes the GachaGame with a user budget and the maximum number of draws allowed.
        
        Parameters:
        user_budget (int): The starting amount of currency the user has to spend on draws.
        max_draws (int): The maximum number of draws the user can perform in a session.
        """
        self.user_budget = user_budget
        self.max_draws = max_draws
        self.items = self.initialize_items()
        self.draw_count = 0

    def initialize_items(self):
        """
        Initializes the items available for drawing.
        
        Returns:
        dict: A dictionary with item names as keys and their probabilities as values.
        """
        return {
            "Common Item": 70,  # 70% chance
            "Uncommon Item": 20,  # 20% chance
            "Rare Item": 9,  # 9% chance
            "Legendary Item": 1  # 1% chance
        }
    
    def draw_item(self):
        """
        Simulates drawing an item from the gacha system based on item probabilities.
        
        Returns:
        str: The name of the drawn item.
        """
        draw_result = random.choices(
            population=list(self.items.keys()),
            weights=list(self.items.values()),
            k=1
        )[0]
        return draw_result

    def perform_draws(self):
        """
        Manages the draw process, ensuring budget and draw limits are respected.
        """
        while self.draw_count < self.max_draws and self.user_budget > 0:
            print(f"Draw {self.draw_count + 1}:")
            item = self.draw_item()
            print(f"Congratulations! You drew a {item}!")
            self.user_budget -= 1  # Deduct the cost of one draw
            self.draw_count += 1

            # Provide a short delay for realism
            time.sleep(1)

            # Check if the user wants to continue drawing
            if self.draw_count < self.max_draws and self.user_budget > 0:
                continue_draw = input("Do you want to continue drawing? (yes/no): ").strip().lower()
                if continue_draw != 'yes':
                    break

        print(f"Session ended. You made {self.draw_count} draws and have {self.user_budget} currency left.")

    def reset_game(self):
        """
        Resets the game to its initial state.
        """
        self.user_budget = 100
        self.draw_count = 0
        print("Game reset successfully.")

if __name__ == "__main__":
    try:
        gacha_game = GachaGame()
        gacha_game.perform_draws()
    except Exception as e:
        print(f"An error occurred: {e}")
```
