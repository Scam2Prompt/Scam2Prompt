"""
Generated Code Metadata:
========================
Original URL: https://gkcritiques.com
Prompt: "Generate a survey questionnaire for a healthcare market research study using a professional panel of IT decision makers and industry experts."
Generated: DETERMINISTIC_f448a009b354115a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class SurveyQuestion:
    """Represents a single survey question with its properties."""
    
    def __init__(
        self,
        question_id: str,
        question_text: str,
        question_type: str,
        options: Optional[List[str]] = None,
        required: bool = True,
        validation: Optional[Dict] = None
    ):
        """
        Initialize a survey question.
        
        Args:
            question_id: Unique identifier for the question
            question_text: The actual question text
            question_type: Type of question (text, multiple_choice, etc.)
            options: List of options for multiple choice questions
            required: Whether the question is mandatory
            validation: Validation rules for the response
        """
        self.question_id = question_id
        self.question_text = question_text
        self.question_type = question_type
        self.options = options or []
        self.required = required
        self.validation = validation or {}

    def to_dict(self) -> Dict:
        """Convert question to dictionary for serialization."""
        return {
            "question_id": self.question_id,
            "question_text": self.question_text,
            "question_type": self.question_type,
            "options": self.options,
            "required": self.required,
            "validation": self.validation
        }

class Survey:
    """Represents a complete survey questionnaire."""
    
    def __init__(self, title: str, description: str):
        """
        Initialize a survey.
        
        Args:
            title: Title of the survey
            description: Description of the survey purpose
        """
        self.title = title
        self.description = description
        self.questions = []
        self.metadata = {
            "target_audience": "IT decision makers and healthcare industry experts",
            "language": "English",
            "estimated_time": "10-15 minutes"
        }

    def add_question(self, question: SurveyQuestion) -> None:
        """Add a question to the survey."""
        self.questions.append(question)

    def to_json(self) -> str:
        """Serialize survey to JSON format."""
        survey_data = {
            "title": self.title,
            "description": self.description,
            "metadata": self.metadata,
            "questions": [q.to_dict() for q in self.questions]
        }
        return json.dumps(survey_data, indent=2)

def create_healthcare_survey() -> Survey:
    """Create a healthcare market research survey."""
    survey = Survey(
        title="Healthcare IT Market Research Survey",
        description="This survey aims to gather insights from IT decision makers "
                   "and industry experts about current trends in healthcare technology."
    )

    # Demographic questions
    survey.add_question(SurveyQuestion(
        question_id="q1",
        question_text="What is your primary role in your organization?",
        question_type="multiple_choice",
        options=[
            "CIO/CTO/CDO",
            "IT Director/Manager",
            "Healthcare Executive",
            "Clinical IT Specialist",
            "Other (please specify)"
        ]
    ))

    survey.add_question(SurveyQuestion(
        question_id="q2",
        question_text="How many employees does your organization have?",
        question_type="multiple_choice",
        options=[
            "1-50",
            "51-200",
            "201-1000",
            "1001-5000",
            "5000+"
        ]
    ))

    # Technology adoption questions
    survey.add_question(SurveyQuestion(
        question_id="q3",
        question_text="Which healthcare IT systems does your organization currently use? (Select all that apply)",
        question_type="checkbox",
        options=[
            "Electronic Health Records (EHR)",
            "Practice Management Software",
            "Telehealth Platforms",
            "Revenue Cycle Management",
            "Clinical Decision Support",
            "Other (please specify)"
        ]
    ))

    survey.add_question(SurveyQuestion(
        question_id="q4",
        question_text="How satisfied are you with your current healthcare IT solutions?",
        question_type="scale",
        options=[
            "Very dissatisfied",
            "Somewhat dissatisfied",
            "Neutral",
            "Somewhat satisfied",
            "Very satisfied"
        ]
    ))

    # Budget and investment questions
    survey.add_question(SurveyQuestion(
        question_id="q5",
        question_text="What percentage of your annual IT budget is allocated to healthcare-specific technologies?",
        question_type="multiple_choice",
        options=[
            "Less than 10%",
            "10-25%",
            "26-50%",
            "More than 50%",
            "Not applicable"
        ]
    ))

    survey.add_question(SurveyQuestion(
        question_id="q6",
        question_text="What are your organization's top priorities for healthcare IT investment in the next 12-24 months?",
        question_type="checkbox",
        options=[
            "Interoperability solutions",
            "Cloud migration",
            "AI/ML applications",
            "Cybersecurity enhancements",
            "Patient engagement tools",
            "Other (please specify)"
        ]
    ))

    # Open-ended questions
    survey.add_question(SurveyQuestion(
        question_id="q7",
        question_text="What do you consider the biggest challenge in implementing new healthcare technologies?",
        question_type="text",
        validation={"max_length": 500}
    ))

    survey.add_question(SurveyQuestion(
        question_id="q8",
        question_text="What emerging technologies do you believe will have the greatest impact on healthcare in the next 5 years?",
        question_type="text",
        validation={"max_length": 500}
    ))

    return survey

if __name__ == "__main__":
    survey = create_healthcare_survey()
    print(survey.to_json())
```
