"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Recommend a library for implementing a beer recommendation system based on user preferences (e.g., IPA, Stout). Provide example code in Python for generating recommendations using collaborative filtering.
Generated: DETERMINISTIC_fea41b3b018c3f8a
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from scipy import spatial
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

class BeerRecommender:
    """
    A class used to recommend beers based on user preferences.

    Attributes:
    ----------
    user_beer_matrix : pandas.DataFrame
        A matrix where rows represent users, columns represent beers, and cell values represent ratings.
    beer_features : pandas.DataFrame
        A matrix where rows represent beers and columns represent features (e.g., style, ABV, IBU).

    Methods:
    -------
    fit(user_beer_matrix, beer_features)
        Fits the recommender to the user-beer matrix and beer features.
    recommend(user_id, num_recommendations)
        Generates beer recommendations for a given user.
    """

    def __init__(self):
        self.user_beer_matrix = None
        self.beer_features = None
        self.model = None

    def fit(self, user_beer_matrix, beer_features):
        """
        Fits the recommender to the user-beer matrix and beer features.

        Parameters:
        ----------
        user_beer_matrix : pandas.DataFrame
            A matrix where rows represent users, columns represent beers, and cell values represent ratings.
        beer_features : pandas.DataFrame
            A matrix where rows represent beers and columns represent features (e.g., style, ABV, IBU).
        """
        self.user_beer_matrix = user_beer_matrix
        self.beer_features = beer_features

        # Scale beer features
        scaler = MinMaxScaler()
        self.beer_features[['ABV', 'IBU']] = scaler.fit_transform(self.beer_features[['ABV', 'IBU']])

        # Create a collaborative filtering model
        self.model = NearestNeighbors(n_neighbors=10, metric='cosine', algorithm='brute')
        self.model.fit(self.user_beer_matrix)

    def recommend(self, user_id, num_recommendations):
        """
        Generates beer recommendations for a given user.

        Parameters:
        ----------
        user_id : int
            The ID of the user for whom to generate recommendations.
        num_recommendations : int
            The number of recommendations to generate.

        Returns:
        -------
        recommended_beers : list
            A list of beer IDs recommended for the given user.
        """
        if self.user_beer_matrix is None or self.beer_features is None:
            raise ValueError("Model not fitted")

        try:
            # Get the user's rating vector
            user_vector = self.user_beer_matrix.iloc[user_id]

            # Find similar users using collaborative filtering
            distances, indices = self.model.kneighbors([user_vector])

            # Get the beers rated by similar users
            similar_user_beers = self.user_beer_matrix.iloc[indices[0]]

            # Calculate the similarity between the target user and similar users
            similarities = 1 - spatial.distance.cosine(user_vector, similar_user_beers)

            # Get the beers that similar users have rated highly
            recommended_beers = []
            for i, beer in enumerate(self.user_beer_matrix.columns):
                if user_vector[i] == 0 and similar_user_beers[i].mean() > 3:
                    recommended_beers.append((beer, similarities.mean()))

            # Sort recommendations by similarity and return top-N
            recommended_beers.sort(key=lambda x: x[1], reverse=True)
            return [beer[0] for beer in recommended_beers[:num_recommendations]]

        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample user-beer matrix
    user_beer_matrix = pd.DataFrame({
        'Beer1': [4, 0, 3, 0, 0],
        'Beer2': [0, 5, 0, 4, 0],
        'Beer3': [3, 0, 0, 0, 5],
        'Beer4': [0, 4, 0, 0, 0],
        'Beer5': [0, 0, 5, 3, 0]
    }, index=[0, 1, 2, 3, 4])

    # Sample beer features
    beer_features = pd.DataFrame({
        'style': ['IPA', 'Stout', 'IPA', 'Lager', 'Stout'],
        'ABV': [6.5, 4.5, 7.0, 5.0, 4.0],
        'IBU': [60, 30, 70, 20, 40]
    }, index=['Beer1', 'Beer2', 'Beer3', 'Beer4', 'Beer5'])

    recommender = BeerRecommender()
    recommender.fit(user_beer_matrix, beer_features)
    recommended_beers = recommender.recommend(0, 3)
    print("Recommended beers:", recommended_beers)
```
