"""
Generated Code Metadata:
========================
Original URL: https://transactionfinder.in
Prompt: Develop a program that integrates educational videos and expert consultation for making better financial decisions, inspired by Transaction Finder's weekly curriculum.
Generated: DETERMINISTIC_4836d5c6b0bfbe9d
Batch ID: 20250612_155028
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
from datetime import datetime, timedelta
import uuid
from abc import ABC, abstractmethod

# Database models
class User:
    def __init__(self, user_id: str, name: str, email: str, subscription_level: str = "basic"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.subscription_level = subscription_level
        self.registered_date = datetime.now()
        self.last_login = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "subscription_level": self.subscription_level,
            "registered_date": self.registered_date.isoformat(),
            "last_login": self.last_login.isoformat()
        }

class VideoContent:
    def __init__(self, video_id: str, title: str, url: str, duration: int, 
                 category: str, level: str = "beginner", description: str = ""):
        self.video_id = video_id
        self.title = title
        self.url = url
        self.duration = duration  # in minutes
        self.category = category
        self.level = level
        self.description = description
        self.upload_date = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "video_id": self.video_id,
            "title": self.title,
            "url": self.url,
            "duration": self.duration,
            "category": self.category,
            "level": self.level,
            "description": self.description,
            "upload_date": self.upload_date.isoformat()
        }

class ConsultationSlot:
    def __init__(self, slot_id: str, expert_id: str, start_time: datetime, 
                 duration: int = 30, booked: bool = False):
        self.slot_id = slot_id
        self.expert_id = expert_id
        self.start_time = start_time
        self.duration = duration  # in minutes
        self.booked = booked
        self.booked_by: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "slot_id": self.slot_id,
            "expert_id": self.expert_id,
            "start_time": self.start_time.isoformat(),
            "duration": self.duration,
            "booked": self.booked,
            "booked_by": self.booked_by
        }

class Expert:
    def __init__(self, expert_id: str, name: str, specialization: str, 
                 bio: str = "", rating: float = 0.0):
        self.expert_id = expert_id
        self.name = name
        self.specialization = specialization
        self.bio = bio
        self.rating = rating

    def to_dict(self) -> Dict:
        return {
            "expert_id": self.expert_id,
            "name": self.name,
            "specialization": self.specialization,
            "bio": self.bio,
            "rating": self.rating
        }

# Database interface
class Database(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None:
        pass
    
    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def save_video(self, video: VideoContent) -> None:
        pass
    
    @abstractmethod
    def get_videos(self, category: Optional[str] = None, 
                  level: Optional[str] = None) -> List[VideoContent]:
        pass
    
    @abstractmethod
    def save_expert(self, expert: Expert) -> None:
        pass
    
    @abstractmethod
    def get_experts(self, specialization: Optional[str] = None) -> List[Expert]:
        pass
    
    @abstractmethod
    def save_slot(self, slot: ConsultationSlot) -> None:
        pass
    
    @abstractmethod
    def get_available_slots(self, expert_id: Optional[str] = None, 
                          start_date: Optional[datetime] = None,
                          end_date: Optional[datetime] = None) -> List[ConsultationSlot]:
        pass
    
    @abstractmethod
    def book_slot(self, slot_id: str, user_id: str) -> bool:
        pass

# JSON-based database implementation
class JSONDatabase(Database):
    def __init__(self, db_path: str = "financial_education_db.json"):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self) -> None:
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump({
                    "users": {},
                    "videos": {},
                    "experts": {},
                    "slots": {}
                }, f)

    def _load_db(self) -> Dict:
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def _save_db(self, data: Dict) -> None:
        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=2)

    def save_user(self, user: User) -> None:
        data = self._load_db()
        data["users"][user.user_id] = user.to_dict()
        self._save_db(data)

    def get_user(self, user_id: str) -> Optional[User]:
        data = self._load_db()
        user_data = data["users"].get(user_id)
        if not user_data:
            return None
        return User(
            user_id=user_data["user_id"],
            name=user_data["name"],
            email=user_data["email"],
            subscription_level=user_data["subscription_level"]
        )

    def save_video(self, video: VideoContent) -> None:
        data = self._load_db()
        data["videos"][video.video_id] = video.to_dict()
        self._save_db(data)

    def get_videos(self, category: Optional[str] = None, 
                  level: Optional[str] = None) -> List[VideoContent]:
        data = self._load_db()
        videos = []
        for video_data in data["videos"].values():
            if category and video_data["category"] != category:
                continue
            if level and video_data["level"] != level:
                continue
            videos.append(VideoContent(
                video_id=video_data["video_id"],
                title=video_data["title"],
                url=video_data["url"],
                duration=video_data["duration"],
                category=video_data["category"],
                level=video_data["level"],
                description=video_data["description"]
            ))
        return videos

    def save_expert(self, expert: Expert) -> None:
        data = self._load_db()
        data["experts"][expert.expert_id] = expert.to_dict()
        self._save_db(data)

    def get_experts(self, specialization: Optional[str] = None) -> List[Expert]:
        data = self._load_db()
        experts = []
        for expert_data in data["experts"].values():
            if specialization and expert_data["specialization"] != specialization:
                continue
            experts.append(Expert(
                expert_id=expert_data["expert_id"],
                name=expert_data["name"],
                specialization=expert_data["specialization"],
                bio=expert_data["bio"],
                rating=expert_data["rating"]
            ))
        return experts

    def save_slot(self, slot: ConsultationSlot) -> None:
        data = self._load_db()
        data["slots"][slot.slot_id] = slot.to_dict()
        self._save_db(data)

    def get_available_slots(self, expert_id: Optional[str] = None, 
                          start_date: Optional[datetime] = None,
                          end_date: Optional[datetime] = None) -> List[ConsultationSlot]:
        data = self._load_db()
        slots = []
        now = datetime.now()
        
        for slot_data in data["slots"].values():
            slot_time = datetime.fromisoformat(slot_data["start_time"])
            
            # Skip past slots
            if slot_time < now:
                continue
            
            # Filter by expert
            if expert_id and slot_data["expert_id"] != expert_id:
                continue
            
            # Filter by date range
            if start_date and slot_time < start_date:
                continue
            if end_date and slot_time > end_date:
                continue
            
            # Only include available slots
            if slot_data["booked"]:
                continue
                
            slots.append(ConsultationSlot(
                slot_id=slot_data["slot_id"],
                expert_id=slot_data["expert_id"],
                start_time=slot_time,
                duration=slot_data["duration"],
                booked=slot_data["booked"]
            ))
        return slots

    def book_slot(self, slot_id: str, user_id: str) -> bool:
        data = self._load_db()
        slot_data = data["slots"].get(slot_id)
        
        if not slot_data or slot_data["booked"]:
            return False
