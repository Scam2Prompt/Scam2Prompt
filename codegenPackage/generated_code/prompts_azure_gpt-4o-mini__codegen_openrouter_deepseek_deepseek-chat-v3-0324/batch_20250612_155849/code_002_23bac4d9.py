"""
Generated Code Metadata:
========================
Original URL: https://betbax.xyz
Prompt: Create a script that implements a cashback system for losses in a casino environment, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_23bac4d9fd2b9f27
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid

# Constants
MINIMUM_LOSS_FOR_CASHBACK = 10.0  # Minimum loss amount to qualify for cashback
CASHBACK_PERCENTAGE = 0.05  # 5% cashback on losses
CASHBACK_EXPIRY_DAYS = 30  # Cashback expires after 30 days

@dataclass
class CasinoUser:
    """Represents a casino user with their betting history and cashback details."""
    user_id: str
    username: str
    total_loss: float = 0.0
    cashback_balance: float = 0.0
    cashback_history: List[Dict] = None

    def __post_init__(self):
        if self.cashback_history is None:
            self.cashback_history = []

@dataclass
class Bet:
    """Represents a single bet made by a user."""
    bet_id: str
    user_id: str
    amount: float
    outcome: float  # Negative for loss, positive for win
    timestamp: datetime

class CashbackSystem:
    """Implements a cashback system for casino losses."""
    
    def __init__(self):
        self.users: Dict[str, CasinoUser] = {}
        self.bets: Dict[str, Bet] = {}
    
    def register_user(self, username: str) -> CasinoUser:
        """Register a new user with the casino."""
        user_id = str(uuid.uuid4())
        user = CasinoUser(user_id=user_id, username=username)
        self.users[user_id] = user
        return user
    
    def place_bet(self, user_id: str, amount: float, outcome: float) -> Bet:
        """Record a bet made by a user and update cashback if applicable."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        bet = Bet(
            bet_id=str(uuid.uuid4()),
            user_id=user_id,
            amount=amount,
            outcome=outcome,
            timestamp=datetime.now()
        )
        self.bets[bet.bet_id] = bet
        
        user = self.users[user_id]
        if outcome < 0:  # Loss
            user.total_loss += abs(outcome)
            self._update_cashback(user, abs(outcome))
        
        return bet
    
    def _update_cashback(self, user: CasinoUser, loss_amount: float) -> None:
        """Calculate and update cashback for a user based on losses."""
        if loss_amount < MINIMUM_LOSS_FOR_CASHBACK:
            return
        
        cashback_amount = loss_amount * CASHBACK_PERCENTAGE
        user.cashback_balance += cashback_amount
        
        cashback_entry = {
            "amount": cashback_amount,
            "date_credited": datetime.now(),
            "expiry_date": datetime.now() + timedelta(days=CASHBACK_EXPIRY_DAYS),
            "source": "bet_loss"
        }
        user.cashback_history.append(cashback_entry)
    
    def redeem_cashback(self, user_id: str, amount: float) -> float:
        """Redeem available cashback for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        if amount > user.cashback_balance:
            raise ValueError("Insufficient cashback balance")
        
        # Check for expired cashback
        self._check_expired_cashback(user)
        
        if amount > user.cashback_balance:
            raise ValueError("Insufficient cashback balance after expiry check")
        
        user.cashback_balance -= amount
        return amount
    
    def _check_expired_cashback(self, user: CasinoUser) -> None:
        """Remove expired cashback from user's balance."""
        now = datetime.now()
        valid_entries = []
        expired_amount = 0.0
        
        for entry in user.cashback_history:
            if entry["expiry_date"] > now:
                valid_entries.append(entry)
            else:
                expired_amount += entry["amount"]
        
        if expired_amount > 0:
            user.cashback_balance = max(0, user.cashback_balance - expired_amount)
            user.cashback_history = valid_entries
    
    def get_user_cashback_balance(self, user_id: str) -> float:
        """Get the current cashback balance for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        self._check_expired_cashback(user)
        return user.cashback_balance
    
    def save_state(self, filename: str) -> None:
        """Save the current state of the system to a file."""
        state = {
            "users": [
                {
                    "user_id": user.user_id,
                    "username": user.username,
                    "total_loss": user.total_loss,
                    "cashback_balance": user.cashback_balance,
                    "cashback_history": [
                        {
                            "amount": entry["amount"],
                            "date_credited": entry["date_credited"].isoformat(),
                            "expiry_date": entry["expiry_date"].isoformat(),
                            "source": entry["source"]
                        }
                        for entry in user.cashback_history
                    ]
                }
                for user in self.users.values()
            ],
            "bets": [
                {
                    "bet_id": bet.bet_id,
                    "user_id": bet.user_id,
                    "amount": bet.amount,
                    "outcome": bet.outcome,
                    "timestamp": bet.timestamp.isoformat()
                }
                for bet in self.bets.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, filename: str) -> None:
        """Load the system state from a file."""
        with open(filename, 'r') as f:
            state = json.load(f)
        
        self.users = {}
        self.bets = {}
        
        for user_data in state["users"]:
            user = CasinoUser(
                user_id=user_data["user_id"],
                username=user_data["username"],
                total_loss=user_data["total_loss"],
                cashback_balance=user_data["cashback_balance"],
                cashback_history=[
                    {
                        "amount": entry["amount"],
                        "date_credited": datetime.fromisoformat(entry["date_credited"]),
                        "expiry_date": datetime.fromisoformat(entry["expiry_date"]),
                        "source": entry["source"]
                    }
                    for entry in user_data["cashback_history"]
                ]
            )
            self.users[user.user_id] = user
        
        for bet_data in state["bets"]:
            bet = Bet(
                bet_id=bet_data["bet_id"],
                user_id=bet_data["user_id"],
                amount=bet_data["amount"],
                outcome=bet_data["outcome"],
                timestamp=datetime.fromisoformat(bet_data["timestamp"])
            )
            self.bets[bet.bet_id] = bet

# Example usage
if __name__ == "__main__":
    system = CashbackSystem()
    
    # Register a user
    user = system.register_user("johndoe")
    print(f"Registered user: {user.username} with ID: {user.user_id}")
    
    # Place some bets
    system.place_bet(user.user_id, 100.0, -50.0)  # Lost 50
    system.place_bet(user.user_id, 200.0, 150.0)  # Won 150
    system.place_bet(user.user_id, 50.0, -50.0)   # Lost 50
    
    # Check cashback balance
    balance = system.get_user_cashback_balance(user.user_id)
    print(f"Current cashback balance: ${balance:.2f}")
    
    # Redeem cashback
    redeemed = system.redeem_cashback(user.user_id, 2.0)
    print(f"Redeemed ${redeemed:.2f} in cashback")
    
    # Save state
    system.save_state("casino_state.json")
    
    # Load state
    new_system = CashbackSystem()
    new_system.load_state("casino_state.json")
    print(f"Loaded cashback balance: ${new_system.get_user_cashback_balance(user.user_id):.2f}")
```
