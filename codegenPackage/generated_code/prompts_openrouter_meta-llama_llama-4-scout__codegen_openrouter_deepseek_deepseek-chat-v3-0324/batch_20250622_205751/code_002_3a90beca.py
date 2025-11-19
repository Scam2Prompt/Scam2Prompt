"""
Generated Code Metadata:
========================
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Generate code for a tokenomics system that includes features like Trump debates and MAGA rallies.
Generated: DETERMINISTIC_3a90beca65c1bdf5
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics.py
# Tokenomics system with Trump debates and MAGA rallies features

import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum
import hashlib
import json

class TokenType(Enum):
    """Enum representing different token types in the system"""
    PRIMARY = "PRIMARY"
    DEBATE = "DEBATE"
    RALLY = "RALLY"

class User:
    """Class representing a user in the tokenomics system"""
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.token_balance: Dict[TokenType, int] = {
            TokenType.PRIMARY: 0,
            TokenType.DEBATE: 0,
            TokenType.RALLY: 0
        }
        self.vote_power = 1.0
        self.last_rally_attendance: Optional[datetime] = None

    def add_tokens(self, token_type: TokenType, amount: int) -> None:
        """Add tokens to user's balance"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.token_balance[token_type] += amount

    def spend_tokens(self, token_type: TokenType, amount: int) -> None:
        """Spend tokens from user's balance"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.token_balance[token_type] < amount:
            raise ValueError("Insufficient token balance")
        self.token_balance[token_type] -= amount

    def __str__(self) -> str:
        return f"User {self.name} (ID: {self.user_id})"

class DebateTopic:
    """Class representing a debate topic"""
    def __init__(self, topic_id: str, title: str, description: str):
        self.topic_id = topic_id
        self.title = title
        self.description = description
        self.votes: Dict[str, int] = {}  # user_id: vote_amount
        self.is_active = True
        self.created_at = datetime.now()

    def add_vote(self, user: User, amount: int) -> None:
        """Add vote to the debate topic"""
        if not self.is_active:
            raise ValueError("Debate is closed for voting")
        if user.user_id in self.votes:
            self.votes[user.user_id] += amount
        else:
            self.votes[user.user_id] = amount

    def close_debate(self) -> Tuple[str, int]:
        """Close debate and return winning side and total votes"""
        self.is_active = False
        total_votes = sum(self.votes.values())
        winning_side = "Affirmative" if total_votes > 0 else "Negative"
        return winning_side, abs(total_votes)

    def __str__(self) -> str:
        return f"Debate: {self.title} ({'Active' if self.is_active else 'Closed'})"

class MAGARally:
    """Class representing a MAGA rally event"""
    def __init__(self, rally_id: str, location: str, capacity: int):
        self.rally_id = rally_id
        self.location = location
        self.capacity = capacity
        self.attendees: List[str] = []  # List of user IDs
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=2)
        self.token_reward = 10  # Tokens awarded per attendance

    def attend_rally(self, user: User) -> None:
        """Register user attendance at rally"""
        if datetime.now() > self.end_time:
            raise ValueError("Rally has ended")
        if len(self.attendees) >= self.capacity:
            raise ValueError("Rally at full capacity")
        if user.user_id in self.attendees:
            raise ValueError("User already attending this rally")
        
        self.attendees.append(user.user_id)
        user.add_tokens(TokenType.RALLY, self.token_reward)
        user.last_rally_attendance = datetime.now()

    def __str__(self) -> str:
        return f"MAGA Rally at {self.location} ({len(self.attendees)}/{self.capacity} attendees)"

class TokenomicsSystem:
    """Main tokenomics system class"""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.debates: Dict[str, DebateTopic] = {}
        self.rallies: Dict[str, MAGARally] = {}
        self.token_supply: Dict[TokenType, int] = {
            TokenType.PRIMARY: 1_000_000,
            TokenType.DEBATE: 100_000,
            TokenType.RALLY: 50_000
        }

    def register_user(self, name: str) -> User:
        """Register a new user in the system"""
        user_id = hashlib.sha256(name.encode()).hexdigest()[:8]
        if user_id in self.users:
            raise ValueError("User already exists")
        
        new_user = User(user_id, name)
        self.users[user_id] = new_user
        return new_user

    def create_debate(self, title: str, description: str) -> DebateTopic:
        """Create a new debate topic"""
        topic_id = hashlib.sha256(title.encode()).hexdigest()[:8]
        if topic_id in self.debates:
            raise ValueError("Debate topic already exists")
        
        new_debate = DebateTopic(topic_id, title, description)
        self.debates[topic_id] = new_debate
        return new_debate

    def create_rally(self, location: str, capacity: int) -> MAGARally:
        """Create a new MAGA rally"""
        rally_id = hashlib.sha256(location.encode()).hexdigest()[:8]
        if rally_id in self.rallies:
            raise ValueError("Rally already exists at this location")
        
        new_rally = MAGARally(rally_id, location, capacity)
        self.rallies[rally_id] = new_rally
        return new_rally

    def distribute_tokens(self, user: User, token_type: TokenType, amount: int) -> None:
        """Distribute tokens to a user from the system supply"""
        if token_type not in self.token_supply:
            raise ValueError("Invalid token type")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.token_supply[token_type] < amount:
            raise ValueError("Insufficient token supply")
        
        user.add_tokens(token_type, amount)
        self.token_supply[token_type] -= amount

    def vote_in_debate(self, user: User, debate: DebateTopic, amount: int, side: str) -> None:
        """Vote in a debate using DEBATE tokens"""
        if user.token_balance[TokenType.DEBATE] < amount:
            raise ValueError("Insufficient DEBATE tokens")
        
        vote_amount = amount if side.lower() == "affirmative" else -amount
        debate.add_vote(user, vote_amount)
        user.spend_tokens(TokenType.DEBATE, amount)

    def get_user_stats(self, user: User) -> Dict:
        """Get statistics for a user"""
        return {
            "user_id": user.user_id,
            "name": user.name,
            "token_balances": {t.name: user.token_balance[t] for t in TokenType},
            "vote_power": user.vote_power,
            "last_rally_attendance": user.last_rally_attendance.isoformat() if user.last_rally_attendance else None
        }

    def get_system_stats(self) -> Dict:
        """Get statistics for the entire system"""
        return {
            "total_users": len(self.users),
            "active_debates": sum(1 for d in self.debates.values() if d.is_active),
            "upcoming_rallies": sum(1 for r in self.rallies.values() if datetime.now() < r.end_time),
            "token_supply": {t.name: self.token_supply[t] for t in TokenType}
        }

    def save_state(self, filename: str) -> None:
        """Save system state to file"""
        state = {
            "users": {uid: self.get_user_stats(u) for uid, u in self.users.items()},
            "debates": {
                did: {
                    "topic_id": d.topic_id,
                    "title": d.title,
                    "description": d.description,
                    "votes": d.votes,
                    "is_active": d.is_active,
                    "created_at": d.created_at.isoformat()
                } for did, d in self.debates.items()
            },
            "rallies": {
                rid: {
                    "rally_id": r.rally_id,
                    "location": r.location,
                    "capacity": r.capacity,
                    "attendees": r.attendees,
                    "start_time": r.start_time.isoformat(),
                    "end_time": r
