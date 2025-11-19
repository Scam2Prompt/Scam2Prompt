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
# beer_recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BeerRecommender:
    def __init__(self, customer_purchases, beer_data):
        """
        Initialize the BeerRecommender with customer purchase history and beer data.

        :param customer_purchases: DataFrame with customer_id, beer_id, and purchase_date
        :param beer_data: DataFrame with beer_id, name, style, and description
        """
        self.customer_purchases = customer_purchases
        self.beer_data = beer_data

    def _build_customer_profiles(self):
        """
        Build a TF-IDF vectorizer to represent customer preferences.

        :return: customer_profiles DataFrame with customer_id and vector representation
        """
        # Create a TF-IDF vectorizer to transform beer descriptions into vectors
        vectorizer = TfidfVectorizer(stop_words='english')

        # Fit the vectorizer to the beer descriptions and transform them into vectors
        beer_vectors = vectorizer.fit_transform(self.beer_data['description'])

        # Create a matrix to store customer profiles
        customer_profiles = pd.DataFrame({
            'customer_id': self.customer_purchases['customer_id'].unique()
        })

        # Iterate over each customer and build their profile
        for index, row in customer_profiles.iterrows():
            customer_id = row['customer_id']
            customer_beers = self.customer_purchases[self.customer_purchases['customer_id'] == customer_id]['beer_id']

            # Get the vector representation of the beers purchased by the customer
            customer_vector = None
            for beer_id in customer_beers:
                beer_vector = beer_vectors.toarray()[self.beer_data[self.beer_data['beer_id'] == beer_id].index[0]]
                if customer_vector is None:
                    customer_vector = beer_vector
                else:
                    customer_vector += beer_vector

            # Normalize the customer vector
            customer_vector = customer_vector / len(customer_beers)

            customer_profiles.loc[index, 'vector'] = customer_vector

        return customer_profiles

    def _calculate_similarities(self, customer_id):
        """
        Calculate the cosine similarity between a customer's profile and all beers.

        :param customer_id: ID of the customer
        :return: similarities DataFrame with beer_id and similarity score
        """
        # Get the customer's profile
        customer_profiles = self._build_customer_profiles()
        customer_vector = customer_profiles[customer_profiles['customer_id'] == customer_id]['vector'].iloc[0]

        # Calculate the cosine similarity between the customer vector and all beer vectors
        vectorizer = TfidfVectorizer(stop_words='english')
        beer_vectors = vectorizer.fit_transform(self.beer_data['description'])
        beer_vectors_array = beer_vectors.toarray()

        similarities = cosine_similarity([customer_vector], beer_vectors_array).flatten()

        # Create a DataFrame with the similarities
        similarities_df = pd.DataFrame({
            'beer_id': self.beer_data['beer_id'],
            'similarity': similarities
        })

        return similarities_df

    def recommend_beers(self, customer_id, num_recommendations=5):
        """
        Recommend beers to a customer based on their purchase history and preferences.

        :param customer_id: ID of the customer
        :param num_recommendations: Number of beer recommendations
        :return: recommended_beers DataFrame with beer_id, name, and similarity score
        """
        try:
            # Calculate the similarities between the customer and all beers
            similarities_df = self._calculate_similarities(customer_id)

            # Get the top-N recommended beers
            recommended_beers = similarities_df.nlargest(num_recommendations, 'similarity')

            # Merge the recommended beers with their names
            recommended_beers = recommended_beers.merge(self.beer_data[['beer_id', 'name']], on='beer_id')

            return recommended_beers[['beer_id', 'name', 'similarity']]
        except Exception as e:
            print(f"Error recommending beers: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Sample data
    customer_purchases = pd.DataFrame({
        'customer_id': [1, 1, 1, 2, 2, 3],
        'beer_id': [101, 102, 103, 101, 104, 105],
        'purchase_date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-01-05', '2022-02-10', '2022-03-01']
    })

    beer_data = pd.DataFrame({
        'beer_id': [101, 102, 103, 104, 105],
        'name': ['IPA', 'Pilsner', 'Stout', 'Sour', 'Wheat Beer'],
        'style': ['IPA', 'Pilsner', 'Stout', 'Sour', 'Wheat Beer'],
        'description': [
            'Hoppy and bitter IPA',
            'Crisp and refreshing Pilsner',
            'Rich and smooth Stout',
            'Tart and fruity Sour',
            'Light and citrusy Wheat Beer'
        ]
    })

    recommender = BeerRecommender(customer_purchases, beer_data)
    recommended_beers = recommender.recommend_beers(1)

    if recommended_beers is not None:
        print(recommended_beers)
```
