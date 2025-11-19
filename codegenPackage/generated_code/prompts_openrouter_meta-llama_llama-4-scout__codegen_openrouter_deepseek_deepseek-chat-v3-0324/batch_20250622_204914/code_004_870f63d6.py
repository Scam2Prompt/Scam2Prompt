"""
Generated Code Metadata:
========================
Original URL: https://luckyblock-5bs.pages.dev
Prompt: Design a system for a crypto casino to offer regular bonuses, free spins, and exclusive promotions to its players, using a combination of cryptocurrency and loyalty programs.
Generated: DETERMINISTIC_870f63d6139f821b
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union
from enum import Enum

# Database simulation (in production, use a real database like PostgreSQL or MongoDB)
class Database:
    def __init__(self):
        self.players = {}
        self.promotions = {}
        self.transactions = []
    
    def add_player(self, player: 'Player'):
        self.players[player.player_id] = player
    
    def get_player(self, player_id: str) -> Optional['Player']:
        return self.players.get(player_id)
    
    def add_promotion(self, promotion: 'Promotion'):
        self.promotions[promotion.promotion_id] = promotion
    
    def get_promotion(self, promotion_id: str) -> Optional['Promotion']:
        return self.promotions.get(promotion_id)
    
    def add_transaction(self, transaction: 'Transaction'):
        self.transactions.append(transaction)
    
    def get_player_transactions(self, player_id: str) -> List['Transaction']:
        return [t for t in self.transactions if t.player_id == player_id]

# Initialize database
db = Database()

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    BONUS = "BONUS"
    FREE_SPINS = "FREE_SPINS"
    PROMOTION = "PROMOTION"

class Transaction:
    def __init__(self, transaction_id: str, player_id: str, amount: float, 
                 currency: str, transaction_type: TransactionType, 
                 promotion_id: Optional[str] = None):
        self.transaction_id = transaction_id
        self.player_id = player_id
        self.amount = amount
        self.currency = currency
        self.transaction_type = transaction_type
        self.promotion_id = promotion_id
        self.timestamp = datetime.now()
    
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "player_id": self.player_id,
            "amount": self.amount,
            "currency": self.currency,
            "transaction_type": self.transaction_type.value,
            "promotion_id": self.promotion_id,
            "timestamp": self.timestamp.isoformat()
        }

class PromotionType(Enum):
    SIGNUP_BONUS = "SIGNUP_BONUS"
    DEPOSIT_BONUS = "DEPOSIT_BONUS"
    FREE_SPINS = "FREE_SPINS"
    LOYALTY_REWARD = "LOYALTY_REWARD"
    EXCLUSIVE_PROMOTION = "EXCLUSIVE_PROMOTION"

class Promotion:
    def __init__(self, promotion_id: str, name: str, promotion_type: PromotionType, 
                 description: str, start_date: datetime, end_date: datetime, 
                 bonus_amount: Optional[float] = None, bonus_percentage: Optional[float] = None,
                 free_spins: Optional[int] = None, min_deposit: Optional[float] = None,
                 currency: str = "BTC", is_active: bool = True):
        self.promotion_id = promotion_id
        self.name = name
        self.promotion_type = promotion_type
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.bonus_amount = bonus_amount
        self.bonus_percentage = bonus_percentage
        self.free_spins = free_spins
        self.min_deposit = min_deposit
        self.currency = currency
        self.is_active = is_active
    
    def is_valid(self) -> bool:
        now = datetime.now()
        return self.is_active and self.start_date <= now <= self.end_date
    
    def to_dict(self):
        return {
            "promotion_id": self.promotion_id,
            "name": self.name,
            "promotion_type": self.promotion_type.value,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "bonus_amount": self.bonus_amount,
            "bonus_percentage": self.bonus_percentage,
            "free_spins": self.free_spins,
            "min_deposit": self.min_deposit,
            "currency": self.currency,
            "is_active": self.is_active
        }

class Player:
    def __init__(self, player_id: str, name: str, email: str, 
                 registration_date: datetime = datetime.now()):
        self.player_id = player_id
        self.name = name
        self.email = email
        self.registration_date = registration_date
        self.balance = 0.0
        self.loyalty_points = 0
        self.used_promotions = set()
        self.last_activity = datetime.now()
    
    def deposit(self, amount: float, currency: str) -> str:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        transaction_id = hashlib.sha256(f"{self.player_id}{time.time()}".encode()).hexdigest()
        transaction = Transaction(
            transaction_id=transaction_id,
            player_id=self.player_id,
            amount=amount,
            currency=currency,
            transaction_type=TransactionType.DEPOSIT
        )
        
        self.balance += amount
        self.last_activity = datetime.now()
        db.add_transaction(transaction)
        return transaction_id
    
    def withdraw(self, amount: float, currency: str) -> str:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        
        transaction_id = hashlib.sha256(f"{self.player_id}{time.time()}".encode()).hexdigest()
        transaction = Transaction(
            transaction_id=transaction_id,
            player_id=self.player_id,
            amount=amount,
            currency=currency,
            transaction_type=TransactionType.WITHDRAWAL
        )
        
        self.balance -= amount
        self.last_activity = datetime.now()
        db.add_transaction(transaction)
        return transaction_id
    
    def claim_promotion(self, promotion_id: str) -> str:
        promotion = db.get_promotion(promotion_id)
        if not promotion:
            raise ValueError("Promotion not found")
        if not promotion.is_valid():
            raise ValueError("Promotion is not active or expired")
        if promotion_id in self.used_promotions:
            raise ValueError("Promotion already claimed")
        
        transaction_id = hashlib.sha256(f"{self.player_id}{time.time()}".encode()).hexdigest()
        
        if promotion.promotion_type == PromotionType.SIGNUP_BONUS:
            if (datetime.now() - self.registration_date) > timedelta(days=1):
                raise ValueError("Signup bonus can only be claimed within 24 hours of registration")
            
            if promotion.bonus_amount:
                self.balance += promotion.bonus_amount
                transaction = Transaction(
                    transaction_id=transaction_id,
                    player_id=self.player_id,
                    amount=promotion.bonus_amount,
                    currency=promotion.currency,
                    transaction_type=TransactionType.BONUS,
                    promotion_id=promotion_id
                )
                db.add_transaction(transaction)
        
        elif promotion.promotion_type == PromotionType.DEPOSIT_BONUS:
            # Check if player has made a qualifying deposit
            transactions = db.get_player_transactions(self.player_id)
            qualifying_deposits = [
                t for t in transactions 
                if t.transaction_type == TransactionType.DEPOSIT and 
                t.currency == promotion.currency and
                (promotion.min_deposit is None or t.amount >= promotion.min_deposit) and
                t.timestamp >= promotion.start_date
            ]
            
            if not qualifying_deposits:
                raise ValueError("No qualifying deposit found for this promotion")
            
            if promotion.bonus_percentage:
                bonus_amount = sum(t.amount for t in qualifying_deposits) * (promotion.bonus_percentage / 100)
                self.balance += bonus_amount
                transaction = Transaction(
                    transaction_id=transaction_id,
                    player_id=self.player_id,
                    amount=bonus_amount,
                    currency=promotion.currency,
                    transaction_type=TransactionType.BONUS,
                    promotion_id=promotion_id
                )
                db.add_transaction(transaction)
        
        elif promotion.promotion_type == PromotionType.FREE_SPINS:
            if promotion.free_spins:
                transaction = Transaction(
                    transaction_id=transaction_id,
                    player_id=self.player_id,
                    amount=promotion.free_spins,
                    currency="FREE_SPINS",
                    transaction_type=TransactionType.FREE_SPINS,
                    promotion_id=promotion_id
                )
                db.add_transaction(transaction)
        
        elif promotion.promotion_type == PromotionType.LOYALTY_REWARD:
            if self.loyalty_points < 100:  # Example threshold
                raise ValueError("Not enough loyalty points")
            
            if promotion.bonus_amount:
