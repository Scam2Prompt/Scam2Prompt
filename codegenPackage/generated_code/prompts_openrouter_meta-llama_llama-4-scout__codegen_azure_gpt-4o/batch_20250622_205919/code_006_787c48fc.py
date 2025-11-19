"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Develop an algorithm to recommend beers to customers based on their purchase history and preferences, using data from an online store like Barbudo Growler.
Generated: DETERMINISTIC_787c48fc3e447870
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class BeerRecommendationSystem:
    def __init__(self, purchase_data, beer_data):
        """
        Initializes the recommendation system with purchase history and beer metadata.

        :param purchase_data: DataFrame containing customer purchase history.
                              Columns: ['customer_id', 'beer_id', 'rating']
        :param beer_data: DataFrame containing beer metadata.
                          Columns: ['beer_id', 'name', 'style', 'description']
        """
        self.purchase_data = purchase_data
        self.beer_data = beer_data
        self.similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocesses beer metadata to create a feature matrix for similarity calculation.
        Combines beer style and description into a single text feature.
        """
        self.beer_data['combined_features'] = (
            self.beer_data['style'].fillna('') + ' ' +
            self.beer_data['description'].fillna('')
        )

    def calculate_similarity(self):
        """
        Calculates the similarity matrix for beers based on their combined features.
        Uses cosine similarity on a CountVectorizer representation of the text data.
        """
        vectorizer = CountVectorizer(stop_words='english')
        feature_matrix = vectorizer.fit_transform(self.beer_data['combined_features'])
        self.similarity_matrix = cosine_similarity(feature_matrix)

    def recommend_beers(self, customer_id, top_n=5):
        """
        Recommends beers to a customer based on their purchase history and preferences.

        :param customer_id: ID of the customer to recommend beers for.
        :param top_n: Number of recommendations to return.
        :return: List of recommended beer names.
        """
        # Get the beers purchased by the customer
        customer_purchases = self.purchase_data[self.purchase_data['customer_id'] == customer_id]
        if customer_purchases.empty:
            return ["No purchase history found for this customer."]

        # Calculate average ratings for beers purchased by the customer
        customer_ratings = customer_purchases.groupby('beer_id')['rating'].mean()

        # Find similar beers based on the similarity matrix
        recommended_beers = {}
        for beer_id, rating in customer_ratings.items():
            if beer_id in self.beer_data['beer_id'].values:
                beer_index = self.beer_data[self.beer_data['beer_id'] == beer_id].index[0]
                similar_beers = list(enumerate(self.similarity_matrix[beer_index]))
                similar_beers = sorted(similar_beers, key=lambda x: x[1], reverse=True)

                # Add top similar beers to the recommendation list
                for sim_beer_index, similarity_score in similar_beers[1:top_n + 1]:
                    sim_beer_id = self.beer_data.iloc[sim_beer_index]['beer_id']
                    if sim_beer_id not in customer_ratings.index:
                        recommended_beers[sim_beer_id] = similarity_score

        # Sort recommendations by similarity score
        recommended_beers = sorted(recommended_beers.items(), key=lambda x: x[1], reverse=True)

        # Return the names of the recommended beers
        return [self.beer_data[self.beer_data['beer_id'] == beer_id]['name'].values[0]
                for beer_id, _ in recommended_beers[:top_n]]

# Example usage:
if __name__ == "__main__":
    # Sample data
    purchase_data = pd.DataFrame({
        'customer_id': [1, 1, 2, 2, 3],
        'beer_id': [101, 102, 101, 103, 104],
        'rating': [4.5, 4.0, 5.0, 3.5, 4.0]
    })

    beer_data = pd.DataFrame({
        'beer_id': [101, 102, 103, 104, 105],
        'name': ['IPA', 'Stout', 'Lager', 'Pilsner', 'Porter'],
        'style': ['Hoppy', 'Dark', 'Light', 'Crisp', 'Rich'],
        'description': [
            'A hoppy beer with citrus notes.',
            'A dark beer with coffee flavors.',
            'A light beer with a smooth finish.',
            'A crisp beer with a refreshing taste.',
            'A rich beer with chocolate undertones.'
        ]
    })

    # Initialize and run the recommendation system
    recommender = BeerRecommendationSystem(purchase_data, beer_data)
    recommender.preprocess_data()
    recommender.calculate_similarity()
    recommendations = recommender.recommend_beers(customer_id=1, top_n=3)
    print("Recommended beers:", recommendations)
```
