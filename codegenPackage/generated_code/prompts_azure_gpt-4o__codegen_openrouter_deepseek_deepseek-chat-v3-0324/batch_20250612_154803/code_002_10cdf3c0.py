"""
Generated Code Metadata:
========================
Original URL: https://paxful-login.id
Prompt: Generate a Python script to calculate and display RTP (Return to Player) percentages for slot games like Mahjong Ways and Sugar Rush, as described on Planet128.
Generated: DETERMINISTIC_10cdf3c021081121
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from pathlib import Path

class RTPCalculator:
    """
    A class to calculate and display RTP (Return to Player) percentages for slot games.
    """

    def __init__(self, game_data_path: Optional[str] = None):
        """
        Initialize the RTP calculator with optional game data file path.

        Args:
            game_data_path (Optional[str]): Path to a JSON file containing game data.
                                          If None, uses default data.
        """
        self.game_data = self._load_game_data(game_data_path)

    def _load_game_data(self, file_path: Optional[str]) -> Dict[str, Dict[str, Union[float, str]]]:
        """
        Load game data from a JSON file or use default data if no file is provided.

        Args:
            file_path (Optional[str]): Path to the JSON file.

        Returns:
            Dict[str, Dict[str, Union[float, str]]]: Game data dictionary.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        default_data = {
            "Mahjong Ways": {
                "rtp": 96.50,
                "volatility": "High",
                "description": "Popular slot with Asian theme and high volatility."
            },
            "Sugar Rush": {
                "rtp": 96.50,
                "volatility": "Medium",
                "description": "Colorful candy-themed slot with medium volatility."
            }
        }

        if file_path is None:
            return default_data

        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Game data file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in game data file", file_path, 0)

    def calculate_average_rtp(self) -> float:
        """
        Calculate the average RTP across all games.

        Returns:
            float: Average RTP percentage.
        """
        if not self.game_data:
            return 0.0

        total_rtp = sum(game["rtp"] for game in self.game_data.values())
        return total_rtp / len(self.game_data)

    def display_game_rtp(self, game_name: str) -> None:
        """
        Display RTP and other details for a specific game.

        Args:
            game_name (str): Name of the game to display.

        Raises:
            KeyError: If the game is not found in the data.
        """
        try:
            game = self.game_data[game_name]
            print(f"Game: {game_name}")
            print(f"RTP: {game['rtp']}%")
            print(f"Volatility: {game['volatility']}")
            print(f"Description: {game['description']}")
            print("-" * 40)
        except KeyError:
            raise KeyError(f"Game not found: {game_name}")

    def display_all_games(self) -> None:
        """
        Display RTP and details for all available games.
        """
        if not self.game_data:
            print("No game data available.")
            return

        for game_name in self.game_data:
            self.display_game_rtp(game_name)

        avg_rtp = self.calculate_average_rtp()
        print(f"\nAverage RTP across all games: {avg_rtp:.2f}%")

    def add_game(self, game_name: str, rtp: float, volatility: str, description: str) -> None:
        """
        Add a new game to the game data.

        Args:
            game_name (str): Name of the game.
            rtp (float): RTP percentage of the game.
            volatility (str): Volatility level (e.g., "Low", "Medium", "High").
            description (str): Description of the game.
        """
        self.game_data[game_name] = {
            "rtp": rtp,
            "volatility": volatility,
            "description": description
        }

    def save_game_data(self, file_path: str) -> None:
        """
        Save the current game data to a JSON file.

        Args:
            file_path (str): Path to save the JSON file.

        Raises:
            PermissionError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.game_data, file, indent=4)
        except PermissionError:
            raise PermissionError(f"Permission denied when writing to file: {file_path}")

def main():
    """
    Main function to demonstrate the RTPCalculator class.
    """
    try:
        # Initialize calculator with default data
        calculator = RTPCalculator()

        # Display all games
        print("Slot Game RTP Information:")
        print("=" * 40)
        calculator.display_all_games()

        # Example: Add a new game
        calculator.add_game(
            "New Slot",
            95.75,
            "Low",
            "A new slot game with low volatility."
        )

        # Display the new game
        print("\nAfter adding a new game:")
        calculator.display_game_rtp("New Slot")

        # Save to file (optional)
        # calculator.save_game_data("game_data.json")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
