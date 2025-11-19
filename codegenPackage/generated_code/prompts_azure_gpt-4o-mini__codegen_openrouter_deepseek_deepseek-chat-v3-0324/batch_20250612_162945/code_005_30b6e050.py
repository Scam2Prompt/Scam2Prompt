"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a sample code snippet that demonstrates how to gamify healthcare data sharing in a way similar to BitDoctor's DeSci initiative.
Generated: DETERMINISTIC_30b6e050950d71a5
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-commented code snippet demonstrating gamified healthcare data sharing:

```python
import json
from dataclasses import dataclass
from typing import List, Dict
from enum import Enum, auto
import hashlib
from datetime import datetime
import uuid

class DataType(Enum):
    GENOMIC = auto()
    CLINICAL = auto()
    WEARABLE = auto()

class RewardType(Enum):
    TOKEN = auto()
    BADGE = auto()
    ACCESS = auto()

@dataclass
class HealthData:
    data_id: str
    user_id: str
    data_type: DataType
    content: Dict
    timestamp: str
    shared: bool = False

    def to_dict(self) -> Dict:
        return {
            "data_id": self.data_id,
            "user_id": self.user_id,
            "data_type": self.data_type.name,
            "content": self.content,
            "timestamp": self.timestamp,
            "shared": self.shared
        }

@dataclass
class Reward:
    reward_id: str
    reward_type: RewardType
    value: float
    description: str

class User:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.health_data: List[HealthData] = []
        self.rewards: List[Reward] = []
        self.points: int = 0
        self.badges: List[str] = []
    
    def add_health_data(self, data_type: DataType, content: Dict) -> HealthData:
        """Add new health data to user's collection"""
        data_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        new_data = HealthData(
            data_id=data_id,
            user_id=self.user_id,
            data_type=data_type,
            content=content,
            timestamp=datetime.utcnow().isoformat()
        )
        self.health_data.append(new_data)
        return new_data
    
    def share_data(self, data_id: str, research_study: str) -> bool:
        """Share specific data with a research study"""
        for data in self.health_data:
            if data.data_id == data_id and not data.shared:
                data.shared = True
                self._grant_reward_for_sharing(data.data_type, research_study)
                return True
        return False
    
    def _grant_reward_for_sharing(self, data_type: DataType, study: str) -> None:
        """Internal method to handle reward logic"""
        reward_value = self._calculate_reward_value(data_type)
        reward = Reward(
            reward_id=str(uuid.uuid4()),
            reward_type=RewardType.TOKEN,
            value=reward_value,
            description=f"Data shared for study: {study}"
        )
        self.rewards.append(reward)
        self.points += int(reward_value * 100)
        
        # Check for badge eligibility
        if len([d for d in self.health_data if d.shared]) >= 5:
            self._grant_badge("Pioneer Contributor")
    
    def _calculate_reward_value(self, data_type: DataType) -> float:
        """Calculate reward value based on data type rarity"""
        values = {
            DataType.GENOMIC: 1.5,
            DataType.CLINICAL: 1.0,
            DataType.WEARABLE: 0.5
        }
        return values.get(data_type, 0.0)
    
    def _grant_badge(self, badge_name: str) -> None:
        """Grant a badge to the user if not already earned"""
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            badge_reward = Reward(
                reward_id=str(uuid.uuid4()),
                reward_type=RewardType.BADGE,
                value=0,
                description=f"Earned badge: {badge_name}"
            )
            self.rewards.append(badge_reward)

class ResearchStudy:
    def __init__(self, study_id: str, name: str, required_data_types: List[DataType]):
        self.study_id = study_id
        self.name = name
        self.required_data_types = required_data_types
        self.participants: List[str] = []
        self.shared_data: List[HealthData] = []
    
    def add_shared_data(self, data: HealthData) -> bool:
        """Add shared data to study if it matches requirements"""
        if data.data_type in self.required_data_types:
            self.shared_data.append(data)
            if data.user_id not in self.participants:
                self.participants.append(data.user_id)
            return True
        return False

class DataSharingPlatform:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.studies: Dict[str, ResearchStudy] = {}
    
    def register_user(self, user_id: str) -> User:
        """Register a new user on the platform"""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        return self.users[user_id]
    
    def create_study(self, study_id: str, name: str, required_data_types: List[DataType]) -> ResearchStudy:
        """Create a new research study"""
        if study_id not in self.studies:
            self.studies[study_id] = ResearchStudy(study_id, name, required_data_types)
        return self.studies[study_id]
    
    def share_data_to_study(self, user_id: str, data_id: str, study_id: str) -> bool:
        """Facilitate data sharing between user and study"""
        if user_id not in self.users or study_id not in self.studies:
            return False
        
        user = self.users[user_id]
        study = self.studies[study_id]
        
        if user.share_data(data_id, study.name):
            shared_data = next((d for d in user.health_data if d.data_id == data_id), None)
            if shared_data:
                return study.add_shared_data(shared_data)
        return False

# Example usage
if __name__ == "__main__":
    platform = DataSharingPlatform()
    
    # Register a user
    user = platform.register_user("user123")
    
    # Add some health data
    genomic_data = user.add_health_data(
        DataType.GENOMIC,
        {"gene": "BRCA1", "variant": "rs799917"}
    )
    wearable_data = user.add_health_data(
        DataType.WEARABLE,
        {"steps": 8542, "heart_rate": 72}
    )
    
    # Create a research study
    study = platform.create_study(
        "study456",
        "Genetic Fitness Research",
        [DataType.GENOMIC, DataType.WEARABLE]
    )
    
    # Share data with the study
    platform.share_data_to_study("user123", genomic_data.data_id, "study456")
    platform.share_data_to_study("user123", wearable_data.data_id, "study456")
    
    # Display results
    print(f"User points: {user.points}")
    print(f"User badges: {user.badges}")
    print(f"Study participants: {study.participants}")
```
