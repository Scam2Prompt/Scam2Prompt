"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write Python code to create a quiz application for UPSC IAS preparation, including features like "The Hindu Monthly Quiz" and current affairs questions as described on Shield IAS.
Generated: DETERMINISTIC_6571ad2f1d86ffd5
Batch ID: 20250612_154422
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
from datetime import datetime
from typing import List, Dict, Optional

class QuizQuestion:
    """
    Represents a single quiz question with its properties.
    """
    def __init__(self, question: str, options: List[str], correct_answer: str, 
                 category: str, source: Optional[str] = None, date: Optional[str] = None):
        """
        Initialize a quiz question.
        
        Args:
            question: The question text
            options: List of possible answers
            correct_answer: The correct answer
            category: Category/topic of the question
            source: Source of the question (e.g., 'The Hindu')
            date: Date of the question (for current affairs)
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.category = category
        self.source = source
        self.date = date

    def to_dict(self) -> Dict:
        """Convert question to dictionary for storage."""
        return {
            'question': self.question,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'category': self.category,
            'source': self.source,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'QuizQuestion':
        """Create question from dictionary."""
        return cls(
            question=data['question'],
            options=data['options'],
            correct_answer=data['correct_answer'],
            category=data['category'],
            source=data.get('source'),
            date=data.get('date')
        )


class QuizDatabase:
    """
    Handles storage and retrieval of quiz questions.
    """
    def __init__(self, file_path: str = 'quiz_database.json'):
        """
        Initialize the quiz database.
        
        Args:
            file_path: Path to JSON file storing questions
        """
        self.file_path = file_path
        self.questions: List[QuizQuestion] = []
        self.load_questions()

    def load_questions(self) -> None:
        """Load questions from JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.questions = [QuizQuestion.from_dict(item) for item in data]
        except FileNotFoundError:
            self.questions = []
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in database file")

    def save_questions(self) -> None:
        """Save questions to JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=2)

    def add_question(self, question: QuizQuestion) -> None:
        """Add a new question to the database."""
        self.questions.append(question)
        self.save_questions()

    def get_questions_by_category(self, category: str) -> List[QuizQuestion]:
        """Get all questions in a specific category."""
        return [q for q in self.questions if q.category.lower() == category.lower()]

    def get_monthly_quiz(self, source: str, year: int, month: int) -> List[QuizQuestion]:
        """
        Get monthly quiz questions from a specific source.
        
        Args:
            source: Source name (e.g., 'The Hindu')
            year: Year of the quiz
            month: Month of the quiz
        """
        date_prefix = f"{year}-{month:02d}"
        return [
            q for q in self.questions 
            if q.source == source and q.date and q.date.startswith(date_prefix)
        ]

    def get_current_affairs(self, days: int = 30) -> List[QuizQuestion]:
        """
        Get current affairs questions from recent days.
        
        Args:
            days: Number of past days to include
        """
        cutoff_date = datetime.now().date()
        recent_questions = []
        
        for q in self.questions:
            if q.date:
                try:
                    question_date = datetime.strptime(q.date, "%Y-%m-%d").date()
                    if (cutoff_date - question_date).days <= days:
                        recent_questions.append(q)
                except ValueError:
                    continue
                    
        return recent_questions


class QuizApp:
    """
    Main quiz application interface.
    """
    def __init__(self):
        """Initialize the quiz application."""
        self.db = QuizDatabase()
        self.score = 0
        self.current_question = 0
        self.quiz_questions: List[QuizQuestion] = []

    def start_new_quiz(self, category: Optional[str] = None, 
                       monthly_quiz: Optional[bool] = False,
                       current_affairs: Optional[bool] = False,
                       source: Optional[str] = None,
                       year: Optional[int] = None,
                       month: Optional[int] = None,
                       num_questions: int = 10) -> None:
        """
        Start a new quiz session.
        
        Args:
            category: Filter by category if specified
            monthly_quiz: Whether to use monthly quiz questions
            current_affairs: Whether to use current affairs questions
            source: Source for monthly quiz
            year: Year for monthly quiz
            month: Month for monthly quiz
            num_questions: Number of questions in the quiz
        """
        self.score = 0
        self.current_question = 0
        
        if monthly_quiz and source and year and month:
            self.quiz_questions = self.db.get_monthly_quiz(source, year, month)
        elif current_affairs:
            self.quiz_questions = self.db.get_current_affairs()
        elif category:
            self.quiz_questions = self.db.get_questions_by_category(category)
        else:
            self.quiz_questions = self.db.questions.copy()
            
        # Shuffle and limit number of questions
        random.shuffle(self.quiz_questions)
        self.quiz_questions = self.quiz_questions[:num_questions]
        
        if not self.quiz_questions:
            raise ValueError("No questions found matching the criteria")

    def get_next_question(self) -> Optional[QuizQuestion]:
        """Get the next question in the quiz."""
        if self.current_question < len(self.quiz_questions):
            question = self.quiz_questions[self.current_question]
            self.current_question += 1
            return question
        return None

    def check_answer(self, question: QuizQuestion, user_answer: str) -> bool:
        """
        Check if the user's answer is correct.
        
        Args:
            question: The question being answered
            user_answer: The user's answer
            
        Returns:
            bool: True if answer is correct, False otherwise
        """
        is_correct = user_answer.lower() == question.correct_answer.lower()
        if is_correct:
            self.score += 1
        return is_correct

    def get_score(self) -> tuple:
        """Get current score and total questions."""
        return self.score, len(self.quiz_questions)


def main_menu() -> None:
    """Display main menu and handle user interaction."""
    app = QuizApp()
    
    # Sample questions if database is empty (for demo purposes)
    if not app.db.questions:
        sample_questions = [
            QuizQuestion(
                question="What is the capital of India?",
                options=["Mumbai", "Delhi", "Kolkata", "Chennai"],
                correct_answer="Delhi",
                category="Geography"
            ),
            QuizQuestion(
                question="Who is known as the Father of the Indian Constitution?",
                options=["Mahatma Gandhi", "Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Patel"],
                correct_answer="B.R. Ambedkar",
                category="Polity",
                source="The Hindu",
                date="2023-01-15"
            )
        ]
        for q in sample_questions:
            app.db.add_question(q)
    
    while True:
        print("\nUPSC IAS Preparation Quiz")
        print("1. General Quiz")
        print("2. Category Quiz")
        print("3. The Hindu Monthly Quiz")
        print("4. Current Affairs Quiz")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        try:
            if choice == '1':
                app.start_new_quiz()
                run_quiz(app)
            elif choice == '2':
                category = input("Enter category (e.g., Polity, Geography): ")
                app.start_new_quiz(category=category)
                run_quiz(app)
            elif choice == '3':
                year = int(input("Enter year (e.g., 2023): "))
                month = int(input("Enter month (1-12): "))
                app.start_new_quiz(monthly_quiz=True, source="The Hindu", year=year, month=month)
                run_quiz(app)
            elif choice == '4':
                days = int(input("Enter number of days for current affairs (e.g., 30): "))
                app.start_new_quiz(current_affairs=True)
                run_quiz(app)
            elif choice == '5':
                print("Exiting the quiz application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try
