"""
Generated Code Metadata:
========================
Original URL: https://sweepstake-seven.vercel.app
Prompt: "Generate code for a basic sweepstakes platform using a prediction market model."
Generated: DETERMINISTIC_3321eae3d684cf75
Batch ID: 20250622_205124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum
import uuid
import json

class SweepstakeStatus(Enum):
    CREATED = "CREATED"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    SETTLED = "SETTLED"

class Participant:
    def __init__(self, user_id: str, name: str, balance: float = 100.0):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.positions: Dict[str, float] = {}  # sweepstake_id: shares

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "balance": self.balance,
            "positions": self.positions
        }

    @classmethod
    def from_dict(cls, data: Dict):
        participant = cls(data["user_id"], data["name"], data["balance"])
        participant.positions = data.get("positions", {})
        return participant

class Outcome:
    def __init__(self, outcome_id: str, description: str):
        self.outcome_id = outcome_id
        self.description = description
        self.price: float = 0.5  # Initial price
        self.shares_issued: float = 0.0

    def to_dict(self):
        return {
            "outcome_id": self.outcome_id,
            "description": self.description,
            "price": self.price,
            "shares_issued": self.shares_issued
        }

    @classmethod
    def from_dict(cls, data: Dict):
        outcome = cls(data["outcome_id"], data["description"])
        outcome.price = data["price"]
        outcome.shares_issued = data["shares_issued"]
        return outcome

class Sweepstake:
    def __init__(self, sweepstake_id: str, title: str, description: str, outcomes: List[Outcome], 
                 creator_id: str, end_time: datetime):
        self.sweepstake_id = sweepstake_id
        self.title = title
        self.description = description
        self.outcomes = {outcome.outcome_id: outcome for outcome in outcomes}
        self.creator_id = creator_id
        self.end_time = end_time
        self.status = SweepstakeStatus.CREATED
        self.winning_outcome_id: Optional[str] = None

    def to_dict(self):
        return {
            "sweepstake_id": self.sweepstake_id,
            "title": self.title,
            "description": self.description,
            "outcomes": {k: v.to_dict() for k, v in self.outcomes.items()},
            "creator_id": self.creator_id,
            "end_time": self.end_time.isoformat(),
            "status": self.status.value,
            "winning_outcome_id": self.winning_outcome_id
        }

    @classmethod
    def from_dict(cls, data: Dict):
        outcomes = [Outcome.from_dict(outcome_data) for outcome_data in data["outcomes"].values()]
        sweepstake = cls(
            data["sweepstake_id"],
            data["title"],
            data["description"],
            outcomes,
            data["creator_id"],
            datetime.fromisoformat(data["end_time"])
        )
        sweepstake.status = SweepstakeStatus(data["status"])
        sweepstake.winning_outcome_id = data.get("winning_outcome_id")
        return sweepstake

    def open_sweepstake(self):
        if self.status != SweepstakeStatus.CREATED:
            raise ValueError("Sweepstake can only be opened from CREATED state")
        self.status = SweepstakeStatus.OPEN

    def close_sweepstake(self):
        if self.status != SweepstakeStatus.OPEN:
            raise ValueError("Sweepstake can only be closed from OPEN state")
        self.status = SweepstakeStatus.CLOSED

    def settle_sweepstake(self, winning_outcome_id: str):
        if self.status != SweepstakeStatus.CLOSED:
            raise ValueError("Sweepstake must be closed before settling")
        if winning_outcome_id not in self.outcomes:
            raise ValueError("Invalid winning outcome ID")
        self.winning_outcome_id = winning_outcome_id
        self.status = SweepstakeStatus.SETTLED

    def calculate_prices(self):
        total_shares = sum(outcome.shares_issued for outcome in self.outcomes.values())
        if total_shares == 0:
            return
        
        for outcome in self.outcomes.values():
            outcome.price = outcome.shares_issued / total_shares

class SweepstakePlatform:
    def __init__(self):
        self.sweepstakes: Dict[str, Sweepstake] = {}
        self.participants: Dict[str, Participant] = {}

    def create_sweepstake(self, title: str, description: str, outcomes: List[str], 
                          creator_id: str, duration_days: int = 7) -> str:
        if creator_id not in self.participants:
            raise ValueError("Creator not found")
        
        sweepstake_id = str(uuid.uuid4())
        outcome_objects = [Outcome(str(uuid.uuid4()), desc) for desc in outcomes]
        end_time = datetime.now() + timedelta(days=duration_days)
        
        sweepstake = Sweepstake(
            sweepstake_id=sweepstake_id,
            title=title,
            description=description,
            outcomes=outcome_objects,
            creator_id=creator_id,
            end_time=end_time
        )
        
        self.sweepstakes[sweepstake_id] = sweepstake
        return sweepstake_id

    def register_participant(self, name: str) -> str:
        user_id = str(uuid.uuid4())
        participant = Participant(user_id, name)
        self.participants[user_id] = participant
        return user_id

    def buy_shares(self, user_id: str, sweepstake_id: str, outcome_id: str, amount: float):
        if user_id not in self.participants:
            raise ValueError("Participant not found")
        if sweepstake_id not in self.sweepstakes:
            raise ValueError("Sweepstake not found")
        if self.sweepstakes[sweepstake_id].status != SweepstakeStatus.OPEN:
            raise ValueError("Sweepstake is not open for trading")
        
        participant = self.participants[user_id]
        sweepstake = self.sweepstakes[sweepstake_id]
        
        if outcome_id not in sweepstake.outcomes:
            raise ValueError("Invalid outcome ID")
        
        outcome = sweepstake.outcomes[outcome_id]
        cost = amount * outcome.price
        
        if participant.balance < cost:
            raise ValueError("Insufficient balance")
        
        participant.balance -= cost
        participant.positions[outcome_id] = participant.positions.get(outcome_id, 0) + amount
        outcome.shares_issued += amount
        
        sweepstake.calculate_prices()

    def settle_random_outcome(self, sweepstake_id: str):
        if sweepstake_id not in self.sweepstakes:
            raise ValueError("Sweepstake not found")
        
        sweepstake = self.sweepstakes[sweepstake_id]
        if sweepstake.status != SweepstakeStatus.CLOSED:
            raise ValueError("Sweepstake must be closed before settling")
        
        winning_outcome_id = random.choice(list(sweepstake.outcomes.keys()))
        sweepstake.settle_sweepstake(winning_outcome_id)
        
        # Distribute winnings
        winning_outcome = sweepstake.outcomes[winning_outcome_id]
        total_shares = winning_outcome.shares_issued
        if total_shares == 0:
            return
        
        for participant in self.participants.values():
            if outcome_shares := participant.positions.get(winning_outcome_id, 0):
                participant.balance += outcome_shares * (1 / winning_outcome.price)

    def save_state(self, filename: str):
        state = {
            "sweepstakes": {k: v.to_dict() for k, v in self.sweepstakes.items()},
            "participants": {k: v.to_dict() for k, v in self.participants.items()}
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)

    def load_state(self, filename: str):
        with open(filename, 'r') as f:
            state = json.load(f)
        
        self.sweepstakes = {
            k: Sweepstake.from_dict(v) for k, v in state["sweepstakes"].items()
        }
        self.participants = {
            k:
