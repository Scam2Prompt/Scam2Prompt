"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Design a question paper generation module for schools, referencing the functionality described in Him Saral's Question Paper module.
Generated: DETERMINISTIC_24ca19274ab48a90
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import logging
from enum import Enum, auto

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuestionType(Enum):
    """Enum representing different types of questions."""
    MULTIPLE_CHOICE = auto()
    TRUE_FALSE = auto()
    SHORT_ANSWER = auto()
    ESSAY = auto()
    FILL_IN_THE_BLANK = auto()

class DifficultyLevel(Enum):
    """Enum representing difficulty levels of questions."""
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()

@dataclass
class Question:
    """Class representing a single question."""
    id: str
    text: str
    question_type: QuestionType
    difficulty: DifficultyLevel
    marks: int
    subject: str
    topic: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None

class QuestionBank:
    """Class representing a collection of questions."""
    def __init__(self):
        self.questions: Dict[str, Question] = {}
    
    def add_question(self, question: Question) -> None:
        """Add a question to the question bank."""
        if question.id in self.questions:
            raise ValueError(f"Question with ID {question.id} already exists")
        self.questions[question.id] = question
        logger.info(f"Added question with ID {question.id}")
    
    def get_question(self, question_id: str) -> Question:
        """Retrieve a question by its ID."""
        if question_id not in self.questions:
            raise ValueError(f"Question with ID {question_id} not found")
        return self.questions[question_id]
    
    def get_questions_by_filter(self, **filters) -> List[Question]:
        """Retrieve questions based on filters like subject, topic, difficulty, etc."""
        filtered_questions = []
        for question in self.questions.values():
            match = True
            for key, value in filters.items():
                if getattr(question, key) != value:
                    match = False
                    break
            if match:
                filtered_questions.append(question)
        return filtered_questions
    
    def remove_question(self, question_id: str) -> None:
        """Remove a question from the question bank."""
        if question_id not in self.questions:
            raise ValueError(f"Question with ID {question_id} not found")
        del self.questions[question_id]
        logger.info(f"Removed question with ID {question_id}")
    
    def save_to_file(self, file_path: str) -> None:
        """Save the question bank to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(
                    {qid: {
                        'text': q.text,
                        'question_type': q.question_type.name,
                        'difficulty': q.difficulty.name,
                        'marks': q.marks,
                        'subject': q.subject,
                        'topic': q.topic,
                        'options': q.options,
                        'correct_answer': q.correct_answer
                    } for qid, q in self.questions.items()},
                    f,
                    indent=2
                )
            logger.info(f"Question bank saved to {file_path}")
        except IOError as e:
            logger.error(f"Error saving question bank: {e}")
            raise
    
    def load_from_file(self, file_path: str) -> None:
        """Load the question bank from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for qid, q_data in data.items():
                    question = Question(
                        id=qid,
                        text=q_data['text'],
                        question_type=QuestionType[q_data['question_type']],
                        difficulty=DifficultyLevel[q_data['difficulty']],
                        marks=q_data['marks'],
                        subject=q_data['subject'],
                        topic=q_data['topic'],
                        options=q_data.get('options'),
                        correct_answer=q_data.get('correct_answer')
                    )
                    self.questions[qid] = question
            logger.info(f"Question bank loaded from {file_path}")
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading question bank: {e}")
            raise

class QuestionPaperGenerator:
    """Class for generating question papers based on criteria."""
    def __init__(self, question_bank: QuestionBank):
        self.question_bank = question_bank
    
    def generate_paper(
        self,
        subject: str,
        total_marks: int,
        difficulty_distribution: Dict[DifficultyLevel, float],
        question_type_distribution: Dict[QuestionType, float],
        topics: Optional[List[str]] = None
    ) -> List[Question]:
        """Generate a question paper based on specified criteria."""
        try:
            # Validate distributions
            if not self._validate_distribution(difficulty_distribution):
                raise ValueError("Invalid difficulty distribution")
            if not self._validate_distribution(question_type_distribution):
                raise ValueError("Invalid question type distribution")
            
            # Get filtered questions
            filters = {'subject': subject}
            if topics:
                filters['topic__in'] = topics
            filtered_questions = self.question_bank.get_questions_by_filter(**filters)
            
            if not filtered_questions:
                raise ValueError("No questions found matching the criteria")
            
            # Calculate marks per category
            difficulty_marks = self._calculate_marks_per_category(difficulty_distribution, total_marks)
            question_type_marks = self._calculate_marks_per_category(question_type_distribution, total_marks)
            
            # Select questions
            selected_questions = []
            remaining_marks = total_marks
            
            # First pass: try to fulfill both distributions
            for difficulty, marks in difficulty_marks.items():
                for q_type, q_marks in question_type_marks.items():
                    target_marks = min(marks, q_marks)
                    if target_marks <= 0:
                        continue
                    
                    questions = [
                        q for q in filtered_questions
                        if q.difficulty == difficulty and q.question_type == q_type
                    ]
                    if not questions:
                        continue
                    
                    selected = self._select_questions(questions, target_marks)
                    selected_questions.extend(selected)
                    remaining_marks -= sum(q.marks for q in selected)
            
            # Second pass: fill remaining marks with any matching questions
            if remaining_marks > 0:
                remaining_questions = [
                    q for q in filtered_questions
                    if q not in selected_questions
                ]
                if remaining_questions:
                    selected = self._select_questions(remaining_questions, remaining_marks)
                    selected_questions.extend(selected)
                    remaining_marks -= sum(q.marks for q in selected)
            
            if remaining_marks > 0:
                logger.warning(f"Could not fulfill total marks. Remaining: {remaining_marks}")
            
            return selected_questions
        
        except Exception as e:
            logger.error(f"Error generating question paper: {e}")
            raise
    
    def _validate_distribution(self, distribution: Dict[Enum, float]) -> bool:
        """Validate that distribution values sum to ~1.0."""
        return abs(sum(distribution.values()) - 1.0) < 0.001
    
    def _calculate_marks_per_category(self, distribution: Dict[Enum, float], total_marks: int) -> Dict[Enum, int]:
        """Calculate marks per category based on distribution."""
        marks = {}
        remaining_marks = total_marks
        
        # Sort by descending percentage to handle rounding better
        sorted_items = sorted(distribution.items(), key=lambda x: -x[1])
        
        for i, (category, percentage) in enumerate(sorted_items):
            if i == len(sorted_items) - 1:
                # Last category gets remaining marks to avoid rounding issues
                marks[category] = remaining_marks
            else:
                category_marks = round(total_marks * percentage)
                marks[category] = category_marks
                remaining_marks -= category_marks
        
        return marks
    
    def _select_questions(self, questions: List[Question], target_marks: int) -> List[Question]:
        """Select questions that add up to approximately target marks."""
        selected = []
        current_marks = 0
        remaining_questions = questions.copy()
        
        # Try to find exact matches first
        for question in remaining_questions:
            if current_marks + question.marks <= target_marks:
                selected.append(question)
                current_marks += question.marks
        
        # If no exact matches, find the closest combination
        if current_marks == 0 and remaining_questions:
            # Simple approach: pick the question with marks closest to target
            closest = min(remaining_questions, key=lambda q: abs(q.marks - target_marks))
            selected.append(closest)
            current_marks += closest.marks
        
        return selected

class QuestionPaperFormatter:
    """Class for formatting generated question papers."""
    @staticmethod
    def format_to_text(questions: List[Question]) -> str:
        """Format questions to plain text."""
        paper = []
        for
