"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Write a Python script to create an interactive learning platform that utilizes gamification and live worksheets, like the ones used at Heart of Jesus College."
Generated: DETERMINISTIC_674a9050b2dc6328
Batch ID: 20250622_210650
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
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class User:
    """Represents a user of the learning platform."""
    
    def __init__(self, user_id: int, username: str, role: str = "student"):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.points = 0
        self.badges: List[str] = []
        self.completed_worksheets: List[int] = []
        self.last_active = datetime.now()
    
    def add_points(self, points: int) -> None:
        """Add points to user's total."""
        self.points += points
    
    def add_badge(self, badge_name: str) -> None:
        """Add a badge to user's collection if not already earned."""
        if badge_name not in self.badges:
            self.badges.append(badge_name)
    
    def complete_worksheet(self, worksheet_id: int) -> None:
        """Mark a worksheet as completed."""
        if worksheet_id not in self.completed_worksheets:
            self.completed_worksheets.append(worksheet_id)
    
    def to_dict(self) -> Dict:
        """Convert user object to dictionary for storage."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "role": self.role,
            "points": self.points,
            "badges": self.badges,
            "completed_worksheets": self.completed_worksheets,
            "last_active": self.last_active.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create user object from dictionary."""
        user = cls(data["user_id"], data["username"], data.get("role", "student"))
        user.points = data["points"]
        user.badges = data["badges"]
        user.completed_worksheets = data["completed_worksheets"]
        user.last_active = datetime.fromisoformat(data["last_active"])
        return user

class Worksheet:
    """Represents a learning worksheet with questions."""
    
    def __init__(self, worksheet_id: int, title: str, questions: List[Dict], difficulty: str = "medium"):
        self.worksheet_id = worksheet_id
        self.title = title
        self.questions = questions
        self.difficulty = difficulty
        self.points_reward = self._calculate_points_reward()
    
    def _calculate_points_reward(self) -> int:
        """Calculate points reward based on difficulty."""
        difficulty_points = {
            "easy": 10,
            "medium": 20,
            "hard": 30
        }
        return difficulty_points.get(self.difficulty, 10) * len(self.questions)
    
    def to_dict(self) -> Dict:
        """Convert worksheet object to dictionary for storage."""
        return {
            "worksheet_id": self.worksheet_id,
            "title": self.title,
            "questions": self.questions,
            "difficulty": self.difficulty,
            "points_reward": self.points_reward
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Worksheet':
        """Create worksheet object from dictionary."""
        return cls(
            data["worksheet_id"],
            data["title"],
            data["questions"],
            data.get("difficulty", "medium")
        )

class LearningPlatform:
    """Main class for the interactive learning platform."""
    
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.worksheets: Dict[int, Worksheet] = {}
        self.next_user_id = 1
        self.next_worksheet_id = 1
        self._load_data()
    
    def _load_data(self) -> None:
        """Load user and worksheet data from files."""
        try:
            with open("users.json", "r") as f:
                users_data = json.load(f)
                for user_data in users_data:
                    user = User.from_dict(user_data)
                    self.users[user.user_id] = user
                    if user.user_id >= self.next_user_id:
                        self.next_user_id = user.user_id + 1
        except FileNotFoundError:
            pass
        
        try:
            with open("worksheets.json", "r") as f:
                worksheets_data = json.load(f)
                for worksheet_data in worksheets_data:
                    worksheet = Worksheet.from_dict(worksheet_data)
                    self.worksheets[worksheet.worksheet_id] = worksheet
                    if worksheet.worksheet_id >= self.next_worksheet_id:
                        self.next_worksheet_id = worksheet.worksheet_id + 1
        except FileNotFoundError:
            pass
    
    def _save_data(self) -> None:
        """Save user and worksheet data to files."""
        with open("users.json", "w") as f:
            json.dump([user.to_dict() for user in self.users.values()], f)
        
        with open("worksheets.json", "w") as f:
            json.dump([worksheet.to_dict() for worksheet in self.worksheets.values()], f)
    
    def register_user(self, username: str, role: str = "student") -> User:
        """Register a new user."""
        user = User(self.next_user_id, username, role)
        self.users[user.user_id] = user
        self.next_user_id += 1
        self._save_data()
        return user
    
    def create_worksheet(self, title: str, questions: List[Dict], difficulty: str = "medium") -> Worksheet:
        """Create a new worksheet."""
        worksheet = Worksheet(self.next_worksheet_id, title, questions, difficulty)
        self.worksheets[worksheet.worksheet_id] = worksheet
        self.next_worksheet_id += 1
        self._save_data()
        return worksheet
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by ID."""
        return self.users.get(user_id)
    
    def get_worksheet(self, worksheet_id: int) -> Optional[Worksheet]:
        """Retrieve a worksheet by ID."""
        return self.worksheets.get(worksheet_id)
    
    def complete_worksheet(self, user_id: int, worksheet_id: int) -> Tuple[bool, str]:
        """Mark a worksheet as completed for a user and award points."""
        user = self.get_user(user_id)
        worksheet = self.get_worksheet(worksheet_id)
        
        if not user:
            return False, "User not found"
        if not worksheet:
            return False, "Worksheet not found"
        
        user.complete_worksheet(worksheet_id)
        user.add_points(worksheet.points_reward)
        
        # Check for badge eligibility
        completed_count = len(user.completed_worksheets)
        if completed_count >= 5 and "Worksheet Master" not in user.badges:
            user.add_badge("Worksheet Master")
        
        self._save_data()
        return True, f"Completed worksheet! Earned {worksheet.points_reward} points."
    
    def get_leaderboard(self) -> List[Dict]:
        """Get the top users by points."""
        sorted_users = sorted(
            self.users.values(),
            key=lambda u: u.points,
            reverse=True
        )
        return [
            {
                "username": user.username,
                "points": user.points,
                "badges": len(user.badges)
            }
            for user in sorted_users[:10]
        ]
    
    def get_random_worksheet(self) -> Optional[Worksheet]:
        """Get a random worksheet."""
        if not self.worksheets:
            return None
        return random.choice(list(self.worksheets.values()))

def interactive_cli():
    """Command-line interface for the learning platform."""
    platform = LearningPlatform()
    
    print("Welcome to Heart of Jesus College Learning Platform!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter username: ")
        user = platform.register_user(username)
        print(f"Registered successfully! Your user ID is {user.user_id}")
    elif choice == "2":
        user_id = int(input("Enter your user ID: "))
        user = platform.get_user(user_id)
        if not user:
            print("User not found.")
            return
        
        print(f"Welcome back, {user.username}!")
        print(f"Points: {user.points}")
        print(f"Badges: {', '.join(user.badges) if user.badges else 'None'}")
        
        while True:
            print("\nMenu:")
            print("1. View worksheets")
            print("2. Complete worksheet")
            print("3. View leaderboard")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                print("\nAvailable Worksheets:")
                for worksheet in platform.worksheets.values():
                    print(f"ID: {worksheet.worksheet_id}, Title: {worksheet.title}, Difficulty: {worksheet.difficulty}")
            
            elif choice == "2":
                worksheet_id = int(input("Enter worksheet ID to complete: "))
                success, message = platform.complete_
