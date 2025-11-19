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
# rating_system.py

from typing import List, Dict, Optional
from statistics import mean

class Rating:
    """Class to represent a single rating given by a user."""
    
    def __init__(self, user_id: str, score: int, comment: Optional[str] = None):
        """
        Initialize a new rating.

        :param user_id: Unique identifier for the user giving the rating.
        :param score: Rating score (1 to 5).
        :param comment: Optional comment provided by the user.
        """
        if score < 1 or score > 5:
            raise ValueError("Score must be between 1 and 5.")
        
        self.user_id = user_id
        self.score = score
        self.comment = comment


class AIAgent:
    """Class to represent an AI agent with community-driven ratings."""
    
    def __init__(self, agent_id: str, name: str):
        """
        Initialize a new AI agent.

        :param agent_id: Unique identifier for the AI agent.
        :param name: Name of the AI agent.
        """
        self.agent_id = agent_id
        self.name = name
        self.ratings: List[Rating] = []

    def add_rating(self, rating: Rating):
        """
        Add a rating to the AI agent.

        :param rating: Rating object to be added.
        """
        self.ratings.append(rating)

    def average_rating(self) -> float:
        """
        Calculate the average rating of the AI agent.

        :return: Average rating score.
        """
        if not self.ratings:
            return 0.0
        return mean(rating.score for rating in self.ratings)

    def get_ratings(self) -> List[Dict]:
        """
        Get a list of all ratings for the AI agent.

        :return: List of ratings as dictionaries.
        """
        return [{"user_id": rating.user_id, "score": rating.score, "comment": rating.comment} for rating in self.ratings]


class RatingSystem:
    """Class to manage the rating system for multiple AI agents."""
    
    def __init__(self):
        """Initialize the rating system with an empty agent registry."""
        self.agents: Dict[str, AIAgent] = {}

    def register_agent(self, agent_id: str, name: str) -> AIAgent:
        """
        Register a new AI agent in the system.

        :param agent_id: Unique identifier for the AI agent.
        :param name: Name of the AI agent.
        :return: The created AIAgent object.
        """
        if agent_id in self.agents:
            raise ValueError("Agent ID already exists.")
        
        agent = AIAgent(agent_id, name)
        self.agents[agent_id] = agent
        return agent

    def rate_agent(self, agent_id: str, user_id: str, score: int, comment: Optional[str] = None):
        """
        Rate an AI agent.

        :param agent_id: Unique identifier for the AI agent to be rated.
        :param user_id: Unique identifier for the user giving the rating.
        :param score: Rating score (1 to 5).
        :param comment: Optional comment provided by the user.
        """
        if agent_id not in self.agents:
            raise ValueError("Agent not found.")
        
        rating = Rating(user_id, score, comment)
        self.agents[agent_id].add_rating(rating)

    def get_agent_average_rating(self, agent_id: str) -> float:
        """
        Get the average rating of an AI agent.

        :param agent_id: Unique identifier for the AI agent.
        :return: Average rating score.
        """
        if agent_id not in self.agents:
            raise ValueError("Agent not found.")
        
        return self.agents[agent_id].average_rating()

    def get_agent_ratings(self, agent_id: str) -> List[Dict]:
        """
        Get all ratings for a specific AI agent.

        :param agent_id: Unique identifier for the AI agent.
        :return: List of ratings as dictionaries.
        """
        if agent_id not in self.agents:
            raise ValueError("Agent not found.")
        
        return self.agents[agent_id].get_ratings()


# Example usage (commented out for production readiness)
# if __name__ == "__main__":
#     rating_system = RatingSystem()
#     agent = rating_system.register_agent("agent_1", "AI Assistant")
#     rating_system.rate_agent("agent_1", "user_1", 5, "Excellent service!")
#     rating_system.rate_agent("agent_1", "user_2", 4, "Very helpful.")
#     print("Average Rating:", rating_system.get_agent_average_rating("agent_1"))
#     print("All Ratings:", rating_system.get_agent_ratings("agent_1"))
```
