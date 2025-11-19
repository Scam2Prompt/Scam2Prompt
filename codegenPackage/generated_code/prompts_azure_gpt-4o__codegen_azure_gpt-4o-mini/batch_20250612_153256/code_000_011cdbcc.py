"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Write Python code to create a search filter for an anime streaming platform, referencing HiAnime's features like genre-based filtering and trending titles such as "One Piece" and "Dragon Ball Daima."
Generated: DETERMINISTIC_011cdbcc928cf75e
Batch ID: 20250612_153256
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

class Anime:
    """Class representing an anime with its attributes."""
    
    def __init__(self, title: str, genre: List[str], trending: bool):
        self.title = title
        self.genre = genre
        self.trending = trending

    def to_dict(self) -> Dict:
        """Convert the Anime object to a dictionary."""
        return {
            "title": self.title,
            "genre": self.genre,
            "trending": self.trending
        }

class AnimeFilter:
    """Class to filter anime based on genre and trending status."""
    
    def __init__(self, animes: List[Anime]):
        self.animes = animes

    def filter_by_genre(self, genre: str) -> List[Anime]:
        """Filter anime by a specific genre."""
        return [anime for anime in self.animes if genre in anime.genre]

    def filter_trending(self) -> List[Anime]:
        """Filter anime that are currently trending."""
        return [anime for anime in self.animes if anime.trending]

    def search(self, title: Optional[str] = None, genre: Optional[str] = None) -> List[Anime]:
        """Search for anime by title and/or genre."""
        results = self.animes
        
        if title:
            results = [anime for anime in results if title.lower() in anime.title.lower()]
        
        if genre:
            results = self.filter_by_genre(genre)
        
        return results

def load_anime_data(file_path: str) -> List[Anime]:
    """Load anime data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Anime(anime['title'], anime['genre'], anime['trending']) for anime in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """Main function to demonstrate the anime filtering functionality."""
    # Load anime data from a JSON file
    anime_list = load_anime_data('anime_data.json')
    
    # Create an instance of AnimeFilter
    anime_filter = AnimeFilter(anime_list)
    
    # Example usage of the filter
    trending_animes = anime_filter.filter_trending()
    print("Trending Animes:")
    for anime in trending_animes:
        print(anime.title)

    # Search for specific anime by title
    search_results = anime_filter.search(title="One Piece")
    print("\nSearch Results for 'One Piece':")
    for anime in search_results:
        print(anime.title)

    # Filter by genre
    genre_results = anime_filter.filter_by_genre("Action")
    print("\nAction Genre Animes:")
    for anime in genre_results:
        print(anime.title)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a JSON file named `anime_data.json` with the appropriate structure to test this code. The JSON should contain a list of anime objects with `title`, `genre`, and `trending` attributes.
