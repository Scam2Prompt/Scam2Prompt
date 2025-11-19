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
# novel_recommender.py

class Novel:
    """Represents a novel with its title, genres, and rating."""

    def __init__(self, title, genres, rating):
        """
        Initializes a Novel object.

        Args:
            title (str): The title of the novel.
            genres (list[str]): A list of genres the novel belongs to.
            rating (float): The average rating of the novel.
        """
        self.title = title
        self.genres = genres
        self.rating = rating

    def __repr__(self):
        return f"Novel('{self.title}', {self.genres}, {self.rating})"


class Reader:
    """Represents a reader with their preferred genres."""

    def __init__(self, name, preferred_genres):
        """
        Initializes a Reader object.

        Args:
            name (str): The name of the reader.
            preferred_genres (list[str]): A list of genres the reader prefers.
        """
        self.name = name
        self.preferred_genres = preferred_genres

    def __repr__(self):
        return f"Reader('{self.name}', {self.preferred_genres})"


class NovelRecommender:
    """Recommends novels to readers based on their preferred genres."""

    def __init__(self, novels):
        """
        Initializes a NovelRecommender object.

        Args:
            novels (list[Novel]): A list of Novel objects.
        """
        self.novels = novels

    def recommend(self, reader, num_recommendations=5):
        """
        Recommends novels to a reader based on their preferred genres.

        Args:
            reader (Reader): The reader to recommend novels to.
            num_recommendations (int, optional): The number of recommendations. Defaults to 5.

        Returns:
            list[Novel]: A list of recommended novels.
        """
        # Filter novels by reader's preferred genres
        recommended_novels = [
            novel
            for novel in self.novels
            if any(genre in reader.preferred_genres for genre in novel.genres)
        ]

        # Sort recommended novels by rating
        recommended_novels.sort(key=lambda novel: novel.rating, reverse=True)

        # Return top N recommendations
        return recommended_novels[:num_recommendations]


def main():
    # Example usage
    novels = [
        Novel("Novel 1", ["Fiction", "Thriller"], 4.5),
        Novel("Novel 2", ["Romance", "Drama"], 4.2),
        Novel("Novel 3", ["Fiction", "Science Fiction"], 4.8),
        Novel("Novel 4", ["Thriller", "Mystery"], 4.6),
        Novel("Novel 5", ["Romance", "Comedy"], 4.1),
    ]

    reader = Reader("John", ["Fiction", "Thriller", "Romance"])

    recommender = NovelRecommender(novels)
    recommendations = recommender.recommend(reader)

    print("Recommended novels:")
    for i, novel in enumerate(recommendations):
        print(f"{i+1}. {novel.title} ({', '.join(novel.genres)}) - {novel.rating}/5")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
