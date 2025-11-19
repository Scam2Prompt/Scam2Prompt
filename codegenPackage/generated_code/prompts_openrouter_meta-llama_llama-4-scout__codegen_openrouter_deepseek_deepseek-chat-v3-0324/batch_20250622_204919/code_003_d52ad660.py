"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Develop a simple gaming platform, like Popo's Gaming Lounge, where users can play, participate in tournaments, and earn rewards in $FROP tokens.
Generated: DETERMINISTIC_d52ad660cbb49652
Batch ID: 20250622_204919
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from uuid import uuid4

# Database simulation using dictionaries
users_db = {}
tournaments_db = {}
games_db = {}
rewards_db = {}

# Token contract simulation
class FROPToken:
    def __init__(self):
        self.balances = {}
    
    def mint(self, address: str, amount: float) -> bool:
        if address not in self.balances:
            self.balances[address] = 0.0
        self.balances[address] += amount
        return True
    
    def transfer(self, from_address: str, to_address: str, amount: float) -> bool:
        if self.balances.get(from_address, 0) < amount:
            return False
        self.balances[from_address] -= amount
        if to_address not in self.balances:
            self.balances[to_address] = 0.0
        self.balances[to_address] += amount
        return True
    
    def balance_of(self, address: str) -> float:
        return self.balances.get(address, 0.0)

token_contract = FROPToken()

# Models
class User:
    def __init__(self, username: str, wallet_address: str):
        self.user_id = str(uuid4())
        self.username = username
        self.wallet_address = wallet_address
        self.games_played = 0
        self.tournaments_participated = 0
        self.achievements = []
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "wallet_address": self.wallet_address,
            "games_played": self.games_played,
            "tournaments_participated": self.tournaments_participated,
            "achievements": self.achievements,
            "created_at": self.created_at.isoformat()
        }

class Game:
    def __init__(self, name: str, description: str, reward_per_win: float):
        self.game_id = str(uuid4())
        self.name = name
        self.description = description
        self.reward_per_win = reward_per_win
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "game_id": self.game_id,
            "name": self.name,
            "description": self.description,
            "reward_per_win": self.reward_per_win,
            "created_at": self.created_at.isoformat()
        }

class Tournament:
    def __init__(self, game_id: str, name: str, entry_fee: float, prize_pool: float, start_time: datetime, end_time: datetime):
        self.tournament_id = str(uuid4())
        self.game_id = game_id
        self.name = name
        self.entry_fee = entry_fee
        self.prize_pool = prize_pool
        self.start_time = start_time
        self.end_time = end_time
        self.participants = []
        self.winners = []
        self.status = "upcoming"  # upcoming, ongoing, completed
    
    def to_dict(self) -> Dict:
        return {
            "tournament_id": self.tournament_id,
            "game_id": self.game_id,
            "name": self.name,
            "entry_fee": self.entry_fee,
            "prize_pool": self.prize_pool,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "participants": self.participants,
            "winners": self.winners,
            "status": self.status
        }

class Reward:
    def __init__(self, user_id: str, amount: float, reason: str):
        self.reward_id = str(uuid4())
        self.user_id = user_id
        self.amount = amount
        self.reason = reason
        self.claimed = False
        self.created_at = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            "reward_id": self.reward_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "reason": self.reason,
            "claimed": self.claimed,
            "created_at": self.created_at.isoformat()
        }

# Core functions
def register_user(username: str, wallet_address: str) -> Tuple[bool, str]:
    if not username or not wallet_address:
        return False, "Username and wallet address are required"
    
    if any(u["username"] == username for u in users_db.values()):
        return False, "Username already exists"
    
    if any(u["wallet_address"] == wallet_address for u in users_db.values()):
        return False, "Wallet address already registered"
    
    user = User(username, wallet_address)
    users_db[user.user_id] = user.to_dict()
    return True, user.user_id

def create_game(name: str, description: str, reward_per_win: float) -> Tuple[bool, str]:
    if not name or not description or reward_per_win <= 0:
        return False, "Invalid game parameters"
    
    game = Game(name, description, reward_per_win)
    games_db[game.game_id] = game.to_dict()
    return True, game.game_id

def create_tournament(game_id: str, name: str, entry_fee: float, prize_pool: float, duration_hours: int) -> Tuple[bool, str]:
    if game_id not in games_db:
        return False, "Game not found"
    
    if entry_fee < 0 or prize_pool <= 0 or duration_hours <= 0:
        return False, "Invalid tournament parameters"
    
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=duration_hours)
    
    tournament = Tournament(game_id, name, entry_fee, prize_pool, start_time, end_time)
    tournaments_db[tournament.tournament_id] = tournament.to_dict()
    return True, tournament.tournament_id

def join_tournament(user_id: str, tournament_id: str) -> Tuple[bool, str]:
    if user_id not in users_db:
        return False, "User not found"
    
    if tournament_id not in tournaments_db:
        return False, "Tournament not found"
    
    tournament = tournaments_db[tournament_id]
    if tournament["status"] != "upcoming":
        return False, "Tournament is not open for registration"
    
    if user_id in tournament["participants"]:
        return False, "User already registered"
    
    # Check if user has enough balance to pay entry fee
    wallet_address = users_db[user_id]["wallet_address"]
    if token_contract.balance_of(wallet_address) < tournament["entry_fee"]:
        return False, "Insufficient balance for entry fee"
    
    # Deduct entry fee
    if not token_contract.transfer(wallet_address, "platform_wallet", tournament["entry_fee"]):
        return False, "Payment failed"
    
    tournament["participants"].append(user_id)
    users_db[user_id]["tournaments_participated"] += 1
    return True, "Successfully joined tournament"

def play_game(user_id: str, game_id: str) -> Tuple[bool, str]:
    if user_id not in users_db:
        return False, "User not found"
    
    if game_id not in games_db:
        return False, "Game not found"
    
    # Simulate game outcome (random win/loss)
    is_winner = random.random() > 0.5
    game = games_db[game_id]
    users_db[user_id]["games_played"] += 1
    
    if is_winner:
        reward_amount = game["reward_per_win"]
        wallet_address = users_db[user_id]["wallet_address"]
        token_contract.mint(wallet_address, reward_amount)
        
        reward = Reward(user_id, reward_amount, f"Won game: {game['name']}")
        rewards_db[reward.reward_id] = reward.to_dict()
        
        return True, f"Congratulations! You won {reward_amount} $FROP"
    else:
        return True, "Better luck next time!"

def complete_tournament(tournament_id: str) -> Tuple[bool, str]:
    if tournament_id not in tournaments_db:
        return False, "Tournament not found"
    
    tournament = tournaments_db[tournament_id]
    if tournament["status"] == "completed":
        return False, "Tournament already completed"
    
    if datetime.now() < datetime.fromisoformat(tournament["end_time"]):
        return False, "Tournament is not yet over"
    
    participants = tournament["participants"]
    if not participants:
        tournament["status"] = "completed"
        return True, "Tournament completed with no participants"
    
    # Select random winners (top 3 for example)
    winners = random.sample(participants, min(3, len(participants)))
