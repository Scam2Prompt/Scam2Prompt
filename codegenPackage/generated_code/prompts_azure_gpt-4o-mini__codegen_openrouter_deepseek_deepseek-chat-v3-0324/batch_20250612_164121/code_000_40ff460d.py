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
from typing import List, Dict

class QuestionGenerator:
    """
    A class to generate random questions from various topics.
    """

    def __init__(self):
        """
        Initialize the QuestionGenerator with predefined topics and questions.
        """
        self.topics: Dict[str, List[str]] = {
            "music": [
                "What's your favorite music genre and why?",
                "Which artist or band has had the biggest impact on your life?",
                "If you could only listen to one album for the rest of your life, what would it be?",
                "What song always puts you in a good mood?",
                "Do you prefer live music or studio recordings? Why?"
            ],
            "food": [
                "What's your favorite comfort food?",
                "If you could only eat one cuisine for the rest of your life, what would it be?",
                "What's the most unusual food you've ever tried?",
                "Do you prefer cooking at home or eating out? Why?",
                "What's your go-to recipe when you need to impress someone?"
            ],
            "technology": [
                "What's the most impactful piece of technology in your life?",
                "How do you think AI will change the world in the next 10 years?",
                "What's your favorite programming language and why?",
                "Do you think technology is making us more or less social? Why?",
                "What tech gadget could you not live without?"
            ]
        }

    def get_random_question(self, topic: str = None) -> str:
        """
        Get a random question from the specified topic or a random topic if none is specified.

        Args:
            topic (str, optional): The topic to select a question from. Defaults to None.

        Returns:
            str: A randomly selected question.

        Raises:
            ValueError: If the specified topic does not exist.
        """
        if topic and topic not in self.topics:
            raise ValueError(f"Topic '{topic}' not found. Available topics: {list(self.topics.keys())}")

        selected_topic = topic if topic else random.choice(list(self.topics.keys()))
        return random.choice(self.topics[selected_topic])

    def get_all_topics(self) -> List[str]:
        """
        Get a list of all available topics.

        Returns:
            List[str]: A list of topic names.
        """
        return list(self.topics.keys())

def main():
    """
    Main function to demonstrate the QuestionGenerator.
    """
    try:
        qg = QuestionGenerator()
        print("Available topics:", qg.get_all_topics())
        
        # Get a random question from a random topic
        random_question = qg.get_random_question()
        print("\nRandom question:", random_question)
        
        # Get a random question from a specific topic
        tech_question = qg.get_random_question("technology")
        print("\nTechnology question:", tech_question)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
