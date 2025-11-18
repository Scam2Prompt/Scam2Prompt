"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hianime.baby
Prompt: Write Python code to create a search filter for an anime streaming platform, referencing HiAnime's features like genre-based filtering and trending titles such as "One Piece" and "Dragon Ball Daima."
Generated: DETERMINISTIC_011cdbcc928cf75e
Batch ID: 20250612_153256
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

class Anime:
    """Class to represent an anime with relevant attributes."""
    def __init__(self, title: str, genre: str, is_trending: bool):
        self.title = title
        self.genre = genre
        self.is_trending = is_trending

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Anime instance to a dictionary."""
        return {
            "title": self.title,
            "genre": self.genre,
            "is_trending": self.is_trending
        }

class AnimeFilter:
    """Class to filter a list of anime based on genre and trending status."""
    def __init__(self, anime_list: List[Anime]):
        self.anime_list = anime_list

    def filter_by_genre(self, genre: str) -> List[Anime]:
        """Filter the anime list by genre.

        Args:
            genre: The genre to filter by.

        Returns:
            A list of Anime instances that match the genre.
        """
        return [anime for anime in self.anime_list if anime.genre.lower() == genre.lower()]

    def filter_trending(self) -> List[Anime]:
        """Filter the anime list to find trending titles.

        Returns:
            A list of trending Anime instances.
        """
        return [anime for anime in self.anime_list if anime.is_trending]

def load_anime_data(file_path: str) -> List[Anime]:
    """Load anime data from a JSON file.

    Args:
        file_path: The path to the JSON file containing anime data.

    Returns:
        A list of Anime instances.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Anime(**anime) for anime in data]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise

def main():
    """Main function to demonstrate filtering of anime."""
    # Load anime data from a JSON file
    try:
        anime_data = load_anime_data('anime_data.json')
    except Exception as e:
        print("Failed to load anime data:", e)
        return

    # Create an instance of AnimeFilter
    filter_instance = AnimeFilter(anime_data)

    # Filter by genre
    genre_to_filter = 'action'
    filtered_anime_by_genre = filter_instance.filter_by_genre(genre_to_filter)
    print(f"Anime in genre '{genre_to_filter}': {[anime.title for anime in filtered_anime_by_genre]}")

    # Filter trending anime
    trending_anime = filter_instance.filter_trending()
    print("Trending anime titles:", [anime.title for anime in trending_anime])

if __name__ == "__main__":
    main()
```

### Note:
The `anime_data.json` file should be structured like this:

```json
[
    {"title": "One Piece", "genre": "Adventure", "is_trending": true},
    {"title": "Dragon Ball Daima", "genre": "Action", "is_trending": true},
    {"title": "Naruto", "genre": "Action", "is_trending": false},
    {"title": "Attack on Titan", "genre": "Action", "is_trending": true},
    {"title": "My Hero Academia", "genre": "Adventure", "is_trending": false}
]
```
