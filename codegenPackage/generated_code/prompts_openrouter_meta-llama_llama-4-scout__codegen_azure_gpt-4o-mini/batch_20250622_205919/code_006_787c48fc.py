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
from sklearn.preprocessing import StandardScaler
import numpy as np

class BeerRecommender:
    def __init__(self, purchase_history: pd.DataFrame, beer_profiles: pd.DataFrame):
        """
        Initializes the BeerRecommender with purchase history and beer profiles.

        :param purchase_history: DataFrame containing customer purchase history with columns ['customer_id', 'beer_id', 'rating']
        :param beer_profiles: DataFrame containing beer profiles with columns ['beer_id', 'style', 'abv', 'ibu', 'flavor_profile']
        """
        self.purchase_history = purchase_history
        self.beer_profiles = beer_profiles
        self.user_preferences = None
        self.similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocesses the purchase history to create a user-item matrix and calculates user preferences.
        """
        # Create a user-item matrix
        user_item_matrix = self.purchase_history.pivot_table(index='customer_id', columns='beer_id', values='rating').fillna(0)
        
        # Standardize the user-item matrix
        scaler = StandardScaler()
        self.user_preferences = scaler.fit_transform(user_item_matrix)

    def calculate_similarity(self):
        """
        Calculates the cosine similarity between users based on their preferences.
        """
        self.similarity_matrix = cosine_similarity(self.user_preferences)
        
    def recommend_beers(self, customer_id: int, num_recommendations: int = 5) -> list:
        """
        Recommends beers to a customer based on their purchase history and preferences.

        :param customer_id: The ID of the customer for whom to recommend beers.
        :param num_recommendations: The number of beer recommendations to return.
        :return: A list of recommended beer IDs.
        """
        try:
            # Check if the similarity matrix is calculated
            if self.similarity_matrix is None:
                raise ValueError("Similarity matrix has not been calculated. Please run 'calculate_similarity()' first.")

            # Get the index of the customer
            customer_index = self.purchase_history['customer_id'].unique().tolist().index(customer_id)

            # Get similar users
            similar_users = list(enumerate(self.similarity_matrix[customer_index]))
            similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:]  # Exclude self

            # Get beer recommendations based on similar users' ratings
            recommended_beers = {}
            for user_index, similarity_score in similar_users:
                user_id = self.purchase_history['customer_id'].unique()[user_index]
                user_ratings = self.purchase_history[self.purchase_history['customer_id'] == user_id]
                
                for _, row in user_ratings.iterrows():
                    beer_id = row['beer_id']
                    rating = row['rating']
                    if beer_id not in recommended_beers:
                        recommended_beers[beer_id] = 0
                    recommended_beers[beer_id] += rating * similarity_score

            # Sort beers by score and return the top recommendations
            recommended_beers = sorted(recommended_beers.items(), key=lambda x: x[1], reverse=True)
            return [beer[0] for beer in recommended_beers[:num_recommendations]]

        except ValueError as e:
            print(f"Error: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data for purchase history and beer profiles
    purchase_history_data = {
        'customer_id': [1, 1, 2, 2, 3, 3, 3],
        'beer_id': [101, 102, 101, 103, 102, 104, 105],
        'rating': [5, 4, 4, 5, 3, 4, 2]
    }
    beer_profiles_data = {
        'beer_id': [101, 102, 103, 104, 105],
        'style': ['IPA', 'Lager', 'Stout', 'Pale Ale', 'Wheat'],
        'abv': [6.5, 5.0, 7.0, 5.5, 4.5],
        'ibu': [60, 20, 40, 30, 15],
        'flavor_profile': ['Citrus', 'Malty', 'Roasty', 'Fruity', 'Spicy']
    }

    purchase_history_df = pd.DataFrame(purchase_history_data)
    beer_profiles_df = pd.DataFrame(beer_profiles_data)

    recommender = BeerRecommender(purchase_history_df, beer_profiles_df)
    recommender.preprocess_data()
    recommender.calculate_similarity()
    
    # Get recommendations for customer with ID 1
    recommendations = recommender.recommend_beers(customer_id=1)
    print("Recommended beers for customer 1:", recommendations)
```
