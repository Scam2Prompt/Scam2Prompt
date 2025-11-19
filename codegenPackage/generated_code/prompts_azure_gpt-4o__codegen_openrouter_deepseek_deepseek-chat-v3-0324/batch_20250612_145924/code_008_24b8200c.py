"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Create a Python application that performs knowledge checks and assignments for forex trading learners, modeled after FinTrends' course structure.
Generated: DETERMINISTIC_24b8200c4f661b1f
Batch ID: 20250612_145924
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
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ForexTradingCourse:
    """
    A class to manage forex trading course content, knowledge checks, and assignments.
    Modeled after FinTrends' course structure.
    """
    
    def __init__(self):
        self.course_content = self._load_course_content()
        self.user_progress = {}
        self.quiz_questions = self._load_quiz_questions()
        self.assignments = self._load_assignments()
    
    def _load_course_content(self) -> Dict[str, Dict]:
        """Load course content from JSON file."""
        try:
            with open('course_content.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "modules": {
                    "1": {
                        "title": "Introduction to Forex Trading",
                        "lessons": {
                            "1": "Forex Market Basics",
                            "2": "Currency Pairs and Quotes",
                            "3": "Market Participants"
                        }
                    },
                    "2": {
                        "title": "Technical Analysis",
                        "lessons": {
                            "1": "Support and Resistance",
                            "2": "Chart Patterns",
                            "3": "Technical Indicators"
                        }
                    }
                }
            }
        except json.JSONDecodeError:
            raise ValueError("Invalid course content JSON file")
    
    def _load_quiz_questions(self) -> Dict[str, List[Dict]]:
        """Load quiz questions from JSON file."""
        try:
            with open('quiz_questions.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "1": [
                    {
                        "question": "What is the base currency in the EUR/USD pair?",
                        "options": ["Euro", "US Dollar", "Yen", "Pound"],
                        "answer": 0
                    },
                    {
                        "question": "Which of these is NOT a major currency pair?",
                        "options": ["EUR/USD", "USD/JPY", "GBP/USD", "USD/ZAR"],
                        "answer": 3
                    }
                ],
                "2": [
                    {
                        "question": "What does a head and shoulders pattern typically indicate?",
                        "options": ["Market continuation", "Market reversal", "Market consolidation", "None of the above"],
                        "answer": 1
                    }
                ]
            }
        except json.JSONDecodeError:
            raise ValueError("Invalid quiz questions JSON file")
    
    def _load_assignments(self) -> Dict[str, Dict]:
        """Load assignments from JSON file."""
        try:
            with open('assignments.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "1": {
                    "title": "Currency Pair Analysis",
                    "description": "Analyze the EUR/USD pair for the last week and identify key support/resistance levels.",
                    "due_date": "2023-12-15"
                },
                "2": {
                    "title": "Technical Pattern Identification",
                    "description": "Find and document 3 different chart patterns in current market data.",
                    "due_date": "2023-12-22"
                }
            }
        except json.JSONDecodeError:
            raise ValueError("Invalid assignments JSON file")
    
    def register_user(self, user_id: str) -> None:
        """Register a new user with empty progress."""
        if user_id in self.user_progress:
            raise ValueError("User already exists")
        self.user_progress[user_id] = {
            "completed_lessons": [],
            "quiz_scores": {},
            "assignment_submissions": {},
            "last_accessed": datetime.now().isoformat()
        }
    
    def get_course_modules(self) -> Dict[str, Dict]:
        """Return all course modules."""
        return self.course_content["modules"]
    
    def get_lesson_content(self, module_id: str, lesson_id: str) -> Optional[str]:
        """Get content for a specific lesson."""
        try:
            module = self.course_content["modules"][module_id]
            lesson_title = module["lessons"][lesson_id]
            return f"Content for {lesson_title} would be displayed here."
        except KeyError:
            return None
    
    def mark_lesson_complete(self, user_id: str, module_id: str, lesson_id: str) -> bool:
        """Mark a lesson as complete for a user."""
        if user_id not in self.user_progress:
            raise ValueError("User not found")
        
        lesson_key = f"{module_id}-{lesson_id}"
        if lesson_key not in self.user_progress[user_id]["completed_lessons"]:
            self.user_progress[user_id]["completed_lessons"].append(lesson_key)
            self.user_progress[user_id]["last_accessed"] = datetime.now().isoformat()
            return True
        return False
    
    def get_quiz_questions(self, module_id: str, num_questions: int = 5) -> List[Dict]:
        """Get quiz questions for a module."""
        try:
            all_questions = self.quiz_questions[module_id]
            return random.sample(all_questions, min(num_questions, len(all_questions)))
        except KeyError:
            return []
    
    def submit_quiz_answers(self, user_id: str, module_id: str, answers: List[int]) -> Tuple[int, int]:
        """Submit quiz answers and return score."""
        if user_id not in self.user_progress:
            raise ValueError("User not found")
        
        questions = self.quiz_questions.get(module_id, [])
        if len(answers) != len(questions):
            raise ValueError("Number of answers doesn't match number of questions")
        
        score = sum(1 for i, q in enumerate(questions) if answers[i] == q["answer"])
        total = len(questions)
        
        self.user_progress[user_id]["quiz_scores"][module_id] = score
        self.user_progress[user_id]["last_accessed"] = datetime.now().isoformat()
        
        return score, total
    
    def get_assignments(self, module_id: str) -> Optional[Dict]:
        """Get assignments for a module."""
        return self.assignments.get(module_id)
    
    def submit_assignment(self, user_id: str, module_id: str, submission: str) -> bool:
        """Submit an assignment for a user."""
        if user_id not in self.user_progress:
            raise ValueError("User not found")
        if module_id not in self.assignments:
            raise ValueError("Invalid module ID")
        
        self.user_progress[user_id]["assignment_submissions"][module_id] = {
            "submission": submission,
            "submission_date": datetime.now().isoformat(),
            "graded": False
        }
        self.user_progress[user_id]["last_accessed"] = datetime.now().isoformat()
        return True
    
    def get_user_progress(self, user_id: str) -> Dict:
        """Get progress for a specific user."""
        if user_id not in self.user_progress:
            raise ValueError("User not found")
        return self.user_progress[user_id]
    
    def save_data(self) -> None:
        """Save all data to JSON files."""
        try:
            with open('course_content.json', 'w') as f:
                json.dump(self.course_content, f, indent=2)
            with open('quiz_questions.json', 'w') as f:
                json.dump(self.quiz_questions, f, indent=2)
            with open('assignments.json', 'w') as f:
                json.dump(self.assignments, f, indent=2)
            with open('user_progress.json', 'w') as f:
                json.dump(self.user_progress, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save data: {str(e)}")


# Example usage
if __name__ == "__main__":
    course = ForexTradingCourse()
    
    # Register a new user
    course.register_user("user123")
    
    # Get course modules
    modules = course.get_course_modules()
    print("Available modules:", modules)
    
    # Get lesson content
    lesson_content = course.get_lesson_content("1", "1")
    print("\nLesson content:", lesson_content)
    
    # Mark lesson complete
    course.mark_lesson_complete("user123", "1", "1")
    
    # Take a quiz
    questions = course.get_quiz_questions("1")
    print("\nQuiz questions:")
    for i, q in enumerate(questions):
        print(f"{i+1}. {q['question']}")
        for j, opt in enumerate(q['options']):
            print(f"   {j}. {opt}")
    
    # Submit quiz answers (assuming all first options are selected)
    answers = [0] * len(questions)
    score, total = course.submit_quiz_answers("user123", "1", answers)
    print(f"\nQuiz score: {score}/{total}")
    
    # Get assignments
    assignment = course.get_assignments("1")
    print("\nAssignment:", assignment)
