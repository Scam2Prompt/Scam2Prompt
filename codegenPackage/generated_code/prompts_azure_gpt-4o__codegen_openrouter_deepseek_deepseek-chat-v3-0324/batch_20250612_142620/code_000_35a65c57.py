"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Write Python code to simulate a periodic test system for JEE/NEET preparation, incorporating difficulty levels and performance tracking, as described in Potencia Academy's approach.
Generated: DETERMINISTIC_35a65c5734d3f36f
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import datetime
from typing import List, Dict, Optional, Tuple

class Question:
    def __init__(self, question_id: int, text: str, subject: str, topic: str, 
                 difficulty: str, options: List[str], correct_answer: str):
        """
        Represents a single question in the test system.
        
        Args:
            question_id: Unique identifier for the question
            text: The question text
            subject: Subject (e.g., Physics, Chemistry)
            topic: Topic within the subject
            difficulty: Difficulty level (Easy, Medium, Hard)
            options: List of answer options
            correct_answer: Correct answer option
        """
        self.question_id = question_id
        self.text = text
        self.subject = subject
        self.topic = topic
        self.difficulty = difficulty
        self.options = options
        self.correct_answer = correct_answer
    
    def to_dict(self) -> Dict:
        """Convert question object to dictionary for serialization."""
        return {
            'question_id': self.question_id,
            'text': self.text,
            'subject': self.subject,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'options': self.options,
            'correct_answer': self.correct_answer
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Question':
        """Create question object from dictionary."""
        return cls(
            question_id=data['question_id'],
            text=data['text'],
            subject=data['subject'],
            topic=data['topic'],
            difficulty=data['difficulty'],
            options=data['options'],
            correct_answer=data['correct_answer']
        )

class Test:
    def __init__(self, test_id: int, name: str, subjects: List[str], 
                 difficulty_distribution: Dict[str, float], duration_minutes: int):
        """
        Represents a test configuration.
        
        Args:
            test_id: Unique identifier for the test
            name: Name of the test
            subjects: List of subjects included
            difficulty_distribution: Dict of difficulty percentages (e.g., {'Easy': 0.3, 'Medium': 0.5, 'Hard': 0.2})
            duration_minutes: Duration of test in minutes
        """
        self.test_id = test_id
        self.name = name
        self.subjects = subjects
        self.difficulty_distribution = difficulty_distribution
        self.duration_minutes = duration_minutes
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        """Add a question to the test."""
        if question.subject not in self.subjects:
            raise ValueError(f"Question subject {question.subject} not in test subjects")
        self.questions.append(question)
    
    def generate_test_paper(self, num_questions: int) -> List[Question]:
        """
        Generate a test paper with questions based on difficulty distribution.
        
        Args:
            num_questions: Total number of questions in the test
            
        Returns:
            List of selected questions
        """
        if not self.questions:
            raise ValueError("No questions available in the test")
        
        # Group questions by difficulty
        difficulty_groups = {'Easy': [], 'Medium': [], 'Hard': []}
        for q in self.questions:
            difficulty_groups[q.difficulty].append(q)
        
        # Calculate number of questions per difficulty
        questions_per_difficulty = {
            diff: int(perc * num_questions) 
            for diff, perc in self.difficulty_distribution.items()
        }
        
        # Adjust for rounding errors
        total = sum(questions_per_difficulty.values())
        if total < num_questions:
            remaining = num_questions - total
            questions_per_difficulty['Medium'] += remaining  # Default to Medium
        
        selected_questions = []
        
        # Select questions for each difficulty level
        for difficulty, count in questions_per_difficulty.items():
            available = difficulty_groups.get(difficulty, [])
            if len(available) < count:
                raise ValueError(f"Not enough {difficulty} questions available")
            
            selected = random.sample(available, count)
            selected_questions.extend(selected)
        
        return selected_questions
    
    def to_dict(self) -> Dict:
        """Convert test object to dictionary for serialization."""
        return {
            'test_id': self.test_id,
            'name': self.name,
            'subjects': self.subjects,
            'difficulty_distribution': self.difficulty_distribution,
            'duration_minutes': self.duration_minutes,
            'questions': [q.to_dict() for q in self.questions]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Test':
        """Create test object from dictionary."""
        test = cls(
            test_id=data['test_id'],
            name=data['name'],
            subjects=data['subjects'],
            difficulty_distribution=data['difficulty_distribution'],
            duration_minutes=data['duration_minutes']
        )
        for q_data in data['questions']:
            test.add_question(Question.from_dict(q_data))
        return test

class TestAttempt:
    def __init__(self, attempt_id: int, test: Test, student_id: int):
        """
        Represents a student's attempt at a test.
        
        Args:
            attempt_id: Unique identifier for the attempt
            test: The test being attempted
            student_id: ID of the student attempting
        """
        self.attempt_id = attempt_id
        self.test = test
        self.student_id = student_id
        self.start_time = datetime.datetime.now()
        self.end_time: Optional[datetime.datetime] = None
        self.answers: Dict[int, str] = {}  # question_id: selected_answer
        self.score: Optional[float] = None
        self.difficulty_analysis: Dict[str, Dict[str, float]] = {
            'Easy': {'correct': 0, 'total': 0, 'percentage': 0.0},
            'Medium': {'correct': 0, 'total': 0, 'percentage': 0.0},
            'Hard': {'correct': 0, 'total': 0, 'percentage': 0.0}
        }
        self.test_paper = self.test.generate_test_paper(30)  # Default to 30 questions
    
    def submit_answer(self, question_id: int, answer: str) -> None:
        """Record a student's answer to a question."""
        if self.end_time is not None:
            raise ValueError("Cannot submit answers after test is completed")
        
        self.answers[question_id] = answer
    
    def complete_test(self) -> None:
        """Mark test as completed and calculate results."""
        if self.end_time is not None:
            raise ValueError("Test already completed")
        
        self.end_time = datetime.datetime.now()
        self._calculate_score()
        self._analyze_performance_by_difficulty()
    
    def _calculate_score(self) -> None:
        """Calculate the test score based on correct answers."""
        correct = 0
        for question in self.test_paper:
            if question.question_id in self.answers:
                if self.answers[question.question_id] == question.correct_answer:
                    correct += 1
        
        self.score = (correct / len(self.test_paper)) * 100
    
    def _analyze_performance_by_difficulty(self) -> None:
        """Analyze performance breakdown by difficulty level."""
        for question in self.test_paper:
            difficulty = question.difficulty
            self.difficulty_analysis[difficulty]['total'] += 1
            
            if (question.question_id in self.answers and 
                self.answers[question.question_id] == question.correct_answer):
                self.difficulty_analysis[difficulty]['correct'] += 1
        
        # Calculate percentages
        for diff in self.difficulty_analysis:
            total = self.difficulty_analysis[diff]['total']
            correct = self.difficulty_analysis[diff]['correct']
            if total > 0:
                self.difficulty_analysis[diff]['percentage'] = (correct / total) * 100
    
    def get_time_taken(self) -> float:
        """Return time taken for test in minutes."""
        if self.end_time is None:
            raise ValueError("Test not yet completed")
        return (self.end_time - self.start_time).total_seconds() / 60
    
    def to_dict(self) -> Dict:
        """Convert attempt object to dictionary for serialization."""
        return {
            'attempt_id': self.attempt_id,
            'test': self.test.to_dict(),
            'student_id': self.student_id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'answers': self.answers,
            'score': self.score,
            'difficulty_analysis': self.difficulty_analysis,
            'test_paper': [q.to_dict() for q in self.test_paper]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TestAttempt':
        """Create attempt object from dictionary."""
        test = Test.from_dict(data['
