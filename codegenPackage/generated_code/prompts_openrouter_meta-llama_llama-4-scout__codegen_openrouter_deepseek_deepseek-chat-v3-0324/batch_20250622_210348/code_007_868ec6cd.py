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
import json
from typing import List, Dict, Optional

class BookRecommendationChatbot:
    """
    A chatbot that provides personalized book recommendations for children based on their interests
    and reading level, leveraging Muna Kalati's resources and expertise.
    """

    def __init__(self, books_db_path: str = "books_database.json"):
        """
        Initialize the chatbot with a database of books.
        
        Args:
            books_db_path: Path to JSON file containing book database
        """
        try:
            with open(books_db_path, 'r', encoding='utf-8') as f:
                self.books_db = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Book database file not found at {books_db_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in book database")

    def get_recommendations(
        self,
        interests: List[str],
        reading_level: str,
        max_recommendations: int = 5
    ) -> List[Dict[str, str]]:
        """
        Get book recommendations based on child's interests and reading level.
        
        Args:
            interests: List of topics/themes the child is interested in
            reading_level: Reading level (e.g., "beginner", "intermediate", "advanced")
            max_recommendations: Maximum number of recommendations to return
            
        Returns:
            List of recommended books with title, author, and description
        """
        if not interests:
            raise ValueError("At least one interest must be provided")
            
        if reading_level not in ["beginner", "intermediate", "advanced"]:
            raise ValueError("Invalid reading level. Must be 'beginner', 'intermediate', or 'advanced'")

        matched_books = []
        
        for book in self.books_db:
            # Check reading level match
            if book["reading_level"].lower() != reading_level.lower():
                continue
                
            # Check interest match
            book_interests = [i.lower() for i in book["interests"]]
            input_interests = [i.lower() for i in interests]
            
            if any(interest in book_interests for interest in input_interests):
                matched_books.append({
                    "title": book["title"],
                    "author": book["author"],
                    "description": book["description"],
                    "age_range": book["age_range"],
                    "publisher": book.get("publisher", "Muna Kalati")
                })
        
        # Sort by relevance (number of matching interests)
        matched_books.sort(
            key=lambda x: sum(
                1 for interest in interests 
                if interest.lower() in [i.lower() for i in x.get("interests", [])]
            ),
            reverse=True
        )
        
        return matched_books[:max_recommendations]

    def generate_prompt(self) -> str:
        """
        Generate a prompt for the chatbot to collect user preferences.
        
        Returns:
            Formatted prompt string
        """
        return """
        Welcome to Muna Kalati's Children's Book Recommendation Chatbot!
        
        I'll help you find the perfect books for your child based on their interests and reading level.
        
        Please provide:
        1. Your child's interests (e.g., animals, space, fairy tales) - separate with commas
        2. Their reading level (beginner, intermediate, or advanced)
        3. Optional: Preferred maximum number of recommendations (default is 5)
        
        Example response:
        "My child likes dinosaurs and science. They're at intermediate level. Please suggest 3 books."
        """

# Example usage
if __name__ == "__main__":
    try:
        chatbot = BookRecommendationChatbot()
        print(chatbot.generate_prompt())
        
        # Simulate user input
        interests = ["animals", "science"]
        reading_level = "intermediate"
        
        recommendations = chatbot.get_recommendations(interests, reading_level)
        print("\nRecommendations:")
        for i, book in enumerate(recommendations, 1):
            print(f"{i}. {book['title']} by {book['author']}")
            print(f"   {book['description']}")
            print(f"   Age: {book['age_range']}")
            print()
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
