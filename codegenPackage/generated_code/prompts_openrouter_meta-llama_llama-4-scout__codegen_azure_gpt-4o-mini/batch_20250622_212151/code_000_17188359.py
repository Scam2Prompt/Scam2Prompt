"""
Generated Code Metadata:
========================
Original URL: https://memeindex.it.com
Prompt: What is Memeindex and how does it relate to IT or technology?
Generated: DETERMINISTIC_17188359b84222bd
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MemeIndex:
    """
    A class to represent a Meme Index, which tracks the popularity and trends of memes
    in relation to technology and IT.
    """

    def __init__(self):
        """
        Initializes the MemeIndex with an empty list of memes.
        """
        self.memes = []

    def add_meme(self, meme_name: str, popularity_score: int):
        """
        Adds a new meme to the index.

        Parameters:
        meme_name (str): The name of the meme.
        popularity_score (int): The popularity score of the meme (0-100).

        Raises:
        ValueError: If the popularity score is not between 0 and 100.
        """
        if not (0 <= popularity_score <= 100):
            raise ValueError("Popularity score must be between 0 and 100.")
        
        meme = {
            'name': meme_name,
            'popularity_score': popularity_score
        }
        self.memes.append(meme)

    def get_meme(self, meme_name: str):
        """
        Retrieves a meme by its name.

        Parameters:
        meme_name (str): The name of the meme to retrieve.

        Returns:
        dict: The meme details if found, otherwise None.
        """
        for meme in self.memes:
            if meme['name'] == meme_name:
                return meme
        return None

    def get_top_memes(self, top_n: int = 5):
        """
        Retrieves the top N memes based on their popularity score.

        Parameters:
        top_n (int): The number of top memes to retrieve.

        Returns:
        list: A list of the top N memes sorted by popularity score.
        """
        # Sort memes by popularity score in descending order
        sorted_memes = sorted(self.memes, key=lambda x: x['popularity_score'], reverse=True)
        return sorted_memes[:top_n]

    def __str__(self):
        """
        Returns a string representation of the MemeIndex.
        """
        return f"MemeIndex with {len(self.memes)} memes."

# Example usage
if __name__ == "__main__":
    try:
        meme_index = MemeIndex()
        meme_index.add_meme("Distracted Boyfriend", 85)
        meme_index.add_meme("Change My Mind", 90)
        meme_index.add_meme("Is This a Pigeon?", 75)

        print(meme_index.get_top_memes(2))  # Get top 2 memes
        print(meme_index.get_meme("Distracted Boyfriend"))  # Get specific meme
    except ValueError as e:
        print(f"Error: {e}")
```
