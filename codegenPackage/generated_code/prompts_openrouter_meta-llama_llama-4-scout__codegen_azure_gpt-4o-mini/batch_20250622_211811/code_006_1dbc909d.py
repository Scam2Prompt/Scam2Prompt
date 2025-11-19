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
from collections import defaultdict

class ConversationCategorizer:
    def __init__(self):
        # Define categories and their associated keywords
        self.categories = {
            'weird_and_funny': ['weird', 'funny', 'strange', 'quirky', 'odd'],
            'technology': ['technology', 'tech', 'gadget', 'AI', 'robot', 'software'],
            'philosophy': ['philosophy', 'thought', 'existential', 'meaning', 'life'],
            'science': ['science', 'biology', 'physics', 'chemistry', 'experiment'],
            'sports': ['sports', 'game', 'team', 'athlete', 'competition']
        }
        # Create a default dictionary to hold categorized questions
        self.categorized_questions = defaultdict(list)

    def categorize_question(self, question):
        """
        Categorizes a given question into predefined topics based on keywords.

        Args:
            question (str): The question to categorize.

        Returns:
            str: The category of the question or 'uncategorized' if no match is found.
        """
        # Normalize the question to lower case for matching
        normalized_question = question.lower()
        
        # Check each category for matching keywords
        for category, keywords in self.categories.items():
            if any(re.search(r'\b' + re.escape(keyword) + r'\b', normalized_question) for keyword in keywords):
                self.categorized_questions[category].append(question)
                return category
        
        # If no category matches, return 'uncategorized'
        self.categorized_questions['uncategorized'].append(question)
        return 'uncategorized'

    def categorize_questions(self, questions):
        """
        Categorizes a list of questions.

        Args:
            questions (list): A list of questions to categorize.

        Returns:
            dict: A dictionary with categories as keys and lists of questions as values.
        """
        for question in questions:
            try:
                self.categorize_question(question)
            except Exception as e:
                print(f"Error categorizing question '{question}': {e}")
        
        return dict(self.categorized_questions)

# Example usage
if __name__ == "__main__":
    questions_list = [
        "What is the weirdest thing you've ever seen?",
        "How does artificial intelligence work?",
        "Is there life after death?",
        "What is your favorite sport?",
        "Tell me a funny joke!"
    ]

    categorizer = ConversationCategorizer()
    categorized = categorizer.categorize_questions(questions_list)

    # Print categorized questions
    for category, questions in categorized.items():
        print(f"{category.capitalize()}:")
        for q in questions:
            print(f" - {q}")
```
