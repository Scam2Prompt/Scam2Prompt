"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Develop a leaderboard system for tracking top traders, inspired by the "Leaderboard" functionality on the Deeptrade UI platform.
Generated: DETERMINISTIC_3fffe97085709cb9
Batch ID: 20250612_153758
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
from typing import List, Dict, Optional
import heapq
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Trader:
    """Represents a trader with their performance metrics."""
    
    def __init__(self, trader_id: str, name: str, pnl: float, volume: float, trades: int):
        """
        Initialize a Trader instance.
        
        Args:
            trader_id: Unique identifier for the trader
            name: Trader's display name
            pnl: Profit and Loss (can be positive or negative)
            volume: Total trading volume
            trades: Number of trades executed
        """
        self.trader_id = trader_id
        self.name = name
        self.pnl = pnl
        self.volume = volume
        self.trades = trades
        self.last_updated = datetime.utcnow()
    
    def to_dict(self) -> Dict:
        """Convert Trader object to dictionary for serialization."""
        return {
            'trader_id': self.trader_id,
            'name': self.name,
            'pnl': self.pnl,
            'volume': self.volume,
            'trades': self.trades,
            'last_updated': self.last_updated.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Trader':
        """Create Trader object from dictionary."""
        trader = cls(
            trader_id=data['trader_id'],
            name=data['name'],
            pnl=data['pnl'],
            volume=data['volume'],
            trades=data['trades']
        )
        trader.last_updated = datetime.fromisoformat(data['last_updated'])
        return trader

class Leaderboard:
    """Manages a leaderboard of top traders based on different metrics."""
    
    def __init__(self, max_entries: int = 100, data_file: str = 'leaderboard_data.json'):
        """
        Initialize the Leaderboard.
        
        Args:
            max_entries: Maximum number of entries to keep in each leaderboard
            data_file: File to persist leaderboard data
        """
        self.max_entries = max_entries
        self.data_file = Path(data_file)
        
        # Initialize leaderboards
        self.pnl_leaders = []  # Max-heap based on PnL
        self.volume_leaders = []  # Max-heap based on volume
        self.active_leaders = []  # Max-heap based on number of trades
        
        # Load existing data if available
        self._load_data()
    
    def add_trader(self, trader: Trader) -> None:
        """
        Add or update a trader in the leaderboard.
        
        Args:
            trader: Trader object to add/update
        """
        try:
            # Check if trader exists in any leaderboard
            existing = self._find_trader(trader.trader_id)
            
            if existing:
                # Update existing trader
                existing.pnl = trader.pnl
                existing.volume = trader.volume
                existing.trades = trader.trades
                existing.last_updated = trader.last_updated
            else:
                # Add new trader
                self._add_to_leaderboard(trader)
            
            # Persist the data
            self._save_data()
            
        except Exception as e:
            logger.error(f"Error adding trader {trader.trader_id}: {str(e)}")
            raise
    
    def get_top_pnl_traders(self, limit: int = 10) -> List[Trader]:
        """Get top traders by PnL."""
        return self._get_top_traders(self.pnl_leaders, limit)
    
    def get_top_volume_traders(self, limit: int = 10) -> List[Trader]:
        """Get top traders by volume."""
        return self._get_top_traders(self.volume_leaders, limit)
    
    def get_top_active_traders(self, limit: int = 10) -> List[Trader]:
        """Get top traders by number of trades."""
        return self._get_top_traders(self.active_leaders, limit)
    
    def _add_to_leaderboard(self, trader: Trader) -> None:
        """Add trader to all leaderboards."""
        # For PnL leaderboard (max-heap)
        heapq.heappush(self.pnl_leaders, (-trader.pnl, trader))
        if len(self.pnl_leaders) > self.max_entries:
            heapq.heappop(self.pnl_leaders)
        
        # For volume leaderboard (max-heap)
        heapq.heappush(self.volume_leaders, (-trader.volume, trader))
        if len(self.volume_leaders) > self.max_entries:
            heapq.heappop(self.volume_leaders)
        
        # For active traders leaderboard (max-heap)
        heapq.heappush(self.active_leaders, (-trader.trades, trader))
        if len(self.active_leaders) > self.max_entries:
            heapq.heappop(self.active_leaders)
    
    def _find_trader(self, trader_id: str) -> Optional[Trader]:
        """Find a trader in any of the leaderboards."""
        for heap in [self.pnl_leaders, self.volume_leaders, self.active_leaders]:
            for _, trader in heap:
                if trader.trader_id == trader_id:
                    return trader
        return None
    
    def _get_top_traders(self, heap: List, limit: int) -> List[Trader]:
        """Get top traders from a specific leaderboard."""
        try:
            sorted_traders = sorted([(-score, trader) for score, trader in heap], key=lambda x: x[0])
            return [trader for _, trader in sorted_traders[:limit]]
        except Exception as e:
            logger.error(f"Error getting top traders: {str(e)}")
            return []
    
    def _save_data(self) -> None:
        """Save leaderboard data to file."""
        try:
            data = {
                'pnl_leaders': [trader.to_dict() for _, trader in self.pnl_leaders],
                'volume_leaders': [trader.to_dict() for _, trader in self.volume_leaders],
                'active_leaders': [trader.to_dict() for _, trader in self.active_leaders],
            }
            
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            logger.error(f"Error saving leaderboard data: {str(e)}")
            raise
    
    def _load_data(self) -> None:
        """Load leaderboard data from file."""
        if not self.data_file.exists():
            return
            
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
            self.pnl_leaders = [(-trader['pnl'], Trader.from_dict(trader)) for trader in data['pnl_leaders']]
            self.volume_leaders = [(-trader['volume'], Trader.from_dict(trader)) for trader in data['volume_leaders']]
            self.active_leaders = [(-trader['trades'], Trader.from_dict(trader)) for trader in data['active_leaders']]
            
            # Heapify the loaded data
            heapq.heapify(self.pnl_leaders)
            heapq.heapify(self.volume_leaders)
            heapq.heapify(self.active_leaders)
            
        except Exception as e:
            logger.error(f"Error loading leaderboard data: {str(e)}")
            # Initialize empty leaderboards if loading fails
            self.pnl_leaders = []
            self.volume_leaders = []
            self.active_leaders = []

# Example usage
if __name__ == "__main__":
    # Initialize leaderboard
    leaderboard = Leaderboard()
    
    # Add some traders
    trader1 = Trader("1", "Alice", 5000.50, 100000.75, 42)
    trader2 = Trader("2", "Bob", 7500.25, 85000.50, 35)
    trader3 = Trader("3", "Charlie", 3000.75, 120000.25, 58)
    
    leaderboard.add_trader(trader1)
    leaderboard.add_trader(trader2)
    leaderboard.add_trader(trader3)
    
    # Get top traders
    print("Top PnL Traders:")
    for trader in leaderboard.get_top_pnl_traders():
        print(f"{trader.name}: ${trader.pnl:,.2f}")
    
    print("\nTop Volume Traders:")
    for trader in leaderboard.get_top_volume_traders():
        print(f"{trader.name}: {trader.volume:,.2f} volume")
    
    print("\nMost Active Traders:")
    for trader in leaderboard.get_top_active_traders():
        print(f"{trader.name}:
