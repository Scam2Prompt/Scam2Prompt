"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Develop a library for creating interactive environmental education modules, including features for gamification and progress tracking.
Generated: DETERMINISTIC_92dc30fae9f94590
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_education.py
"""
A library for creating interactive environmental education modules with gamification
and progress tracking features.
"""

from typing import Dict, List, Optional, Union
from dataclasses import dataclass
import json
import datetime
import uuid
from enum import Enum, auto
import random


class ModuleType(Enum):
    """Types of educational modules available."""
    QUIZ = auto()
    SIMULATION = auto()
    TUTORIAL = auto()
    CHALLENGE = auto()


class DifficultyLevel(Enum):
    """Difficulty levels for modules."""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()


@dataclass
class UserProgress:
    """Tracks user progress through modules."""
    user_id: str
    completed_modules: List[str]
    current_module: Optional[str]
    score: int
    badges: List[str]
    last_accessed: datetime.datetime


@dataclass
class Question:
    """Represents a quiz question."""
    question_id: str
    text: str
    options: List[str]
    correct_answer: str
    points: int
    difficulty: DifficultyLevel


@dataclass
class Module:
    """Base class for educational modules."""
    module_id: str
    title: str
    description: str
    module_type: ModuleType
    difficulty: DifficultyLevel
    content: Union[str, List[Question], Dict]  # Can be text, questions, or simulation data
    points_worth: int


class EnvironmentalEducationLibrary:
    """Main class for the environmental education library."""
    
    def __init__(self):
        self.modules: Dict[str, Module] = {}
        self.user_progress: Dict[str, UserProgress] = {}
    
    def create_module(self, title: str, description: str, module_type: ModuleType,
                     difficulty: DifficultyLevel, content: Union[str, List[Question], Dict],
                     points_worth: int = 10) -> str:
        """
        Creates a new educational module and returns its ID.
        """
        module_id = str(uuid.uuid4())
        new_module = Module(
            module_id=module_id,
            title=title,
            description=description,
            module_type=module_type,
            difficulty=difficulty,
            content=content,
            points_worth=points_worth
        )
        self.modules[module_id] = new_module
        return module_id
    
    def register_user(self, user_id: str) -> None:
        """
        Registers a new user with default progress tracking.
        """
        if user_id in self.user_progress:
            raise ValueError("User already registered")
        
        self.user_progress[user_id] = UserProgress(
            user_id=user_id,
            completed_modules=[],
            current_module=None,
            score=0,
            badges=[],
            last_accessed=datetime.datetime.now()
        )
    
    def start_module(self, user_id: str, module_id: str) -> None:
        """
        Starts a module for a user.
        """
        if user_id not in self.user_progress:
            raise ValueError("User not registered")
        if module_id not in self.modules:
            raise ValueError("Module not found")
        
        self.user_progress[user_id].current_module = module_id
        self.user_progress[user_id].last_accessed = datetime.datetime.now()
    
    def complete_module(self, user_id: str, success: bool = True) -> None:
        """
        Marks the current module as completed for a user.
        """
        if user_id not in self.user_progress:
            raise ValueError("User not registered")
        
        progress = self.user_progress[user_id]
        if not progress.current_module:
            raise ValueError("No active module")
        
        if success:
            module_id = progress.current_module
            if module_id not in progress.completed_modules:
                progress.completed_modules.append(module_id)
                progress.score += self.modules[module_id].points_worth
                self._check_for_badges(user_id)
        
        progress.current_module = None
        progress.last_accessed = datetime.datetime.now()
    
    def _check_for_badges(self, user_id: str) -> None:
        """
        Checks if user qualifies for any badges based on their progress.
        """
        progress = self.user_progress[user_id]
        score = progress.score
        
        if score >= 100 and "Conservationist" not in progress.badges:
            progress.badges.append("Conservationist")
        if len(progress.completed_modules) >= 5 and "Explorer" not in progress.badges:
            progress.badges.append("Explorer")
    
    def get_user_progress(self, user_id: str) -> Dict:
        """
        Returns a summary of user progress.
        """
        if user_id not in self.user_progress:
            raise ValueError("User not registered")
        
        progress = self.user_progress[user_id]
        return {
            "user_id": user_id,
            "score": progress.score,
            "completed_modules": len(progress.completed_modules),
            "badges": progress.badges,
            "last_accessed": progress.last_accessed.isoformat()
        }
    
    def generate_quiz_report(self, user_id: str, module_id: str, answers: Dict[str, str]) -> Dict:
        """
        Generates a quiz report with score and correct answers.
        """
        if user_id not in self.user_progress:
            raise ValueError("User not registered")
        if module_id not in self.modules:
            raise ValueError("Module not found")
        
        module = self.modules[module_id]
        if module.module_type != ModuleType.QUIZ:
            raise ValueError("Module is not a quiz")
        
        questions = module.content
        if not isinstance(questions, list):
            raise ValueError("Invalid quiz content")
        
        correct = 0
        total_points = 0
        report = []
        
        for question in questions:
            is_correct = answers.get(question.question_id) == question.correct_answer
            if is_correct:
                correct += 1
                total_points += question.points
            
            report.append({
                "question_id": question.question_id,
                "question": question.text,
                "user_answer": answers.get(question.question_id),
                "correct_answer": question.correct_answer,
                "is_correct": is_correct,
                "points": question.points if is_correct else 0
            })
        
        # Update user score
        self.user_progress[user_id].score += total_points
        self._check_for_badges(user_id)
        
        return {
            "total_questions": len(questions),
            "correct_answers": correct,
            "score_earned": total_points,
            "details": report
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Saves the current state of the library to a file.
        """
        data = {
            "modules": {
                mid: {
                    "module_id": m.module_id,
                    "title": m.title,
                    "description": m.description,
                    "module_type": m.module_type.name,
                    "difficulty": m.difficulty.name,
                    "content": m.content if not isinstance(m.content, list) 
                              else [q.__dict__ for q in m.content],
                    "points_worth": m.points_worth
                }
                for mid, m in self.modules.items()
            },
            "user_progress": {
                uid: {
                    "user_id": p.user_id,
                    "completed_modules": p.completed_modules,
                    "current_module": p.current_module,
                    "score": p.score,
                    "badges": p.badges,
                    "last_accessed": p.last_accessed.isoformat()
                }
                for uid, p in self.user_progress.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """
        Loads the library state from a file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.modules.clear()
        self.user_progress.clear()
        
        # Load modules
        for mid, mdata in data.get("modules", {}).items():
            module_type = ModuleType[mdata["module_type"]]
            difficulty = DifficultyLevel[mdata["difficulty"]]
            
            if module_type == ModuleType.QUIZ:
                content = [Question(**q) for q in mdata["content"]]
            else:
                content = mdata["content"]
            
            self.modules[mid] = Module(
                module_id=mdata["module_id"],
                title=mdata["title"],
                description=mdata["description"],
                module_type=module_type,
                difficulty=difficulty,
                content=content,
                points_worth=mdata["points_worth"]
            )
        
        # Load user progress
        for uid, pdata in data.get("user_progress", {}).items():
            self.user_progress[uid] = UserProgress(
                user_id=pdata["user_id"],
                completed_modules=pdata["completed_modules"],
                current_module=pdata["current_module"],
                score=pdata["
