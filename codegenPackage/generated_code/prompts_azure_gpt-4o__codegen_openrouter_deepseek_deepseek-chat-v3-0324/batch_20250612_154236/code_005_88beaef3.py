"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Create a Python script for managing user interactions with potential matches, including unlocking real chat after avatar conversations and scheduling in-person meetings, as outlined on blur.today.
Generated: DETERMINISTIC_88beaef37e3fbcc7
Batch ID: 20250612_154236
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
from typing import Dict, List, Optional
from enum import Enum


class UserStatus(Enum):
    """Enum representing user status in the matching system."""
    NEW = "new"
    ACTIVE = "active"
    PAUSED = "paused"
    BANNED = "banned"


class MatchStatus(Enum):
    """Enum representing the status of a match between users."""
    PENDING = "pending"
    AVATAR_CHAT = "avatar_chat"
    UNLOCKED = "unlocked"
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    DECLINED = "declined"


class User:
    """Class representing a user in the matching system."""
    
    def __init__(self, user_id: str, name: str, status: UserStatus = UserStatus.NEW):
        """Initialize a User instance.
        
        Args:
            user_id: Unique identifier for the user
            name: Display name of the user
            status: Current status of the user (default: NEW)
        """
        self.user_id = user_id
        self.name = name
        self.status = status
        self.matches: Dict[str, Match] = {}  # key: match_id, value: Match object


class Match:
    """Class representing a match between two users."""
    
    def __init__(self, match_id: str, user1: User, user2: User):
        """Initialize a Match instance.
        
        Args:
            match_id: Unique identifier for the match
            user1: First user in the match
            user2: Second user in the match
        """
        self.match_id = match_id
        self.user1 = user1
        self.user2 = user2
        self.status = MatchStatus.PENDING
        self.avatar_chat_messages: List[Dict] = []
        self.real_chat_messages: List[Dict] = []
        self.scheduled_meeting: Optional[Dict] = None


