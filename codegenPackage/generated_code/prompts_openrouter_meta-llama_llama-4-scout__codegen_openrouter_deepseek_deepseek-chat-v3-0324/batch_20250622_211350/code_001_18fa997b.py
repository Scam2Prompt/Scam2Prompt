"""
Generated Code Metadata:
========================
Original URL: https://app-orbler.pages.dev
Prompt: "Describe the features of a dynamic Web3 marketing platform that bridges Web2 audiences, offering missions, staking, and community-driven growth strategies."
Generated: DETERMINISTIC_18fa997b32e79585
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# web3_marketing_platform.py
"""
A dynamic Web3 marketing platform that bridges Web2 audiences with Web3 features.
Features include missions, staking, and community-driven growth strategies.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import hashlib
from datetime import datetime
from enum import Enum, auto

class MissionStatus(Enum):
    """Enum representing the status of a mission."""
    ACTIVE = auto()
    COMPLETED = auto()
    EXPIRED = auto()

class StakeType(Enum):
    """Enum representing the type of staking."""
    LIQUIDITY = auto()
    TOKEN = auto()
    NFT = auto()

@dataclass
class User:
    """Represents a user in the platform."""
    id: str
    wallet_address: str
    email: Optional[str] = None
    web2_id: Optional[str] = None  # For Web2 audience bridging

@dataclass
class Mission:
    """Represents a mission that users can complete."""
    id: str
    title: str
    description: str
    reward: float  # In platform tokens
    expiry_date: datetime
    status: MissionStatus = MissionStatus.ACTIVE
    participants: List[str] = None  # List of user IDs

    def __post_init__(self):
        if self.participants is None:
            self.participants = []

@dataclass
class Stake:
    """Represents a staking position."""
    id: str
    user_id: str
    amount: float
    stake_type: StakeType
    start_date: datetime
    end_date: datetime
    apy: float  # Annual Percentage Yield

class Web3MarketingPlatform:
    """Core class for the Web3 marketing platform."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.missions: Dict[str, Mission] = {}
        self.stakes: Dict[str, Stake] = {}
        self.community_proposals: List[Dict] = []

    def register_user(self, wallet_address: str, email: str = None, web2_id: str = None) -> User:
        """Register a new user with optional Web2 bridging."""
        if not wallet_address:
            raise ValueError("Wallet address is required")
        
        user_id = hashlib.sha256(wallet_address.encode()).hexdigest()
        user = User(id=user_id, wallet_address=wallet_address, email=email, web2_id=web2_id)
        self.users[user_id] = user
        return user

    def create_mission(self, title: str, description: str, reward: float, expiry_date: datetime) -> Mission:
        """Create a new mission for users to complete."""
        if not title or not description:
            raise ValueError("Title and description are required")
        if reward <= 0:
            raise ValueError("Reward must be positive")
        
        mission_id = hashlib.sha256(f"{title}{datetime.now().isoformat()}".encode()).hexdigest()
        mission = Mission(
            id=mission_id,
            title=title,
            description=description,
            reward=reward,
            expiry_date=expiry_date
        )
        self.missions[mission_id] = mission
        return mission

    def complete_mission(self, user_id: str, mission_id: str) -> bool:
        """Mark a mission as completed by a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if mission_id not in self.missions:
            raise ValueError("Mission not found")
        
        mission = self.missions[mission_id]
        if mission.status != MissionStatus.ACTIVE:
            return False
        
        if user_id not in mission.participants:
            mission.participants.append(user_id)
        
        # In a real implementation, distribute rewards here
        return True

    def create_stake(self, user_id: str, amount: float, stake_type: StakeType, duration_days: int, apy: float) -> Stake:
        """Create a new staking position."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        
        stake_id = hashlib.sha256(f"{user_id}{datetime.now().isoformat()}".encode()).hexdigest()
        start_date = datetime.now()
        end_date = datetime.fromtimestamp(start_date.timestamp() + duration_days * 86400)
        
        stake = Stake(
            id=stake_id,
            user_id=user_id,
            amount=amount,
            stake_type=stake_type,
            start_date=start_date,
            end_date=end_date,
            apy=apy
        )
        self.stakes[stake_id] = stake
        return stake

    def create_proposal(self, creator_id: str, title: str, description: str) -> Dict:
        """Create a new community growth proposal."""
        if creator_id not in self.users:
            raise ValueError("User not found")
        if not title or not description:
            raise ValueError("Title and description are required")
        
        proposal = {
            "id": hashlib.sha256(f"{title}{datetime.now().isoformat()}".encode()).hexdigest(),
            "creator_id": creator_id,
            "title": title,
            "description": description,
            "created_at": datetime.now(),
            "votes": 0,
            "voters": []
        }
        self.community_proposals.append(proposal)
        return proposal

    def vote_proposal(self, user_id: str, proposal_id: str) -> bool:
        """Vote on a community proposal."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        proposal = next((p for p in self.community_proposals if p["id"] == proposal_id), None)
        if not proposal:
            raise ValueError("Proposal not found")
        
        if user_id in proposal["voters"]:
            return False
        
        proposal["voters"].append(user_id)
        proposal["votes"] += 1
        return True

    def get_user_missions(self, user_id: str) -> List[Mission]:
        """Get all missions a user is participating in."""
        return [m for m in self.missions.values() if user_id in m.participants]

    def to_json(self) -> str:
        """Serialize platform data to JSON."""
        data = {
            "users": [user.__dict__ for user in self.users.values()],
            "missions": [mission.__dict__ for mission in self.missions.values()],
            "stakes": [stake.__dict__ for stake in self.stakes.values()],
            "community_proposals": self.community_proposals
        }
        return json.dumps(data, default=str)

# Example usage
if __name__ == "__main__":
    platform = Web3MarketingPlatform()
    
    # Register users
    user1 = platform.register_user("0x123...", "user1@example.com", "web2_user_123")
    user2 = platform.register_user("0x456...")
    
    # Create and complete mission
    mission = platform.create_mission(
        "Social Media Share",
        "Share our post on Twitter",
        10.0,
        datetime.now()
    )
    platform.complete_mission(user1.id, mission.id)
    
    # Create stake
    stake = platform.create_stake(
        user1.id,
        100.0,
        StakeType.TOKEN,
        30,
        0.12
    )
    
    # Create and vote on proposal
    proposal = platform.create_proposal(
        user2.id,
        "New Marketing Campaign",
        "Let's run a campaign on TikTok"
    )
    platform.vote_proposal(user1.id, proposal["id"])
    
    print(platform.to_json())
```
