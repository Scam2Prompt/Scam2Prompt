"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write Python code to simulate a timed ENEM-style exam with multiple-choice questions, incorporating TRI (Item Response Theory) scoring methodology as described in the Maratona do ENEM approach.
Generated: DETERMINISTIC_a67fec48f7e628e8
Batch ID: 20250612_153246
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
import json
import numpy as np
from typing import List, Dict, Tuple, Optional

class IRTModel:
    """
    Implements Item Response Theory (IRT) scoring using the 3-parameter logistic model.
    """
    def __init__(self, a: float = 1.0, b: float = 0.0, c: float = 0.2):
        """
        Initialize IRT parameters:
        a: discrimination parameter
        b: difficulty parameter
        c: guessing parameter
        """
        self.a = a
        self.b = b
        self.c = c
    
    def probability_correct(self, theta: float) -> float:
        """
        Calculate probability of correct response given ability theta.
        Uses 3PL model: P = c + (1-c)/(1 + exp(-a*(theta-b)))
        """
        return self.c + (1 - self.c) / (1 + np.exp(-self.a * (theta - self.b)))
    
    def update_parameters(self, responses: List[bool], thetas: List[float]) -> None:
        """
        Update IRT parameters based on responses and abilities (simplified estimation).
        In production, you'd use more sophisticated estimation methods like EM algorithm.
        """
        if not responses:
            return
        
        # Simplified parameter updates for demonstration
        correct = sum(responses)
        self.b = np.mean([theta for theta, resp in zip(thetas, responses) if not resp])
        self.a = np.std(thetas) * 0.5  # Simplified relationship
        self.c = max(0.1, min(0.3, (correct / len(responses)) * 0.5))  # Constrained guess prob

class Question:
    """
    Represents a multiple-choice question with IRT parameters.
    """
    def __init__(self, id: int, text: str, options: List[str], correct_option: int, 
                 irt_params: Optional[Dict[str, float]] = None):
        self.id = id
        self.text = text
        self.options = options
        self.correct_option = correct_option
        self.irt_model = IRTModel()
        
        if irt_params:
            self.irt_model.a = irt_params.get('a', 1.0)
            self.irt_model.b = irt_params.get('b', 0.0)
            self.irt_model.c = irt_params.get('c', 0.2)
    
    def to_dict(self) -> Dict:
        """Serialize question to dictionary."""
        return {
            'id': self.id,
            'text': self.text,
            'options': self.options,
            'correct_option': self.correct_option,
            'irt_params': {
                'a': self.irt_model.a,
                'b': self.irt_model.b,
                'c': self.irt_model.c
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Question':
        """Deserialize question from dictionary."""
        return cls(
            id=data['id'],
            text=data['text'],
            options=data['options'],
            correct_option=data['correct_option'],
            irt_params=data.get('irt_params')
        )

class ExamSimulator:
    """
    Simulates a timed ENEM-style exam with TRI scoring.
    """
    def __init__(self, questions: List[Question], time_limit_minutes: int = 300):
        self.questions = questions
        self.time_limit = time_limit_minutes * 60  # Convert to seconds
        self.start_time = 0
        self.responses = {}
        self.ability_estimate = 0.0  # Initial theta estimate
    
    def start_exam(self) -> None:
        """Begin the exam timer."""
        self.start_time = time.time()
        print(f"Exam started. You have {self.time_limit//60} minutes.")
    
    def time_remaining(self) -> float:
        """Calculate remaining time in seconds."""
        elapsed = time.time() - self.start_time
        return max(0, self.time_limit - elapsed)
    
    def display_question(self, question: Question) -> None:
        """Display question and options."""
        print(f"\nQuestion {question.id}: {question.text}")
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
    
    def record_response(self, question_id: int, response: int) -> bool:
        """
        Record student's response and return if correct.
        Returns:
            bool: True if response is correct, False otherwise
        """
        question = next((q for q in self.questions if q.id == question_id), None)
        if not question:
            raise ValueError(f"Question {question_id} not found")
        
        is_correct = (response == question.correct_option)
        self.responses[question_id] = {
            'response': response,
            'correct': is_correct,
            'timestamp': time.time() - self.start_time
        }
        return is_correct
    
    def calculate_ability(self) -> float:
        """
        Estimate student's ability (theta) using maximum likelihood estimation.
        Uses Newton-Raphson method for optimization.
        """
        if not self.responses:
            return 0.0  # Default ability if no responses
        
        theta = self.ability_estimate  # Start from previous estimate
        tolerance = 0.01
        max_iterations = 20
        
        for _ in range(max_iterations):
            first_deriv = 0.0
            second_deriv = 0.0
            
            for q_id, response_data in self.responses.items():
                question = next(q for q in self.questions if q.id == q_id)
                p = question.irt_model.probability_correct(theta)
                correct = response_data['correct']
                
                # First derivative (gradient)
                first_deriv += question.irt_model.a * (correct - p) * (p - question.irt_model.c) / (p * (1 - question.irt_model.c))
                
                # Second derivative (Hessian)
                term = (p - question.irt_model.c) / (1 - question.irt_model.c)
                second_deriv -= question.irt_model.a**2 * term * (1 - term)
            
            if second_deriv == 0:
                break  # Avoid division by zero
            
            delta = first_deriv / second_deriv
            theta -= delta
            
            if abs(delta) < tolerance:
                break
        
        self.ability_estimate = theta
        return theta
    
    def calculate_score(self) -> float:
        """
        Calculate final score using TRI methodology.
        Scales the ability estimate to a 0-1000 range similar to ENEM.
        """
        theta = self.calculate_ability()
        # Scale theta to ENEM-like score (simplified)
        return max(0, min(1000, 500 + 100 * theta))
    
    def save_progress(self, filename: str) -> None:
        """Save exam progress to JSON file."""
        data = {
            'questions': [q.to_dict() for q in self.questions],
            'responses': self.responses,
            'ability_estimate': self.ability_estimate,
            'time_remaining': self.time_remaining()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_progress(cls, filename: str) -> 'ExamSimulator':
        """Load exam progress from JSON file."""
        with open(filename) as f:
            data = json.load(f)
        
        questions = [Question.from_dict(q) for q in data['questions']]
        simulator = cls(questions)
        simulator.responses = data['responses']
        simulator.ability_estimate = data['ability_estimate']
        simulator.start_time = time.time() - (simulator.time_limit - data['time_remaining'])
        return simulator

def sample_questions() -> List[Question]:
    """Generate sample questions for demonstration."""
    questions = [
        Question(
            id=1,
            text="What is the capital of Brazil?",
            options=["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
            correct_option=3
        ),
        Question(
            id=2,
            text="Which planet is known as the Red Planet?",
            options=["Venus", "Mars", "Jupiter", "Saturn"],
            correct_option=2
        ),
        Question(
            id=3,
            text="What is the chemical symbol for gold?",
            options=["Go", "Gd", "Au", "Ag"],
            correct_option=3
        )
    ]
    return questions

def main():
    """Run the exam simulation."""
    try:
        # Load or create exam
        try:
            exam = ExamSimulator.load_progress('exam_progress.json')
            print("Loaded previous exam progress.")
        except (FileNotFoundError, json.JSONDecodeError):
            questions = sample_questions()
            exam = ExamSimulator(questions)
            print("Created new exam.")
        
        exam.start_exam()
        
        # Main exam loop
        for question in exam.questions:
            if exam.time_
