"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a recommendation algorithm for an e-commerce site that suggests sports equipment based on user preferences for categories like "Beach Soccer," "Tênis de Mesa," and "Artes Marciais."
Generated: DETERMINISTIC_84012b4728c7c447
Batch ID: 20250612_151414
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
    def __init__(self, user_preferences, inventory_db):
        """
        Initialize the recommendation engine.

        :param user_preferences: A dictionary of user preferences for sports categories
            e.g., {"Beach Soccer": 3, "Tênis de Mesa": 5, "Artes Marciais": 4}
        :param inventory_db: Path to CSV file containing inventory data with columns: ['Item', 'Category', 'Description']
        """
        self.user_preferences = user_preferences
        self.inventory = pd.read_csv(inventory_db)
        self.recommendations = []

    def preprocess_data(self):
        """
        Preprocess inventory data by combining Category and Description into a single text column
        to prepare for similarity comparison.
        """
        self.inventory['CombinedText'] = self.inventory['Category'] + " " + self.inventory['Description']

    def generate_recommendations(self):
        """
        Generate recommendations based on user preferences and inventory similarity scores.
        """
        # Convert user preferences into a weighted preference text
        weighted_text = " ".join(
            [f"{category} " * weight for category, weight in self.user_preferences.items()]
        )

        # Vectorize the inventory and weighted preference text
        vectorizer = CountVectorizer()
        inventory_matrix = vectorizer.fit_transform(self.inventory['CombinedText'])
        user_vector = vectorizer.transform([weighted_text])

        # Calculate cosine similarity between user preferences and inventory items
        similarity_scores = cosine_similarity(user_vector, inventory_matrix).flatten()

        # Add similarity scores to the inventory data
        self.inventory['SimilarityScore'] = similarity_scores

        # Sort inventory by similarity score in descending order
        self.recommendations = self.inventory.sort_values(
            by='SimilarityScore', ascending=False
        ).reset_index(drop=True)

    def get_top_recommendations(self, top_n=5):
        """
        Retrieve the top N recommended items.

        :param top_n: Number of top recommendations to retrieve
        :return: DataFrame containing the top N recommended items
        """
        if self.recommendations.empty:
            raise ValueError("No recommendations found. Ensure you call generate_recommendations() first.")
        return self.recommendations.head(top_n)

if __name__ == "__main__":
    # Example user preferences
    user_preferences = {
        "Beach Soccer": 3,
        "Tênis de Mesa": 5,
        "Artes Marciais": 4
    }

    # Path to inventory database (CSV file containing sports equipment data)
    inventory_db = "sports_inventory.csv"

    try:
        # Initialize recommendation engine and generate recommendations
        engine = RecommendationEngine(user_preferences, inventory_db)
        engine.preprocess_data()
        engine.generate_recommendations()

        # Get the top 5 recommendations
        top_recommendations = engine.get_top_recommendations(top_n=5)
        print("Top Recommendations:")
        print(top_recommendations[['Item', 'Category', 'SimilarityScore']])
    except Exception as e:
        print(f"An error occurred: {e}")
```
