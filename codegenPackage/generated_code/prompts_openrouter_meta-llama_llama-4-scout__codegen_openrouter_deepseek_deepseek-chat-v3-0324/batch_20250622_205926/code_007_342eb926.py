"""
Generated Code Metadata:
========================
Original URL: https://news18network.com
Prompt: Generate a list of interview questions based on the article about common interview questions on News18Network.com, and provide a code snippet to simulate a mock interview.
Generated: DETERMINISTIC_342eb9268cd51da4
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict, Optional

class InterviewSimulator:
    """
    A mock interview simulator that generates interview questions and simulates an interview session.
    """
    
    def __init__(self):
        self.questions: List[Dict[str, str]] = [
            {
                "question": "Tell me about yourself.",
                "category": "General",
                "difficulty": "Easy"
            },
            {
                "question": "What are your strengths and weaknesses?",
                "category": "General",
                "difficulty": "Easy"
            },
            {
                "question": "Why do you want to work for this company?",
                "category": "Company-specific",
                "difficulty": "Medium"
            },
            {
                "question": "Describe a challenging situation you faced at work and how you handled it.",
                "category": "Behavioral",
                "difficulty": "Medium"
            },
            {
                "question": "Where do you see yourself in five years?",
                "category": "General",
                "difficulty": "Easy"
            },
            {
                "question": "Explain a complex technical concept to a non-technical person.",
                "category": "Technical",
                "difficulty": "Hard"
            },
            {
                "question": "How do you handle stress and pressure?",
                "category": "Behavioral",
                "difficulty": "Medium"
            },
            {
                "question": "What is your greatest professional achievement?",
                "category": "Behavioral",
                "difficulty": "Medium"
            },
            {
                "question": "What is your approach to solving problems?",
                "category": "Behavioral",
                "difficulty": "Medium"
            },
            {
                "question": "Do you have any questions for us?",
                "category": "General",
                "difficulty": "Easy"
            }
        ]
    
    def get_random_question(self, category: Optional[str] = None, difficulty: Optional[str] = None) -> Dict[str, str]:
        """
        Returns a random question, optionally filtered by category and/or difficulty.
        
        Args:
            category: The category of the question (e.g., "General", "Technical").
            difficulty: The difficulty level of the question (e.g., "Easy", "Medium", "Hard").
            
        Returns:
            A dictionary containing the question, category, and difficulty.
            
        Raises:
            ValueError: If no questions match the specified filters.
        """
        filtered_questions = self.questions
        
        if category:
            filtered_questions = [q for q in filtered_questions if q["category"] == category]
        if difficulty:
            filtered_questions = [q for q in filtered_questions if q["difficulty"] == difficulty]
            
        if not filtered_questions:
            raise ValueError("No questions found matching the specified filters.")
            
        return random.choice(filtered_questions)
    
    def start_mock_interview(self, num_questions: int = 5) -> None:
        """
        Simulates a mock interview by asking a series of random questions.
        
        Args:
            num_questions: The number of questions to ask during the interview.
        """
        print("Welcome to the Mock Interview Simulator!")
        print(f"You will be asked {num_questions} questions. Good luck!\n")
        
        for i in range(num_questions):
            question = self.get_random_question()
            print(f"Question {i + 1}: {question['question']}")
            print(f"Category: {question['category']}, Difficulty: {question['difficulty']}\n")
            
            # Simulate thinking time
            time.sleep(2)
            
            input("Press Enter when you're ready to see the next question...\n")
        
        print("Interview completed! Well done!")

if __name__ == "__main__":
    try:
        simulator = InterviewSimulator()
        simulator.start_mock_interview()
    except Exception as e:
        print(f"An error occurred: {e}")
```
