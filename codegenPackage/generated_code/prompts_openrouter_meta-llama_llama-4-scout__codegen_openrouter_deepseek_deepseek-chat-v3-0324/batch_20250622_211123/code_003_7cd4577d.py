"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Design a token economy for a gaming guild, taking into account distribution schedules, token metrics, and utility use cases similar to those outlined in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_7cd4577d331840ef
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
import hashlib

@dataclass
class GuildMember:
    """Represents a member of the gaming guild."""
    member_id: str
    name: str
    join_date: datetime
    reputation_score: float = 0.0
    tokens_earned: float = 0.0

@dataclass
class TokenTransaction:
    """Represents a token transaction record."""
    tx_id: str
    member_id: str
    amount: float
    timestamp: datetime
    tx_type: str  # e.g., "REWARD", "PURCHASE", "TRANSFER"
    metadata: Optional[Dict] = None

class TokenEconomy:
    """Implements a token economy system for a gaming guild."""
    
    def __init__(self, initial_supply: float, inflation_rate: float, distribution_schedule: Dict):
        """
        Initialize the token economy.
        
        Args:
            initial_supply: Initial total supply of tokens.
            inflation_rate: Annual inflation rate (e.g., 0.05 for 5%).
            distribution_schedule: Dict defining distribution periods and rates.
        """
        self.total_supply = initial_supply
        self.circulating_supply = 0.0
        self.inflation_rate = inflation_rate
        self.distribution_schedule = distribution_schedule
        self.members: Dict[str, GuildMember] = {}
        self.transactions: List[TokenTransaction] = []
        self.genesis_date = datetime.now()
        
    def add_member(self, member_id: str, name: str) -> None:
        """Add a new member to the guild."""
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already exists")
        self.members[member_id] = GuildMember(
            member_id=member_id,
            name=name,
            join_date=datetime.now()
        )
    
    def _generate_tx_id(self, member_id: str) -> str:
        """Generate a unique transaction ID."""
        timestamp = str(datetime.now().timestamp()).encode('utf-8')
        return hashlib.sha256(member_id.encode('utf-8') + timestamp).hexdigest()
    
    def _validate_member(self, member_id: str) -> None:
        """Validate that a member exists."""
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} not found")
    
    def reward_member(self, member_id: str, amount: float, reason: str = "") -> TokenTransaction:
        """
        Reward a member with tokens.
        
        Args:
            member_id: ID of the member to reward.
            amount: Amount of tokens to award.
            reason: Optional reason for the reward.
            
        Returns:
            The created transaction record.
        """
        self._validate_member(member_id)
        
        if amount <= 0:
            raise ValueError("Reward amount must be positive")
            
        tx = TokenTransaction(
            tx_id=self._generate_tx_id(member_id),
            member_id=member_id,
            amount=amount,
            timestamp=datetime.now(),
            tx_type="REWARD",
            metadata={"reason": reason}
        )
        
        self.members[member_id].tokens_earned += amount
        self.circulating_supply += amount
        self.transactions.append(tx)
        
        return tx
    
    def transfer_tokens(self, from_member_id: str, to_member_id: str, amount: float) -> TokenTransaction:
        """
        Transfer tokens between members.
        
        Args:
            from_member_id: ID of the member sending tokens.
            to_member_id: ID of the member receiving tokens.
            amount: Amount of tokens to transfer.
            
        Returns:
            The created transaction record.
        """
        self._validate_member(from_member_id)
        self._validate_member(to_member_id)
        
        if from_member_id == to_member_id:
            raise ValueError("Cannot transfer to self")
            
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
            
        if self.members[from_member_id].tokens_earned < amount:
            raise ValueError("Insufficient token balance")
            
        tx = TokenTransaction(
            tx_id=self._generate_tx_id(from_member_id),
            member_id=from_member_id,
            amount=-amount,
            timestamp=datetime.now(),
            tx_type="TRANSFER",
            metadata={"to": to_member_id}
        )
        
        # Create corresponding credit transaction
        credit_tx = TokenTransaction(
            tx_id=self._generate_tx_id(to_member_id),
            member_id=to_member_id,
            amount=amount,
            timestamp=datetime.now(),
            tx_type="TRANSFER",
            metadata={"from": from_member_id}
        )
        
        self.members[from_member_id].tokens_earned -= amount
        self.members[to_member_id].tokens_earned += amount
        self.transactions.extend([tx, credit_tx])
        
        return tx
    
    def mint_tokens(self, amount: float) -> None:
        """
        Mint new tokens according to inflation schedule.
        
        Args:
            amount: Amount of tokens to mint.
        """
        if amount <= 0:
            raise ValueError("Mint amount must be positive")
            
        self.total_supply += amount
        self.circulating_supply += amount
    
    def get_member_balance(self, member_id: str) -> float:
        """Get a member's token balance."""
        self._validate_member(member_id)
        return self.members[member_id].tokens_earned
    
    def get_transaction_history(self, member_id: Optional[str] = None) -> List[TokenTransaction]:
        """
        Get transaction history, optionally filtered by member.
        
        Args:
            member_id: Optional member ID to filter transactions.
            
        Returns:
            List of transactions.
        """
        if member_id:
            self._validate_member(member_id)
            return [tx for tx in self.transactions if tx.member_id == member_id]
        return self.transactions
    
    def calculate_inflationary_rewards(self) -> Dict[str, float]:
        """
        Calculate inflationary rewards based on distribution schedule.
        
        Returns:
            Dict mapping member IDs to reward amounts.
        """
        rewards = {}
        current_time = datetime.now()
        time_since_genesis = current_time - self.genesis_date
        
        # Calculate total rewards for this period
        period_rewards = self.total_supply * self.inflation_rate * (time_since_genesis.days / 365)
        
        # Distribute according to schedule and reputation scores
        total_reputation = sum(m.reputation_score for m in self.members.values())
        
        for member_id, member in self.members.items():
            if total_reputation > 0:
                share = member.reputation_score / total_reputation
            else:
                share = 1 / len(self.members)  # Equal distribution if no reputation
            
            rewards[member_id] = period_rewards * share
        
        return rewards
    
    def save_state(self, filepath: str) -> None:
        """Save the current state of the token economy to a file."""
        state = {
            "total_supply": self.total_supply,
            "circulating_supply": self.circulating_supply,
            "genesis_date": self.genesis_date.isoformat(),
            "members": {
                mid: {
                    "member_id": m.member_id,
                    "name": m.name,
                    "join_date": m.join_date.isoformat(),
                    "reputation_score": m.reputation_score,
                    "tokens_earned": m.tokens_earned
                }
                for mid, m in self.members.items()
            },
            "transactions": [
                {
                    "tx_id": tx.tx_id,
                    "member_id": tx.member_id,
                    "amount": tx.amount,
                    "timestamp": tx.timestamp.isoformat(),
                    "tx_type": tx.tx_type,
                    "metadata": tx.metadata
                }
                for tx in self.transactions
            ]
        }
        
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
    
    @classmethod
    def load_state(cls, filepath: str) -> 'TokenEconomy':
        """Load a token economy state from a file."""
        with open(filepath, 'r') as f:
            state = json.load(f)
        
        economy = cls(
            initial_supply=state["total_supply"],
            inflation_rate=0.05,  # Default, will be overwritten if needed
            distribution_schedule={}  # Default, will be overwritten if needed
        )
        
        economy.circulating_supply = state["circulating_supply"]
        economy.genesis_date = datetime.fromisoformat(state["genesis_date"])
        
        for mid, mdata in state["members"].items():
            economy.members[mid] = GuildMember(
                member_id=m
