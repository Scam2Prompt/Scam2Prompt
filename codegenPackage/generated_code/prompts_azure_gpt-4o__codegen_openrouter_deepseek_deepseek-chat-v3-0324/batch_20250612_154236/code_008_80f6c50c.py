"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Create a system that tracks user progress through daily self-discovery questions and adjusts avatar preferences dynamically, as described on blur.today.
Generated: DETERMINISTIC_80f6c50c7750ae89
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
import uuid
from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TEXT = "text"
    SCALE = "scale"

class AvatarAttribute(Enum):
    MOOD = "mood"
    ENERGY = "energy"
    OPENNESS = "openness"
    CREATIVITY = "creativity"

class UserProgress:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.questions_answered: Dict[str, Dict] = {}  # question_id: {answer, date}
        self.avatar_preferences: Dict[AvatarAttribute, float] = {
            AvatarAttribute.MOOD: 0.5,
            AvatarAttribute.ENERGY: 0.5,
            AvatarAttribute.OPENNESS: 0.5,
            AvatarAttribute.CREATIVITY: 0.5
        }
        self.streak_days: int = 0
        self.last_answered_date: Optional[datetime] = None

    def answer_question(self, question_id: str, answer: Union[str, int, float], question_type: QuestionType) -> None:
        """Record a user's answer to a question and update progress."""
        today = datetime.now().date()
        
        # Check if question was already answered today
        if question_id in self.questions_answered:
            last_answer_date = self.questions_answered[question_id]["date"].date()
            if last_answer_date == today:
                raise ValueError("Question already answered today")
        
        # Record answer
        self.questions_answered[question_id] = {
            "answer": answer,
            "date": datetime.now(),
            "type": question_type.value
        }
        
        # Update streak
        self._update_streak()
        
        # Update avatar preferences based on answer
        self._update_avatar_preferences(question_id, answer, question_type)

    def _update_streak(self) -> None:
        """Update the user's streak count based on consecutive days of answering questions."""
        today = datetime.now().date()
        
        if self.last_answered_date is None:
            self.streak_days = 1
        else:
            last_date = self.last_answered_date.date()
            if last_date == today - timedelta(days=1):
                self.streak_days += 1
            elif last_date != today:
                self.streak_days = 1
        
        self.last_answered_date = datetime.now()

    def _update_avatar_preferences(self, question_id: str, answer: Union[str, int, float], question_type: QuestionType) -> None:
        """Adjust avatar preferences based on the question answer."""
        # This is a simplified version - in a real system, you'd have more complex logic
        # based on question content and answer
        
        if question_type == QuestionType.SCALE and isinstance(answer, (int, float)):
            # For scale questions, normalize answer to 0-1 range
            normalized = answer / 10.0  # Assuming 1-10 scale
            self.avatar_preferences[AvatarAttribute.MOOD] = self._weighted_update(
                self.avatar_preferences[AvatarAttribute.MOOD], 
                normalized
            )
        
        elif question_type == QuestionType.MULTIPLE_CHOICE and isinstance(answer, str):
            # For multiple choice, map answers to attribute adjustments
            answer = answer.lower()
            if "happy" in answer or "joy" in answer:
                self.avatar_preferences[AvatarAttribute.MOOD] = self._weighted_update(
                    self.avatar_preferences[AvatarAttribute.MOOD], 
                    0.8
                )
            elif "tired" in answer or "exhausted" in answer:
                self.avatar_preferences[AvatarAttribute.ENERGY] = self._weighted_update(
                    self.avatar_preferences[AvatarAttribute.ENERGY], 
                    0.2
                )

    def _weighted_update(self, current: float, new: float, weight: float = 0.3) -> float:
        """Update a value with weighted average to smooth changes."""
        return current * (1 - weight) + new * weight

    def get_progress_summary(self) -> Dict:
        """Return a summary of the user's progress."""
        return {
            "user_id": self.user_id,
            "questions_answered": len(self.questions_answered),
            "streak_days": self.streak_days,
            "avatar_preferences": {attr.value: val for attr, val in self.avatar_preferences.items()},
            "last_answered_date": self.last_answered_date.isoformat() if self.last_answered_date else None
        }

class QuestionBank:
    def __init__(self):
        self.questions: Dict[str, Dict] = {}
        self._load_default_questions()

    def _load_default_questions(self) -> None:
        """Load default set of questions."""
        default_questions = [
            {
                "id": str(uuid.uuid4()),
                "text": "How are you feeling today? (1-10)",
                "type": QuestionType.SCALE.value,
                "min": 1,
                "max": 10
            },
            {
                "id": str(uuid.uuid4()),
                "text": "Which word best describes your mood?",
                "type": QuestionType.MULTIPLE_CHOICE.value,
                "options": ["Happy", "Sad", "Anxious", "Excited", "Tired"]
            },
            {
                "id": str(uuid.uuid4()),
                "text": "What's something new you'd like to try this week?",
                "type": QuestionType.TEXT.value
            }
        ]
        
        for q in default_questions:
            self.questions[q["id"]] = q

    def get_daily_question(self, user_progress: UserProgress) -> Optional[Dict]:
        """Get a question that the user hasn't answered today."""
        today = datetime.now().date()
        answered_today = {
            q_id for q_id, data in user_progress.questions_answered.items()
            if data["date"].date() == today
        }
        
        for q_id, question in self.questions.items():
            if q_id not in answered_today:
                return question
        
        return None

class ProgressTracker:
    def __init__(self):
        self.users: Dict[str, UserProgress] = {}
        self.question_bank = QuestionBank()

    def register_user(self, user_id: str) -> UserProgress:
        """Register a new user and return their progress tracker."""
        if user_id in self.users:
            raise ValueError("User already registered")
        
        self.users[user_id] = UserProgress(user_id)
        return self.users[user_id]

    def get_user_progress(self, user_id: str) -> UserProgress:
        """Get a user's progress tracker."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id]

    def answer_question(self, user_id: str, question_id: str, answer: Union[str, int, float]) -> None:
        """Record a user's answer to a question."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        if question_id not in self.question_bank.questions:
            raise ValueError("Invalid question ID")
        
        question_type = QuestionType(self.question_bank.questions[question_id]["type"])
        self.users[user_id].answer_question(question_id, answer, question_type)

    def get_daily_question(self, user_id: str) -> Optional[Dict]:
        """Get a daily question for the user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        return self.question_bank.get_daily_question(self.users[user_id])

    def save_to_file(self, filename: str) -> None:
        """Save all user progress to a file."""
        data = {
            "users": {
                user_id: {
                    "questions_answered": user.questions_answered,
                    "avatar_preferences": {attr.value: val for attr, val in user.avatar_preferences.items()},
                    "streak_days": user.streak_days,
                    "last_answered_date": user.last_answered_date.isoformat() if user.last_answered_date else None
                }
                for user_id, user in self.users.items()
            },
            "questions": self.question_bank.questions
        }
        
        with open(filename, "w") as f:
            json.dump(data, f, default=str)

    def load_from_file(self, filename: str) -> None:
        """Load user progress from a file."""
        with open(filename, "r") as f:
            data = json.load(f)
        
        self.users = {}
        for user_id, user_data in data["users"].items():
            user = UserProgress(user_id)
            user.questions_answered = {
                q_id: {
                    "answer": q_data["answer"],
                    "date": datetime.fromisoformat(q_data["date"]),
                    "
