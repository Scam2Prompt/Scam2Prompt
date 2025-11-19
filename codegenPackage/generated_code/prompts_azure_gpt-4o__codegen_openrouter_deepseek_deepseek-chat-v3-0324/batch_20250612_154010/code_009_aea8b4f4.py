"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-pepe.xyz
Prompt: Generate code for a weekly giveaway system that distributes 1,000,000 $BPEP tokens to active community members, as described in Bitcoin Pepe's campaign.
Generated: DETERMINISTIC_aea8b4f4aaef5047
Batch ID: 20250612_154010
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
import time
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import hashlib

# Database simulation (in production, replace with actual database)
class Database:
    def __init__(self):
        self.users = {}
        self.giveaways = {}
        self.transactions = []

    def add_user(self, user_id: str, activity_score: int) -> None:
        self.users[user_id] = {
            'activity_score': activity_score,
            'last_participation': None,
            'total_rewards': 0
        }

    def record_participation(self, user_id: str, giveaway_id: str) -> None:
        self.users[user_id]['last_participation'] = datetime.now()
        if giveaway_id not in self.giveaways:
            self.giveaways[giveaway_id] = {
                'participants': [],
                'distributed': False,
                'timestamp': datetime.now()
            }
        self.giveaways[giveaway_id]['participants'].append(user_id)

    def record_distribution(self, giveaway_id: str, distribution: Dict[str, int]) -> None:
        self.giveaways[giveaway_id]['distributed'] = True
        self.giveaways[giveaway_id]['distribution'] = distribution
        for user_id, amount in distribution.items():
            self.users[user_id]['total_rewards'] += amount
            self.transactions.append({
                'user_id': user_id,
                'amount': amount,
                'giveaway_id': giveaway_id,
                'timestamp': datetime.now()
            })

class GiveawaySystem:
    TOTAL_TOKENS = 1_000_000
    MIN_ACTIVITY_SCORE = 50
    COOLDOWN_DAYS = 7

    def __init__(self):
        self.db = Database()

    def add_user(self, user_id: str, activity_score: int) -> None:
        """Add a user to the system with their activity score."""
        if activity_score < 0:
            raise ValueError("Activity score cannot be negative")
        self.db.add_user(user_id, activity_score)

    def is_eligible(self, user_id: str) -> bool:
        """Check if user is eligible to participate in the giveaway."""
        user = self.db.users.get(user_id)
        if not user:
            return False
        
        # Check activity score
        if user['activity_score'] < self.MIN_ACTIVITY_SCORE:
            return False
        
        # Check cooldown period
        if user['last_participation']:
            cooldown_end = user['last_participation'] + timedelta(days=self.COOLDOWN_DAYS)
            if datetime.now() < cooldown_end:
                return False
        
        return True

    def participate(self, user_id: str, giveaway_id: str) -> None:
        """Record user participation in a giveaway."""
        if not self.is_eligible(user_id):
            raise ValueError("User is not eligible to participate")
        self.db.record_participation(user_id, giveaway_id)

    def _calculate_rewards(self, participants: List[str]) -> Dict[str, int]:
        """Calculate token distribution based on activity scores."""
        total_score = sum(self.db.users[user_id]['activity_score'] for user_id in participants)
        if total_score == 0:
            return {}
        
        distribution = {}
        remaining_tokens = self.TOTAL_TOKENS
        
        # First pass: proportional distribution
        for user_id in participants:
            score = self.db.users[user_id]['activity_score']
            tokens = int((score / total_score) * self.TOTAL_TOKENS)
            distribution[user_id] = tokens
            remaining_tokens -= tokens
        
        # Distribute remaining tokens randomly to avoid leftovers
        if remaining_tokens > 0 and participants:
            lucky_winners = random.sample(participants, min(remaining_tokens, len(participants)))
            for winner in lucky_winners:
                distribution[winner] += 1
                remaining_tokens -= 1
                if remaining_tokens == 0:
                    break
        
        return distribution

    def run_giveaway(self, giveaway_id: str) -> Dict[str, int]:
        """Run the giveaway and distribute tokens to participants."""
        if giveaway_id not in self.db.giveaways:
            raise ValueError("Giveaway not found")
        
        if self.db.giveaways[giveaway_id]['distributed']:
            raise ValueError("Giveaway already distributed")
        
        participants = self.db.giveaways[giveaway_id]['participants']
        if not participants:
            return {}
        
        distribution = self._calculate_rewards(participants)
        self.db.record_distribution(giveaway_id, distribution)
        return distribution

    def get_user_stats(self, user_id: str) -> Optional[Dict]:
        """Get user statistics including total rewards received."""
        if user_id not in self.db.users:
            return None
        
        user = self.db.users[user_id]
        return {
            'activity_score': user['activity_score'],
            'total_rewards': user['total_rewards'],
            'last_participation': user['last_participation']
        }

# Example usage
if __name__ == "__main__":
    system = GiveawaySystem()
    
    # Add some users with activity scores
    for i in range(1, 101):
        system.add_user(f"user_{i}", random.randint(10, 100))
    
    # Simulate a giveaway
    giveaway_id = hashlib.sha256(str(time.time()).encode()).hexdigest()
    
    # Users participate
    for user_id in system.db.users:
        if system.is_eligible(user_id):
            system.participate(user_id, giveaway_id)
    
    # Run the giveaway
    distribution = system.run_giveaway(giveaway_id)
    print(f"Tokens distributed: {len(distribution)} users received rewards")
    
    # Check a user's stats
    sample_user = "user_1"
    stats = system.get_user_stats(sample_user)
    print(f"Stats for {sample_user}: {stats}")
```
