"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Develop a recommendation system for suggesting e-books to users based on their reading preferences and subscription plans on a platform similar to Digielearning."
Generated: DETERMINISTIC_5d61e31aac2e56ac
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List

# Define a class for the recommendation system
class EBookRecommender:
    def __init__(self, ebooks: pd.DataFrame, user_preferences: Dict[int, Dict[str, str]], subscription_plans: Dict[int, List[str]]):
        """
        Initialize the recommendation system.

        Args:
        - ebooks (pd.DataFrame): A DataFrame containing e-book information (id, title, description, genre).
        - user_preferences (Dict[int, Dict[str, str]]): A dictionary of user preferences (user_id, {genre, favorite_author}).
        - subscription_plans (Dict[int, List[str]]): A dictionary of user subscription plans (user_id, [plan1, plan2]).
        """
        self.ebooks = ebooks
        self.user_preferences = user_preferences
        self.subscription_plans = subscription_plans

    def _get_user_profile(self, user_id: int) -> Dict[str, str]:
        """
        Get a user's profile.

        Args:
        - user_id (int): The ID of the user.

        Returns:
        - Dict[str, str]: A dictionary containing the user's genre and favorite author.
        """
        return self.user_preferences.get(user_id, {})

    def _get_subscription_plans(self, user_id: int) -> List[str]:
        """
        Get a user's subscription plans.

        Args:
        - user_id (int): The ID of the user.

        Returns:
        - List[str]: A list of the user's subscription plans.
        """
        return self.subscription_plans.get(user_id, [])

    def _calculate_similarity(self, ebook: pd.Series, user_profile: Dict[str, str]) -> float:
        """
        Calculate the similarity between an e-book and a user's profile.

        Args:
        - ebook (pd.Series): A Series containing an e-book's information.
        - user_profile (Dict[str, str]): A dictionary containing a user's preferences.

        Returns:
        - float: The similarity score between the e-book and the user's profile.
        """
        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english')

        # Fit the vectorizer to the e-book descriptions and transform them into vectors
        ebook_vectors = vectorizer.fit_transform(self.ebooks['description'])

        # Transform the user's profile into a vector
        user_vector = vectorizer.transform([f"{user_profile.get('genre', '')} {user_profile.get('favorite_author', '')}"])

        # Calculate the cosine similarity between the e-book and the user's profile
        similarity = cosine_similarity(ebook_vectors, user_vector).flatten()

        # Return the similarity score for the given e-book
        return similarity[self.ebooks.index == ebook.name]

    def recommend_ebooks(self, user_id: int, num_recommendations: int = 5) -> List[int]:
        """
        Recommend e-books to a user based on their reading preferences and subscription plans.

        Args:
        - user_id (int): The ID of the user.
        - num_recommendations (int): The number of e-book recommendations to return. Defaults to 5.

        Returns:
        - List[int]: A list of recommended e-book IDs.
        """
        try:
            # Get the user's profile and subscription plans
            user_profile = self._get_user_profile(user_id)
            subscription_plans = self._get_subscription_plans(user_id)

            # Filter e-books based on the user's subscription plans
            filtered_ebooks = self.ebooks[self.ebooks['genre'].isin(subscription_plans)]

            # Calculate the similarity between each e-book and the user's profile
            similarities = filtered_ebooks.apply(lambda ebook: self._calculate_similarity(ebook, user_profile), axis=1)

            # Get the top-N recommended e-books
            recommended_ebooks = filtered_ebooks.iloc[similarities.argsort()[-num_recommendations:]].index.tolist()

            return recommended_ebooks

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample e-book data
    ebooks = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'title': ['E-book 1', 'E-book 2', 'E-book 3', 'E-book 4', 'E-book 5'],
        'description': ['This is a great e-book.', 'Another excellent e-book.', 'A fantastic e-book.', 'An amazing e-book.', 'A wonderful e-book.'],
        'genre': ['Fiction', 'Non-Fiction', 'Fiction', 'Non-Fiction', 'Fiction']
    })

    # Sample user preferences
    user_preferences = {
        1: {'genre': 'Fiction', 'favorite_author': 'Author A'},
        2: {'genre': 'Non-Fiction', 'favorite_author': 'Author B'}
    }

    # Sample subscription plans
    subscription_plans = {
        1: ['Fiction', 'Biography'],
        2: ['Non-Fiction', 'History']
    }

    # Create an instance of the recommendation system
    recommender = EBookRecommender(ebooks, user_preferences, subscription_plans)

    # Recommend e-books to a user
    recommended_ebooks = recommender.recommend_ebooks(1)

    print("Recommended e-books:", recommended_ebooks)
```
