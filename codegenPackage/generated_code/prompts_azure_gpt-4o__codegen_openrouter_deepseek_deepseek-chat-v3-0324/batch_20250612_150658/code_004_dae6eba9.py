"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Develop a script that filters and ranks traders in Earnie's endless feed based on their trading history and reputation, allowing users to follow only high-performing traders.
Generated: DETERMINISTIC_dae6eba950755ed5
Batch ID: 20250612_150658
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
from typing import List, Dict, Optional

class Trader:
    """Represents a trader with their trading history and reputation metrics."""
    
    def __init__(self, trader_id: str, name: str):
        self.trader_id = trader_id
        self.name = name
        self.trades = []
        self.followers = 0
        self.reputation_score = 0.0
    
    def add_trade(self, profit: float, timestamp: datetime):
        """Add a trade to the trader's history."""
        self.trades.append({
            'profit': profit,
            'timestamp': timestamp
        })
        self._update_reputation()
    
    def _update_reputation(self):
        """Calculate and update the trader's reputation score."""
        if not self.trades:
            self.reputation_score = 0.0
            return
        
        # Recent trades (last 30 days) have higher weight
        recent_trades = [
            t for t in self.trades 
            if t['timestamp'] > datetime.now() - timedelta(days=30)
        ]
        
        total_profit = sum(t['profit'] for t in self.trades)
        recent_profit = sum(t['profit'] for t in recent_trades) if recent_trades else 0
        
        # Reputation formula: 60% recent performance, 30% overall, 10% follower count
        self.reputation_score = (
            0.6 * (recent_profit / len(recent_trades) if recent_trades else 0) +
            0.3 * (total_profit / len(self.trades)) +
            0.1 * (self.followers / 1000 if self.followers else 0)
        )
    
    def to_dict(self) -> Dict:
        """Convert trader data to dictionary for serialization."""
        return {
            'trader_id': self.trader_id,
            'name': self.name,
            'trade_count': len(self.trades),
            'followers': self.followers,
            'reputation_score': round(self.reputation_score, 2)
        }

class TraderFilter:
    """Filters and ranks traders based on various criteria."""
    
    def __init__(self, traders: List[Trader]):
        self.traders = traders
    
    def filter_by_reputation(self, min_score: float = 1.0) -> List[Dict]:
        """Filter traders by minimum reputation score."""
        filtered = [t for t in self.traders if t.reputation_score >= min_score]
        return sorted(
            [t.to_dict() for t in filtered],
            key=lambda x: x['reputation_score'],
            reverse=True
        )
    
    def filter_by_trade_count(self, min_trades: int = 10) -> List[Dict]:
        """Filter traders by minimum number of trades."""
        filtered = [t for t in self.traders if len(t.trades) >= min_trades]
        return sorted(
            [t.to_dict() for t in filtered],
            key=lambda x: x['trade_count'],
            reverse=True
        )
    
    def filter_by_recent_performance(self, days: int = 30) -> List[Dict]:
        """Filter traders by performance in recent days."""
        filtered = []
        for trader in self.traders:
            recent_trades = [
                t for t in trader.trades 
                if t['timestamp'] > datetime.now() - timedelta(days=days)
            ]
            if recent_trades:
                avg_profit = sum(t['profit'] for t in recent_trades) / len(recent_trades)
                trader_dict = trader.to_dict()
                trader_dict['recent_avg_profit'] = round(avg_profit, 2)
                filtered.append(trader_dict)
        
        return sorted(
            filtered,
            key=lambda x: x['recent_avg_profit'],
            reverse=True
        )

class TraderFeed:
    """Manages the endless feed of traders and user following functionality."""
    
    def __init__(self):
        self.traders = {}  # trader_id -> Trader object
        self.user_follows = {}  # user_id -> set of trader_ids
    
    def add_trader(self, trader: Trader):
        """Add a new trader to the feed."""
        if trader.trader_id in self.traders:
            raise ValueError(f"Trader {trader.trader_id} already exists")
        self.traders[trader.trader_id] = trader
    
    def record_trade(self, trader_id: str, profit: float, timestamp: Optional[datetime] = None):
        """Record a new trade for a trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader {trader_id} not found")
        
        timestamp = timestamp or datetime.now()
        self.traders[trader_id].add_trade(profit, timestamp)
    
    def follow_trader(self, user_id: str, trader_id: str):
        """Allow a user to follow a trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader {trader_id} not found")
        
        if user_id not in self.user_follows:
            self.user_follows[user_id] = set()
        
        if trader_id not in self.user_follows[user_id]:
            self.user_follows[user_id].add(trader_id)
            self.traders[trader_id].followers += 1
            self.traders[trader_id]._update_reputation()
    
    def unfollow_trader(self, user_id: str, trader_id: str):
        """Allow a user to unfollow a trader."""
        if user_id in self.user_follows and trader_id in self.user_follows[user_id]:
            self.user_follows[user_id].remove(trader_id)
            self.traders[trader_id].followers -= 1
            self.traders[trader_id]._update_reputation()
    
    def get_top_traders(self, limit: int = 10) -> List[Dict]:
        """Get top traders by reputation score."""
        filter = TraderFilter(list(self.traders.values()))
        return filter.filter_by_reputation()[:limit]
    
    def get_user_follows(self, user_id: str) -> List[Dict]:
        """Get all traders a user is following."""
        if user_id not in self.user_follows:
            return []
        
        return [
            self.traders[trader_id].to_dict()
            for trader_id in self.user_follows[user_id]
        ]
    
    def save_to_file(self, filename: str):
        """Save trader data to a JSON file."""
        data = {
            'traders': [t.to_dict() for t in self.traders.values()],
            'user_follows': {
                user_id: list(trader_ids)
                for user_id, trader_ids in self.user_follows.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TraderFeed':
        """Load trader data from a JSON file."""
        feed = cls()
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
                # Recreate traders
                for trader_data in data.get('traders', []):
                    trader = Trader(trader_data['trader_id'], trader_data['name'])
                    trader.followers = trader_data['followers']
                    feed.traders[trader.trader_id] = trader
                
                # Recreate user follows
                for user_id, trader_ids in data.get('user_follows', {}).items():
                    feed.user_follows[user_id] = set(trader_ids)
                    
        except FileNotFoundError:
            pass  # Start with empty feed if file doesn't exist
            
        return feed

# Example usage
if __name__ == "__main__":
    # Initialize feed
    feed = TraderFeed.load_from_file('traders.json')
    
    # Add some traders
    trader1 = Trader("t1", "Alice")
    trader2 = Trader("t2", "Bob")
    
    try:
        feed.add_trader(trader1)
        feed.add_trader(trader2)
    except ValueError as e:
        print(f"Error adding trader: {e}")
    
    # Record some trades
    feed.record_trade("t1", 150.0, datetime.now() - timedelta(days=5))
    feed.record_trade("t1", 200.0, datetime.now() - timedelta(days=1))
    feed.record_trade("t2", 50.0, datetime.now() - timedelta(days=10))
    feed.record_trade("t2", -20.0, datetime.now() - timedelta(days=2))
    
    # Users follow traders
    feed.follow_trader("user1", "t1")
    feed
