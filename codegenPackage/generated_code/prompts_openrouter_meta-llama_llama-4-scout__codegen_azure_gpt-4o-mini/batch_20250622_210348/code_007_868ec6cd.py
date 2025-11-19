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
import random

class ReadingRecommendationChatbot:
    def __init__(self):
        # Initialize the chatbot with a list of recommended books
        self.books = {
            'beginner': {
                'animals': ['Brown Bear, Brown Bear, What Do You See?', 'The Very Hungry Caterpillar'],
                'adventure': ['Where the Wild Things Are', 'Goodnight Moon'],
                'fantasy': ['The Gruffalo', 'The Snowy Day']
            },
            'intermediate': {
                'animals': ['Charlotte\'s Web', 'The Tale of Peter Rabbit'],
                'adventure': ['The Magic Tree House Series', 'Pippi Longstocking'],
                'fantasy': ['Harry Potter and the Sorcerer\'s Stone', 'The Chronicles of Narnia']
            },
            'advanced': {
                'animals': ['Life of Pi', 'The Call of the Wild'],
                'adventure': ['Treasure Island', 'Hatchet'],
                'fantasy': ['The Hobbit', 'A Wrinkle in Time']
            }
        }

    def get_recommendations(self, reading_level, interest):
        """
        Get book recommendations based on reading level and interest.

        :param reading_level: The reading level of the child (beginner, intermediate, advanced)
        :param interest: The interest category (animals, adventure, fantasy)
        :return: A list of recommended books or an error message
        """
        try:
            # Validate input
            if reading_level not in self.books:
                raise ValueError("Invalid reading level. Choose from: beginner, intermediate, advanced.")
            if interest not in self.books[reading_level]:
                raise ValueError("Invalid interest category. Choose from: animals, adventure, fantasy.")

            # Return a random selection of books from the specified category
            recommendations = self.books[reading_level][interest]
            return random.sample(recommendations, min(2, len(recommendations)))

        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def chat(self):
        """
        Start a chat session with the user to get reading recommendations.
        """
        print("Welcome to the Reading Recommendation Chatbot!")
        print("Please provide your child's reading level (beginner, intermediate, advanced):")
        reading_level = input().strip().lower()

        print("What is your child's interest? (animals, adventure, fantasy):")
        interest = input().strip().lower()

        # Get recommendations based on user input
        recommendations = self.get_recommendations(reading_level, interest)
        print("Here are some book recommendations for you:")
        if isinstance(recommendations, list):
            for book in recommendations:
                print(f"- {book}")
        else:
            print(recommendations)

if __name__ == "__main__":
    # Run the chatbot
    chatbot = ReadingRecommendationChatbot()
    chatbot.chat()
```
