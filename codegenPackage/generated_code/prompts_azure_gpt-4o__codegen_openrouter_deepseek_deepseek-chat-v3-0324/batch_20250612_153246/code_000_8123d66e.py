"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write Python code to design a survey tool for measuring satisfaction levels among employees, beneficiaries, board members, and general assembly members, as described in the governance section of the Tabuk Community Development Association.
Generated: DETERMINISTIC_8123d66e767ffa8e
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
from typing import List, Dict, Optional
from enum import Enum
import datetime
import csv
import os

class SurveyType(Enum):
    EMPLOYEE = "Employee Satisfaction"
    BENEFICIARY = "Beneficiary Feedback"
    BOARD_MEMBER = "Board Member Evaluation"
    GENERAL_ASSEMBLY = "General Assembly Feedback"

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    SCALE = "scale"
    TEXT = "text"

class SurveyQuestion:
    def __init__(self, question_id: str, text: str, question_type: QuestionType, 
                 options: Optional[List[str]] = None, required: bool = True):
        self.question_id = question_id
        self.text = text
        self.question_type = question_type
        self.options = options if options else []
        self.required = required

    def to_dict(self) -> Dict:
        return {
            "question_id": self.question_id,
            "text": self.text,
            "question_type": self.question_type.value,
            "options": self.options,
            "required": self.required
        }

class SurveyResponse:
    def __init__(self, survey_id: str, respondent_id: str, respondent_type: SurveyType):
        self.survey_id = survey_id
        self.respondent_id = respondent_id
        self.respondent_type = respondent_type
        self.answers = {}
        self.timestamp = datetime.datetime.now().isoformat()

    def add_answer(self, question_id: str, answer: str) -> None:
        self.answers[question_id] = answer

    def to_dict(self) -> Dict:
        return {
            "survey_id": self.survey_id,
            "respondent_id": self.respondent_id,
            "respondent_type": self.respondent_type.value,
            "answers": self.answers,
            "timestamp": self.timestamp
        }

class Survey:
    def __init__(self, survey_id: str, title: str, description: str, survey_type: SurveyType):
        self.survey_id = survey_id
        self.title = title
        self.description = description
        self.survey_type = survey_type
        self.questions = []
        self.responses = []

    def add_question(self, question: SurveyQuestion) -> None:
        self.questions.append(question)

    def add_response(self, response: SurveyResponse) -> None:
        self.responses.append(response)

    def to_dict(self) -> Dict:
        return {
            "survey_id": self.survey_id,
            "title": self.title,
            "description": self.description,
            "survey_type": self.survey_type.value,
            "questions": [q.to_dict() for q in self.questions],
            "responses": [r.to_dict() for r in self.responses]
        }

class SurveyManager:
    def __init__(self):
        self.surveys = {}
        self.survey_templates = self._load_default_templates()

    def _load_default_templates(self) -> Dict[SurveyType, List[Dict]]:
        templates = {
            SurveyType.EMPLOYEE: [
                {
                    "question_id": "emp_q1",
                    "text": "How satisfied are you with your work environment?",
                    "question_type": QuestionType.SCALE,
                    "options": ["1 (Very Dissatisfied)", "2", "3", "4", "5 (Very Satisfied)"],
                    "required": True
                },
                {
                    "question_id": "emp_q2",
                    "text": "What improvements would you suggest for the workplace?",
                    "question_type": QuestionType.TEXT,
                    "required": False
                }
            ],
            SurveyType.BENEFICIARY: [
                {
                    "question_id": "ben_q1",
                    "text": "How satisfied are you with the services provided?",
                    "question_type": QuestionType.SCALE,
                    "options": ["1 (Very Dissatisfied)", "2", "3", "4", "5 (Very Satisfied)"],
                    "required": True
                }
            ],
            SurveyType.BOARD_MEMBER: [
                {
                    "question_id": "board_q1",
                    "text": "How effective is the current governance structure?",
                    "question_type": QuestionType.SCALE,
                    "options": ["1 (Not Effective)", "2", "3", "4", "5 (Very Effective)"],
                    "required": True
                }
            ],
            SurveyType.GENERAL_ASSEMBLY: [
                {
                    "question_id": "ga_q1",
                    "text": "How well does the association represent your interests?",
                    "question_type": QuestionType.SCALE,
                    "options": ["1 (Poorly)", "2", "3", "4", "5 (Very Well)"],
                    "required": True
                }
            ]
        }
        return templates

    def create_survey(self, survey_id: str, title: str, description: str, survey_type: SurveyType) -> Survey:
        if survey_id in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} already exists")
        
        survey = Survey(survey_id, title, description, survey_type)
        
        # Add template questions based on survey type
        for question_data in self.survey_templates.get(survey_type, []):
            question = SurveyQuestion(
                question_id=question_data["question_id"],
                text=question_data["text"],
                question_type=QuestionType(question_data["question_type"]),
                options=question_data.get("options"),
                required=question_data["required"]
            )
            survey.add_question(question)
        
        self.surveys[survey_id] = survey
        return survey

    def get_survey(self, survey_id: str) -> Survey:
        if survey_id not in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} not found")
        return self.surveys[survey_id]

    def submit_response(self, survey_id: str, respondent_id: str, 
                       respondent_type: SurveyType, answers: Dict[str, str]) -> SurveyResponse:
        survey = self.get_survey(survey_id)
        
        # Validate required questions are answered
        for question in survey.questions:
            if question.required and question.question_id not in answers:
                raise ValueError(f"Required question {question.question_id} not answered")
        
        response = SurveyResponse(survey_id, respondent_id, respondent_type)
        for question_id, answer in answers.items():
            response.add_answer(question_id, answer)
        
        survey.add_response(response)
        return response

    def export_responses_to_csv(self, survey_id: str, filename: str) -> None:
        survey = self.get_survey(survey_id)
        
        if not survey.responses:
            raise ValueError("No responses to export")
        
        # Prepare CSV headers
        headers = ["respondent_id", "respondent_type", "timestamp"]
        headers.extend([q.question_id for q in survey.questions])
        
        # Prepare CSV rows
        rows = []
        for response in survey.responses:
            row = {
                "respondent_id": response.respondent_id,
                "respondent_type": response.respondent_type.value,
                "timestamp": response.timestamp
            }
            for question in survey.questions:
                row[question.question_id] = response.answers.get(question.question_id, "")
            rows.append(row)
        
        # Write to CSV
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(rows)
        except IOError as e:
            raise IOError(f"Failed to write CSV file: {str(e)}")

    def save_survey_data(self, filename: str) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(
                    {survey_id: survey.to_dict() for survey_id, survey in self.surveys.items()},
                    file,
                    indent=2
                )
        except IOError as e:
            raise IOError(f"Failed to save survey data: {str(e)}")

    def load_survey_data(self, filename: str) -> None:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.surveys = {}
                for survey_id, survey_data in data.items():
                    survey = Survey(
                        survey_id=survey_data["survey_id"],
                        title=survey_data["title"],
                        description=survey_data["description"],
                        survey_type=SurveyType(survey_data["survey_type"])
                    )
                    for question_data in survey_data["questions"]:
                        question = SurveyQuestion(
                            question_id=question_data["question_id"],
                            text=question_data["text"],
                            question_type=QuestionType(question_data["question_type"]),
                            options=question_data.get("options", []),
                            required=question_data["required"]
                        )
                        survey.add_question(question)
                    for response_data in survey
