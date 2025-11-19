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
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from typing import List, Dict, Optional
import logging
from enum import Enum

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SubscriptionPlan(Enum):
    """Enum representing different subscription plans."""
    BASIC = 1
    STANDARD = 2
    PREMIUM = 3

class User:
    """Class representing a user with reading preferences and subscription plan."""
    
    def __init__(self, user_id: int, preferences: List[str], plan: SubscriptionPlan):
        """
        Initialize a User instance.
        
        Args:
            user_id: Unique identifier for the user.
            preferences: List of book genres/categories the user prefers.
            plan: User's subscription plan.
        """
        self.user_id = user_id
        self.preferences = preferences
        self.plan = plan

class Book:
    """Class representing an e-book."""
    
    def __init__(self, book_id: int, title: str, genres: List[str], plan_required: SubscriptionPlan):
        """
        Initialize a Book instance.
        
        Args:
            book_id: Unique identifier for the book.
            title: Title of the book.
            genres: List of genres/categories the book belongs to.
            plan_required: Minimum subscription plan required to access the book.
        """
        self.book_id = book_id
        self.title = title
        self.genres = genres
        self.plan_required = plan_required

class RecommendationSystem:
    """Class for recommending books to users based on preferences and subscription plans."""
    
    def __init__(self, books: List[Book]):
        """
        Initialize the RecommendationSystem with a list of books.
        
        Args:
            books: List of Book objects available in the system.
        """
        self.books = books
        self.book_data = self._prepare_book_data()
        self.tfidf_matrix = self._compute_tfidf_matrix()
    
    def _prepare_book_data(self) -> pd.DataFrame:
        """Prepare book data for TF-IDF vectorization."""
        book_data = []
        for book in self.books:
            book_data.append({
                'book_id': book.book_id,
                'title': book.title,
                'genres': ' '.join(book.genres),
                'plan_required': book.plan_required
            })
        return pd.DataFrame(book_data)
    
    def _compute_tfidf_matrix(self):
        """Compute TF-IDF matrix for book genres."""
        tfidf = TfidfVectorizer(stop_words='english')
        return tfidf.fit_transform(self.book_data['genres'])
    
    def _filter_by_subscription(self, user: User) -> List[Book]:
        """Filter books based on user's subscription plan."""
        return [book for book in self.books if book.plan_required.value <= user.plan.value]
    
    def recommend_books(self, user: User, top_n: int = 5) -> List[Dict]:
        """
        Recommend books to a user based on their preferences and subscription plan.
        
        Args:
            user: User to recommend books to.
            top_n: Number of recommendations to return.
            
        Returns:
            List of recommended books with titles and book IDs.
        """
        try:
            # Filter books by subscription plan
            available_books = self._filter_by_subscription(user)
            if not available_books:
                logger.warning(f"No books available for user {user.user_id} with plan {user.plan}")
                return []
            
            # Create a user profile based on preferences
            user_profile = ' '.join(user.preferences)
            
            # Transform user profile to TF-IDF vector
            tfidf = TfidfVectorizer(stop_words='english', vocabulary=self.tfidf_matrix.get_feature_names_out())
            user_tfidf = tfidf.fit_transform([user_profile])
            
            # Compute cosine similarity between user profile and books
            cosine_similarities = linear_kernel(user_tfidf, self.tfidf_matrix).flatten()
            
            # Get top N recommendations
            book_indices = cosine_similarities.argsort()[-top_n:][::-1]
            recommendations = []
            
            for idx in book_indices:
                book = self.books[idx]
                if book in available_books:
                    recommendations.append({
                        'book_id': book.book_id,
                        'title': book.title,
                        'match_score': cosine_similarities[idx]
                    })
            
            return recommendations[:top_n]
        
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            return []

# Example Usage
if __name__ == "__main__":
    # Sample books
    books = [
        Book(1, "Python Programming", ["programming", "technology"], SubscriptionPlan.BASIC),
        Book(2, "Advanced Machine Learning", ["programming", "AI", "technology"], SubscriptionPlan.PREMIUM),
        Book(3, "Data Science Handbook", ["data", "programming", "statistics"], SubscriptionPlan.STANDARD),
        Book(4, "Web Development Basics", ["web", "programming"], SubscriptionPlan.BASIC),
        Book(5, "Artificial Intelligence", ["AI", "technology"], SubscriptionPlan.PREMIUM),
    ]
    
    # Sample user
    user = User(101, ["programming", "AI"], SubscriptionPlan.STANDARD)
    
    # Create recommendation system
    recommender = RecommendationSystem(books)
    
    # Get recommendations
    recommendations = recommender.recommend_books(user)
    
    print("Recommended Books:")
    for book in recommendations:
        print(f"{book['title']} (Score: {book['match_score']:.2f})")
```
