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
from typing import Dict, List

def parse_game_data(game_data: str) -> Dict:
    """
    Parse game data from a JSON string.

    Args:
    game_data (str): A JSON string containing game data.

    Returns:
    Dict: A dictionary representing the parsed game data.

    Raises:
    ValueError: If the input string is not a valid JSON.
    """

    try:
        # Attempt to parse the game data from JSON
        data = json.loads(game_data)
        return data
    except json.JSONDecodeError as e:
        # Handle invalid JSON input
        raise ValueError("Invalid JSON input") from e


def extract_distances(game_data: Dict) -> Dict:
    """
    Extract distances for Corpse & Backpack or Resources from game data.

    Args:
    game_data (Dict): A dictionary representing the game data.

    Returns:
    Dict: A dictionary containing the extracted distances.

    Raises:
    KeyError: If the required keys are not found in the game data.
    """

    try:
        # Define the expected keys for distances
        expected_keys = ["corpse_distance", "backpack_distance", "resource_distances"]

        # Initialize an empty dictionary to store the extracted distances
        distances = {}

        # Iterate over the expected keys
        for key in expected_keys:
            # Check if the key exists in the game data
            if key in game_data:
                distances[key] = game_data[key]
            else:
                # Raise an error if a required key is not found
                raise KeyError(f"Missing key: {key}")

        return distances
    except KeyError as e:
        # Handle missing keys in the game data
        raise ValueError("Invalid game data") from e


def parse_rust_resources(game_data: Dict) -> List:
    """
    Parse Rust resources from game data.

    Args:
    game_data (Dict): A dictionary representing the game data.

    Returns:
    List: A list of Rust resources.

    Raises:
    KeyError: If the required keys are not found in the game data.
    """

    try:
        # Define the expected key for Rust resources
        expected_key = "resources"

        # Check if the key exists in the game data
        if expected_key in game_data:
            # Return the Rust resources as a list
            return game_data[expected_key]
        else:
            # Raise an error if the required key is not found
            raise KeyError(f"Missing key: {expected_key}")
    except KeyError as e:
        # Handle missing keys in the game data
        raise ValueError("Invalid game data") from e


# Example usage
if __name__ == "__main__":
    game_data_json = '''
    {
        "corpse_distance": 100,
        "backpack_distance": 50,
        "resource_distances": {
            "ore": 200,
            "wood": 150
        },
        "resources": ["ore", "wood", "stone"]
    }
    '''

    game_data = parse_game_data(game_data_json)
    distances = extract_distances(game_data)
    rust_resources = parse_rust_resources(game_data)

    print("Distances:")
    print(distances)
    print("\nRust Resources:")
    print(rust_resources)
```
