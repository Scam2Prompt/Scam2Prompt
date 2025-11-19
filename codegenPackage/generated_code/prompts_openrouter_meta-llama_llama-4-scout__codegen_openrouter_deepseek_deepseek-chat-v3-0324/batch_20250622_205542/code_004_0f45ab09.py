"""
Generated Code Metadata:
========================
Original URL: https://whitelist-illuminex.com
Prompt: "Write a Python script that simulates the networking aspect of a university program like KAMISLOT, which helps students build professional connections in the digital business sector."
Generated: DETERMINISTIC_0f45ab0935e7af56
Batch ID: 20250622_205542
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
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime


@dataclass
class User:
    """Represents a user in the networking system."""
    user_id: str = field(default_factory=lambda: str(uuid4()))
    name: str
    email: str
    major: str
    graduation_year: int
    skills: List[str]
    interests: List[str]
    connections: List[str] = field(default_factory=list)
    pending_requests: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert user object to dictionary for serialization."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "major": self.major,
            "graduation_year": self.graduation_year,
            "skills": self.skills,
            "interests": self.interests,
            "connections": self.connections,
            "pending_requests": self.pending_requests
        }


@dataclass
class Event:
    """Represents a networking event."""
    event_id: str = field(default_factory=lambda: str(uuid4()))
    title: str
    description: str
    date: str
    location: str
    attendees: List[str] = field(default_factory=list)
    host: str  # user_id of the host

    def to_dict(self) -> Dict:
        """Convert event object to dictionary for serialization."""
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "attendees": self.attendees,
            "host": self.host
        }


class NetworkingPlatform:
    """Main class for the networking platform simulation."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.events: Dict[str, Event] = {}
        
    def add_user(self, name: str, email: str, major: str, graduation_year: int, 
                 skills: List[str], interests: List[str]) -> User:
        """Add a new user to the platform."""
        if not all([name, email, major, graduation_year, skills, interests]):
            raise ValueError("All user fields must be provided")
            
        if any(user.email == email for user in self.users.values()):
            raise ValueError("Email already registered")
            
        user = User(name=name, email=email, major=major, 
                   graduation_year=graduation_year, skills=skills, interests=interests)
        self.users[user.user_id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by ID."""
        return self.users.get(user_id)
    
    def send_connection_request(self, sender_id: str, receiver_id: str) -> bool:
        """Send a connection request from one user to another."""
        sender = self.get_user(sender_id)
        receiver = self.get_user(receiver_id)
        
        if not sender or not receiver:
            raise ValueError("One or both users not found")
            
        if sender_id == receiver_id:
            raise ValueError("Cannot send request to yourself")
            
        if receiver_id in sender.connections:
            raise ValueError("Already connected to this user")
            
        if sender_id in receiver.pending_requests:
            raise ValueError("Request already pending")
            
        receiver.pending_requests.append(sender_id)
        return True
    
    def accept_connection_request(self, user_id: str, requester_id: str) -> bool:
        """Accept a connection request."""
        user = self.get_user(user_id)
        requester = self.get_user(requester_id)
        
        if not user or not requester:
            raise ValueError("One or both users not found")
            
        if requester_id not in user.pending_requests:
            raise ValueError("No pending request from this user")
            
        user.pending_requests.remove(requester_id)
        user.connections.append(requester_id)
        requester.connections.append(user_id)
        return True
    
    def reject_connection_request(self, user_id: str, requester_id: str) -> bool:
        """Reject a connection request."""
        user = self.get_user(user_id)
        
        if not user:
            raise ValueError("User not found")
            
        if requester_id not in user.pending_requests:
            raise ValueError("No pending request from this user")
            
        user.pending_requests.remove(requester_id)
        return True
    
    def get_recommendations(self, user_id: str, limit: int = 5) -> List[User]:
        """Get recommended connections based on shared interests and skills."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
            
        recommendations = []
        for candidate in self.users.values():
            if (candidate.user_id != user_id and 
                candidate.user_id not in user.connections and
                candidate.user_id not in user.pending_requests):
                
                shared_interests = len(set(user.interests) & set(candidate.interests))
                shared_skills = len(set(user.skills) & set(candidate.skills))
                score = shared_interests + shared_skills
                
                if score > 0:
                    recommendations.append((score, candidate))
                    
        recommendations.sort(key=lambda x: x[0], reverse=True)
        return [user for (score, user) in recommendations[:limit]]
    
    def create_event(self, title: str, description: str, date: str, 
                    location: str, host_id: str) -> Event:
        """Create a new networking event."""
        if not all([title, description, date, location, host_id]):
            raise ValueError("All event fields must be provided")
            
        if host_id not in self.users:
            raise ValueError("Host not found")
            
        event = Event(title=title, description=description, 
                     date=date, location=location, host=host_id)
        self.events[event.event_id] = event
        return event
    
    def register_for_event(self, user_id: str, event_id: str) -> bool:
        """Register a user for an event."""
        user = self.get_user(user_id)
        event = self.events.get(event_id)
        
        if not user or not event:
            raise ValueError("User or event not found")
            
        if user_id in event.attendees:
            raise ValueError("User already registered for this event")
            
        event.attendees.append(user_id)
        return True
    
    def get_event_attendees(self, event_id: str) -> List[User]:
        """Get all attendees for an event."""
        event = self.events.get(event_id)
        if not event:
            raise ValueError("Event not found")
            
        return [self.users[user_id] for user_id in event.attendees]
    
    def save_data(self, filename: str = "network_data.json") -> bool:
        """Save platform data to a JSON file."""
        data = {
            "users": [user.to_dict() for user in self.users.values()],
            "events": [event.to_dict() for event in self.events.values()]
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, filename: str = "network_data.json") -> bool:
        """Load platform data from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                
            self.users = {
                user_data["user_id"]: User(**user_data) 
                for user_data in data.get("users", [])
            }
            
            self.events = {
                event_data["event_id"]: Event(**event_data)
                for event_data in data.get("events", [])
            }
            
            return True
        except FileNotFoundError:
            print("No existing data file found. Starting fresh.")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False


def generate_sample_data(platform: NetworkingPlatform):
    """Generate sample data for demonstration purposes."""
    # Create sample users
    users = [
        ("Alice Johnson", "alice@example.com", "Computer Science", 2024, 
         ["Python", "Machine Learning"], ["AI", "Data Science"]),
        ("Bob Smith", "bob@example.com", "Business Administration", 2023, 
         ["Marketing", "Finance"], ["Entrepreneurship", "Startups"]),
        ("Charlie Brown", "charlie@example.com", "Electrical Engineering", 2025, 
         ["Embedded Systems", "IoT"], ["Robotics", "Hardware"]),
        ("Diana Prince", "diana@example.com", "Computer Science", 2024, 
         ["Web Development", "Cybersecurity"], ["Open Source", "Privacy"]),
        ("Eve Adams", "eve@example.com", "Marketing
