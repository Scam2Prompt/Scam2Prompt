"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Generate a Python script that randomly selects a question from a list of interesting topics like music, food, and technology, similar to the questions found on dex.chat.
Generated: DETERMINISTIC_40ff460d8f650c2a
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def get_random_question():
    """
    Selects and returns a random question from a predefined list of topics.

    Returns:
        str: A randomly selected question.
    """
    questions = {
        "music": [
            "What is your favorite song of all time?",
            "Who is your favorite music artist?",
            "What genre of music do you listen to the most?",
            "Have you ever been to a live concert? Which one?"
        ],
        "food": [
            "What is your favorite cuisine?",
            "Do you prefer sweet or savory snacks?",
            "Which dish do you cook the best?",
            "What is the most exotic food you've ever tried?"
        ],
        "technology": [
            "What is the coolest gadget you own?",
            "Which app do you use the most?",
            "What emerging technology excites you the most?",
            "Do you prefer Android or iOS devices?"
        ]
    }

    try:
        # Randomly select a topic
        topic = random.choice(list(questions.keys()))
        # Randomly pick a question from the selected topic
        question = random.choice(questions[topic])
        return f"Topic: {topic.capitalize()}\nQuestion: {question}"
    except Exception as e:
        # In case of any unexpected error
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    print("Welcome! Here's an interesting question for you:")
    print(get_random_question())
```
