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
# recommendation_system.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self, books_df, authors_df, book_author_df):
        """
        Initialize the recommendation system.

        Parameters:
        - books_df (pd.DataFrame): DataFrame containing book information.
        - authors_df (pd.DataFrame): DataFrame containing author information.
        - book_author_df (pd.DataFrame): DataFrame containing book-author relationships.
        """
        self.books_df = books_df
        self.authors_df = authors_df
        self.book_author_df = book_author_df

    def _build_tfidf(self, text_column):
        """
        Build a TF-IDF vectorizer from a text column.

        Parameters:
        - text_column (str): Name of the text column.

        Returns:
        - tfidf (TfidfVectorizer): TF-IDF vectorizer.
        - tfidf_matrix (pd.DataFrame): TF-IDF matrix.
        """
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.books_df[text_column])
        return tfidf, tfidf_matrix

    def _get_similar_books(self, book_idx, tfidf_matrix, num_recommendations=5):
        """
        Get similar books based on cosine similarity.

        Parameters:
        - book_idx (int): Index of the book.
        - tfidf_matrix (pd.DataFrame): TF-IDF matrix.
        - num_recommendations (int): Number of recommendations.

        Returns:
        - similar_books (list): List of similar book indices.
        """
        similarities = cosine_similarity(tfidf_matrix[book_idx:book_idx+1], tfidf_matrix).flatten()
        similar_books = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[1:num_recommendations+1]
        return similar_books

    def _get_author_books(self, author_id):
        """
        Get books written by an author.

        Parameters:
        - author_id (int): ID of the author.

        Returns:
        - author_books (list): List of book indices written by the author.
        """
        author_books = self.book_author_df[self.book_author_df['author_id'] == author_id]['book_id'].tolist()
        return author_books

    def recommend_authors(self, reader_interests):
        """
        Recommend authors to a reader based on their interests.

        Parameters:
        - reader_interests (list): List of book IDs the reader is interested in.

        Returns:
        - recommended_authors (list): List of recommended author IDs.
        """
        recommended_authors = []
        for book_id in reader_interests:
            book_author_id = self.book_author_df[self.book_author_df['book_id'] == book_id]['author_id'].values
            if len(book_author_id) > 0:
                author_id = book_author_id[0]
                similar_books = self._get_similar_books(self.books_df[self.books_df['author_id'] == author_id].index[0], 
                                                        *self._build_tfidf('book_description'))
                similar_authors = self.book_author_df[self.book_author_df['book_id'].isin([self.books_df.iloc[i]['book_id'] for i in similar_books])]['author_id'].unique().tolist()
                recommended_authors.extend([author for author in similar_authors if author != author_id])
        recommended_authors = list(set(recommended_authors))
        return recommended_authors

    def recommend_books(self, reader_interests, num_recommendations=5):
        """
        Recommend books to a reader based on their interests.

        Parameters:
        - reader_interests (list): List of book IDs the reader is interested in.
        - num_recommendations (int): Number of recommendations.

        Returns:
        - recommended_books (list): List of recommended book IDs.
        """
        tfidf, tfidf_matrix = self._build_tfidf('book_description')
        recommended_books = []
        for book_id in reader_interests:
            book_idx = self.books_df[self.books_df['book_id'] == book_id].index[0]
            similar_books = self._get_similar_books(book_idx, tfidf_matrix, num_recommendations)
            recommended_books.extend([self.books_df.iloc[i]['book_id'] for i in similar_books])
        recommended_books = list(set(recommended_books))
        return recommended_books

# Example usage
if __name__ == "__main__":
    # Sample data
    books_df = pd.DataFrame({
        'book_id': [1, 2, 3, 4, 5],
        'book_title': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
        'book_description': ['This is book 1', 'This is book 2', 'This is book 3', 'This is book 4', 'This is book 5'],
        'author_id': [1, 1, 2, 2, 3]
    })

    authors_df = pd.DataFrame({
        'author_id': [1, 2, 3],
        'author_name': ['Radе Milosavljević', 'Author 2', 'Author 3']
    })

    book_author_df = pd.DataFrame({
        'book_id': [1, 2, 3, 4, 5],
        'author_id': [1, 1, 2, 2, 3]
    })

    # Create a recommendation system
    rs = RecommendationSystem(books_df, authors_df, book_author_df)

    # Recommend authors
    reader_interests = [1, 2]
    recommended_authors = rs.recommend_authors(reader_interests)
    print("Recommended authors:", authors_df[authors_df['author_id'].isin(recommended_authors)]['author_name'].tolist())

    # Recommend books
    recommended_books = rs.recommend_books(reader_interests)
    print("Recommended books:", books_df[books_df['book_id'].isin(recommended_books)]['book_title'].tolist())
```
