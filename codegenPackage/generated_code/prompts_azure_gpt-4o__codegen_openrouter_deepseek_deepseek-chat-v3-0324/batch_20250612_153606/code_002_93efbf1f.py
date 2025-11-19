"""
Generated Code Metadata:
========================
Original URL: https://octaviaone.pages.dev
Prompt: How can Octavia's AI memory be leveraged to customize trading preferences for a user? Write code to demonstrate how Octavia learns and adapts to a user's trading history.
Generated: DETERMINISTIC_93efbf1f1ee3b82b
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class TradingPreferenceLearner:
    """
    A class to learn and adapt to user's trading preferences based on their history.
    """
    
    def __init__(self, user_id: str, memory_file: str = 'trading_memory.json'):
        """
        Initialize the learner with user ID and memory storage file.
        
        Args:
            user_id: Unique identifier for the user
            memory_file: Path to JSON file storing trading memory
        """
        self.user_id = user_id
        self.memory_file = memory_file
        self.trading_history: List[Dict] = []
        self.preferences: Dict = {}
        self.load_memory()
        
    def load_memory(self) -> None:
        """Load trading history and preferences from memory file."""
        try:
            with open(self.memory_file, 'r') as f:
                data = json.load(f)
                if self.user_id in data:
                    user_data = data[self.user_id]
                    self.trading_history = user_data.get('history', [])
                    self.preferences = user_data.get('preferences', {})
        except (FileNotFoundError, json.JSONDecodeError):
            # Initialize new file if not exists or corrupted
            self._initialize_memory_file()
    
    def save_memory(self) -> None:
        """Save current trading history and preferences to memory file."""
        try:
            with open(self.memory_file, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            
        data[self.user_id] = {
            'history': self.trading_history,
            'preferences': self.preferences
        }
        
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _initialize_memory_file(self) -> None:
        """Initialize memory file with empty structure."""
        with open(self.memory_file, 'w') as f:
            json.dump({}, f)
    
    def record_trade(self, 
                    symbol: str, 
                    action: str, 
                    amount: float, 
                    price: float, 
                    timestamp: Optional[datetime] = None,
                    tags: Optional[List[str]] = None) -> None:
        """
        Record a new trade in the user's history.
        
        Args:
            symbol: Trading symbol (e.g., BTC-USD)
            action: 'buy' or 'sell'
            amount: Quantity traded
            price: Price per unit
            timestamp: When the trade occurred (defaults to now)
            tags: Optional list of tags for the trade
        """
        if timestamp is None:
            timestamp = datetime.utcnow()
            
        trade = {
            'symbol': symbol,
            'action': action,
            'amount': amount,
            'price': price,
            'timestamp': timestamp.isoformat(),
            'tags': tags or []
        }
        
        self.trading_history.append(trade)
        self._update_preferences()
        self.save_memory()
    
    def _update_preferences(self) -> None:
        """Analyze trading history and update preferences."""
        if not self.trading_history:
            return
            
        # Analyze preferred trading pairs
        symbol_counts = {}
        for trade in self.trading_history:
            symbol = trade['symbol']
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
        
        self.preferences['preferred_symbols'] = sorted(
            symbol_counts.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:5]  # Top 5 most traded symbols
        
        # Analyze buy/sell ratio
        buy_count = sum(1 for t in self.trading_history if t['action'] == 'buy')
        sell_count = sum(1 for t in self.trading_history if t['action'] == 'sell')
        self.preferences['buy_sell_ratio'] = buy_count / max(1, buy_count + sell_count)
        
        # Analyze trading times (if timestamps are available)
        try:
            times = [datetime.fromisoformat(t['timestamp']).hour for t in self.trading_history]
            if times:
                self.preferences['active_hours'] = self._cluster_active_hours(times)
        except (ValueError, KeyError):
            pass
        
        # Analyze trade sizes
        amounts = [t['amount'] for t in self.trading_history]
        if amounts:
            self.preferences['avg_trade_size'] = np.mean(amounts)
            self.preferences['median_trade_size'] = np.median(amounts)
        
        # Extract tags if present
        all_tags = [tag for t in self.trading_history for tag in t.get('tags', [])]
        if all_tags:
            tag_counts = {}
            for tag in all_tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            self.preferences['preferred_tags'] = sorted(
                tag_counts.items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:3]  # Top 3 most used tags
    
    def _cluster_active_hours(self, hours: List[int]) -> List[Tuple[int, int]]:
        """
        Cluster active trading hours into time ranges.
        
        Args:
            hours: List of hours (0-23) when trades occurred
            
        Returns:
            List of tuples representing (start_hour, end_hour) ranges
        """
        if not hours:
            return []
            
        # Reshape for sklearn
        X = np.array(hours).reshape(-1, 1)
        
        # Standardize and cluster
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Use elbow method or fixed small number of clusters
        n_clusters = min(3, len(set(hours)))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(X_scaled)
        
        # Get cluster centers and sort
        centers = scaler.inverse_transform(kmeans.cluster_centers_)
        centers = sorted([int(round(c[0])) for c in centers])
        
        # Create ranges
        ranges = []
        for i in range(len(centers)):
            if i == 0:
                start = 0
            else:
                start = (centers[i-1] + centers[i]) // 2
                
            if i == len(centers) - 1:
                end = 23
            else:
                end = (centers[i] + centers[i+1]) // 2
                
            ranges.append((start, end))
            
        return ranges
    
    def get_recommendations(self) -> Dict:
        """
        Generate trading recommendations based on learned preferences.
        
        Returns:
            Dictionary containing personalized recommendations
        """
        rec = {
            'recommended_symbols': [s[0] for s in self.preferences.get('preferred_symbols', [])],
            'trading_style': self._get_trading_style(),
            'optimal_times': self._format_time_ranges(
                self.preferences.get('active_hours', [])
            ),
            'position_sizing': self._get_position_sizing()
        }
        
        if 'preferred_tags' in self.preferences:
            rec['preferred_categories'] = [t[0] for t in self.preferences['preferred_tags']]
            
        return rec
    
    def _get_trading_style(self) -> str:
        """Determine if user is more of a buyer or seller."""
        ratio = self.preferences.get('buy_sell_ratio', 0.5)
        if ratio > 0.7:
            return "Aggressive buyer"
        elif ratio > 0.55:
            return "Moderate buyer"
        elif ratio < 0.3:
            return "Aggressive seller"
        elif ratio < 0.45:
            return "Moderate seller"
        else:
            return "Balanced trader"
    
    def _format_time_ranges(self, ranges: List[Tuple[int, int]]) -> List[str]:
        """Convert hour ranges to human-readable format."""
        formatted = []
        for start, end in ranges:
            start_str = f"{start % 12 or 12}{'AM' if start < 12 else 'PM'}"
            end_str = f"{end % 12 or 12}{'AM' if end < 12 else 'PM'}"
            formatted.append(f"{start_str} - {end_str}")
        return formatted
    
    def _get_position_sizing(self) -> Dict:
        """Recommend position sizing based on historical trades."""
        avg = self.preferences.get('avg_trade_size', 0)
        median = self.preferences.get('median_trade_size', 0)
        
        if avg == 0:
            return {}
            
        return {
            'suggested_min': round(median * 0.5, 4),
            'suggested_avg': round(avg, 4),
            'suggested_max': round(
