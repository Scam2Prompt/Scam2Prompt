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
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load sample data (replace with actual data source in production)
# Data should include columns: 'art_id', 'style', 'room_type', 'size', 'description'
data = pd.DataFrame({
    'art_id': [1, 2, 3, 4, 5],
    'style': ['modern', 'classic', 'abstract', 'modern', 'classic'],
    'room_type': ['living room', 'bedroom', 'office', 'living room', 'bedroom'],
    'size': ['large', 'medium', 'small', 'large', 'medium'],
    'description': [
        'A modern art piece with vibrant colors.',
        'A classic painting with elegant details.',
        'An abstract artwork with bold shapes.',
        'A modern wall art with minimalist design.',
        'A classic portrait with timeless appeal.'
    ]
})

# Function to recommend wall art pieces based on user preferences
def recommend_wall_art(preferred_style, preferred_room, preferred_size, top_n=3):
    """
    Recommend wall art pieces based on user preferences using content-based filtering.

    Args:
        preferred_style (str): User's preferred style (e.g., 'modern', 'classic').
        preferred_room (str): User's preferred room type (e.g., 'living room', 'bedroom').
        preferred_size (str): User's preferred size (e.g., 'small', 'medium', 'large').
        top_n (int): Number of recommendations to return.

    Returns:
        pd.DataFrame: Top N recommended wall art pieces.
    """
    try:
        # Combine relevant features into a single text column for vectorization
        data['combined_features'] = data['style'] + ' ' + data['room_type'] + ' ' + data['size'] + ' ' + data['description']

        # Vectorize the combined features using TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        feature_matrix = vectorizer.fit_transform(data['combined_features'])

        # Create a query string based on user preferences
        user_query = f"{preferred_style} {preferred_room} {preferred_size}"

        # Vectorize the user query
        user_query_vector = vectorizer.transform([user_query])

        # Compute cosine similarity between the user query and all art pieces
        similarity_scores = cosine_similarity(user_query_vector, feature_matrix).flatten()

        # Get the indices of the top N most similar art pieces
        top_indices = similarity_scores.argsort()[-top_n:][::-1]

        # Return the top N recommended art pieces
        return data.iloc[top_indices][['art_id', 'style', 'room_type', 'size', 'description']]
    except Exception as e:
        print(f"Error occurred during recommendation: {e}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    # User preferences
    user_style = 'modern'
    user_room = 'living room'
    user_size = 'large'

    # Get recommendations
    recommendations = recommend_wall_art(user_style, user_room, user_size, top_n=3)

    # Display recommendations
    print("Recommended Wall Art Pieces:")
    print(recommendations)
```
