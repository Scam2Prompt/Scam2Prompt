"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Write Python code to create a scheduling system for organizing group eye therapy sessions, including features like customizable exercise plans and reminders, inspired by the offerings on Klar Sehen.
Generated: DETERMINISTIC_57db972354a195be
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict, Optional, Union
from enum import Enum
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytz
from abc import ABC, abstractmethod


class ExerciseType(Enum):
    """Types of eye therapy exercises."""
    PALMING = "Palming"
    FOCUS_SHIFTING = "Focus Shifting"
    EYE_ROLLING = "Eye Rolling"
    NEAR_FAR_FOCUS = "Near-Far Focus"
    BLINKING = "Blinking"


class Exercise:
    """Represents an eye therapy exercise with duration and instructions."""
    
    def __init__(self, name: ExerciseType, duration_minutes: int, instructions: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.duration_minutes = duration_minutes
        self.instructions = instructions
    
    def to_dict(self) -> Dict:
        """Convert exercise to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name.value,
            "duration_minutes": self.duration_minutes,
            "instructions": self.instructions
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Exercise':
        """Create exercise from dictionary."""
        return cls(
            name=ExerciseType(data["name"]),
            duration_minutes=data["duration_minutes"],
            instructions=data["instructions"]
        )


class ExercisePlan:
    """A collection of exercises forming a therapy plan."""
    
    def __init__(self, name: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.exercises: List[Exercise] = []
    
    def add_exercise(self, exercise: Exercise) -> None:
        """Add an exercise to the plan."""
        self.exercises.append(exercise)
    
    def remove_exercise(self, exercise_id: str) -> bool:
        """Remove an exercise by ID. Returns True if found and removed."""
        for i, exercise in enumerate(self.exercises):
            if exercise.id == exercise_id:
                self.exercises.pop(i)
                return True
        return False
    
    def total_duration(self) -> int:
        """Calculate total duration of all exercises in minutes."""
        return sum(ex.duration_minutes for ex in self.exercises)
    
    def to_dict(self) -> Dict:
        """Convert plan to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "exercises": [ex.to_dict() for ex in self.exercises]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ExercisePlan':
        """Create plan from dictionary."""
        plan = cls(name=data["name"], description=data.get("description", ""))
        for ex_data in data["exercises"]:
            plan.add_exercise(Exercise.from_dict(ex_data))
        return plan


class User:
    """Represents a user of the therapy scheduling system."""
    
    def __init__(self, name: str, email: str, timezone: str = "UTC"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.timezone = timezone
        self.plans: List[str] = []  # Stores plan IDs
    
    def add_plan(self, plan_id: str) -> None:
        """Add a plan reference to the user."""
        if plan_id not in self.plans:
            self.plans.append(plan_id)
    
    def remove_plan(self, plan_id: str) -> bool:
        """Remove a plan reference from the user. Returns True if found."""
        if plan_id in self.plans:
            self.plans.remove(plan_id)
            return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert user to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "timezone": self.timezone,
            "plans": self.plans
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create user from dictionary."""
        user = cls(
            name=data["name"],
            email=data["email"],
            timezone=data.get("timezone", "UTC")
        )
        user.id = data["id"]
        user.plans = data.get("plans", [])
        return user


class Session:
    """A scheduled therapy session for a group of users."""
    
    def __init__(self, plan_id: str, start_time: datetime.datetime, leader_id: str):
        self.id = str(uuid.uuid4())
        self.plan_id = plan_id
        self.start_time = start_time
        self.leader_id = leader_id  # User ID of session leader
        self.participant_ids: List[str] = []  # List of user IDs
    
    def add_participant(self, user_id: str) -> None:
        """Add a participant to the session."""
        if user_id not in self.participant_ids:
            self.participant_ids.append(user_id)
    
    def remove_participant(self, user_id: str) -> bool:
        """Remove a participant from the session. Returns True if found."""
        if user_id in self.participant_ids:
            self.participant_ids.remove(user_id)
            return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert session to dictionary for serialization."""
        return {
            "id": self.id,
            "plan_id": self.plan_id,
            "start_time": self.start_time.isoformat(),
            "leader_id": self.leader_id,
            "participant_ids": self.participant_ids
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Session':
        """Create session from dictionary."""
        session = cls(
            plan_id=data["plan_id"],
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
            leader_id=data["leader_id"]
        )
        session.id = data["id"]
        session.participant_ids = data.get("participant_ids", [])
        return session


class NotificationHandler(ABC):
    """Abstract base class for notification handlers."""
    
    @abstractmethod
    def send_notification(self, recipient: str, message: str, subject: str = "") -> bool:
        """Send a notification to the recipient."""
        pass


class EmailNotificationHandler(NotificationHandler):
    """Notification handler that sends emails."""
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_notification(self, recipient: str, message: str, subject: str = "") -> bool:
        """Send an email notification."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


class TherapyScheduler:
    """Main class for managing the eye therapy scheduling system."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.users: Dict[str, User] = {}
        self.plans: Dict[str, ExercisePlan] = {}
        self.sessions: Dict[str, Session] = {}
        self.notification_handler: Optional[NotificationHandler] = None
        
        os.makedirs(data_dir, exist_ok=True)
        self._load_data()
    
    def set_notification_handler(self, handler: NotificationHandler) -> None:
        """Set the notification handler for reminders."""
        self.notification_handler = handler
    
    def _load_data(self) -> None:
        """Load data from JSON files."""
        try:
            # Load users
            users_path = os.path.join(self.data_dir, "users.json")
            if os.path.exists(users_path):
                with open(users_path, "r") as f:
                    users_data = json.load(f)
                    self.users = {u["id"]: User.from_dict(u) for u in users_data}
            
            # Load plans
            plans_path = os.path.join(self.data_dir, "plans.json")
            if os.path.exists(plans_path):
                with open(plans_path, "r") as f:
                    plans_data = json.load(f)
                    self.plans = {p["id"]: Exercise
