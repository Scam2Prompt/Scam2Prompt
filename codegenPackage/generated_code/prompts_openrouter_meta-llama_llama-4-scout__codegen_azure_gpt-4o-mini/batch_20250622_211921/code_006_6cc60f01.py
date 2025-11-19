"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Generate a list of natural stone types and their properties, similar to those featured on Hoorainz, and suggest how they could be used in coding a product recommendation engine."
Generated: DETERMINISTIC_6cc60f01c8a55284
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Stone:
    """
    A class to represent a natural stone and its properties.
    """

    def __init__(self, name: str, properties: Dict[str, Any]):
        """
        Initializes a new instance of Stone.

        :param name: The name of the stone.
        :param properties: A dictionary containing properties of the stone.
        """
        self.name = name
        self.properties = properties

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Stone instance to a dictionary.

        :return: A dictionary representation of the stone.
        """
        return {
            "name": self.name,
            "properties": self.properties
        }

class StoneRecommendationEngine:
    """
    A class to recommend stones based on user preferences.
    """

    def __init__(self, stones: List[Stone]):
        """
        Initializes the recommendation engine with a list of stones.

        :param stones: A list of Stone instances.
        """
        self.stones = stones

    def recommend(self, criteria: Dict[str, Any]) -> List[Stone]:
        """
        Recommends stones based on the given criteria.

        :param criteria: A dictionary of criteria to filter stones.
        :return: A list of recommended stones.
        """
        recommendations = []
        for stone in self.stones:
            if self._matches_criteria(stone, criteria):
                recommendations.append(stone)
        return recommendations

    def _matches_criteria(self, stone: Stone, criteria: Dict[str, Any]) -> bool:
        """
        Checks if a stone matches the given criteria.

        :param stone: The stone to check.
        :param criteria: The criteria to match against.
        :return: True if the stone matches the criteria, False otherwise.
        """
        for key, value in criteria.items():
            if key in stone.properties and stone.properties[key] != value:
                return False
        return True

def load_stones_from_json(file_path: str) -> List[Stone]:
    """
    Loads stones from a JSON file.

    :param file_path: The path to the JSON file containing stone data.
    :return: A list of Stone instances.
    """
    try:
        with open(file_path, 'r') as file:
            stone_data = json.load(file)
            return [Stone(name=stone['name'], properties=stone['properties']) for stone in stone_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Load stones from a JSON file
    stones = load_stones_from_json('stones.json')

    # Initialize the recommendation engine
    recommendation_engine = StoneRecommendationEngine(stones)

    # Define user criteria for recommendations
    user_criteria = {
        "color": "blue",
        "hardness": "high"
    }

    # Get recommendations based on user criteria
    recommended_stones = recommendation_engine.recommend(user_criteria)

    # Print recommended stones
    for stone in recommended_stones:
        print(stone.to_dict())
```
