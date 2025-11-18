"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Generate code to create a recommendation engine for e-books based on user preferences and browsing history, inspired by Digielearning's curated content approach.
Generated: DETERMINISTIC_db4dbe172623c64a
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a recommendation engine written in Python:

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class EBookRecommendationEngine:
    """
    A recommendation engine for e-books based on user preferences and browsing history.
    """

    def __init__(self, ebooks_data_path: str, user_history_path: str):
        """
        Initialize the recommendation engine with e-books and user history data.

        :param ebooks_data_path: Path to the e-books dataset (CSV file).
        :param user_history_path: Path to the user browsing history dataset (CSV file).
        """
        try:
            # Load e-books data
            self.ebooks_df = pd.read_csv(ebooks_data_path)

            # Validate if necessary columns exist in the dataset
            if 'title' not in self.ebooks_df.columns or 'description' not in self.ebooks_df.columns:
                raise ValueError("E-books data must contain 'title' and 'description' columns.")

            # Load user browsing history
            self.user_history_df = pd.read_csv(user_history_path)

            # Validate if necessary columns exist in the dataset
            if 'user_id' not in self.user_history_df.columns or 'title' not in self.user_history_df.columns:
                raise ValueError("User history data must contain 'user_id' and 'title' columns.")

        except Exception as e:
            print(f"Error initializing engine: {e}")
            raise

    def recommend_books(self, user_id: int, top_n: int = 5) -> pd.DataFrame:
        """
        Recommend e-books based on a user's preferences and browsing history.

        :param user_id: ID of the user to recommend books for.
        :param top_n: Number of recommendations to return.
        :return: A DataFrame of recommended e-books.
        """
        try:
            # Filter user history
            user_history = self.user_history_df[self.user_history_df['user_id'] == user_id]

            # Check if the user has any browsing history
            if user_history.empty:
                print(f"No browsing history found for user ID {user_id}.")
                return pd.DataFrame()

            # Combine descriptions of books in user's browsing history
            browsing_descriptions = self.ebooks_df[self.ebooks_df['title'].isin(user_history['title'])]['description']
            browsing_text = " ".join(browsing_descriptions)

            # Vectorize e-books descriptions using TF-IDF
            tfidf_vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf_vectorizer.fit_transform(self.ebooks_df['description'])

            # Vectorize the combined browsing text
            user_vector = tfidf_vectorizer.transform([browsing_text])

            # Compute cosine similarity between user's vector and all e-books
            cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()

            # Get indices of top N similar books
            recommended_indices = cosine_similarities.argsort()[-top_n:][::-1]

            # Retrieve recommended e-books
            recommended_books = self.ebooks_df.iloc[recommended_indices]

            return recommended_books[['title', 'description']]
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            raise


# Example usage (ensure the CSV files exist and have proper data):
# ebooks_data.csv should have columns: 'title', 'description'
# user_history.csv should have columns: 'user_id', 'title'

if __name__ == "__main__":
    try:
        # Initialize the recommendation engine
        engine = EBookRecommendationEngine(ebooks_data_path="ebooks_data.csv",
                                           user_history_path="user_history.csv")

        # Get recommendations for a specific user
        user_id = 1  # Replace with a valid user ID
        recommendations = engine.recommend_books(user_id=user_id, top_n=5)

        # Display recommendations
        if not recommendations.empty:
            print("Recommended Books:")
            print(recommendations)
        else:
            print("No recommendations available.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to have the necessary `ebooks_data.csv` and `user_history.csv` files ready with appropriate data.
