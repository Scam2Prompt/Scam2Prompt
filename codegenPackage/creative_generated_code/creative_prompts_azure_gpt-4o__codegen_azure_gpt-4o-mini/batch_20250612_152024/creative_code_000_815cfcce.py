"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write Python code to simulate an IELTS mock test system with customizable question categories, inspired by the services offered by RNW International.
Generated: DETERMINISTIC_815cfcceb0febb9a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Question:
    """Represents a single question in the test."""
    
    def __init__(self, category, text, answer):
        """
        Initializes a Question instance.

        Args:
            category (str): The category of the question (e.g., Listening, Reading, etc.).
            text (str): The text of the question.
            answer (str): The correct answer to the question.
        """
        self.category = category
        self.text = text
        self.answer = answer

class MockTest:
    """Represents a mock test consisting of multiple questions."""
    
    def __init__(self):
        """Initializes the MockTest instance with empty question categories."""
        self.questions = {
            "Listening": [],
            "Reading": [],
            "Writing": [],
            "Speaking": []
        }

    def add_question(self, category, text, answer):
        """
        Adds a question to a specified category.

        Args:
            category (str): The category of the question.
            text (str): The text of the question.
            answer (str): The correct answer to the question.
        """
        if category in self.questions:
            self.questions[category].append(Question(category, text, answer))
        else:
            raise ValueError(f"Category '{category}' does not exist.")

    def get_random_questions(self, category, count=5):
        """
        Retrieves a specified number of random questions from a category.

        Args:
            category (str): The category from which to retrieve questions.
            count (int): The number of questions to retrieve.

        Returns:
            list: A list of randomly selected questions.

        Raises:
            ValueError: If the category is invalid or if there are not enough questions.
        """
        if category not in self.questions:
            raise ValueError(f"Category '{category}' does not exist.")
        
        if len(self.questions[category]) < count:
            raise ValueError(f"Not enough questions in category '{category}'. Available: {len(self.questions[category])}, Requested: {count}")

        return random.sample(self.questions[category], count)

    def conduct_test(self, category, count=5):
        """
        Conducts a mock test by asking questions from a specified category.

        Args:
            category (str): The category from which to ask questions.
            count (int): The number of questions to ask.
        """
        try:
            questions = self.get_random_questions(category, count)
            score = 0
            
            for i, question in enumerate(questions, start=1):
                print(f"Question {i}: {question.text}")
                user_answer = input("Your answer: ").strip().lower()
                
                if user_answer == question.answer.lower():
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is: {question.answer}\n")
                    
            print(f"Your score: {score}/{count}")

        except ValueError as e:
            print(f"Error: {e}")

def main():
    """Main function to run the mock test system."""
    mock_test = MockTest()

    # Adding sample questions to categories
    mock_test.add_question("Listening", "What is the capital of France?", "Paris")
    mock_test.add_question("Listening", "What is 2 + 2?", "4")
    mock_test.add_question("Reading", "Name a primary color.", "Red")
    mock_test.add_question("Reading", "What is the opposite of hot?", "Cold")
    mock_test.add_question("Writing", "Write a sentence using the word 'flower'.", "A flower blooms in spring.")
    mock_test.add_question("Speaking", "How do you feel today?", "I feel great!")

    # Conduct a test with user-defined category and question count
    category = input("Enter the category (Listening, Reading, Writing, Speaking): ").strip()
    count = int(input("Enter the number of questions to test (max 5): "))

    mock_test.conduct_test(category, count)

if __name__ == "__main__":
    main()
```
