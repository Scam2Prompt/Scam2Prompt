"""
Generated Code Metadata:
========================
Original URL: https://elonswaps.com
Prompt: Write code to implement a user reputation system for a blockchain-based escrow service, inspired by Elon Swaps' self-regulation mechanisms.
Generated: DETERMINISTIC_d42b85c07454331e
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from datetime import datetime

class ReputationAction(Enum):
    """Enum representing possible reputation actions"""
    SUCCESSFUL_TRANSACTION = 1
    FAILED_TRANSACTION = 2
    DISPUTE_WIN = 3
    DISPUTE_LOSS = 4
    TIMELY_COMPLETION = 5
    DELAYED_COMPLETION = 6

@dataclass
class UserReputation:
    """Data class representing a user's reputation"""
    user_id: str
    score: float = 100.0  # Default starting score
    total_transactions: int = 0
    successful_transactions: int = 0
    disputes_won: int = 0
    disputes_lost: int = 0
    last_updated: datetime = datetime.now()

class ReputationSystem:
    """Blockchain-based escrow reputation system"""
    
    def __init__(self):
        self.user_reputations: Dict[str, UserReputation] = {}
        self.reputation_weights = {
            ReputationAction.SUCCESSFUL_TRANSACTION: 5.0,
            ReputationAction.FAILED_TRANSACTION: -10.0,
            ReputationAction.DISPUTE_WIN: 15.0,
            ReputationAction.DISPUTE_LOSS: -20.0,
            ReputationAction.TIMELY_COMPLETION: 3.0,
            ReputationAction.DELAYED_COMPLETION: -5.0
        }
    
    def _get_user_reputation(self, user_id: str) -> UserReputation:
        """Get or create user reputation record"""
        if user_id not in self.user_reputations:
            self.user_reputations[user_id] = UserReputation(user_id=user_id)
        return self.user_reputations[user_id]
    
    def _validate_score(self, score: float) -> float:
        """Ensure score stays within reasonable bounds (0-200)"""
        return max(0.0, min(score, 200.0))
    
    def update_reputation(self, user_id: str, action: ReputationAction) -> UserReputation:
        """
        Update user reputation based on an action
        Args:
            user_id: Unique identifier for the user
            action: Reputation action to process
        Returns:
            Updated UserReputation object
        """
        if not isinstance(action, ReputationAction):
            raise ValueError("Invalid reputation action")
            
        user_rep = self._get_user_reputation(user_id)
        weight = self.reputation_weights.get(action, 0.0)
        
        # Update score
        user_rep.score = self._validate_score(user_rep.score + weight)
        
        # Update counters
        user_rep.total_transactions += 1
        if action == ReputationAction.SUCCESSFUL_TRANSACTION:
            user_rep.successful_transactions += 1
        elif action == ReputationAction.DISPUTE_WIN:
            user_rep.disputes_won += 1
        elif action == ReputationAction.DISPUTE_LOSS:
            user_rep.disputes_lost += 1
        
        user_rep.last_updated = datetime.now()
        return user_rep
    
    def get_reputation(self, user_id: str) -> Optional[UserReputation]:
        """Get user reputation if it exists"""
        return self.user_reputations.get(user_id)
    
    def calculate_trust_score(self, user_id: str) -> float:
        """
        Calculate comprehensive trust score (0-1) based on reputation metrics
        """
        user_rep = self.get_reputation(user_id)
        if not user_rep:
            return 0.5  # Default neutral score for new users
        
        # Base score (normalized to 0-1)
        base_score = user_rep.score / 200.0
        
        # Success rate component
        if user_rep.total_transactions > 0:
            success_rate = user_rep.successful_transactions / user_rep.total_transactions
        else:
            success_rate = 0.5
            
        # Dispute component
        total_disputes = user_rep.disputes_won + user_rep.disputes_lost
        if total_disputes > 0:
            dispute_score = user_rep.disputes_won / total_disputes
        else:
            dispute_score = 1.0  # No disputes is good
            
        # Weighted trust score
        trust_score = (base_score * 0.5) + (success_rate * 0.3) + (dispute_score * 0.2)
        return max(0.0, min(trust_score, 1.0))
    
    def to_blockchain_data(self, user_id: str) -> Dict:
        """Convert reputation data to blockchain-compatible format"""
        user_rep = self.get_reputation(user_id)
        if not user_rep:
            return {}
            
        data = {
            "user_id": user_id,
            "score": user_rep.score,
            "total_transactions": user_rep.total_transactions,
            "successful_transactions": user_rep.successful_transactions,
            "disputes_won": user_rep.disputes_won,
            "disputes_lost": user_rep.disputes_lost,
            "last_updated": user_rep.last_updated.isoformat(),
            "trust_score": self.calculate_trust_score(user_id)
        }
        
        # Create hash for data integrity
        data_str = json.dumps(data, sort_keys=True)
        data["hash"] = hashlib.sha256(data_str.encode()).hexdigest()
        return data
    
    def from_blockchain_data(self, data: Dict) -> UserReputation:
        """Load reputation data from blockchain format"""
        if not data or "user_id" not in data:
            raise ValueError("Invalid reputation data")
            
        # Verify hash
        data_copy = data.copy()
        original_hash = data_copy.pop("hash", None)
        data_str = json.dumps(data_copy, sort_keys=True)
        computed_hash = hashlib.sha256(data_str.encode()).hexdigest()
        
        if original_hash != computed_hash:
            raise ValueError("Data integrity check failed")
            
        # Create reputation object
        user_rep = UserReputation(
            user_id=data["user_id"],
            score=float(data["score"]),
            total_transactions=int(data["total_transactions"]),
            successful_transactions=int(data["successful_transactions"]),
            disputes_won=int(data["disputes_won"]),
            disputes_lost=int(data["disputes_lost"]),
            last_updated=datetime.fromisoformat(data["last_updated"])
        )
        
        self.user_reputations[data["user_id"]] = user_rep
        return user_rep

# Example usage
if __name__ == "__main__":
    rep_system = ReputationSystem()
    
    # Simulate some actions
    user1 = "user_123"
    rep_system.update_reputation(user1, ReputationAction.SUCCESSFUL_TRANSACTION)
    rep_system.update_reputation(user1, ReputationAction.TIMELY_COMPLETION)
    
    user2 = "user_456"
    rep_system.update_reputation(user2, ReputationAction.FAILED_TRANSACTION)
    rep_system.update_reputation(user2, ReputationAction.DISPUTE_LOSS)
    
    # Get and display reputation
    print(f"User 1 Trust Score: {rep_system.calculate_trust_score(user1):.2f}")
    print(f"User 2 Trust Score: {rep_system.calculate_trust_score(user2):.2f}")
    
    # Blockchain integration example
    blockchain_data = rep_system.to_blockchain_data(user1)
    print("Blockchain Data:", blockchain_data)
```
