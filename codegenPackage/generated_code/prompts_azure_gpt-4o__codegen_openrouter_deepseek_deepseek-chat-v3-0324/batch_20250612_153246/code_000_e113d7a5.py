"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: Write Python code to simulate a quiz system with multiple-choice questions, referencing the structure described in the NR10 - SEP course (62 lessons, 2 quizzes) from the website.
Generated: DETERMINISTIC_e113d7a503b09813
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict, Optional

class QuizQuestion:
    """Represents a single quiz question with multiple choices."""
    
    def __init__(self, question: str, choices: List[str], correct_answer: str, explanation: str):
        """
        Initialize a quiz question.
        
        Args:
            question: The question text.
            choices: List of possible answers.
            correct_answer: The correct answer.
            explanation: Explanation of the correct answer.
        """
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation
    
    def display_question(self) -> None:
        """Display the question and choices."""
        print(f"\nQuestion: {self.question}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")
    
    def check_answer(self, user_answer: str) -> bool:
        """
        Check if the user's answer is correct.
        
        Args:
            user_answer: The user's selected answer.
            
        Returns:
            bool: True if correct, False otherwise.
        """
        return user_answer.lower() == self.correct_answer.lower()

class Quiz:
    """Represents a quiz containing multiple questions."""
    
    def __init__(self, title: str, questions: List[QuizQuestion], passing_score: float = 0.7):
        """
        Initialize a quiz.
        
        Args:
            title: Title of the quiz.
            questions: List of QuizQuestion objects.
            passing_score: Minimum score to pass (default 70%).
        """
        self.title = title
        self.questions = questions
        self.passing_score = passing_score
    
    def take_quiz(self) -> Dict[str, float]:
        """
        Simulate taking the quiz.
        
        Returns:
            Dict[str, float]: Quiz results with score and passed status.
        """
        print(f"\n=== {self.title} ===\n")
        score = 0
        
        # Shuffle questions for variety
        random.shuffle(self.questions)
        
        for question in self.questions:
            question.display_question()
            while True:
                try:
                    user_choice = input("Your answer (number): ")
                    user_answer = question.choices[int(user_choice) - 1]
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid choice number.")
            
            if question.check_answer(user_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {question.correct_answer}")
                print(f"Explanation: {question.explanation}")
        
        total_questions = len(self.questions)
        final_score = score / total_questions
        passed = final_score >= self.passing_score
        
        return {
            "score": final_score,
            "passed": passed,
            "correct_answers": score,
            "total_questions": total_questions
        }

class QuizSystem:
    """Manages multiple quizzes and user interactions."""
    
    def __init__(self):
        """Initialize the quiz system with empty quizzes."""
        self.quizzes: Dict[str, Quiz] = {}
    
    def load_quiz_from_file(self, file_path: str) -> Optional[Quiz]:
        """
        Load a quiz from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Optional[Quiz]: Loaded Quiz object or None if error occurs.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                quiz_data = json.load(file)
                
            questions = [
                QuizQuestion(
                    question=q["question"],
                    choices=q["choices"],
                    correct_answer=q["correct_answer"],
                    explanation=q["explanation"]
                ) for q in quiz_data["questions"]
            ]
            
            quiz = Quiz(
                title=quiz_data["title"],
                questions=questions,
                passing_score=quiz_data.get("passing_score", 0.7)
            )
            
            self.quizzes[quiz.title] = quiz
            return quiz
            
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading quiz: {e}")
            return None
    
    def list_quizzes(self) -> None:
        """Display all available quizzes."""
        print("\nAvailable Quizzes:")
        for idx, title in enumerate(self.quizzes.keys(), start=1):
            print(f"{idx}. {title}")
    
    def run(self) -> None:
        """Main loop for the quiz system."""
        print("Welcome to the NR10 - SEP Quiz System!")
        
        while True:
            print("\nMain Menu:")
            print("1. Take a quiz")
            print("2. Exit")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                if not self.quizzes:
                    print("No quizzes available. Please load quizzes first.")
                    continue
                
                self.list_quizzes()
                try:
                    quiz_choice = int(input("Select a quiz: ")) - 1
                    quiz_title = list(self.quizzes.keys())[quiz_choice]
                    quiz = self.quizzes[quiz_title]
                    
                    results = quiz.take_quiz()
                    
                    print("\nQuiz Results:")
                    print(f"Score: {results['score'] * 100:.1f}%")
                    print(f"Correct answers: {results['correct_answers']}/{results['total_questions']}")
                    print("Status:", "Passed" if results['passed'] else "Failed")
                    
                except (ValueError, IndexError):
                    print("Invalid selection. Please try again.")
            
            elif choice == "2":
                print("Thank you for using the quiz system. Goodbye!")
                break
            
            else:
                print("Invalid option. Please try again.")

# Sample usage
if __name__ == "__main__":
    # Example quiz data structure (would normally be loaded from a file)
    sample_quiz_data = {
        "title": "NR10 - SEP Safety Quiz 1",
        "passing_score": 0.7,
        "questions": [
            {
                "question": "What is the minimum working distance from energized parts up to 50kV?",
                "choices": ["1.0m", "1.5m", "2.0m", "2.5m"],
                "correct_answer": "1.5m",
                "explanation": "NR10 standard specifies 1.5m as the minimum safe distance for work near energized parts up to 50kV."
            },
            {
                "question": "Which PPE is mandatory for electrical work?",
                "choices": ["Hard hat", "Insulating gloves", "Safety shoes", "All of the above"],
                "correct_answer": "All of the above",
                "explanation": "All listed PPE are mandatory for electrical work according to NR10 standards."
            }
        ]
    }
    
    # Create and run the quiz system
    quiz_system = QuizSystem()
    
    # For demonstration, we'll create a quiz directly
    questions = [
        QuizQuestion(
            question=q["question"],
            choices=q["choices"],
            correct_answer=q["correct_answer"],
            explanation=q["explanation"]
        ) for q in sample_quiz_data["questions"]
    ]
    
    quiz = Quiz(
        title=sample_quiz_data["title"],
        questions=questions,
        passing_score=sample_quiz_data["passing_score"]
    )
    
    quiz_system.quizzes[quiz.title] = quiz
    quiz_system.run()
```
