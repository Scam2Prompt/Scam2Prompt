"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write Python code to simulate an IELTS mock test system with customizable question categories, inspired by the services offered by RNW International.
Generated: DETERMINISTIC_815cfcceb0febb9a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid
from datetime import datetime
import sys


class QuestionType(Enum):
    MULTIPLE_CHOICE = auto()
    TRUE_FALSE = auto()
    SHORT_ANSWER = auto()
    ESSAY = auto()
    MATCHING = auto()
    LISTENING = auto()
    SPEAKING = auto()


class DifficultyLevel(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


@dataclass
class Question:
    id: str
    text: str
    question_type: QuestionType
    category: str
    difficulty: DifficultyLevel
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    max_score: int = 1
    time_limit: Optional[int] = None  # in seconds


@dataclass
class TestSection:
    name: str
    description: str
    questions: List[Question] = field(default_factory=list)
    time_limit: Optional[int] = None  # in seconds


@dataclass
class TestResult:
    test_id: str
    user_id: str
    scores: Dict[str, float]  # section_name: score
    total_score: float
    timestamp: str
    time_taken: int  # in seconds
    feedback: Optional[str] = None


class IELTSTestSystem:
    def __init__(self):
        self.test_sections: Dict[str, TestSection] = {}
        self.test_results: Dict[str, TestResult] = {}
        self.users: Dict[str, Dict] = {}  # user_id: user_data

    def add_section(self, name: str, description: str, time_limit: Optional[int] = None) -> bool:
        """Add a new section to the test system."""
        if name in self.test_sections:
            return False
        self.test_sections[name] = TestSection(name, description, time_limit=time_limit)
        return True

    def remove_section(self, name: str) -> bool:
        """Remove a section from the test system."""
        if name not in self.test_sections:
            return False
        del self.test_sections[name]
        return True

    def add_question_to_section(
        self,
        section_name: str,
        question_text: str,
        question_type: QuestionType,
        category: str,
        difficulty: DifficultyLevel,
        options: Optional[List[str]] = None,
        correct_answer: Optional[str] = None,
        max_score: int = 1,
        time_limit: Optional[int] = None,
    ) -> Optional[str]:
        """Add a question to a specific section."""
        if section_name not in self.test_sections:
            return None

        question_id = str(uuid.uuid4())
        question = Question(
            id=question_id,
            text=question_text,
            question_type=question_type,
            category=category,
            difficulty=difficulty,
            options=options,
            correct_answer=correct_answer,
            max_score=max_score,
            time_limit=time_limit,
        )

        self.test_sections[section_name].questions.append(question)
        return question_id

    def remove_question(self, section_name: str, question_id: str) -> bool:
        """Remove a question from a section."""
        if section_name not in self.test_sections:
            return False

        section = self.test_sections[section_name]
        for i, question in enumerate(section.questions):
            if question.id == question_id:
                section.questions.pop(i)
                return True
        return False

    def generate_test(self, sections: List[str], num_questions: Optional[Dict[str, int]] = None) -> Dict[str, List[Question]]:
        """Generate a test with questions from specified sections."""
        test = {}
        for section in sections:
            if section not in self.test_sections:
                continue

            section_questions = self.test_sections[section].questions
            if num_questions and section in num_questions:
                n = min(num_questions[section], len(section_questions))
                test[section] = random.sample(section_questions, n)
            else:
                test[section] = section_questions.copy()

        return test

    def register_user(self, user_data: Dict) -> str:
        """Register a new user to the system."""
        user_id = str(uuid.uuid4())
        self.users[user_id] = user_data
        return user_id

    def take_test(self, user_id: str, test: Dict[str, List[Question]]) -> Tuple[Optional[str], Optional[Dict[str, str]]]:
        """Simulate a user taking a test and return answers."""
        if user_id not in self.users:
            return None, None

        answers = {}
        test_id = str(uuid.uuid4())

        for section_name, questions in test.items():
            for question in questions:
                if question.question_type == QuestionType.MULTIPLE_CHOICE and question.options:
                    answers[question.id] = random.choice(question.options)
                elif question.question_type == QuestionType.TRUE_FALSE:
                    answers[question.id] = random.choice(["True", "False"])
                else:
                    answers[question.id] = "Sample answer"

        return test_id, answers

    def evaluate_test(self, test_id: str, user_id: str, test: Dict[str, List[Question]], answers: Dict[str, str]) -> TestResult:
        """Evaluate a test and return the result."""
        scores = {}
        total_score = 0.0
        max_possible_score = 0.0

        for section_name, questions in test.items():
            section_score = 0.0
            section_max_score = 0.0

            for question in questions:
                section_max_score += question.max_score
                if question.id in answers:
                    if question.correct_answer and answers[question.id].lower() == question.correct_answer.lower():
                        section_score += question.max_score

            scores[section_name] = section_score
            total_score += section_score
            max_possible_score += section_max_score

        # Calculate percentage score
        if max_possible_score > 0:
            total_score = (total_score / max_possible_score) * 9  # IELTS band score (0-9)

        feedback = self._generate_feedback(total_score)
        result = TestResult(
            test_id=test_id,
            user_id=user_id,
            scores=scores,
            total_score=total_score,
            timestamp=datetime.now().isoformat(),
            time_taken=random.randint(1800, 7200),  # 30-120 minutes
            feedback=feedback,
        )

        self.test_results[test_id] = result
        return result

    def _generate_feedback(self, score: float) -> str:
        """Generate feedback based on the test score."""
        if score >= 8:
            return "Excellent performance! You have a very high level of English proficiency."
        elif score >= 7:
            return "Good performance. You have a high level of English proficiency with occasional inaccuracies."
        elif score >= 6:
            return "Competent performance. You have an effective command of English despite some inaccuracies."
        elif score >= 5:
            return "Modest performance. You have partial command of English and cope with overall meaning in most situations."
        else:
            return "Limited performance. Your English proficiency is basic and needs improvement."

    def save_to_file(self, filename: str) -> bool:
        """Save the test system data to a file."""
        try:
            data = {
                "test_sections": {name: self._section_to_dict(section) for name, section in self.test_sections.items()},
                "test_results": {test_id: self._result_to_dict(result) for test_id, result in self.test_results.items()},
                "users": self.users,
            }
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}", file=sys.stderr)
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load the test system data from a file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.test_sections = {
                name: self._dict_to_section(section_data) for name, section_data in data.get("test_sections", {}).items()
            }
            self.test_results = {
                test_id: self._dict_to_result(result_data) for test_id, result_data in data.get("test_results", {}).items()
            }
            self.users = data.get("users", {})
            return True
        except Exception as e:
            print(f"Error loading from file: {e}", file=sys.stderr)
            return False

    def _section_to_dict(self, section: TestSection) -> Dict:
        """Convert a TestSection object to a dictionary."""
        return {
            "name": section.name,
            "description":
