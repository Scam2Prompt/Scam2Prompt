"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Write a code snippet that categorizes conversation questions into topics, such as weird and funny or technology.
Generated: DETERMINISTIC_1dbc909d162697cc
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def categorize_question(question):
    """
    Categorizes a given question into predefined topics.

    Args:
        question (str): The question to be categorized.

    Returns:
        str: The category of the question.
    """
    # Predefined categories and their associated keywords
    categories = {
        "Weird and Funny": ["weird", "funny", "joke", "strange", "odd", "humor"],
        "Technology": ["technology", "tech", "computer", "software", "hardware", "AI", "robot"],
        "Science": ["science", "biology", "physics", "chemistry", "experiment", "research"],
        "Sports": ["sports", "game", "football", "basketball", "soccer", "athlete"],
        "General": []  # Default category for uncategorized questions
    }

    # Normalize the question to lowercase for case-insensitive matching
    normalized_question = question.lower()

    # Check each category for matching keywords
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', normalized_question):
                return category

    # If no keywords match, return the default category
    return "General"


# Example usage
if __name__ == "__main__":
    try:
        # Sample questions
        questions = [
            "What is the weirdest thing you've ever seen?",
            "How does artificial intelligence work?",
            "Tell me a funny joke!",
            "What is the latest discovery in physics?",
            "Who won the football game last night?",
            "What is your favorite color?"
        ]

        # Categorize each question
        for question in questions:
            category = categorize_question(question)
            print(f"Question: \"{question}\" -> Category: {category}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
