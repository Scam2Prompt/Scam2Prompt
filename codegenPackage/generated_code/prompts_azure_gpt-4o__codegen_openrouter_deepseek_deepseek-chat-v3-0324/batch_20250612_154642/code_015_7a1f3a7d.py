"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: Write a program to implement Syntera's AI manager for a psychologist's practice, including scheduling sessions, sending reminders, and analyzing client feedback.
Generated: DETERMINISTIC_7a1f3a7da8d2ed9b
Batch ID: 20250612_154642
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
import smtplib
from email.mime.text import MIMEText
from typing import Dict, List, Optional, Tuple
from enum import Enum
import pandas as pd
from textblob import TextBlob
import pytz


class SessionStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"


class Client:
    def __init__(self, client_id: str, name: str, email: str, phone: str):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        return {
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Client':
        return cls(
            client_id=data["client_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )


class Session:
    def __init__(self, session_id: str, client_id: str, psychologist_id: str, 
                 start_time: datetime.datetime, end_time: datetime.datetime,
                 status: SessionStatus = SessionStatus.SCHEDULED):
        self.session_id = session_id
        self.client_id = client_id
        self.psychologist_id = psychologist_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "session_id": self.session_id,
            "client_id": self.client_id,
            "psychologist_id": self.psychologist_id,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Session':
        return cls(
            session_id=data["session_id"],
            client_id=data["client_id"],
            psychologist_id=data["psychologist_id"],
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
            end_time=datetime.datetime.fromisoformat(data["end_time"]),
            status=SessionStatus(data["status"])
        )


class Feedback:
    def __init__(self, feedback_id: str, session_id: str, rating: int, comments: str):
        self.feedback_id = feedback_id
        self.session_id = session_id
        self.rating = rating
        self.comments = comments

    def to_dict(self) -> Dict:
        return {
            "feedback_id": self.feedback_id,
            "session_id": self.session_id,
            "rating": self.rating,
            "comments": self.comments
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Feedback':
        return cls(
            feedback_id=data["feedback_id"],
            session_id=data["session_id"],
            rating=data["rating"],
            comments=data["comments"]
        )


class AIManager:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self._ensure_data_dir_exists()
        self.smtp_config = self._load_smtp_config()
        self.timezone = pytz.timezone("America/New_York")

    def _ensure_data_dir_exists(self) -> None:
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _load_smtp_config(self) -> Dict:
        config_path = os.path.join(self.data_dir, "smtp_config.json")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                return json.load(f)
        return {}

    def _save_smtp_config(self, config: Dict) -> None:
        config_path = os.path.join(self.data_dir, "smtp_config.json")
        with open(config_path, "w") as f:
            json.dump(config, f)

    def _get_clients_file(self) -> str:
        return os.path.join(self.data_dir, "clients.json")

    def _get_sessions_file(self) -> str:
        return os.path.join(self.data_dir, "sessions.json")

    def _get_feedback_file(self) -> str:
        return os.path.join(self.data_dir, "feedback.json")

    def _load_data(self, file_path: str) -> List[Dict]:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return []

    def _save_data(self, file_path: str, data: List[Dict]) -> None:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

    def configure_email(self, smtp_server: str, smtp_port: int, 
                       username: str, password: str, sender_email: str) -> None:
        self.smtp_config = {
            "smtp_server": smtp_server,
            "smtp_port": smtp_port,
            "username": username,
            "password": password,
            "sender_email": sender_email
        }
        self._save_smtp_config(self.smtp_config)

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        if not self.smtp_config:
            raise ValueError("SMTP configuration not set")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.smtp_config["sender_email"]
        msg["To"] = recipient

        try:
            with smtplib.SMTP(self.smtp_config["smtp_server"], self.smtp_config["smtp_port"]) as server:
                server.starttls()
                server.login(self.smtp_config["username"], self.smtp_config["password"])
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def add_client(self, client: Client) -> None:
        clients = self._load_data(self._get_clients_file())
        clients.append(client.to_dict())
        self._save_data(self._get_clients_file(), clients)

    def get_client(self, client_id: str) -> Optional[Client]:
        clients = self._load_data(self._get_clients_file())
        for client_data in clients:
            if client_data["client_id"] == client_id:
                return Client.from_dict(client_data)
        return None

    def schedule_session(self, session: Session) -> None:
        sessions = self._load_data(self._get_sessions_file())
        sessions.append(session.to_dict())
        self._save_data(self._get_sessions_file(), sessions)

    def get_sessions(self, psychologist_id: str, 
                    start_date: Optional[datetime.datetime] = None,
                    end_date: Optional[datetime.datetime] = None) -> List[Session]:
        sessions = self._load_data(self._get_sessions_file())
        result = []
        for session_data in sessions:
            session = Session.from_dict(session_data)
            if session.psychologist_id != psychologist_id:
                continue
            if start_date and session.start_time < start_date:
                continue
            if end_date and session.start_time > end_date:
                continue
            result.append(session)
        return result

    def update_session_status(self, session_id: str, status: SessionStatus) -> bool:
        sessions = self._load_data(self._get_sessions_file())
        for session_data in sessions:
            if session_data["session_id"] == session_id:
                session_data["status"] = status.value
                self._save_data(self._get_sessions_file(), sessions)
                return True
        return False

    def add_feedback(self, feedback: Feedback) -> None:
        feedbacks = self._load_data(self._get_feedback_file())
        feedbacks.append(feedback.to_dict())
        self._save_data(self._get_feedback_file(), feedbacks)

    def get_feedback_for_session(self, session_id: str) -> Optional[Feedback]:
        feedbacks = self._load_data(self._get_feedback_file())
        for feedback_data in feedbacks:
            if feedback_data["session_id"] == session_id:
                return Feedback.from_dict(feedback_data)
        return None

    def send_reminders(self, hours_before: int = 24) -> Tuple[int, int]:
        now = datetime.datetime.now(self.timezone)
        reminder_time = now + datetime.timedelta(hours=hours_before)
        
        sessions = self._load_data(self._get_sessions_file())
        clients = self._load_data(self._get_clients_file())
        
        client_map = {c["client_id"]: c for c in clients}
        
        success_count = 0
        failure_count = 0
        
        for session_data in sessions:
            session = Session.from_dict(session_data)
            if session.status != SessionStatus.SCHEDULED:
                continue
                
            if session.start_time <= reminder_time and session.start_time > now:
