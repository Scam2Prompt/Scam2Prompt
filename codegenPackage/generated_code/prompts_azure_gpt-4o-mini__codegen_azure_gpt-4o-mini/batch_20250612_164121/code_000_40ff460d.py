"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Generate a Python script that randomly selects a question from a list of interesting topics like music, food, and technology, similar to the questions found on dex.chat.
Generated: DETERMINISTIC_40ff460d8f650c2a
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class QuestionSelector:
    """A class to randomly select a question from a predefined list of topics."""

    def __init__(self):
        """Initialize the QuestionSelector with a list of questions."""
        self.questions = {
            "music": [
                "What is your favorite music genre and why?",
                "Who is your favorite artist or band?",
                "What song always makes you feel nostalgic?",
                "If you could attend any concert, past or present, which would it be?"
            ],
            "food": [
                "What is your favorite dish to cook?",
                "If you could only eat one cuisine for the rest of your life, what would it be?",
                "What is the most unusual food you've ever tried?",
                "Do you prefer sweet or savory snacks?"
            ],
            "technology": [
                "What piece of technology can you not live without?",
                "How do you think technology will change in the next 10 years?",
                "What is your favorite gadget and why?",
                "Have you ever experienced a tech failure? What happened?"
            ]
        }

    def get_random_question(self, topic):
        """Select a random question from the specified topic.

        Args:
            topic (str): The topic from which to select a question.

        Returns:
            str: A randomly selected question.

        Raises:
            ValueError: If the topic is not found in the questions list.
        """
        if topic not in self.questions:
            raise ValueError(f"Topic '{topic}' not found. Available topics: {', '.join(self.questions.keys())}")

        return random.choice(self.questions[topic])

def main():
    """Main function to run the question selector."""
    selector = QuestionSelector()
    
    # Example usage
    try:
        topic = input("Enter a topic (music, food, technology): ").strip().lower()
        question = selector.get_random_question(topic)
        print(f"Random Question: {question}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
