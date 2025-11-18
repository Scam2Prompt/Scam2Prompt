"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Generate code for a recommendation system that suggests Himalayan salt products based on user preferences, such as salt lamps, bath salts, or salt inhalers, using the categories provided by Craftimus Industries.
Generated: DETERMINISTIC_7818c53154541ffe
Batch ID: 20250612_152924
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
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class RecommendationSystem:
    def __init__(self, product_data):
        """
        Initializes the RecommendationSystem with product data.

        :param product_data: DataFrame containing product information and user ratings.
        """
        self.product_data = product_data
        self.scaler = StandardScaler()
        self.user_preferences = None
        self.similarity_matrix = None

    def preprocess_data(self):
        """
        Preprocess the product data for similarity calculations.
        This involves scaling the ratings.
        """
        # Fill missing values with the mean rating
        self.product_data.fillna(self.product_data.mean(), inplace=True)
        # Scale the features for better similarity measurement
        scaled_features = self.scaler.fit_transform(self.product_data.iloc[:, 1:])
        self.similarity_matrix = cosine_similarity(scaled_features)

    def set_user_preferences(self, preferences):
        """
        Set user preferences for the recommendation.

        :param preferences: Dictionary with product categories and user ratings.
        """
        self.user_preferences = preferences

    def recommend(self, top_n=5):
        """
        Recommend products based on user preferences.

        :param top_n: Number of top recommendations to return.
        :return: List of recommended product names.
        """
        if self.user_preferences is None:
            raise ValueError("User preferences are not set. Please set preferences before recommending.")

        # Create a DataFrame for user preferences
        user_pref_df = pd.DataFrame([self.user_preferences])
        scaled_user_pref = self.scaler.transform(user_pref_df)

        # Calculate similarity of user preferences with product data
        user_similarity = cosine_similarity(scaled_user_pref, self.similarity_matrix)

        # Get indices of top_n similar products
        similar_indices = user_similarity.argsort()[0][-top_n:][::-1]

        # Return the recommended product names
        return self.product_data.iloc[similar_indices, 0].tolist()

# Example usage
if __name__ == "__main__":
    # Sample product data
    data = {
        'Product Name': ['Himalayan Salt Lamp', 'Bath Salt', 'Salt Inhaler', 'Cooking Salt', 'Salt Block'],
        'Quality Rating': [4.5, 4.0, 4.8, 3.5, 4.2],
        'Popularity Score': [200, 150, 250, 100, 180],
        'Price': [25.99, 14.99, 19.99, 9.99, 21.99]
    }
    
    product_df = pd.DataFrame(data)

    # Initialize the recommendation system
    recommender = RecommendationSystem(product_df)

    # Preprocess the data
    recommender.preprocess_data()

    # Set user preferences for the recommendation
    user_preferences = {
        'Quality Rating': 5.0,
        'Popularity Score': 200,
        'Price': 20.0
    }
    recommender.set_user_preferences(user_preferences)

    # Get recommendations
    try:
        recommendations = recommender.recommend(top_n=3)
        print("Recommended Products:", recommendations)
    except ValueError as e:
        print("Error:", e)
```
