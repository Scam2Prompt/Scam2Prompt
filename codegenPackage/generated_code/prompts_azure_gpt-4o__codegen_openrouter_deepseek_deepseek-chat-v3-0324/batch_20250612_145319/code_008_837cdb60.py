"""
Generated Code Metadata:
========================
Original URL: https://www.gigzio.com
Prompt: Generate code to implement an assessment preparation tool for job seekers, referencing Gigzio's career preparation features.
Generated: DETERMINISTIC_837cdb6077d46400
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import random
from datetime import datetime
import uuid

@dataclass
class Question:
    id: str
    text: str
    category: str
    difficulty: str
    options: List[str]
    correct_answer: str
    explanation: str

@dataclass
class Assessment:
    id: str
    title: str
    description: str
    questions: List[Question]
    time_limit: int  # in minutes
    passing_score: float
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class UserProgress:
    user_id: str
    assessment_id: str
    completed_questions: List[str] = field(default_factory=list)
    score: float = 0.0
    attempts: int = 0
    last_attempt: Optional[str] = None

class AssessmentPreparationTool:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.assessments: Dict[str, Assessment] = {}
        self.user_progress: Dict[str, Dict[str, UserProgress]] = {}  # user_id -> assessment_id -> progress
        self._initialize_data_directory()
        self._load_data()

    def _initialize_data_directory(self) -> None:
        """Create data directory if it doesn't exist."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _load_data(self) -> None:
        """Load assessment and user progress data from files."""
        try:
            # Load assessments
            assessments_path = os.path.join(self.data_dir, "assessments.json")
            if os.path.exists(assessments_path):
                with open(assessments_path, "r") as f:
                    assessments_data = json.load(f)
                    for assessment_data in assessments_data:
                        questions = [
                            Question(**question_data) for question_data in assessment_data["questions"]
                        ]
                        self.assessments[assessment_data["id"]] = Assessment(
                            id=assessment_data["id"],
                            title=assessment_data["title"],
                            description=assessment_data["description"],
                            questions=questions,
                            time_limit=assessment_data["time_limit"],
                            passing_score=assessment_data["passing_score"]
                        )

            # Load user progress
            progress_path = os.path.join(self.data_dir, "user_progress.json")
            if os.path.exists(progress_path):
                with open(progress_path, "r") as f:
                    progress_data = json.load(f)
                    for user_id, assessments_progress in progress_data.items():
                        self.user_progress[user_id] = {
                            assessment_id: UserProgress(**progress)
                            for assessment_id, progress in assessments_progress.items()
                        }
        except Exception as e:
            print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save assessment and user progress data to files."""
        try:
            # Save assessments
            assessments_path = os.path.join(self.data_dir, "assessments.json")
            assessments_data = [
                {
                    "id": assessment.id,
                    "title": assessment.title,
                    "description": assessment.description,
                    "questions": [
                        {
                            "id": question.id,
                            "text": question.text,
                            "category": question.category,
                            "difficulty": question.difficulty,
                            "options": question.options,
                            "correct_answer": question.correct_answer,
                            "explanation": question.explanation
                        }
                        for question in assessment.questions
                    ],
                    "time_limit": assessment.time_limit,
                    "passing_score": assessment.passing_score
                }
                for assessment in self.assessments.values()
            ]
            with open(assessments_path, "w") as f:
                json.dump(assessments_data, f, indent=2)

            # Save user progress
            progress_path = os.path.join(self.data_dir, "user_progress.json")
            progress_data = {
                user_id: {
                    assessment_id: {
                        "user_id": progress.user_id,
                        "assessment_id": progress.assessment_id,
                        "completed_questions": progress.completed_questions,
                        "score": progress.score,
                        "attempts": progress.attempts,
                        "last_attempt": progress.last_attempt
                    }
                    for assessment_id, progress in assessments_progress.items()
                }
                for user_id, assessments_progress in self.user_progress.items()
            }
            with open(progress_path, "w") as f:
                json.dump(progress_data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def create_assessment(
        self,
        title: str,
        description: str,
        questions: List[Question],
        time_limit: int,
        passing_score: float
    ) -> Assessment:
        """Create a new assessment."""
        assessment_id = str(uuid.uuid4())
        assessment = Assessment(
            id=assessment_id,
            title=title,
            description=description,
            questions=questions,
            time_limit=time_limit,
            passing_score=passing_score
        )
        self.assessments[assessment_id] = assessment
        self._save_data()
        return assessment

    def get_assessment(self, assessment_id: str) -> Optional[Assessment]:
        """Get an assessment by ID."""
        return self.assessments.get(assessment_id)

    def list_assessments(self) -> List[Assessment]:
        """List all available assessments."""
        return list(self.assessments.values())

    def start_assessment(self, user_id: str, assessment_id: str) -> Optional[List[Question]]:
        """Start an assessment for a user."""
        if assessment_id not in self.assessments:
            return None

        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}

        if assessment_id not in self.user_progress[user_id]:
            self.user_progress[user_id][assessment_id] = UserProgress(
                user_id=user_id,
                assessment_id=assessment_id
            )

        assessment = self.assessments[assessment_id]
        return assessment.questions

    def submit_answer(
        self,
        user_id: str,
        assessment_id: str,
        question_id: str,
        answer: str
    ) -> bool:
        """Submit an answer to a question and update progress."""
        if (user_id not in self.user_progress or
                assessment_id not in self.user_progress[user_id]):
            return False

        assessment = self.get_assessment(assessment_id)
        if not assessment:
            return False

        question = next((q for q in assessment.questions if q.id == question_id), None)
        if not question:
            return False

        progress = self.user_progress[user_id][assessment_id]
        if question_id in progress.completed_questions:
            return False  # Question already answered

        is_correct = answer == question.correct_answer
        if is_correct:
            progress.score += 1

        progress.completed_questions.append(question_id)
        progress.last_attempt = datetime.now().isoformat()
        self._save_data()
        return is_correct

    def complete_assessment(self, user_id: str, assessment_id: str) -> Dict:
        """Complete an assessment and return results."""
        if (user_id not in self.user_progress or
                assessment_id not in self.user_progress[user_id]):
            return {"error": "Invalid user or assessment"}

        progress = self.user_progress[user_id][assessment_id]
        assessment = self.get_assessment(assessment_id)
        if not assessment:
            return {"error": "Assessment not found"}

        progress.attempts += 1
        total_questions = len(assessment.questions)
        score_percentage = (progress.score / total_questions) * 100
        passed = score_percentage >= assessment.passing_score

        result = {
            "assessment_id": assessment_id,
            "user_id": user_id,
            "score": progress.score,
            "total_questions": total_questions,
            "percentage": score_percentage,
            "passed": passed,
            "passing_score": assessment.passing_score,
            "attempts": progress.attempts,
            "completed_at": datetime.now().isoformat()
        }

        self._save_data()
        return result

    def get_user_progress(self, user_id: str, assessment_id: str) -> Optional[UserProgress]:
        """Get a user's progress for a specific assessment."""
        if (user_id not in self.user_progress or
                assessment_id not in self.user_progress[user_id]):
            return None
        return self.user_progress[user_id][assessment_id]

    def get_recommended_assessments(self, user_id: str) -> List[Assessment]:
        """Get recommended assessments based on user's progress."""
        # Simple implementation: return random assessments not yet completed
        completed_assessments = set()
        if user_id in self.user_progress:
            completed_assessments = set(self.user_progress[user_id].keys())

        available_assessments = [
            assessment for assessment in self.ass
