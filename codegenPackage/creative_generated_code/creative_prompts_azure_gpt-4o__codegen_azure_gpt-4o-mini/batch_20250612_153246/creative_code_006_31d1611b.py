"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Generate code to implement a recommendation system for safety footwear based on user input, such as "durable leather boots for construction work" or "lightweight composite shoes for airport management."
Generated: DETERMINISTIC_31d1611bfcad13c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FootwearRecommendationSystem:
    """
    A class to implement a recommendation system for safety footwear
    based on user input using cosine similarity on TF-IDF features.
    """

    def __init__(self, footwear_data):
        """
        Initializes the recommendation system with footwear data.

        Args:
            footwear_data (pd.DataFrame): A DataFrame containing footwear details.
        """
        self.footwear_data = footwear_data
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.footwear_data['description'])

    def recommend(self, user_input, num_recommendations=5):
        """
        Recommends safety footwear based on user input.

        Args:
            user_input (str): The user's input describing the desired footwear.
            num_recommendations (int): The number of recommendations to return.

        Returns:
            pd.DataFrame: A DataFrame containing recommended footwear.
        """
        # Validate user input
        if not isinstance(user_input, str) or not user_input.strip():
            raise ValueError("User input must be a non-empty string.")

        # Transform user input into TF-IDF matrix
        user_tfidf = self.vectorizer.transform([user_input])

        # Calculate cosine similarity between user input and footwear data
        cosine_similarities = cosine_similarity(user_tfidf, self.tfidf_matrix).flatten()

        # Get indices of the top N recommendations
        recommended_indices = cosine_similarities.argsort()[-num_recommendations:][::-1]

        # Return recommended footwear details
        return self.footwear_data.iloc[recommended_indices]

# Example footwear data - In production, this should come from a reliable database
footwear_data = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'description': [
        "durable leather boots for construction work",
        "lightweight composite shoes for airport management",
        "rugged waterproof boots for outdoor work",
        "steel-toe shoes for heavy machinery operation"
    ]
})

# Initialize the recommendation system with footwear data
recommendation_system = FootwearRecommendationSystem(footwear_data)

# Example user input
user_input = "durable leather boots for construction work"

try:
    # Get recommendations based on user input
    recommendations = recommendation_system.recommend(user_input)
    print("Recommended Footwear:")
    print(recommendations)
except ValueError as e:
    print(f"Error: {e}")
```