class MatchManager:
    """Class managing user interactions with potential matches."""
    
    def __init__(self):
        """Initialize the MatchManager with empty storage."""
        self.users: Dict[str, User] = {}  # key: user_id, value: User object
        self.matches: Dict[str, Match] = {}  # key: match_id, value: Match object
    
    def add_user(self, user_id: str, name: str) -> User:
        """Add a new user to the system.
        
        Args:
            user_id: Unique identifier for the user
            name: Display name of the user
            
        Returns:
            The created User object
            
        Raises:
            ValueError: If user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists")
        
        user = User(user_id, name)
        self.users[user_id] = user
        return user
    
    def create_match(self, user1_id: str, user2_id: str) -> Match:
        """Create a new match between two users.
        
        Args:
            user1_id: ID of the first user
            user2_id: ID of the second user
            
        Returns:
            The created Match object
            
        Raises:
            ValueError: If either user doesn't exist or match already exists
        """
        if user1_id not in self.users or user2_id not in self.users:
            raise ValueError("One or both users do not exist")
            
        # Generate a unique match ID
        match_id = f"{user1_id}_{user2_id}_{datetime.datetime.now().timestamp()}"
        
        if match_id in self.matches:
            raise ValueError("Match already exists")
            
        user1 = self.users[user1_id]
        user2 = self.users[user2_id]
        
        match = Match(match_id, user1, user2)
        self.matches[match_id] = match
        user1.matches[match_id] = match
        user2.matches[match_id] = match
        
        return match
    
    def add_avatar_chat_message(self, match_id: str, sender_id: str, message: str) -> Dict:
        """Add a message to the avatar chat of a match.
        
        Args:
            match_id: ID of the match
            sender_id: ID of the user sending the message
            message: Content of the message
            
        Returns:
            The added message object
            
        Raises:
            ValueError: If match doesn't exist or user not in match
            RuntimeError: If match status doesn't allow avatar chat
        """
        if match_id not in self.matches:
            raise ValueError("Match does not exist")
            
        match = self.matches[match_id]
        
        if sender_id not in (match.user1.user_id, match.user2.user_id):
            raise ValueError("User not part of this match")
            
        if match.status not in (MatchStatus.PENDING, MatchStatus.AVATAR_CHAT):
            raise RuntimeError("Match status does not allow avatar chat")
            
        if match.status == MatchStatus.PENDING:
            match.status = MatchStatus.AVATAR_CHAT
            
        message_obj = {
            "sender_id": sender_id,
            "message": message,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        match.avatar_chat_messages.append(message_obj)
        return message_obj
    
    def unlock_real_chat(self, match_id: str, requesting_user_id: str) -> Match:
        """Unlock real chat between users after avatar conversation.
        
        Args:
            match_id: ID of the match
            requesting_user_id: ID of the user requesting the unlock
            
        Returns:
            The updated Match object
            
        Raises:
            ValueError: If match doesn't exist or user not in match
            RuntimeError: If match status doesn't allow unlocking
        """
        if match_id not in self.matches:
            raise ValueError("Match does not exist")
            
        match = self.matches[match_id]
        
        if requesting_user_id not in (match.user1.user_id, match.user2.user_id):
            raise ValueError("User not part of this match")
            
        if match.status != MatchStatus.AVATAR_CHAT:
            raise RuntimeError("Match status does not allow unlocking real chat")
            
        match.status = MatchStatus.UNLOCKED
        return match
    
    def add_real_chat_message(self, match_id: str, sender_id: str, message: str) -> Dict:
        """Add a message to the real chat of a match.
        
        Args:
            match_id: ID of the match
            sender_id: ID of the user sending the message
            message: Content of the message
            
        Returns:
            The added message object
            
        Raises:
            ValueError: If match doesn't exist or user not in match
            RuntimeError: If match status doesn't allow real chat
        """
        if match_id not in self.matches:
            raise ValueError("Match does not exist")
            
        match = self.matches[match_id]
        
        if sender_id not in (match.user1.user_id, match.user2.user_id):
            raise ValueError("User not part of this match")
            
        if match.status not in (MatchStatus.UNLOCKED, MatchStatus.SCHEDULED):
            raise RuntimeError("Match status does not allow real chat")
            
        message_obj = {
            "sender_id": sender_id,
            "message": message,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        match.real_chat_messages.append(message_obj)
        return message_obj
    
    def schedule_meeting(self, match_id: str, initiator_id: str, 
                         datetime_str: str, location: str) -> Dict:
        """Schedule an in-person meeting between matched users.
        
        Args:
            match_id: ID of the match
            initiator_id: ID of the user initiating the meeting
            datetime_str: ISO format datetime string for the meeting
            location: Description of the meeting location
            
        Returns:
            The scheduled meeting object
            
        Raises:
            ValueError: If match doesn't exist or user not in match
            RuntimeError: If match status doesn't allow scheduling
        """
        if match_id not in self.matches:
            raise ValueError("Match does not exist")
            
        match = self.matches[match_id]
        
        if initiator_id not in (match.user1.user_id, match.user2.user_id):
            raise ValueError("User not part of this match")
            
        if match.status != MatchStatus.UNLOCKED:
            raise RuntimeError("Match status does not allow scheduling meetings")
            
        try:
            meeting_time = datetime.datetime.fromisoformat(datetime_str)
        except ValueError as e:
            raise ValueError("Invalid datetime format") from e
            
        if meeting_time < datetime.datetime.now():
            raise ValueError("Meeting time must be in the future")
            
        meeting_obj = {
            "initiator_id": initiator_id,
            "datetime": datetime_str,
            "location": location,
            "confirmed": False,
            "confirmed_by": None
        }
        
        match.scheduled_meeting = meeting_obj
        match.status = MatchStatus.SCHEDULED
        return meeting_obj
    
    def confirm_meeting(self, match_id: str, confirming_user_id: str) -> Dict:
