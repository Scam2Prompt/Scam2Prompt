"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: Generate code to create a recommendation engine for e-books based on user preferences and browsing history, inspired by Digielearning's curated content approach.
Generated: DETERMINISTIC_db4dbe172623c64a
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Recommendation Engine for E-books**
=====================================

**dependencies**
---------------

*   `numpy` for numerical computations
*   `pandas` for data manipulation and storage
*   `scikit-learn` for machine learning algorithms

**Code**
------

```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class EBookRecommender:
    def __init__(self, ebooks_df, user_history_df):
        """
        Initialize the recommendation engine.

        Parameters:
        ebooks_df (pd.DataFrame): DataFrame containing e-book information (title, author, description, genre)
        user_history_df (pd.DataFrame): DataFrame containing user browsing history (user_id, ebook_id)
        """
        self.ebooks_df = ebooks_df
        self.user_history_df = user_history_df
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def _create_ebook_vectors(self):
        """
        Create TF-IDF vectors for e-book descriptions.

        Returns:
        ebook_vectors (np.array): Matrix of TF-IDF vectors for e-book descriptions
        """
        ebook_descriptions = self.ebooks_df['description']
        ebook_vectors = self.vectorizer.fit_transform(ebook_descriptions)
        return ebook_vectors

    def _get_user_profile(self, user_id):
        """
        Create a user profile based on their browsing history.

        Parameters:
        user_id (int): ID of the user

        Returns:
        user_profile (np.array): TF-IDF vector representing the user's preferences
        """
        user_history = self.user_history_df[self.user_history_df['user_id'] == user_id]
        ebook_ids = user_history['ebook_id']
        ebook_descriptions = self.ebooks_df[self.ebooks_df['id'].isin(ebook_ids)]['description']
        user_profile = self.vectorizer.transform(ebook_descriptions).mean(axis=0)
        return user_profile

    def _calculate_similarities(self, ebook_vectors, user_profile):
        """
        Calculate cosine similarities between the user profile and e-book vectors.

        Parameters:
        ebook_vectors (np.array): Matrix of TF-IDF vectors for e-book descriptions
        user_profile (np.array): TF-IDF vector representing the user's preferences

        Returns:
        similarities (np.array): Cosine similarities between the user profile and e-book vectors
        """
        similarities = cosine_similarity(user_profile, ebook_vectors).flatten()
        return similarities

    def recommend(self, user_id, num_recommendations=5):
        """
        Generate e-book recommendations for a user.

        Parameters:
        user_id (int): ID of the user
        num_recommendations (int): Number of recommendations to generate (default=5)

        Returns:
        recommendations (list): List of recommended e-book IDs
        """
        ebook_vectors = self._create_ebook_vectors()
        user_profile = self._get_user_profile(user_id)
        similarities = self._calculate_similarities(ebook_vectors, user_profile)

        # Get the top-N recommended e-book IDs
        recommended_ebook_ids = self.ebooks_df['id'][np.argsort(-similarities)[:num_recommendations]].tolist()

        # Filter out e-books already in the user's browsing history
        user_history = self.user_history_df[self.user_history_df['user_id'] == user_id]
        filtered_recommendations = [ebook_id for ebook_id in recommended_ebook_ids if ebook_id not in user_history['ebook_id'].values]

        return filtered_recommendations

# Example usage
if __name__ == '__main__':
    # Sample e-book data
    ebooks_data = {
        'id': [1, 2, 3, 4, 5],
        'title': ['E-book 1', 'E-book 2', 'E-book 3', 'E-book 4', 'E-book 5'],
        'author': ['Author 1', 'Author 2', 'Author 3', 'Author 4', 'Author 5'],
        'description': ['This is a sample e-book about machine learning.', 'This is a sample e-book about data science.', 'This is a sample e-book about artificial intelligence.', 'This is a sample e-book about programming.', 'This is a sample e-book about software engineering.'],
        'genre': ['Machine Learning', 'Data Science', 'Artificial Intelligence', 'Programming', 'Software Engineering']
    }
    ebooks_df = pd.DataFrame(ebooks_data)

    # Sample user browsing history data
    user_history_data = {
        'user_id': [1, 1, 1, 2, 2],
        'ebook_id': [1, 2, 3, 4, 5]
    }
    user_history_df = pd.DataFrame(user_history_data)

    # Create a recommendation engine instance
    recommender = EBookRecommender(ebooks_df, user_history_df)

    # Generate recommendations for a user
    user_id = 1
    recommendations = recommender.recommend(user_id)
    print(f"Recommendations for User {user_id}: {recommendations}")
```
