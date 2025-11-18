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

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class EbookRecommendationEngine:
    def __init__(self, ebooks_df):
        """
        Initializes the recommendation engine with a DataFrame of e-books.
        
        :param ebooks_df: A pandas DataFrame with columns ['title', 'author', 'genre', 'description']
        """
        if not isinstance(ebooks_df, pd.DataFrame):
            raise ValueError("ebooks_df must be a pandas DataFrame.")
        self.ebooks_df = ebooks_df
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.similarity_matrix = None
        self._create_similarity_matrix()

    def _create_similarity_matrix(self):
        """
        Creates a TF-IDF based cosine similarity matrix for the e-books.
        """
        # Combine relevant features into a single string
        self.ebooks_df['combined_features'] = (
            self.ebooks_df['author'] + ' ' + 
            self.ebooks_df['genre'] + ' ' + 
            self.ebooks_df['description']
        )
        
        # Compute the TF-IDF matrix
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.ebooks_df['combined_features'])
        
        # Compute the cosine similarity matrix
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend(self, title, num_recommendations=5):
        """
        Recommend e-books based on the given title.

        :param title: The title of the e-book for which recommendations are to be made.
        :param num_recommendations: The number of recommendations to return.
        :return: A DataFrame of recommended e-books.
        """
        # Check if the title exists in the DataFrame
        if title not in self.ebooks_df['title'].values:
            raise ValueError(f"E-book titled '{title}' not found in the database.")
        
        # Get the index of the e-book that matches the title
        idx = self.ebooks_df.index[self.ebooks_df['title'] == title].tolist()[0]

        # Get the pairwise similarity scores of all e-books with that e-book
        sim_scores = list(enumerate(self.similarity_matrix[idx]))

        # Sort the e-books based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the most similar e-books
        sim_scores = sim_scores[1:num_recommendations + 1]  # Exclude the first entry (itself)

        # Get the indices of the recommended e-books
        ebook_indices = [i[0] for i in sim_scores]

        # Return the top recommended e-books as a DataFrame
        return self.ebooks_df.iloc[ebook_indices][['title', 'author', 'genre']]

# Example usage:
if __name__ == "__main__":
    # Sample DataFrame of e-books
    data = {
        'title': ['Ebook A', 'Ebook B', 'Ebook C', 'Ebook D', 'Ebook E'],
        'author': ['Author 1', 'Author 2', 'Author 1', 'Author 3', 'Author 2'],
        'genre': ['Fiction', 'Non-Fiction', 'Fiction', 'Science', 'Non-Fiction'],
        'description': [
            'A great fiction book about life.',
            'An insightful non-fiction book.',
            'A journey through fictional worlds.',
            'Exploring the universe and science.',
            'Facts and figures in a non-fiction format.'
        ]
    }
    
    ebooks_df = pd.DataFrame(data)
    
    # Initialize the recommendation engine
    recommendation_engine = EbookRecommendationEngine(ebooks_df)

    # Get recommendations for a specific e-book
    try:
        recommendations = recommendation_engine.recommend('Ebook A', num_recommendations=3)
        print(recommendations)
    except ValueError as e:
        print(e)
```
