"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write code to implement a search tool that allows users to find casinos based on game types like poker, slots, and bingo, as seen on Santa Claus Casino.
Generated: DETERMINISTIC_88725ee253817fe6
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CasinoSearchTool:
    def __init__(self, casino_data_file):
        """
        Initialize the CasinoSearchTool with a JSON file containing casino data.
        :param casino_data_file: Path to the JSON file containing casino data.
        """
        try:
            with open(casino_data_file, 'r') as file:
                self.casino_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Casino data file '{casino_data_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Casino data file '{casino_data_file}' contains invalid JSON.")

    def search_casinos_by_game(self, game_type):
        """
        Search for casinos offering a specific game type.
        :param game_type: The type of game to search for (e.g., 'poker', 'slots', 'bingo').
        :return: List of casino names offering the specified game type.
        """
        if not game_type or not isinstance(game_type, str):
            raise ValueError("Invalid game type. Please provide a non-empty string.")

        # Filter casinos based on game type
        matching_casinos = [
            casino['name'] for casino in self.casino_data
            if game_type.lower() in map(str.lower, casino.get('games', []))
        ]

        return matching_casinos

if __name__ == "__main__":
    # Example usage
    try:
        # Load casino data
        casino_file = "casinos.json"  # Path to your JSON file
        search_tool = CasinoSearchTool(casino_file)

        # Prompt user for input
        game = input("Enter a game type to search for (e.g., poker, slots, bingo): ").strip()
        
        # Perform search
        results = search_tool.search_casinos_by_game(game)

        # Display results
        if results:
            print(f"Casinos offering {game.capitalize()}:")
            for casino in results:
                print(f"- {casino}")
        else:
            print(f"No casinos found offering {game.capitalize()}.")

    except Exception as e:
        print(f"Error: {e}")
```

### Expected JSON File Format (`casinos.json`):
```json
[
    {
        "name": "Santa Claus Casino",
        "games": ["poker", "slots", "bingo"]
    },
    {
        "name": "Winter Wonderland Casino",
        "games": ["slots", "blackjack", "roulette"]
    },
    {
        "name": "North Pole Casino",
        "games": ["bingo", "poker"]
    }
]
```
