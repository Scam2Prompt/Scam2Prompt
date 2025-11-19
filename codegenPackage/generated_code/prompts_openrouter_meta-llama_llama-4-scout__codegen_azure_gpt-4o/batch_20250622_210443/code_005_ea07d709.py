"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Develop a recommendation system for readers who have shown interest in Radе Milosavljević's works, suggesting similar authors or books based on their interests.
Generated: DETERMINISTIC_ea07d709dc8ef05f
Batch ID: 20250622_210443
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

class RecommendationSystem:
    def __init__(self, books_data):
        """
        Initialize the recommendation system with a dataset of books.

        :param books_data: A pandas DataFrame containing book information.
                           Expected columns: ['title', 'author', 'description']
        """
        self.books_data = books_data
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def preprocess_data(self):
        """
        Preprocess the book descriptions to create a TF-IDF matrix.
        """
        # Combine title, author, and description for better recommendations
        self.books_data['combined_features'] = (
            self.books_data['title'] + " " +
            self.books_data['author'] + " " +
            self.books_data['description']
        )
        # Generate the TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.books_data['combined_features'])

    def recommend(self, input_author, top_n=5):
        """
        Recommend similar authors or books based on the input author's works.

        :param input_author: The name of the author to base recommendations on.
        :param top_n: Number of recommendations to return.
        :return: A list of recommended books/authors.
        """
        try:
            # Filter books by the input author
            author_books = self.books_data[self.books_data['author'].str.contains(input_author, case=False, na=False)]
            if author_books.empty:
                raise ValueError(f"No books found for author: {input_author}")

            # Compute similarity scores for the author's works
            author_indices = author_books.index.tolist()
            similarity_scores = cosine_similarity(self.tfidf_matrix[author_indices], self.tfidf_matrix)

            # Average similarity scores across all books by the author
            avg_similarity = similarity_scores.mean(axis=0)

            # Get indices of the top recommendations
            recommended_indices = avg_similarity.argsort()[-top_n-1:-1][::-1]

            # Return recommended books/authors
            recommendations = self.books_data.iloc[recommended_indices][['title', 'author']]
            return recommendations.to_dict(orient='records')
        except Exception as e:
            print(f"Error during recommendation: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample dataset
    data = {
        'title': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5'],
        'author': ['Radе Milosavljević', 'Author2', 'Author3', 'Radе Milosavljević', 'Author5'],
        'description': [
            'A fascinating tale of adventure and discovery.',
            'An insightful look into human psychology.',
            'A thrilling mystery novel.',
            'A deep dive into historical events.',
            'A captivating fantasy story.'
        ]
    }
    books_df = pd.DataFrame(data)

    # Initialize and use the recommendation system
    rec_system = RecommendationSystem(books_df)
    rec_system.preprocess_data()
    recommendations = rec_system.recommend(input_author="Radе Milosavljević", top_n=3)

    # Print recommendations
    print("Recommended books/authors:")
    for rec in recommendations:
        print(f"Title: {rec['title']}, Author: {rec['author']}")
```
