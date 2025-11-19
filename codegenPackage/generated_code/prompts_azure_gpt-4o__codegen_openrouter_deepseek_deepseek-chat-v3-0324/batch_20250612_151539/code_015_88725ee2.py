"""
Generated Code Metadata:
========================
Original URL: https://casinouniswap.com
Prompt: Write code to implement a search tool that allows users to find casinos based on game types like poker, slots, and bingo, as seen on Santa Claus Casino.
Generated: DETERMINISTIC_88725ee253817fe6
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class CasinoSearchTool:
    """
    A search tool to find casinos based on game types.
    """

    def __init__(self, data_file: str = "casinos.json"):
        """
        Initialize the search tool with casino data.
        
        Args:
            data_file: Path to JSON file containing casino data.
        """
        self.casinos = self._load_data(data_file)

    def _load_data(self, data_file: str) -> List[Dict]:
        """
        Load casino data from JSON file.
        
        Args:
            data_file: Path to JSON file.
            
        Returns:
            List of casino dictionaries.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            json.JSONDecodeError: If data file is not valid JSON.
        """
        try:
            with open(data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {data_file} not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in {data_file}", doc="", pos=0)

    def search_by_game(self, game_type: str) -> List[Dict]:
        """
        Search casinos by game type.
        
        Args:
            game_type: Game type to search for (e.g., 'poker', 'slots', 'bingo').
            
        Returns:
            List of casinos that offer the specified game type.
        """
        if not self.casinos:
            return []

        game_type = game_type.lower().strip()
        return [casino for casino in self.casinos 
                if game_type in [g.lower() for g in casino.get('games', [])]]

    def get_all_game_types(self) -> List[str]:
        """
        Get all unique game types available across all casinos.
        
        Returns:
            List of unique game types.
        """
        if not self.casinos:
            return []

        game_types = set()
        for casino in self.casinos:
            for game in casino.get('games', []):
                game_types.add(game.lower())
        return sorted(game_types)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize search tool
        search_tool = CasinoSearchTool()
        
        # Get all available game types
        print("Available game types:")
        for game in search_tool.get_all_game_types():
            print(f"- {game}")
        
        # Search for casinos with poker
        print("\nCasinos with poker:")
        poker_casinos = search_tool.search_by_game("poker")
        for casino in poker_casinos:
            print(f"{casino['name']} - Games: {', '.join(casino['games'])}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
