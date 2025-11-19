"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Design a library that helps young leaders assess their leadership styles, based on the principles outlined in the UngLeder resource bank.
Generated: DETERMINISTIC_8c5787bb7d0aa3e1
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Leadership Style Assessment Library

This library helps young leaders assess their leadership styles based on the
UngLeder resource bank principles. It provides assessment tools, scoring,
and personalized feedback.
"""

from enum import Enum
from typing import Dict, List, Tuple, Optional
import json
import os

class LeadershipDimension(Enum):
    """Enum representing different leadership dimensions."""
    VISIONARY = "Visionary"
    COACH = "Coach"
    SERVANT = "Servant"
    DEMOCRATIC = "Democratic"
    AUTHORITATIVE = "Authoritative"
    TRANSFORMATIONAL = "Transformational"

class Question:
    """Class representing an assessment question."""
    
    def __init__(self, id: int, text: str, dimension: LeadershipDimension, weight: float = 1.0):
        """
        Initialize a question.
        
        Args:
            id: Unique identifier for the question
            text: The question text
            dimension: Which leadership dimension this question assesses
            weight: How much this question contributes to the dimension score (default 1.0)
        """
        self.id = id
        self.text = text
        self.dimension = dimension
        self.weight = weight
    
    def to_dict(self) -> Dict:
        """Convert question to dictionary for serialization."""
        return {
            'id': self.id,
            'text': self.text,
            'dimension': self.dimension.value,
            'weight': self.weight
        }

class Assessment:
    """Class representing a leadership style assessment."""
    
    def __init__(self, questions: List[Question] = None):
        """
        Initialize an assessment.
        
        Args:
            questions: List of questions for this assessment (optional)
        """
        self.questions = questions if questions else []
        self.responses = {}
    
    def add_question(self, question: Question) -> None:
        """Add a question to the assessment."""
        self.questions.append(question)
    
    def record_response(self, question_id: int, response: int) -> None:
        """
        Record a response to a question.
        
        Args:
            question_id: ID of the question being answered
            response: Response value (typically 1-5 Likert scale)
        
        Raises:
            ValueError: If question_id is not found or response is invalid
        """
        if not any(q.id == question_id for q in self.questions):
            raise ValueError(f"Question ID {question_id} not found in assessment")
        
        if not 1 <= response <= 5:
            raise ValueError("Response must be between 1 and 5")
        
        self.responses[question_id] = response
    
    def calculate_scores(self) -> Dict[LeadershipDimension, float]:
        """
        Calculate scores for each leadership dimension.
        
        Returns:
            Dictionary mapping each dimension to its normalized score (0-100)
        
        Raises:
            ValueError: If not all questions have been answered
        """
        if len(self.responses) != len(self.questions):
            raise ValueError("All questions must be answered before calculating scores")
        
        dimension_totals = {dim: 0.0 for dim in LeadershipDimension}
        dimension_weights = {dim: 0.0 for dim in LeadershipDimension}
        
        for question in self.questions:
            response = self.responses[question.id]
            dimension = question.dimension
            dimension_totals[dimension] += response * question.weight
            dimension_weights[dimension] += 5 * question.weight  # Max possible per question
        
        # Normalize scores to 0-100 range
        scores = {
            dim: (total / dimension_weights[dim]) * 100
            for dim, total in dimension_totals.items()
            if dimension_weights[dim] > 0
        }
        
        return scores
    
    def get_primary_style(self, scores: Dict[LeadershipDimension, float]) -> LeadershipDimension:
        """
        Identify the primary leadership style based on scores.
        
        Args:
            scores: Dictionary of dimension scores from calculate_scores()
        
        Returns:
            The primary leadership dimension
        """
        return max(scores.items(), key=lambda x: x[1])[0]
    
    def generate_feedback(self, scores: Dict[LeadershipDimension, float]) -> str:
        """
        Generate personalized feedback based on assessment scores.
        
        Args:
            scores: Dictionary of dimension scores from calculate_scores()
        
        Returns:
            String containing personalized feedback
        """
        primary_style = self.get_primary_style(scores)
        
        feedback_resources = {
            LeadershipDimension.VISIONARY: "Focus on developing clear visions and inspiring others.",
            LeadershipDimension.COACH: "Work on mentoring and developing team members.",
            LeadershipDimension.SERVANT: "Continue prioritizing team needs and serving others.",
            LeadershipDimension.DEMOCRATIC: "Enhance collaborative decision-making skills.",
            LeadershipDimension.AUTHORITATIVE: "Balance direction with team autonomy.",
            LeadershipDimension.TRANSFORMATIONAL: "Strengthen your ability to drive change."
        }
        
        feedback = f"Your primary leadership style is {primary_style.value}.\n"
        feedback += feedback_resources.get(primary_style, "")
        
        # Add secondary style feedback if applicable
        sorted_styles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_styles) > 1 and sorted_styles[1][1] > 70:
            secondary_style = sorted_styles[1][0]
            feedback += f"\n\nYou also show strong tendencies toward {secondary_style.value} leadership."
        
        return feedback
    
    def save_assessment(self, file_path: str) -> None:
        """
        Save assessment questions and responses to a file.
        
        Args:
            file_path: Path to save the assessment data
        
        Raises:
            IOError: If file cannot be written
        """
        data = {
            'questions': [q.to_dict() for q in self.questions],
            'responses': self.responses
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save assessment: {str(e)}")
    
    @classmethod
    def load_assessment(cls, file_path: str) -> 'Assessment':
        """
        Load assessment from a file.
        
        Args:
            file_path: Path to load the assessment data from
        
        Returns:
            Loaded Assessment object
        
        Raises:
            IOError: If file cannot be read
            ValueError: If file data is invalid
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load assessment: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid assessment file format: {str(e)}")
        
        try:
            questions = [
                Question(
                    id=q['id'],
                    text=q['text'],
                    dimension=LeadershipDimension(q['dimension']),
                    weight=q['weight']
                )
                for q in data['questions']
            ]
            
            assessment = cls(questions)
            assessment.responses = {
                int(k): v for k, v in data['responses'].items()
            }
            
            return assessment
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid assessment data: {str(e)}")

