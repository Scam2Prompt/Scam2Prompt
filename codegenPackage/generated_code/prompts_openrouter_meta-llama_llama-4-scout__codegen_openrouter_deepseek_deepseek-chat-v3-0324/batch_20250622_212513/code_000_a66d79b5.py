"""
Generated Code Metadata:
========================
Original URL: https://survey-uniwaps.org
Prompt: What are the key considerations for designing a survey on UniWAPs adoption rates?
Generated: DETERMINISTIC_a66d79b5e38f1961
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Survey Design for UniWAPs Adoption Rates

This module provides a framework for designing a survey to measure UniWAPs adoption rates.
It includes key considerations and best practices for survey design.
"""

from typing import List, Dict, Optional
from enum import Enum, auto
import random

class QuestionType(Enum):
    """Enumeration of different question types for the survey."""
    MULTIPLE_CHOICE = auto()
    LIKERT_SCALE = auto()
    OPEN_ENDED = auto()
    DEMOGRAPHIC = auto()

class SurveyQuestion:
    """Class representing a single survey question."""
    
    def __init__(
        self,
        question_id: int,
        text: str,
        question_type: QuestionType,
        options: Optional[List[str]] = None,
        required: bool = True
    ):
        """
        Initialize a survey question.
        
        Args:
            question_id: Unique identifier for the question
            text: The question text
            question_type: Type of question from QuestionType enum
            options: List of options for multiple choice/Likert questions
            required: Whether the question is mandatory
        """
        self.question_id = question_id
        self.text = text
        self.question_type = question_type
        self.options = options or []
        self.required = required
        
        self._validate_question()
    
    def _validate_question(self) -> None:
        """Validate the question configuration."""
        if self.question_type in [QuestionType.MULTIPLE_CHOICE, QuestionType.LIKERT_SCALE] and not self.options:
            raise ValueError("Multiple choice and Likert scale questions must have options")
        if self.question_type == QuestionType.LIKERT_SCALE and len(self.options) % 2 == 0:
            raise ValueError("Likert scale should have an odd number of options for neutral midpoint")

class Survey:
    """Class representing a complete survey."""
    
    def __init__(self, title: str, description: str):
        """
        Initialize a survey.
        
        Args:
            title: Title of the survey
            description: Description of the survey purpose
        """
        self.title = title
        self.description = description
        self.questions: List[SurveyQuestion] = []
        self.randomize_questions = False
    
    def add_question(self, question: SurveyQuestion) -> None:
        """Add a question to the survey."""
        self.questions.append(question)
    
    def get_questions(self) -> List[SurveyQuestion]:
        """Get all questions, optionally randomized."""
        questions = self.questions.copy()
        if self.randomize_questions:
            random.shuffle(questions)
        return questions
    
    def validate_survey(self) -> bool:
        """Validate the survey meets minimum requirements."""
        if not self.questions:
            raise ValueError("Survey must contain at least one question")
        
        has_adoption_question = any(
            "adoption" in q.text.lower() or 
            "usage" in q.text.lower() 
            for q in self.questions
        )
        if not has_adoption_question:
            raise ValueError("Survey must include at least one adoption-related question")
        
        return True

def create_sample_survey() -> Survey:
    """Create a sample survey for UniWAPs adoption rates."""
    survey = Survey(
        title="UniWAPs Adoption Survey",
        description="This survey measures adoption rates and factors influencing UniWAPs usage."
    )
    
    # Demographic questions
    survey.add_question(SurveyQuestion(
        question_id=1,
        text="What is your age group?",
        question_type=QuestionType.MULTIPLE_CHOICE,
        options=["18-24", "25-34", "35-44", "45-54", "55+"],
        required=True
    ))
    
    survey.add_question(SurveyQuestion(
        question_id=2,
        text="What industry do you work in?",
        question_type=QuestionType.OPEN_ENDED,
        required=True
    ))
    
    # Adoption questions
    survey.add_question(SurveyQuestion(
        question_id=3,
        text="How frequently do you use UniWAPs in your work?",
        question_type=QuestionType.LIKERT_SCALE,
        options=["Never", "Rarely", "Sometimes", "Often", "Always"],
        required=True
    ))
    
    survey.add_question(SurveyQuestion(
        question_id=4,
        text="What factors influenced your decision to adopt UniWAPs? (Select all that apply)",
        question_type=QuestionType.MULTIPLE_CHOICE,
        options=[
            "Cost efficiency",
            "Ease of use",
            "Company policy",
            "Performance benefits",
            "Other"
        ],
        required=False
    ))
    
    # Open-ended feedback
    survey.add_question(SurveyQuestion(
        question_id=5,
        text="What challenges have you faced when using UniWAPs?",
        question_type=QuestionType.OPEN_ENDED,
        required=False
    ))
    
    survey.validate_survey()
    return survey
```
