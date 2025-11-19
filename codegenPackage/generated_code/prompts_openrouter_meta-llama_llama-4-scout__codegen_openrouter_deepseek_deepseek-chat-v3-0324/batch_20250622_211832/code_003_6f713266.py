"""
Generated Code Metadata:
========================
Original URL: https://norwegianget.net
Prompt: "Create a Python script to build a simple novel recommendation system based on genres and reader preferences, inspired by the variety of novels listed on NorwegianGet."
Generated: DETERMINISTIC_6f71326684b726de
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict, Optional

class NovelRecommendationSystem:
    """
    A simple novel recommendation system based on genres and reader preferences.
    """

    def __init__(self, novels_data: List[Dict]):
        """
        Initialize the recommendation system with a list of novels.

        Args:
            novels_data: List of dictionaries containing novel data.
                        Each dictionary should have 'title', 'author', and 'genres' keys.
        """
        self.novels = novels_data
        self.genre_index = self._build_genre_index()

    def _build_genre_index(self) -> Dict[str, List[Dict]]:
        """
        Build an index of novels grouped by genre for faster lookup.

        Returns:
            Dictionary where keys are genres and values are lists of novels in that genre.
        """
        genre_index = {}
        for novel in self.novels:
            for genre in novel['genres']:
                if genre not in genre_index:
                    genre_index[genre] = []
                genre_index[genre].append(novel)
        return genre_index

    def recommend_by_genres(
        self,
        preferred_genres: List[str],
        exclude_read: Optional[List[str]] = None,
        num_recommendations: int = 5
    ) -> List[Dict]:
        """
        Recommend novels based on preferred genres.

        Args:
            preferred_genres: List of genres the reader prefers.
            exclude_read: Optional list of novel titles to exclude from recommendations.
            num_recommendations: Number of recommendations to return.

        Returns:
            List of recommended novel dictionaries.
        """
        if exclude_read is None:
            exclude_read = []

        # Collect all novels in preferred genres
        candidates = []
        for genre in preferred_genres:
            if genre in self.genre_index:
                candidates.extend(self.genre_index[genre])

        # Remove duplicates and exclude already read novels
        unique_candidates = []
        seen_titles = set(exclude_read)
        for novel in candidates:
            if novel['title'] not in seen_titles:
                unique_candidates.append(novel)
                seen_titles.add(novel['title'])

        # Sort by number of matching genres (higher is better)
        unique_candidates.sort(
            key=lambda x: len(set(x['genres']) & set(preferred_genres)),
            reverse=True
        )

        # Return top recommendations
        return unique_candidates[:num_recommendations]

    def recommend_random(
        self,
        exclude_read: Optional[List[str]] = None,
        num_recommendations: int = 5
    ) -> List[Dict]:
        """
        Recommend random novels from the collection.

        Args:
            exclude_read: Optional list of novel titles to exclude from recommendations.
            num_recommendations: Number of recommendations to return.

        Returns:
            List of recommended novel dictionaries.
        """
        if exclude_read is None:
            exclude_read = []

        candidates = [novel for novel in self.novels if novel['title'] not in exclude_read]
        return random.sample(candidates, min(num_recommendations, len(candidates)))


def load_novels_from_file(file_path: str) -> List[Dict]:
    """
    Load novels data from a JSON file.

    Args:
        file_path: Path to the JSON file containing novels data.

    Returns:
        List of novels as dictionaries.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Novels data file not found at {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in novels data file", file_path, 0)


def main():
    """
    Example usage of the NovelRecommendationSystem.
    """
    try:
        # Load sample data (in a real application, this would be from a database or file)
        novels_data = load_novels_from_file('novels.json')
        
        # Initialize recommendation system
        recommender = NovelRecommendationSystem(novels_data)

        # Example: Get recommendations for a user who likes Fantasy and Adventure
        preferred_genres = ['Fantasy', 'Adventure']
        recommendations = recommender.recommend_by_genres(preferred_genres)

        print("Recommended novels:")
        for i, novel in enumerate(recommendations, 1):
            print(f"{i}. {novel['title']} by {novel['author']} (Genres: {', '.join(novel['genres'])})")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
