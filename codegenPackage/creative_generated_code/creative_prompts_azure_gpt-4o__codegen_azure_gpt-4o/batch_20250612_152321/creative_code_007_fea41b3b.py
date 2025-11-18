"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://barbudogrowler.cl
Prompt: Recommend a library for implementing a beer recommendation system based on user preferences (e.g., IPA, Stout). Provide example code in Python for generating recommendations using collaborative filtering.
Generated: DETERMINISTIC_fea41b3b018c3f8a
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample dataset for demonstration purposes
# DataFrame containing beer IDs, names, and style preferences
data = {
    "BeerID": [1, 2, 3, 4, 5],
    "BeerName": ["IPA Bliss", "Stout Supreme", "Wheat Wonder", "Amber Ale", "Double IPA"],
    "Style": ["IPA", "Stout", "Wheat", "Amber", "IPA"]
}
beer_df = pd.DataFrame(data)

# User preference data
# Dictionary containing user IDs and a list of beer IDs they have rated positively
user_preferences = {
    "User1": [1, 3],
    "User2": [2, 4],
    "User3": [1, 5],
    "User4": [3, 4]
}

# Function to calculate beer similarity based on style
def calculate_similarity(beer_data):
    """
    Calculates the similarity between beers based on their style using cosine similarity.

    Args:
        beer_data (pd.DataFrame): DataFrame containing beer information.

    Returns:
        pd.DataFrame: DataFrame representing the similarity matrix.
    """
    # Convert beer styles into a string format for similarity computation
    count_vectorizer = CountVectorizer()
    style_matrix = count_vectorizer.fit_transform(beer_data["Style"])
    
    # Compute cosine similarity between beer styles
    similarity = cosine_similarity(style_matrix)
    
    # Create similarity matrix DataFrame
    similarity_df = pd.DataFrame(similarity, index=beer_data["BeerName"], columns=beer_data["BeerName"])
    return similarity_df

# Function to recommend beers for a user
def recommend_beers(user_id, user_data, beer_data, similarity_matrix, n_recommendations=3):
    """
    Generates beer recommendations for a user based on collaborative filtering.

    Args:
        user_id (str): ID of the user to generate recommendations for.
        user_data (dict): Dictionary of user preferences.
        beer_data (pd.DataFrame): DataFrame containing beer information.
        similarity_matrix (pd.DataFrame): Beer similarity matrix.
        n_recommendations (int): Number of recommendations to generate.

    Returns:
        list: List of recommended beers.
    """
    try:
        # Get the list of beers rated positively by the user
        user_rated_beers = user_data.get(user_id, [])
        if not user_rated_beers:
            raise ValueError(f"No ratings found for user: {user_id}")

        # Aggregate similarity scores for beers rated by the user
        similarity_scores = similarity_matrix.loc[beer_data[beer_data["BeerID"].isin(user_rated_beers)]["BeerName"]]
        aggregate_scores = similarity_scores.sum(axis=0)

        # Exclude beers the user has already rated
        aggregate_scores = aggregate_scores[~aggregate_scores.index.isin(beer_data[beer_data["BeerID"].isin(user_rated_beers)]["BeerName"])]

        # Recommend top N beers based on similarity scores
        recommended_beers = aggregate_scores.nlargest(n_recommendations).index.tolist()
        return recommended_beers
    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return []

# Calculate similarity matrix
similarity_matrix = calculate_similarity(beer_df)

# Generate recommendations for a user
user_id = "User1"
recommendations = recommend_beers(user_id, user_preferences, beer_df, similarity_matrix, n_recommendations=3)

# Display recommendations
print(f"Recommended beers for {user_id}: {recommendations}")
```
