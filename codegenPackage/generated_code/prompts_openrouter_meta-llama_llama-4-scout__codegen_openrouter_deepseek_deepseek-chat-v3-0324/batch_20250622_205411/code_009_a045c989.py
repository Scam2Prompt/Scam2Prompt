"""
Generated Code Metadata:
========================
Original URL: https://collapse.fun
Prompt: "Develop a function to parse game data, like the distances for Corpse & Backpack or Resources in Rust, as showcased in Collapse.fun's product features."
Generated: DETERMINISTIC_a045c989352dad90
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from typing import Dict, List, Optional, Union

class GameDataParser:
    """
    A class to parse game data similar to Rust's Corpse & Backpack distances or Resources.
    Handles JSON data and provides methods to extract specific game metrics.
    """
    
    def __init__(self, game_data: Union[str, Dict]):
        """
        Initialize the parser with game data.
        
        Args:
            game_data: Either a JSON string or a pre-parsed dictionary containing game data.
        
        Raises:
            ValueError: If game_data is neither a string nor a dictionary.
            json.JSONDecodeError: If game_data is a string but not valid JSON.
        """
        if isinstance(game_data, str):
            try:
                self.data = json.loads(game_data)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Invalid JSON data: {e}", e.doc, e.pos)
        elif isinstance(game_data, dict):
            self.data = game_data
        else:
            raise ValueError("game_data must be a JSON string or a dictionary")
    
    def get_distance_metrics(self) -> Dict[str, float]:
        """
        Extract distance metrics like Corpse & Backpack distances from the game data.
        
        Returns:
            A dictionary with metric names as keys and their values as floats.
            
        Raises:
            KeyError: If required distance fields are missing.
        """
        try:
            distances = {
                'corpse_distance': float(self.data['distances']['corpse']),
                'backpack_distance': float(self.data['distances']['backpack'])
            }
            return distances
        except KeyError as e:
            raise KeyError(f"Missing required distance field: {e}")
    
    def get_resources(self) -> Dict[str, Union[int, float]]:
        """
        Extract resource quantities from the game data.
        
        Returns:
            A dictionary with resource names as keys and their quantities as values.
            
        Raises:
            KeyError: If required resource fields are missing.
        """
        try:
            resources = {
                'wood': self.data['resources']['wood'],
                'stone': self.data['resources']['stone'],
                'metal': self.data['resources']['metal'],
                'sulfur': self.data['resources']['sulfur']
            }
            return resources
        except KeyError as e:
            raise KeyError(f"Missing required resource field: {e}")
    
    def find_pattern_in_data(self, pattern: str) -> List[str]:
        """
        Search for a regex pattern in the game data's string values.
        
        Args:
            pattern: The regex pattern to search for.
            
        Returns:
            A list of all matches found in string values.
            
        Raises:
            re.error: If the pattern is not a valid regex.
        """
        try:
            regex = re.compile(pattern)
        except re.error as e:
            raise re.error(f"Invalid regex pattern: {e}")
        
        matches = []
        self._search_dict(self.data, regex, matches)
        return matches
    
    def _search_dict(self, data: Union[Dict, List], regex: re.Pattern, matches: List[str]):
        """
        Recursively search a dictionary or list for regex matches in string values.
        
        Args:
            data: The dictionary or list to search.
            regex: The compiled regex pattern.
            matches: List to store found matches.
        """
        if isinstance(data, dict):
            for value in data.values():
                self._search_dict(value, regex, matches)
        elif isinstance(data, list):
            for item in data:
                self._search_dict(item, regex, matches)
        elif isinstance(data, str) and regex.search(data):
            matches.append(data)
```
