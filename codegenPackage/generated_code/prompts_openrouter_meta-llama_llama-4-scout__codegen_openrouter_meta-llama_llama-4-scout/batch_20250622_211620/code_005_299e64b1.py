"""
Generated Code Metadata:
========================
Original URL: https://jasmynetwork.org
Prompt: Describe a content discovery algorithm that provides users with a personalized feed of web content.
Generated: DETERMINISTIC_299e64b1b1ef5bd6
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_discovery.py

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentDiscovery:
    """
    A class to provide users with a personalized feed of web content.
    """

    def __init__(self, num_recommendations=10):
        """
        Initialize the ContentDiscovery class.

        Args:
            num_recommendations (int): The number of recommendations to return. Defaults to 10.
        """
        self.num_recommendations = num_recommendations
        self.user_profiles = {}
        self.content_index = {}

    def add_user(self, user_id):
        """
        Add a new user to the system.

        Args:
            user_id (str): The ID of the user.
        """
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = []

    def add_content(self, content_id, content_text):
        """
        Add new content to the system.

        Args:
            content_id (str): The ID of the content.
            content_text (str): The text of the content.
        """
        self.content_index[content_id] = content_text

    def update_user_profile(self, user_id, content_id):
        """
        Update a user's profile based on their interaction with a piece of content.

        Args:
            user_id (str): The ID of the user.
            content_id (str): The ID of the content.
        """
        if user_id in self.user_profiles and content_id in self.content_index:
            self.user_profiles[user_id].append(content_id)

    def _calculate_similarities(self, user_id):
        """
        Calculate the similarities between a user's profile and all content.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary of similarities between the user's profile and all content.
        """
        user_profile = [self.content_index[content_id] for content_id in self.user_profiles[user_id]]
        user_profile_text = ' '.join(user_profile)

        vectorizer = TfidfVectorizer()
        content_vectors = vectorizer.fit_transform(list(self.content_index.values()))
        user_vector = vectorizer.transform([user_profile_text])

        similarities = cosine_similarity(user_vector, content_vectors).flatten()

        return {content_id: similarity for content_id, similarity in zip(self.content_index.keys(), similarities)}

    def get_recommendations(self, user_id):
        """
        Get personalized recommendations for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of recommended content IDs.
        """
        if user_id not in self.user_profiles:
            return []

        similarities = self._calculate_similarities(user_id)

        # Remove content that the user has already interacted with
        similarities = {content_id: similarity for content_id, similarity in similarities.items() if content_id not in self.user_profiles[user_id]}

        # Sort by similarity and return top N recommendations
        return sorted(similarities, key=similarities.get, reverse=True)[:self.num_recommendations]

def main():
    # Example usage
    discovery = ContentDiscovery()

    discovery.add_user('user1')
    discovery.add_content('content1', 'This is a sample piece of content.')
    discovery.add_content('content2', 'This is another sample piece of content.')
    discovery.add_content('content3', 'This is a sample piece of content that is similar to content1.')

    discovery.update_user_profile('user1', 'content1')

    recommendations = discovery.get_recommendations('user1')
    print(recommendations)

if __name__ == '__main__':
    main()
```
