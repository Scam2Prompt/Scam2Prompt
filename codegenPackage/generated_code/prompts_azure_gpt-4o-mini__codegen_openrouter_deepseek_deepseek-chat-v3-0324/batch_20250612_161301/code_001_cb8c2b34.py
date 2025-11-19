"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: How can I implement a system to track and manage user bonuses and VIP rewards in a gaming application like Betpanda?
Generated: DETERMINISTIC_cb8c2b3499103d19
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
import json
from abc import ABC, abstractmethod

# Database simulation
class Database:
    def __init__(self):
        self.users = {}
        self.bonuses = {}
        self.vip_tiers = {}
        self.transactions = {}
    
    def save(self, collection: str, key: str, value: dict):
        if collection == "users":
            self.users[key] = value
        elif collection == "bonuses":
            self.bonuses[key] = value
        elif collection == "vip_tiers":
            self.vip_tiers[key] = value
        elif collection == "transactions":
            self.transactions[key] = value
    
    def get(self, collection: str, key: str) -> Optional[dict]:
        if collection == "users":
            return self.users.get(key)
        elif collection == "bonuses":
            return self.bonuses.get(key)
        elif collection == "vip_tiers":
            return self.vip_tiers.get(key)
        elif collection == "transactions":
            return self.transactions.get(key)
        return None
    
    def query(self, collection: str, query: dict) -> List[dict]:
        results = []
        if collection == "users":
            data = self.users.values()
        elif collection == "bonuses":
            data = self.bonuses.values()
        elif collection == "vip_tiers":
            data = self.vip_tiers.values()
        elif collection == "transactions":
            data = self.transactions.values()
        else:
            return results
        
        for item in data:
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                results.append(item)
        return results

# Enums
class BonusStatus(Enum):
    ACTIVE = "active"
    USED = "used"
    EXPIRED = "expired"

class BonusType(Enum):
    SIGNUP = "signup"
    DEPOSIT = "deposit"
    LOYALTY = "loyalty"
    VIP = "vip"

class VIPStatus(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"
    DIAMOND = "diamond"

# Data Models
@dataclass
class User:
    user_id: str
    username: str
    email: str
    balance: float
    vip_status: VIPStatus
    points: int
    created_at: datetime.datetime
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "balance": self.balance,
            "vip_status": self.vip_status.value,
            "points": self.points,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"],
            balance=data["balance"],
            vip_status=VIPStatus(data["vip_status"]),
            points=data["points"],
            created_at=datetime.datetime.fromisoformat(data["created_at"])
        )

@dataclass
class Bonus:
    bonus_id: str
    user_id: str
    bonus_type: BonusType
    amount: float
    status: BonusStatus
    created_at: datetime.datetime
    expires_at: datetime.datetime
    wagering_requirement: float
    
    def to_dict(self):
        return {
            "bonus_id": self.bonus_id,
            "user_id": self.user_id,
            "bonus_type": self.bonus_type.value,
            "amount": self.amount,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat(),
            "wagering_requirement": self.wagering_requirement
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            bonus_id=data["bonus_id"],
            user_id=data["user_id"],
            bonus_type=BonusType(data["bonus_type"]),
            amount=data["amount"],
            status=BonusStatus(data["status"]),
            created_at=datetime.datetime.fromisoformat(data["created_at"]),
            expires_at=datetime.datetime.fromisoformat(data["expires_at"]),
            wagering_requirement=data["wagering_requirement"]
        )

@dataclass
class VIPTier:
    tier_id: str
    name: VIPStatus
    min_points: int
    deposit_multiplier: float
    withdrawal_limit: float
    cashback_percentage: float
    
    def to_dict(self):
        return {
            "tier_id": self.tier_id,
            "name": self.name.value,
            "min_points": self.min_points,
            "deposit_multiplier": self.deposit_multiplier,
            "withdrawal_limit": self.withdrawal_limit,
            "cashback_percentage": self.cashback_percentage
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            tier_id=data["tier_id"],
            name=VIPStatus(data["name"]),
            min_points=data["min_points"],
            deposit_multiplier=data["deposit_multiplier"],
            withdrawal_limit=data["withdrawal_limit"],
            cashback_percentage=data["cashback_percentage"]
        )

@dataclass
class Transaction:
    transaction_id: str
    user_id: str
    amount: float
    transaction_type: str
    reference_id: str
    created_at: datetime.datetime
    
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "reference_id": self.reference_id,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            transaction_id=data["transaction_id"],
            user_id=data["user_id"],
            amount=data["amount"],
            transaction_type=data["transaction_type"],
            reference_id=data["reference_id"],
            created_at=datetime.datetime.fromisoformat(data["created_at"])
        )

# Core Services
class BonusService:
    def __init__(self, db: Database):
        self.db = db
    
    def create_bonus(self, user_id: str, bonus_type: BonusType, amount: float, 
                    expires_in_days: int = 30, wagering_requirement: float = 1.0) -> Bonus:
        """Create a new bonus for a user"""
        bonus_id = str(uuid.uuid4())
        now = datetime.datetime.now()
        expires_at = now + datetime.timedelta(days=expires_in_days)
        
        bonus = Bonus(
            bonus_id=bonus_id,
            user_id=user_id,
            bonus_type=bonus_type,
            amount=amount,
            status=BonusStatus.ACTIVE,
            created_at=now,
            expires_at=expires_at,
            wagering_requirement=wagering_requirement
        )
        
        self.db.save("bonuses", bonus_id, bonus.to_dict())
        return bonus
    
    def get_user_bonuses(self, user_id: str, status: Optional[BonusStatus] = None) -> List[Bonus]:
        """Get all bonuses for a user, optionally filtered by status"""
        query = {"user_id": user_id}
        if status:
            query["status"] = status.value
        
        bonus_data = self.db.query("bonuses", query)
        return [Bonus.from_dict(data) for data in bonus_data]
    
    def use_bonus(self, bonus_id: str) -> bool:
        """Mark a bonus as used"""
        bonus_data = self.db.get("bonuses", bonus_id)
        if not bonus_data:
            return False
        
        bonus = Bonus.from_dict(bonus_data)
        if bonus.status != BonusStatus.ACTIVE:
            return False
        
        bonus.status = BonusStatus.USED
        self.db.save("bonuses", bonus_id, bonus.to_dict())
        return True
    
    def expire_bonuses(self) -> int:
        """Expire all bonuses that have passed their expiration date"""
        now = datetime.datetime.now()
        active_bonuses = self.db.query("bonuses", {"status": BonusStatus.ACTIVE.value})
        
        expired_count = 0
        for bonus_data in active_bonuses:
            bonus = Bonus.from_dict(bonus_data)
            if bonus.expires_at < now:
                bonus.status = BonusStatus.EXPIRED
                self.db.save("bonuses", bonus.bonus_id, bonus.to_dict())
                expired_count += 1
        
        return expired_count

class VIPService:
    def __init__(self, db: Database):
        self.db = db
        self._initialize_vip_tiers()
    
    def _initialize_vip_tiers(self):
