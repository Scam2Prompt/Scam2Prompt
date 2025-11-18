"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the scarcity of resources in SIMemes, ensuring competition among players for limited "poop" and other assets.
Generated: DETERMINISTIC_9a7840f297a6b1ff
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SIMemesGame:
    """
    SIMemesGame simulates a resource scarcity game where players compete for limited assets.
    """

    def __init__(self, player_count, resource_count):
        """
        Initialize the game with the given number of players and resources.
        
        Args:
            player_count (int): The number of players competing.
            resource_count (dict): Dictionary representing resources and their quantities.
        """
        if player_count < 1:
            raise ValueError("There must be at least one player.")
        if not isinstance(resource_count, dict) or len(resource_count) == 0:
            raise ValueError("Resource count must be a non-empty dictionary.")
        
        self.players = [f"Player_{i+1}" for i in range(player_count)]
        self.resources = resource_count
        self.player_scores = {player: 0 for player in self.players}

    def allocate_resources(self):
        """
        Simulate players competing for resources. Each player tries to claim 
        random amounts of resources, but resources are limited.
        """
        for player in self.players:
            print(f"\n{player}'s turn:")
            for resource_name, available_quantity in self.resources.items():
                if available_quantity <= 0:
                    print(f"  {resource_name} is depleted!")
                    continue

                # Player randomly attempts to claim an amount of the resource
                claim_amount = random.randint(1, 5)
                if claim_amount <= available_quantity:
                    self.resources[resource_name] -= claim_amount
                    self.player_scores[player] += claim_amount
                    print(f"  {player} claimed {claim_amount} {resource_name}.")
                else:
                    print(f"  {player} attempted to claim {claim_amount} {resource_name}, but only {available_quantity} available.")
    
    def display_game_state(self):
        """
        Display the current state of resources and player scores.
        """
        print("\n=== Current Game State ===")
        print("Resources:")
        for resource_name, quantity in self.resources.items():
            print(f"  {resource_name}: {quantity}")
        print("\nPlayer Scores:")
        for player, score in self.player_scores.items():
            print(f"  {player}: {score}")

    def play_game(self, rounds):
        """
        Play the game for a specified number of rounds.
        
        Args:
            rounds (int): The number of rounds to simulate.
        """
        if rounds < 1:
            raise ValueError("Number of rounds must be at least 1.")
        
        print("\n=== Starting SIMemes Resource Scarcity Game ===")
        for round_number in range(1, rounds + 1):
            print(f"\n-- Round {round_number} --")
            self.allocate_resources()
            self.display_game_state()
            # End game if all resources are depleted
            if all(quantity <= 0 for quantity in self.resources.values()):
                print("\nAll resources are depleted! Game over.")
                break
    
        print("\n=== Final Results ===")
        self.display_game_state()

# Example usage
if __name__ == "__main__":
    # Define initial resources
    initial_resources = {
        "poop": 20,
        "memes": 15,
        "bananas": 10
    }

    # Create the game instance
    game = SIMemesGame(player_count=3, resource_count=initial_resources)

    # Play the game for 5 rounds
    try:
        game.play_game(rounds=5)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
