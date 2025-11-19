"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Create a basic gaming platform for Popo's Gaming Lounge, allowing users to participate in tournaments and earn rewards in $FROP tokens.
Generated: DETERMINISTIC_8d40cb4eb6c7fd10
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Popo's Gaming Lounge Platform
A basic gaming platform for tournaments and $FROP token rewards.
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Database simulation
class Database:
    def __init__(self):
        self.users = {}
        self.tournaments = {}
        self.rewards = {}
        self.transactions = []
    
    def add_user(self, user_id: str, username: str, wallet_address: str) -> None:
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = {
            "username": username,
            "wallet_address": wallet_address,
            "balance": 0.0,
            "joined_at": datetime.now().isoformat(),
            "tournaments_played": 0,
            "tournaments_won": 0
        }
    
    def get_user(self, user_id: str) -> Optional[Dict]:
        return self.users.get(user_id)
    
    def update_user_balance(self, user_id: str, amount: float) -> None:
        if user_id not in self.users:
            raise ValueError("User not found")
        self.users[user_id]["balance"] += amount
    
    def create_tournament(self, tournament_id: str, name: str, entry_fee: float, prize_pool: float) -> None:
        if tournament_id in self.tournaments:
            raise ValueError("Tournament already exists")
        self.tournaments[tournament_id] = {
            "name": name,
            "entry_fee": entry_fee,
            "prize_pool": prize_pool,
            "start_time": (datetime.now() + timedelta(hours=1)).isoformat(),
            "end_time": (datetime.now() + timedelta(hours=3)).isoformat(),
            "participants": [],
            "winner": None,
            "status": "upcoming"
        }
    
    def get_tournament(self, tournament_id: str) -> Optional[Dict]:
        return self.tournaments.get(tournament_id)
    
    def join_tournament(self, user_id: str, tournament_id: str) -> None:
        tournament = self.get_tournament(tournament_id)
        if not tournament:
            raise ValueError("Tournament not found")
        
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        if user["balance"] < tournament["entry_fee"]:
            raise ValueError("Insufficient balance")
        
        if user_id in tournament["participants"]:
            raise ValueError("User already joined")
        
        self.update_user_balance(user_id, -tournament["entry_fee"])
        tournament["participants"].append(user_id)
        self.users[user_id]["tournaments_played"] += 1
        
        self.transactions.append({
            "type": "tournament_entry",
            "user_id": user_id,
            "tournament_id": tournament_id,
            "amount": -tournament["entry_fee"],
            "timestamp": datetime.now().isoformat()
        })
    
    def complete_tournament(self, tournament_id: str) -> str:
        tournament = self.get_tournament(tournament_id)
        if not tournament:
            raise ValueError("Tournament not found")
        
        if tournament["status"] != "upcoming":
            raise ValueError("Tournament already completed")
        
        if len(tournament["participants"]) < 1:
            tournament["status"] = "cancelled"
            return "Tournament cancelled - no participants"
        
        winner = random.choice(tournament["participants"])
        tournament["winner"] = winner
        tournament["status"] = "completed"
        
        prize = tournament["prize_pool"]
        self.update_user_balance(winner, prize)
        self.users[winner]["tournaments_won"] += 1
        
        self.transactions.append({
            "type": "tournament_prize",
            "user_id": winner,
            "tournament_id": tournament_id,
            "amount": prize,
            "timestamp": datetime.now().isoformat()
        })
        
        return winner

# Token contract simulation
class FROPToken:
    def __init__(self, db: Database):
        self.db = db
        self.total_supply = 1000000
        self.token_name = "$FROP"
    
    def transfer(self, sender_id: str, receiver_id: str, amount: float) -> None:
        sender = self.db.get_user(sender_id)
        receiver = self.db.get_user(receiver_id)
        
        if not sender or not receiver:
            raise ValueError("User not found")
        
        if sender["balance"] < amount:
            raise ValueError("Insufficient balance")
        
        self.db.update_user_balance(sender_id, -amount)
        self.db.update_user_balance(receiver_id, amount)
        
        self.db.transactions.append({
            "type": "token_transfer",
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })
    
    def mint(self, user_id: str, amount: float) -> None:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        self.total_supply += amount
        self.db.update_user_balance(user_id, amount)
        
        self.db.transactions.append({
            "type": "token_mint",
            "user_id": user_id,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })

# Main platform class
class PoposGamingLounge:
    def __init__(self):
        self.db = Database()
        self.token = FROPToken(self.db)
    
    def register_user(self, username: str, wallet_address: str) -> str:
        user_id = f"user_{len(self.db.users) + 1}"
        self.db.add_user(user_id, username, wallet_address)
        return user_id
    
    def create_tournament(self, name: str, entry_fee: float, prize_pool: float) -> str:
        tournament_id = f"tournament_{len(self.db.tournaments) + 1}"
        self.db.create_tournament(tournament_id, name, entry_fee, prize_pool)
        return tournament_id
    
    def join_tournament(self, user_id: str, tournament_id: str) -> None:
        self.db.join_tournament(user_id, tournament_id)
    
    def complete_tournament(self, tournament_id: str) -> str:
        return self.db.complete_tournament(tournament_id)
    
    def get_user_balance(self, user_id: str) -> float:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        return user["balance"]
    
    def transfer_tokens(self, sender_id: str, receiver_id: str, amount: float) -> None:
        self.token.transfer(sender_id, receiver_id, amount)
    
    def mint_tokens(self, user_id: str, amount: float) -> None:
        self.token.mint(user_id, amount)
    
    def get_user_stats(self, user_id: str) -> Dict:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        return {
            "username": user["username"],
            "wallet_address": user["wallet_address"],
            "balance": user["balance"],
            "tournaments_played": user["tournaments_played"],
            "tournaments_won": user["tournaments_won"],
            "win_rate": user["tournaments_won"] / user["tournaments_played"] if user["tournaments_played"] > 0 else 0
        }
    
    def get_tournament_info(self, tournament_id: str) -> Dict:
        tournament = self.db.get_tournament(tournament_id)
        if not tournament:
            raise ValueError("Tournament not found")
        
        return {
            "name": tournament["name"],
            "entry_fee": tournament["entry_fee"],
            "prize_pool": tournament["prize_pool"],
            "status": tournament["status"],
            "participants": len(tournament["participants"]),
            "winner": tournament["winner"],
            "start_time": tournament["start_time"],
            "end_time": tournament["end_time"]
        }

# Example usage
if __name__ == "__main__":
    platform = PoposGamingLounge()
    
    # Register users
    user1 = platform.register_user("gamer1", "0x123...")
    user2 = platform.register_user("gamer2", "0x456...")
    
    # Mint some tokens
    platform.mint_tokens(user1, 1000)
    platform.mint_tokens(user2, 1000)
    
    # Create tournament
    tournament_id = platform.create_tournament("Weekly Showdown", 50, 500)
    
    # Join tournament
    platform.join_tournament(user1, tournament_id)
    platform.join_tournament(user2, tournament_id)
    
    # Complete tournament
    winner = platform
