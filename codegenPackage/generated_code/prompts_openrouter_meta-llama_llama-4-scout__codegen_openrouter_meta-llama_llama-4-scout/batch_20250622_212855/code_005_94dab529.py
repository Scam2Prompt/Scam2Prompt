"""
Generated Code Metadata:
========================
Original URL: https://cuadrosblangar.es
Prompt: "Develop a recommendation system for suggesting wall art pieces to customers based on their preferred style, room type, and size, using techniques like collaborative filtering or content-based filtering."
Generated: DETERMINISTIC_94dab529ef9a66a4
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recommendation_system.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

class WallArtRecommender:
    def __init__(self, wall_art_data):
        """
        Initialize the WallArtRecommender with wall art data.

        Parameters:
        wall_art_data (pd.DataFrame): DataFrame containing wall art information.
            - 'style' (str): Style of the wall art (e.g., modern, abstract, etc.)
            - 'room_type' (str): Type of room the wall art is suitable for (e.g., living room, bedroom, etc.)
            - 'size' (str): Size of the wall art (e.g., small, medium, large)
            - 'description' (str): Brief description of the wall art
        """
        self.wall_art_data = wall_art_data

    def _build_content_based_filtering_model(self):
        """
        Build a content-based filtering model using TF-IDF vectorization and cosine similarity.

        Returns:
        tfidf (TfidfVectorizer): TF-IDF vectorizer
        cosine_sim (pd.DataFrame): Cosine similarity matrix
        """
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.wall_art_data['description'])

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        cosine_sim = pd.DataFrame(cosine_sim, index=self.wall_art_data.index, columns=self.wall_art_data.index)

        return tfidf, cosine_sim

    def _get_similar_items(self, item_id, cosine_sim, num_similar=5):
        """
        Get similar items to the given item.

        Parameters:
        item_id (int): ID of the item
        cosine_sim (pd.DataFrame): Cosine similarity matrix
        num_similar (int): Number of similar items to retrieve

        Returns:
        similar_items (pd.DataFrame): DataFrame containing similar items
        """
        sim_scores = list(enumerate(cosine_sim[item_id]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_similar+1]

        similar_items = self.wall_art_data.iloc[[i[0] for i in sim_scores]]
        return similar_items

    def recommend(self, preferred_style, room_type, size, num_recommendations=5):
        """
        Recommend wall art pieces based on the customer's preferences.

        Parameters:
        preferred_style (str): Customer's preferred style
        room_type (str): Type of room
        size (str): Size of the wall art
        num_recommendations (int): Number of recommendations to generate

        Returns:
        recommendations (pd.DataFrame): DataFrame containing recommended wall art pieces
        """
        filtered_data = self.wall_art_data[
            (self.wall_art_data['style'] == preferred_style) &
            (self.wall_art_data['room_type'] == room_type) &
            (self.wall_art_data['size'] == size)
        ]

        if filtered_data.empty:
            # If no exact matches, use content-based filtering to find similar items
            tfidf, cosine_sim = self._build_content_based_filtering_model()
            query = f"{preferred_style} {room_type} {size}"
            query_vector = tfidf.transform([query])
            sim_scores = linear_kernel(query_vector, tfidf_matrix).flatten()
            sim_scores = pd.DataFrame({'item_id': self.wall_art_data.index, 'sim_score': sim_scores})
            sim_scores = sim_scores.sort_values(by='sim_score', ascending=False).head(num_recommendations)

            recommendations = self.wall_art_data.loc[sim_scores['item_id']]
        else:
            # Use collaborative filtering ( simple popularity-based approach )
            popularity_scores = filtered_data['style'].value_counts().sort_index()
            recommended_items = popularity_scores.nlargest(num_recommendations).index

            recommendations = self.wall_art_data[self.wall_art_data['style'].isin(recommended_items)]

        return recommendations

def main():
    # Example usage
    wall_art_data = pd.DataFrame({
        'style': ['modern', 'abstract', 'modern', 'traditional', 'abstract', 'modern'],
        'room_type': ['living room', 'bedroom', 'living room', 'kitchen', 'bedroom', 'living room'],
        'size': ['large', 'small', 'medium', 'large', 'small', 'medium'],
        'description': [
            'A modern art piece for the living room',
            'An abstract art piece for the bedroom',
            'A modern art piece with geometric shapes',
            'A traditional art piece for the kitchen',
            'An abstract art piece with vibrant colors',
            'A modern art piece with a minimalist design'
        ]
    })

    recommender = WallArtRecommender(wall_art_data)

    preferred_style = 'modern'
    room_type = 'living room'
    size = 'medium'

    recommendations = recommender.recommend(preferred_style, room_type, size)
    print(recommendations)

if __name__ == "__main__":
    main()
```
