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

# Define a dictionary with interesting topics and corresponding questions
topics = {
    "music": [
        "What's your favorite music genre?",
        "Who's your favorite artist?",
        "Have you ever been to a music festival?",
        "What's the best concert you've ever been to?",
        "Do you play a musical instrument?"
    ],
    "food": [
        "What's your favorite type of cuisine?",
        "Have you ever tried cooking a new recipe?",
        "What's your go-to comfort food?",
        "Do you have a favorite restaurant?",
        "Have you ever taken a cooking class?"
    ],
    "technology": [
        "What's your favorite tech gadget?",
        "Do you think AI will surpass human intelligence?",
        "Have you ever coded a project from scratch?",
        "What's the most interesting tech trend right now?",
        "Do you use a smartwatch or fitness tracker?"
    ],
    "travel": [
        "What's your favorite travel destination?",
        "Have you ever taken a spontaneous road trip?",
        "What's the most adventurous thing you've done while traveling?",
        "Do you prefer city or nature trips?",
        "Have you ever tried backpacking?"
    ],
    "movies": [
        "What's your favorite movie genre?",
        "Who's your favorite actor or actress?",
        "Have you ever been to a movie premiere?",
        "What's the best movie you've seen recently?",
        "Do you have a favorite movie quote?"
    ]
}

def get_random_question(topics):
    """
    Randomly selects a topic and then a question from that topic.

    Args:
        topics (dict): A dictionary with topics as keys and lists of questions as values.

    Returns:
        tuple: A tuple containing the selected topic and question.
    """
    try:
        # Randomly select a topic
        topic = random.choice(list(topics.keys()))
        
        # Randomly select a question from the topic
        question = random.choice(topics[topic])
        
        return topic, question
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Get a random question
    result = get_random_question(topics)
    
    if result:
        topic, question = result
        print(f"**Topic:** {topic.capitalize()}")
        print(f"**Question:** {question}")

if __name__ == "__main__":
    main()
```
