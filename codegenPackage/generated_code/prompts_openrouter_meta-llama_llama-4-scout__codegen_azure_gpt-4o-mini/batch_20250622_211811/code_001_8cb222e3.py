"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Write a Python script that recommends a random question from a predefined list of topics, including music and food.
Generated: DETERMINISTIC_8cb222e3595df931
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class QuestionRecommender:
    """A class to recommend random questions from predefined topics."""

    def __init__(self):
        """Initialize the recommender with predefined questions."""
        self.questions = {
            'music': [
                "What is your favorite song and why?",
                "Who is your favorite music artist?",
                "What genre of music do you enjoy the most?",
                "Have you ever been to a live concert? If so, which one?",
                "What instrument would you like to learn and why?"
            ],
            'food': [
                "What is your favorite dish to cook?",
                "Do you prefer sweet or savory foods?",
                "What is the most unusual food you've ever tried?",
                "If you could only eat one cuisine for the rest of your life, what would it be?",
                "What is your go-to comfort food?"
            ]
        }

    def get_random_question(self, topic):
        """Return a random question from the specified topic.

        Args:
            topic (str): The topic from which to get a question.

        Returns:
            str: A random question from the specified topic.

        Raises:
            ValueError: If the topic is not recognized.
        """
        if topic not in self.questions:
            raise ValueError(f"Topic '{topic}' is not recognized. Available topics: {', '.join(self.questions.keys())}")

        return random.choice(self.questions[topic])

def main():
    """Main function to run the question recommender."""
    recommender = QuestionRecommender()
    
    # Define the topics to choose from
    topics = recommender.questions.keys()
    
    # Randomly select a topic
    selected_topic = random.choice(list(topics))
    
    try:
        # Get a random question from the selected topic
        question = recommender.get_random_question(selected_topic)
        print(f"Topic: {selected_topic.capitalize()}\nQuestion: {question}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
