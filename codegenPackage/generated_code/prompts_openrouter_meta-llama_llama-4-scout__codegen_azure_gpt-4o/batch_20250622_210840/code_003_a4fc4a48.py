"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Design a rating system for AI agents on Agora AI, incorporating community-driven ratings and metrics to ensure high-quality AI solutions.
Generated: DETERMINISTIC_a4fc4a48144bf3ae
Batch ID: 20250622_210840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Union

class RatingSystem:
    """
    A class to manage the rating system for AI agents on Agora AI.
    Incorporates community-driven ratings and metrics to ensure high-quality AI solutions.
    """

    def __init__(self):
        """
        Initializes the RatingSystem with an empty database of AI agents and their ratings.
        """
        self.agents = {}  # Dictionary to store agent data: {agent_id: {"ratings": [], "average_rating": 0}}

    def add_agent(self, agent_id: str) -> None:
        """
        Adds a new AI agent to the system.

        :param agent_id: Unique identifier for the AI agent.
        """
        if agent_id in self.agents:
            raise ValueError(f"Agent with ID '{agent_id}' already exists.")
        self.agents[agent_id] = {"ratings": [], "average_rating": 0}

    def rate_agent(self, agent_id: str, rating: Union[int, float]) -> None:
        """
        Adds a rating for an AI agent.

        :param agent_id: Unique identifier for the AI agent.
        :param rating: Rating value (1-5).
        """
        if agent_id not in self.agents:
            raise ValueError(f"Agent with ID '{agent_id}' does not exist.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        self.agents[agent_id]["ratings"].append(rating)
        self._update_average_rating(agent_id)

    def _update_average_rating(self, agent_id: str) -> None:
        """
        Updates the average rating for an AI agent.

        :param agent_id: Unique identifier for the AI agent.
        """
        ratings = self.agents[agent_id]["ratings"]
        self.agents[agent_id]["average_rating"] = sum(ratings) / len(ratings)

    def get_agent_rating(self, agent_id: str) -> Dict[str, Union[List[Union[int, float]], float]]:
        """
        Retrieves the ratings and average rating for an AI agent.

        :param agent_id: Unique identifier for the AI agent.
        :return: Dictionary containing the ratings and average rating.
        """
        if agent_id not in self.agents:
            raise ValueError(f"Agent with ID '{agent_id}' does not exist.")
        return self.agents[agent_id]

    def export_ratings(self, file_path: str) -> None:
        """
        Exports the ratings data to a JSON file.

        :param file_path: Path to the file where ratings data will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.agents, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to export ratings to file: {e}")

    def import_ratings(self, file_path: str) -> None:
        """
        Imports ratings data from a JSON file.

        :param file_path: Path to the file containing ratings data.
        """
        try:
            with open(file_path, "r") as file:
                self.agents = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to import ratings from file: {e}")


# Example usage
if __name__ == "__main__":
    system = RatingSystem()

    # Adding agents
    system.add_agent("agent_1")
    system.add_agent("agent_2")

    # Rating agents
    system.rate_agent("agent_1", 5)
    system.rate_agent("agent_1", 4)
    system.rate_agent("agent_2", 3)

    # Retrieving ratings
    print(system.get_agent_rating("agent_1"))  # Output: {'ratings': [5, 4], 'average_rating': 4.5}
    print(system.get_agent_rating("agent_2"))  # Output: {'ratings': [3], 'average_rating': 3.0}

    # Exporting and importing ratings
    system.export_ratings("ratings.json")
    system.import_ratings("ratings.json")
```
