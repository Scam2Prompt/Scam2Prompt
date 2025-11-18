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
from typing import List, Dict, Any

class Casino:
    """Class representing a casino with its details."""
    
    def __init__(self, name: str, location: str, game_types: List[str]):
        self.name = name
        self.location = location
        self.game_types = game_types

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Casino object to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "game_types": self.game_types
        }

class CasinoSearchTool:
    """Class to search casinos based on game types."""
    
    def __init__(self, casinos: List[Casino]):
        self.casinos = casinos

    def search_by_game_type(self, game_type: str) -> List[Dict[str, Any]]:
        """Searches for casinos that offer a specific game type.

        Args:
            game_type (str): The type of game to search for.

        Returns:
            List[Dict[str, Any]]: List of casinos that match the game type.
        """
        if not game_type:
            raise ValueError("Game type must be a non-empty string.")
        
        matching_casinos = [casino.to_dict() for casino in self.casinos if game_type.lower() in map(str.lower, casino.game_types)]
        
        if not matching_casinos:
            print(f"No casinos found for game type: {game_type}")
        
        return matching_casinos

def load_casinos_from_json(file_path: str) -> List[Casino]:
    """Loads casinos from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Casino]: List of Casino objects.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Casino(**casino) for casino in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        raise

def main():
    """Main function to demonstrate the casino search tool."""
    # Load casinos from a JSON file
    file_path = 'casinos.json'
    
    try:
        casinos = load_casinos_from_json(file_path)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Could not load casinos: {e}")
        return

    # Create the search tool
    search_tool = CasinoSearchTool(casinos)

    # Search for casinos by game type
    game_type = input("Enter the game type to search for (e.g., Poker, Slots, Bingo): ")
    try:
        results = search_tool.search_by_game_type(game_type)
        print("Casinos found:")
        for casino in results:
            print(f"- {casino['name']} located in {casino['location']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
