"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Develop a content recommendation algorithm for a martial arts VOD platform that prioritizes user engagement and encourages users to explore different styles and genres of martial arts cinema.
Generated: DETERMINISTIC_f1580075003a4ae6
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

class ContentRecommender:
    """
    A class to recommend martial arts content to users based on their engagement history.
    """

    def __init__(self, user_history, content_data):
        """
        Initialize the content recommender.

        Parameters:
        user_history (pd.DataFrame): A DataFrame containing user engagement history.
        content_data (pd.DataFrame): A DataFrame containing information about martial arts content.
        """
        self.user_history = user_history
        self.content_data = content_data
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def _build_user_profiles(self):
        """
        Build user profiles based on their engagement history.

        Returns:
        dict: A dictionary where each key is a user ID and each value is a TF-IDF vector representing the user's profile.
        """
        user_profiles = {}
        for user_id, history in self.user_history.groupby('user_id'):
            watched_content = history['content_id'].tolist()
            content_features = self.content_data.loc[self.content_data['content_id'].isin(watched_content), 'genres'].tolist()
            user_profile = self.vectorizer.fit_transform([' '.join(content_features)])
            user_profiles[user_id] = user_profile
        return user_profiles

    def _build_content_profiles(self):
        """
        Build content profiles based on their genres.

        Returns:
        dict: A dictionary where each key is a content ID and each value is a TF-IDF vector representing the content's profile.
        """
        content_profiles = {}
        content_features = self.content_data['genres'].tolist()
        content_ids = self.content_data['content_id'].tolist()
        content_profile = self.vectorizer.fit_transform(content_features)
        for content_id, profile in zip(content_ids, content_profile):
            content_profiles[content_id] = profile
        return content_profiles

    def recommend(self, user_id, num_recommendations=5):
        """
        Recommend martial arts content to a user.

        Parameters:
        user_id (int): The ID of the user to recommend content to.
        num_recommendations (int): The number of recommendations to return.

        Returns:
        list: A list of recommended content IDs.
        """
        try:
            user_profiles = self._build_user_profiles()
            content_profiles = self._build_content_profiles()

            if user_id not in user_profiles:
                raise ValueError("User not found")

            user_profile = user_profiles[user_id]
            similarities = []
            for content_id, content_profile in content_profiles.items():
                similarity = cosine_similarity(user_profile, content_profile).flatten()[0]
                similarities.append((content_id, similarity))

            # Filter out content the user has already watched
            watched_content = self.user_history[self.user_history['user_id'] == user_id]['content_id'].tolist()
            similarities = [(content_id, similarity) for content_id, similarity in similarities if content_id not in watched_content]

            # Sort by similarity and return top N recommendations
            similarities.sort(key=lambda x: x[1], reverse=True)
            recommended_content = [content_id for content_id, _ in similarities[:num_recommendations]]

            return recommended_content

        except Exception as e:
            print(f"Error recommending content: {e}")
            return []

    def diversify_recommendations(self, recommended_content, num_styles=3):
        """
        Diversify recommendations to encourage users to explore different styles and genres.

        Parameters:
        recommended_content (list): A list of recommended content IDs.
        num_styles (int): The number of different styles/genres to include.

        Returns:
        list: A list of diversified recommended content IDs.
        """
        try:
            content_styles = self.content_data.set_index('content_id')['style'].to_dict()
            style_counts = defaultdict(int)
            diversified_recommendations = []

            for content_id in recommended_content:
                style = content_styles[content_id]
                if style_counts[style] < num_styles:
                    diversified_recommendations.append(content_id)
                    style_counts[style] += 1

            # Fill remaining recommendations with other content
            remaining_recommendations = num_styles * num_recommendations - len(diversified_recommendations)
            other_content = [content_id for content_id in self.content_data['content_id'].tolist() if content_id not in diversified_recommendations]
            diversified_recommendations += other_content[:remaining_recommendations]

            return diversified_recommendations

        except Exception as e:
            print(f"Error diversifying recommendations: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data
    user_history = pd.DataFrame({
        'user_id': [1, 1, 1, 2, 2],
        'content_id': [101, 102, 103, 101, 104],
        'engagement': [1, 1, 0.5, 1, 1]
    })

    content_data = pd.DataFrame({
        'content_id': [101, 102, 103, 104, 105],
        'title': ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5'],
        'genres': ['Action, Drama', 'Comedy, Action', 'Drama, Romance', 'Action, Thriller', 'Comedy, Romance'],
        'style': ['Karate', 'Taekwondo', 'Judo', 'Boxing', 'Wrestling']
    })

    recommender = ContentRecommender(user_history, content_data)
    recommended_content = recommender.recommend(1, num_recommendations=5)
    diversified_recommendations = recommender.diversify_recommendations(recommended_content, num_styles=3)
    print("Recommended content:", recommended_content)
    print("Diversified recommendations:", diversified_recommendations)
```
