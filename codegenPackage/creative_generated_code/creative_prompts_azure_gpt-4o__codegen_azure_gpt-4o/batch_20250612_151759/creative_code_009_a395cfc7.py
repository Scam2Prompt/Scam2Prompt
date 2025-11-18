"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-lab.net
Prompt: Develop a recommendation engine that suggests similar artists to those listed on Soniculture, such as Elias Landberg or Misc., based on user preferences.
Generated: DETERMINISTIC_a395cfc73cbffbc6
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


class RecommendationEngine:
    """Recommendation Engine for suggesting similar artists based on user preferences."""

    def __init__(self, artist_data):
        """
        Initializes the recommendation engine with artist data.

        Args:
            artist_data (pd.DataFrame): DataFrame containing artist names and descriptions.
                                       Should have columns: ['artist', 'description'].
        """
        # Validate input data
        if not {'artist', 'description'}.issubset(artist_data.columns):
            raise ValueError("Input DataFrame must contain 'artist' and 'description' columns.")

        # Store artist data
        self.artist_data = artist_data

        # Initialize CountVectorizer for text-based similarity
        self.vectorizer = CountVectorizer(stop_words='english')

        # Precompute artist similarity matrix
        self.similarity_matrix = self._compute_similarity_matrix()

    def _compute_similarity_matrix(self):
        """
        Computes the cosine similarity matrix between artist descriptions.

        Returns:
            pd.DataFrame: Cosine similarity matrix with artists as both rows and columns.
        """
        # Transform descriptions into a matrix of token counts
        description_matrix = self.vectorizer.fit_transform(self.artist_data['description'])

        # Compute cosine similarity
        similarity_scores = cosine_similarity(description_matrix)

        # Convert similarity scores into a DataFrame for better usability
        similarity_df = pd.DataFrame(
            similarity_scores,
            index=self.artist_data['artist'],
            columns=self.artist_data['artist']
        )

        return similarity_df

    def recommend(self, artist_name, top_n=5):
        """
        Provides recommendations for similar artists.

        Args:
            artist_name (str): Name of the artist to base recommendations on.
            top_n (int): Number of similar artists to recommend. Default is 5.

        Returns:
            list: A list of recommended artist names.
        """
        # Validate artist name exists in the dataset
        if artist_name not in self.similarity_matrix.index:
            raise ValueError(f"Artist '{artist_name}' not found in the dataset.")

        # Fetch similarity scores for the given artist
        similarity_scores = self.similarity_matrix.loc[artist_name]

        # Sort scores in descending order and exclude the artist itself
        similar_artists = similarity_scores.sort_values(ascending=False).drop(artist_name)

        # Return the top N recommended artists
        return similar_artists.head(top_n).index.tolist()


# Example usage
if __name__ == '__main__':
    # Sample dataset containing artists and their descriptions
    data = {
        'artist': ['Elias Landberg', 'Misc.', 'Artist A', 'Artist B', 'Artist C'],
        'description': [
            'Deep techno beats and atmospheric soundscapes',
            'Minimalist electronic compositions',
            'Experimental techno with industrial influences',
            'Ambient electronica with dreamy textures',
            'Progressive house music with melodic layers'
        ]
    }

    # Convert sample data into a DataFrame
    artist_df = pd.DataFrame(data)

    try:
        # Initialize the recommendation engine
        recommender = RecommendationEngine(artist_df)

        # Get recommendations for a specific artist
        recommendations = recommender.recommend('Elias Landberg', top_n=3)
        print(f"Recommendations for Elias Landberg: {recommendations}")
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
