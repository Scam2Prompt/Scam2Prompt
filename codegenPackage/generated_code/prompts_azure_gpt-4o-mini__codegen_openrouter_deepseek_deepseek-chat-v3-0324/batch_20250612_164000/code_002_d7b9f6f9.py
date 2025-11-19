"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a quiz application that tests users on the monthly current affairs topics covered by Shield IAS, including features for tracking performance.
Generated: DETERMINISTIC_d7b9f6f9318f3a53
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Quiz Application for Shield IAS Current Affairs

```python
import json
import random
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class QuizQuestion:
    """Class to represent a single quiz question"""
    def __init__(self, question: str, options: List[str], correct_answer: str, topic: str, month: str, year: str):
        """
        Initialize a quiz question
        
        Args:
            question: The question text
            options: List of answer options
            correct_answer: The correct answer
            topic: Topic/category of the question
            month: Month the question relates to
            year: Year the question relates to
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.topic = topic
        self.month = month
        self.year = year

    def to_dict(self) -> Dict:
        """Convert question to dictionary for storage"""
        return {
            'question': self.question,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'topic': self.topic,
            'month': self.month,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'QuizQuestion':
        """Create question from dictionary"""
        return cls(
            question=data['question'],
            options=data['options'],
            correct_answer=data['correct_answer'],
            topic=data['topic'],
            month=data['month'],
            year=data['year']
        )


class Quiz:
    """Class to manage the quiz application"""
    def __init__(self, data_file: str = 'quiz_data.json'):
        """
        Initialize the quiz application
        
        Args:
            data_file: Path to JSON file storing questions and user data
        """
        self.data_file = data_file
        self.questions: List[QuizQuestion] = []
        self.user_performance: Dict[str, Dict] = {}
        self.load_data()

    def load_data(self) -> None:
        """Load questions and user performance data from JSON file"""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.questions = [QuizQuestion.from_dict(q) for q in data.get('questions', [])]
                self.user_performance = data.get('user_performance', {})
        except FileNotFoundError:
            # Initialize with empty data if file doesn't exist
            self.questions = []
            self.user_performance = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid data file format")

    def save_data(self) -> None:
        """Save questions and user performance data to JSON file"""
        data = {
            'questions': [q.to_dict() for q in self.questions],
            'user_performance': self.user_performance
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_question(self, question: QuizQuestion) -> None:
        """Add a new question to the quiz"""
        self.questions.append(question)
        self.save_data()

    def get_questions_by_filter(self, month: Optional[str] = None, 
                              year: Optional[str] = None, 
                              topic: Optional[str] = None) -> List[QuizQuestion]:
        """
        Get questions filtered by month, year, and/or topic
        
        Args:
            month: Filter by month (e.g., 'January')
            year: Filter by year (e.g., '2023')
            topic: Filter by topic (e.g., 'Politics')
            
        Returns:
            List of filtered questions
        """
        filtered = self.questions
        
        if month:
            filtered = [q for q in filtered if q.month.lower() == month.lower()]
        if year:
            filtered = [q for q in filtered if q.year == year]
        if topic:
            filtered = [q for q in filtered if q.topic.lower() == topic.lower()]
            
        return filtered

    def generate_quiz(self, num_questions: int = 10, 
                     month: Optional[str] = None, 
                     year: Optional[str] = None, 
                     topic: Optional[str] = None) -> List[QuizQuestion]:
        """
        Generate a quiz with random questions
        
        Args:
            num_questions: Number of questions in quiz
            month: Filter by month
            year: Filter by year
            topic: Filter by topic
            
        Returns:
            List of quiz questions
        """
        filtered = self.get_questions_by_filter(month, year, topic)
        
        if not filtered:
            raise ValueError("No questions match the specified filters")
            
        if len(filtered) < num_questions:
            num_questions = len(filtered)
            
        return random.sample(filtered, num_questions)

    def record_user_performance(self, user_id: str, questions: List[QuizQuestion], 
                               answers: List[str]) -> Dict[str, float]:
        """
        Record user's quiz performance and calculate statistics
        
        Args:
            user_id: Unique identifier for user
            questions: List of questions answered
            answers: List of user's answers
            
        Returns:
            Dictionary with performance statistics
        """
        if len(questions) != len(answers):
            raise ValueError("Questions and answers lists must be the same length")
            
        correct = 0
        topic_stats = {}
        month_stats = {}
        
        for q, a in zip(questions, answers):
            is_correct = a.lower() == q.correct_answer.lower()
            if is_correct:
                correct += 1
                
            # Update topic statistics
            if q.topic not in topic_stats:
                topic_stats[q.topic] = {'correct': 0, 'total': 0}
            topic_stats[q.topic]['total'] += 1
            if is_correct:
                topic_stats[q.topic]['correct'] += 1
                
            # Update month statistics
            month_key = f"{q.month} {q.year}"
            if month_key not in month_stats:
                month_stats[month_key] = {'correct': 0, 'total': 0}
            month_stats[month_key]['total'] += 1
            if is_correct:
                month_stats[month_key]['correct'] += 1
        
        score = (correct / len(questions)) * 100 if questions else 0
        
        # Update user performance
        if user_id not in self.user_performance:
            self.user_performance[user_id] = {
                'total_quizzes': 0,
                'average_score': 0,
                'topic_stats': {},
                'month_stats': {},
                'history': []
            }
            
        user_data = self.user_performance[user_id]
        user_data['total_quizzes'] += 1
        user_data['average_score'] = (
            (user_data['average_score'] * (user_data['total_quizzes'] - 1) + score) 
            / user_data['total_quizzes']
        )
        
        # Update topic stats
        for topic, stats in topic_stats.items():
            if topic not in user_data['topic_stats']:
                user_data['topic_stats'][topic] = {'correct': 0, 'total': 0}
            user_data['topic_stats'][topic]['correct'] += stats['correct']
            user_data['topic_stats'][topic]['total'] += stats['total']
            
        # Update month stats
        for month, stats in month_stats.items():
            if month not in user_data['month_stats']:
                user_data['month_stats'][month] = {'correct': 0, 'total': 0}
            user_data['month_stats'][month]['correct'] += stats['correct']
            user_data['month_stats'][month]['total'] += stats['total']
            
        # Add to history
        user_data['history'].append({
            'date': datetime.now().isoformat(),
            'score': score,
            'num_questions': len(questions),
            'topics': list(topic_stats.keys()),
            'months': list(month_stats.keys())
        })
        
        self.save_data()
        
        return {
            'score': score,
            'correct': correct,
            'total': len(questions),
            'topic_stats': topic_stats,
            'month_stats': month_stats
        }

    def get_user_stats(self, user_id: str) -> Dict:
        """
        Get performance statistics for a user
        
        Args:
            user_id: Unique identifier for user
            
        Returns:
            Dictionary with user performance data
        """
        return self.user_performance.get(user_id, {})

    def get_all_topics(self) -> List[str]:
        """Get list of all unique topics"""
        return list(set(q.topic for q in self.questions))

    def get_all_months(self) -> List[Tuple[str, str]]:
        """Get list of all unique month-year combinations"""
        return list(set((q.month, q.year) for q in self.questions))


class QuizInterface:
    """Class to handle user interaction with the quiz"""
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.current_user = None

    def start(self) -> None:
        """Main entry point for the quiz interface"""
        print("Welcome to Shield IAS Current Affairs Quiz")
