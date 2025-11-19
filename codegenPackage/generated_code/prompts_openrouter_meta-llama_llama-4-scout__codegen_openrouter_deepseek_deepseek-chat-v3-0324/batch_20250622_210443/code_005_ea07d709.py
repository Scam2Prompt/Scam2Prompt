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
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BookRecommendationSystem:
    """
    A recommendation system for suggesting similar authors/books based on user interests.
    """
    
    def __init__(self, data_path: str = "book_data.csv"):
        """
        Initialize the recommendation system with book data.
        
        Args:
            data_path (str): Path to the CSV file containing book data.
                           Expected columns: 'title', 'author', 'description', 'genre'
        """
        try:
            self.df = pd.read_csv(data_path)
            logger.info(f"Successfully loaded data from {data_path}")
            
            # Preprocess data
            self.df['content'] = self.df['title'] + " " + self.df['author'] + " " + self.df['description'] + " " + self.df['genre']
            self.df['content'] = self.df['content'].fillna('')
            
            # Initialize TF-IDF Vectorizer
            self.vectorizer = TfidfVectorizer(stop_words='english')
            self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
            
        except FileNotFoundError:
            logger.error(f"File not found: {data_path}")
            raise
        except Exception as e:
            logger.error(f"Error initializing recommendation system: {str(e)}")
            raise
    
    def get_recommendations(self, liked_books: List[str], num_recommendations: int = 5) -> List[Dict]:
        """
        Get book recommendations based on liked books.
        
        Args:
            liked_books (List[str]): List of book titles the user has liked
            num_recommendations (int): Number of recommendations to return
            
        Returns:
            List[Dict]: List of recommended books with details
        """
        try:
            # Find indices of liked books
            liked_indices = []
            for book in liked_books:
                matches = self.df[self.df['title'].str.contains(book, case=False)].index
                if len(matches) > 0:
                    liked_indices.extend(matches)
            
            if not liked_indices:
                logger.warning("No matching books found in the database")
                return []
            
            # Calculate average vector for liked books
            liked_vectors = self.tfidf_matrix[liked_indices]
            avg_vector = liked_vectors.mean(axis=0)
            
            # Calculate cosine similarity with all books
            similarities = cosine_similarity(avg_vector, self.tfidf_matrix).flatten()
            
            # Get top recommendations (excluding liked books)
            similar_indices = similarities.argsort()[::-1]
            recommendations = []
            
            for idx in similar_indices:
                if idx not in liked_indices:
                    book = self.df.iloc[idx]
                    recommendations.append({
                        'title': book['title'],
                        'author': book['author'],
                        'description': book['description'],
                        'genre': book['genre'],
                        'similarity_score': similarities[idx]
                    })
                    if len(recommendations) >= num_recommendations:
                        break
            
            return recommendations
        
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return []
    
    def get_author_recommendations(self, author_name: str, num_recommendations: int = 5) -> List[Dict]:
        """
        Get author recommendations based on a liked author.
        
        Args:
            author_name (str): Name of the author the user likes
            num_recommendations (int): Number of recommendations to return
            
        Returns:
            List[Dict]: List of recommended authors with details
        """
        try:
            # Find books by the author
            author_books = self.df[self.df['author'].str.contains(author_name, case=False)]
            
            if author_books.empty:
                logger.warning(f"No books found for author: {author_name}")
                return []
            
            # Get recommendations based on these books
            book_titles = author_books['title'].tolist()
            recommendations = self.get_recommendations(book_titles, num_recommendations)
            
            # Group by author and get top authors
            author_recs = {}
            for rec in recommendations:
                author = rec['author']
                if author not in author_recs:
                    author_recs[author] = {
                        'author': author,
                        'books': [],
                        'avg_similarity': 0,
                        'count': 0
                    }
                author_recs[author]['books'].append(rec['title'])
                author_recs[author]['avg_similarity'] += rec['similarity_score']
                author_recs[author]['count'] += 1
            
            # Calculate average similarity and prepare final list
            final_recommendations = []
            for author, data in author_recs.items():
                data['avg_similarity'] /= data['count']
                final_recommendations.append({
                    'author': author,
                    'recommended_books': data['books'][:3],  # Show top 3 books
                    'similarity_score': data['avg_similarity']
                })
            
            # Sort by similarity score
            final_recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
            
            return final_recommendations[:num_recommendations]
        
        except Exception as e:
            logger.error(f"Error generating author recommendations: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    try:
        # Initialize recommendation system
        recommender = BookRecommendationSystem()
        
        # Example: Get recommendations for someone who likes Radе Milosavljević's works
        author_recs = recommender.get_author_recommendations("Radе Milosavljević")
        
        print("Author Recommendations:")
        for i, rec in enumerate(author_recs, 1):
            print(f"{i}. Author: {rec['author']}")
            print(f"   Similarity Score: {rec['similarity_score']:.2f}")
            print(f"   Recommended Books: {', '.join(rec['recommended_books'])}")
            print()
        
        # Example: Get book recommendations based on specific liked books
        book_recs = recommender.get_recommendations(["Book Title 1", "Book Title 2"])
        
        print("\nBook Recommendations:")
        for i, rec in enumerate(book_recs, 1):
            print(f"{i}. Title: {rec['title']}")
            print(f"   Author: {rec['author']}")
            print(f"   Genre: {rec['genre']}")
            print(f"   Similarity Score: {rec['similarity_score']:.2f}")
            print()
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
