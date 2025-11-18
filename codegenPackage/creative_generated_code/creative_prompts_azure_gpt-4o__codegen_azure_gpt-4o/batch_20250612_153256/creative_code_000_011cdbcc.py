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

class AnimeStreamingPlatform:
    """
    A class to represent an anime streaming platform with search and filtering functionality.
    """
    def __init__(self):
        # Example dataset representing anime titles with genres and trending status.
        self.anime_catalog = [
            {"title": "One Piece", "genre": ["Adventure", "Fantasy"], "is_trending": True},
            {"title": "Dragon Ball Daima", "genre": ["Action", "Fantasy"], "is_trending": True},
            {"title": "Naruto", "genre": ["Action", "Adventure"], "is_trending": False},
            {"title": "Attack on Titan", "genre": ["Action", "Horror"], "is_trending": False},
            {"title": "My Hero Academia", "genre": ["Action", "School"], "is_trending": False},
        ]

    def search_by_genre(self, genre):
        """
        Filter anime title(s) based on genre.

        :param genre: Genre to filter by (e.g., "Action", "Fantasy").
        :return: List of anime titles matching the genre.
        """
        try:
            # Filter the catalog based on the specified genre
            filtered_anime = [anime["title"] for anime in self.anime_catalog if genre in anime["genre"]]
            return filtered_anime
        except Exception as e:
            # Handle unexpected errors
            print(f"An error occurred while filtering by genre: {e}")
            return []

    def get_trending_titles(self):
        """
        Get a list of trending anime titles.

        :return: List of trending anime titles.
        """
        try:
            # Filter the catalog to include only trending titles
            trending_anime = [anime["title"] for anime in self.anime_catalog if anime["is_trending"]]
            return trending_anime
        except Exception as e:
            # Handle unexpected errors
            print(f"An error occurred while fetching trending titles: {e}")
            return []

    def export_to_json(self, file_name):
        """
        Export the anime catalog to a JSON file.

        :param file_name: Name of the JSON file to export to.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(self.anime_catalog, file, ensure_ascii=False, indent=4)
            print(f"Anime catalog successfully exported to {file_name}")
        except Exception as e:
            # Handle file I/O errors
            print(f"An error occurred while exporting to JSON: {e}")


# Example usage
if __name__ == "__main__":
    platform = AnimeStreamingPlatform()

    # Search by genre
    action_anime = platform.search_by_genre("Action")
    print("Action Anime:", action_anime)

    # Get trending titles
    trending_anime = platform.get_trending_titles()
    print("Trending Anime:", trending_anime)

    # Export catalog to JSON
    platform.export_to_json("anime_catalog.json")
```
