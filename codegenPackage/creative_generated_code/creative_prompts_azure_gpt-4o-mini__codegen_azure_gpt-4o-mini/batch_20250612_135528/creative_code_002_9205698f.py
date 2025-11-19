"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetvietnam.wordpress.com
Prompt: Write a tutorial on building a game using Cairo on StarkNet, highlighting the unique features of the StarkNet ecosystem.
Generated: DETERMINISTIC_9205698f4accfbeb
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from cairo import *
from starknet import StarknetAPI, Contract, Event

# Define the main game class
class Game:
    def __init__(self, api: StarknetAPI, contract_address: str):
        """
        Initializes the game with the provided StarkNet API and contract address.

        :param api: An instance of StarknetAPI for blockchain interactions.
        :param contract_address: The address of the deployed contract on StarkNet.
        """
        self.api = api
        self.contract_address = contract_address
        self.contract = Contract(self.api, self.contract_address)

    def start_game(self):
        """
        Starts the game by calling the contract's start_game method.
        Includes error handling for potential issues.
        """
        try:
            response = self.contract.start_game()
            print(f"Game started successfully: {response}")
        except Exception as e:
            print(f"Failed to start game: {e}")

    def make_move(self, player_id: int, move: str):
        """
        Allows a player to make a move in the game.

        :param player_id: The ID of the player making the move.
        :param move: The move being made.
        """
        try:
            response = self.contract.make_move(player_id, move)
            print(f"Move made successfully: {response}")
        except Exception as e:
            print(f"Failed to make move: {e}")

    def end_game(self):
        """
        Ends the game by calling the contract's end_game method.
        Includes error handling for potential issues.
        """
        try:
            response = self.contract.end_game()
            print(f"Game ended successfully: {response}")
        except Exception as e:
            print(f"Failed to end game: {e}")

# Main function to run the game
if __name__ == "__main__":
    # Create an instance of StarknetAPI
    api = StarknetAPI()

    # Set the deployed contract address (to be replaced with an actual address)
    contract_address = "0xYourContractAddress"

    # Initialize the game
    game = Game(api, contract_address)

    # Start the game
    game.start_game()

    # Example of making moves
    game.make_move(1, "move1")
    game.make_move(2, "move2")

    # End the game
    game.end_game()
```