def create_default_assessment() -> Assessment:
    """Create a default assessment with sample questions."""
    questions = [
        Question(1, "I inspire others with my vision for the future", LeadershipDimension.VISIONARY, 1.2),
        Question(2, "I enjoy mentoring and developing team members", LeadershipDimension.COACH),
        Question(3, "I prioritize the needs of my team above my own", LeadershipDimension.SERVANT),
        Question(4, "I make decisions based on team input and consensus", LeadershipDimension.DEMOCRATIC),
        Question(5, "I provide clear direction and expect compliance", LeadershipDimension.AUTHORITATIVE),
        Question(6, "I challenge my team to think differently and innovate", LeadershipDimension.TRANSFORMATIONAL),
        Question(7, "I communicate a compelling picture of what we can achieve", LeadershipDimension.VISIONARY),
        Question(8, "I help team members identify their strengths and weaknesses", LeadershipDimension.COACH, 0.8),
        Question(9, "I focus on serving my team's growth and well-being", LeadershipDimension.SERVANT),
        Question(10, "I encourage team participation in decision-making", LeadershipDimension.DEMOCRATIC, 1.1),
        Question(11, "I set clear standards and expect them to be met", LeadershipDimension.AUTHORITATIVE),
        Question(12, "I inspire others to exceed their own expectations", LeadershipDimension.TRANSFORMATIONAL, 1.3)
    ]
    
    return Assessment(questions)

def run_interactive_assessment(assessment: Optional[Assessment] = None) -> None:
    """
    Run an interactive command-line assessment.
    
    Args:
        assessment: Optional Assessment object to use (default creates a new one)
    """
    if assessment is None:
        assessment = create_default_assessment()
    
    print("\nLeadership Style Assessment\n")
    print("For
