"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Generate a prompt to create a chatbot that provides reading recommendations for children based on their interests and reading level, incorporating Muna Kalati's resources and expertise.
Generated: DETERMINISTIC_868ec6cd26a1d8cc
Batch ID: 20250622_210348
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

# Define a class for the chatbot
class ReadingRecommendationChatbot:
    def __init__(self, books_df, interests_df):
        """
        Initialize the chatbot with a dataframe of books and interests.

        Args:
            books_df (pd.DataFrame): A dataframe containing book information.
            interests_df (pd.DataFrame): A dataframe containing interest information.
        """
        self.books_df = books_df
        self.interests_df = interests_df
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def get_recommendations(self, user_interests, reading_level):
        """
        Get reading recommendations for a user based on their interests and reading level.

        Args:
            user_interests (list): A list of the user's interests.
            reading_level (str): The user's reading level.

        Returns:
            list: A list of recommended books.
        """
        # Filter books by reading level
        filtered_books = self.books_df[self.books_df['reading_level'] == reading_level]

        # Vectorize book descriptions and user interests
        book_vectors = self.vectorizer.fit_transform(filtered_books['description'])
        interest_vectors = self.vectorizer.transform([' '.join(user_interests)])

        # Calculate cosine similarity between book vectors and interest vectors
        similarities = cosine_similarity(book_vectors, interest_vectors).flatten()

        # Get indices of top 5 similar books
        top_indices = similarities.argsort()[-5:][::-1]

        # Return recommended books
        return filtered_books.iloc[top_indices]['title'].tolist()

    def get_book_info(self, book_title):
        """
        Get information about a book.

        Args:
            book_title (str): The title of the book.

        Returns:
            dict: A dictionary containing book information.
        """
        book_info = self.books_df[self.books_df['title'] == book_title].to_dict(orient='records')
        return book_info[0] if book_info else None

def load_data(books_file, interests_file):
    """
    Load book and interest data from CSV files.

    Args:
        books_file (str): The path to the books CSV file.
        interests_file (str): The path to the interests CSV file.

    Returns:
        tuple: A tuple containing the books and interests dataframes.
    """
    try:
        books_df = pd.read_csv(books_file)
        interests_df = pd.read_csv(interests_file)
        return books_df, interests_df
    except FileNotFoundError:
        print("Error: One or both of the files were not found.")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: One or both of the files are empty.")
        return None, None

def main():
    # Load book and interest data
    books_df, interests_df = load_data('books.csv', 'interests.csv')

    if books_df is not None and interests_df is not None:
        # Create a chatbot instance
        chatbot = ReadingRecommendationChatbot(books_df, interests_df)

        # Example usage
        user_interests = ['animals', 'adventure']
        reading_level = 'grade_3'
        recommendations = chatbot.get_recommendations(user_interests, reading_level)
        print("Recommended books:")
        for book in recommendations:
            print(book)

        # Get book info
        book_title = recommendations[0]
        book_info = chatbot.get_book_info(book_title)
        print("\nBook info:")
        print(book_info)

if __name__ == "__main__":
    main()
```
