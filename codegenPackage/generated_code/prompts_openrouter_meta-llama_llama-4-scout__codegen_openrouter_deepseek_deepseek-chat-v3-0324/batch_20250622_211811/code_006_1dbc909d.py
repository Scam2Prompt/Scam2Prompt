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
from typing import Dict, List, Optional

class QuestionCategorizer:
    """
    A class to categorize conversation questions into predefined topics based on keywords.
    """

    def __init__(self):
        """
        Initialize the categorizer with predefined topics and their associated keywords.
        """
        self.topic_keywords: Dict[str, List[str]] = {
            "weird_and_funny": [
                "weird", "funny", "hilarious", "strange", "bizarre", "joke", "laugh"
            ],
            "technology": [
                "technology", "computer", "software", "hardware", "code", "programming",
                "ai", "machine learning", "algorithm", "data"
            ],
            "personal": [
                "you", "your", "family", "friend", "relationship", "hobby", "interest"
            ],
            "hypothetical": [
                "if", "would", "could", "what if", "imagine", "scenario"
            ]
        }

    def categorize_question(self, question: str) -> Optional[str]:
        """
        Categorize a given question into one of the predefined topics.

        Args:
            question: The input question string to categorize.

        Returns:
            The topic name if a match is found, otherwise None.
        """
        if not question or not isinstance(question, str):
            raise ValueError("Input must be a non-empty string.")

        question_lower = question.lower()
        
        for topic, keywords in self.topic_keywords.items():
            for keyword in keywords:
                # Use regex to find whole words to avoid partial matches
                if re.search(rf'\b{keyword}\b', question_lower):
                    return topic
        
        return None

    def categorize_questions(self, questions: List[str]) -> Dict[str, List[str]]:
        """
        Categorize a list of questions into their respective topics.

        Args:
            questions: A list of question strings to categorize.

        Returns:
            A dictionary mapping topic names to lists of questions in that topic.
        """
        if not isinstance(questions, list):
            raise ValueError("Input must be a list of strings.")

        categorized: Dict[str, List[str]] = {topic: [] for topic in self.topic_keywords}
        categorized["uncategorized"] = []

        for question in questions:
            try:
                topic = self.categorize_question(question)
                if topic:
                    categorized[topic].append(question)
                else:
                    categorized["uncategorized"].append(question)
            except ValueError as e:
                print(f"Skipping invalid question: {e}")
                continue

        return categorized

# Example usage
if __name__ == "__main__":
    categorizer = QuestionCategorizer()
    sample_questions = [
        "What is the weirdest thing you've ever eaten?",
        "How does machine learning work?",
        "If you could travel anywhere, where would you go?",
        "What's your favorite hobby?",
        "Tell me a funny joke.",
        "",
        123  # Invalid input
    ]

    categorized_questions = categorizer.categorize_questions(sample_questions)
    for topic, questions in categorized_questions.items():
        print(f"{topic.capitalize()}:")
        for q in questions:
            print(f" - {q}")
        print()
```
