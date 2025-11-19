"""
Generated Code Metadata:
========================
Original URL: https://blur-nft-marketplace.org
Prompt: Generate code for tracking and calculating RTP values for a gambling platform, similar to the RTP monitoring system mentioned on PAIZA99.
Generated: DETERMINISTIC_22b6375dec834300
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('rtp_monitor.log', maxBytes=5*1024*1024, backupCount=3)
    ]
)
logger = logging.getLogger(__name__)

class RTPTracker:
    """
    A class to track and calculate RTP (Return to Player) values for gambling games.
    """
    
    def __init__(self, game_id: str, window_size_days: int = 30):
        """
        Initialize the RTP tracker for a specific game.
        
        Args:
            game_id: Unique identifier for the game
            window_size_days: Number of days to consider for RTP calculation (default 30)
        """
        self.game_id = game_id
        self.window_size_days = window_size_days
        
        # Data storage structures
        self.bets: Dict[str, List[Tuple[datetime, float]]] = defaultdict(list)
        self.wins: Dict[str, List[Tuple[datetime, float]]] = defaultdict(list)
        
        # Cache for performance
        self._rtp_cache: Dict[str, Dict[str, float]] = {}
        self._last_calculation_time: Dict[str, datetime] = {}
        
    def record_bet(self, player_id: str, amount: float, timestamp: Optional[datetime] = None):
        """
        Record a bet made by a player.
        
        Args:
            player_id: ID of the player making the bet
            amount: Amount of the bet
            timestamp: Optional timestamp of the bet (defaults to now)
        """
        try:
            if amount <= 0:
                raise ValueError("Bet amount must be positive")
                
            ts = timestamp or datetime.now()
            self.bets[player_id].append((ts, amount))
            logger.info(f"Recorded bet for player {player_id}: {amount} at {ts}")
            
            # Invalidate cache for this player
            if player_id in self._rtp_cache:
                del self._rtp_cache[player_id]
                
        except Exception as e:
            logger.error(f"Error recording bet: {str(e)}")
            raise
            
    def record_win(self, player_id: str, amount: float, timestamp: Optional[datetime] = None):
        """
        Record a win by a player.
        
        Args:
            player_id: ID of the player winning
            amount: Amount of the win
            timestamp: Optional timestamp of the win (defaults to now)
        """
        try:
            if amount < 0:
                raise ValueError("Win amount cannot be negative")
                
            ts = timestamp or datetime.now()
            self.wins[player_id].append((ts, amount))
            logger.info(f"Recorded win for player {player_id}: {amount} at {ts}")
            
            # Invalidate cache for this player
            if player_id in self._rtp_cache:
                del self._rtp_cache[player_id]
                
        except Exception as e:
            logger.error(f"Error recording win: {str(e)}")
            raise
            
    def _filter_recent_transactions(self, transactions: List[Tuple[datetime, float]]) -> List[Tuple[datetime, float]]:
        """
        Filter transactions to only include those within the time window.
        
        Args:
            transactions: List of (timestamp, amount) tuples
            
        Returns:
            Filtered list of transactions within the time window
        """
        cutoff = datetime.now() - timedelta(days=self.window_size_days)
        return [(ts, amt) for ts, amt in transactions if ts >= cutoff]
        
    def calculate_player_rtp(self, player_id: str) -> Dict[str, float]:
        """
        Calculate RTP for a specific player.
        
        Args:
            player_id: ID of the player to calculate RTP for
            
        Returns:
            Dictionary containing:
            - 'rtp': The RTP percentage (wins/bets)
            - 'total_bets': Total bets in the period
            - 'total_wins': Total wins in the period
        """
        try:
            # Check cache first
            if player_id in self._rtp_cache:
                if (datetime.now() - self._last_calculation_time.get(player_id, datetime.min)).seconds < 60:
                    return self._rtp_cache[player_id]
                    
            # Get recent transactions
            recent_bets = self._filter_recent_transactions(self.bets.get(player_id, []))
            recent_wins = self._filter_recent_transactions(self.wins.get(player_id, []))
            
            total_bets = sum(amt for _, amt in recent_bets)
            total_wins = sum(amt for _, amt in recent_wins)
            
            if total_bets == 0:
                rtp = 0.0
            else:
                rtp = (total_wins / total_bets) * 100
                
            result = {
                'rtp': round(rtp, 2),
                'total_bets': round(total_bets, 2),
                'total_wins': round(total_wins, 2)
            }
            
            # Update cache
            self._rtp_cache[player_id] = result
            self._last_calculation_time[player_id] = datetime.now()
            
            logger.info(f"Calculated RTP for player {player_id}: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Error calculating RTP for player {player_id}: {str(e)}")
            raise
            
    def calculate_overall_rtp(self) -> Dict[str, float]:
        """
        Calculate overall RTP for all players in the game.
        
        Returns:
            Dictionary containing:
            - 'rtp': The overall RTP percentage
            - 'total_bets': Total bets in the period
            - 'total_wins': Total wins in the period
            - 'player_count': Number of active players
        """
        try:
            total_bets = 0.0
            total_wins = 0.0
            player_count = 0
            
            # Get all unique players who have bets
            all_players = set(self.bets.keys())
            
            for player_id in all_players:
                player_data = self.calculate_player_rtp(player_id)
                total_bets += player_data['total_bets']
                total_wins += player_data['total_wins']
                if player_data['total_bets'] > 0:
                    player_count += 1
                    
            if total_bets == 0:
                overall_rtp = 0.0
            else:
                overall_rtp = (total_wins / total_bets) * 100
                
            result = {
                'rtp': round(overall_rtp, 2),
                'total_bets': round(total_bets, 2),
                'total_wins': round(total_wins, 2),
                'player_count': player_count
            }
            
            logger.info(f"Calculated overall RTP for game {self.game_id}: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Error calculating overall RTP: {str(e)}")
            raise
            
    def save_state(self, file_path: str):
        """
        Save the current state of the tracker to a file.
        
        Args:
            file_path: Path to the file where state will be saved
        """
        try:
            state = {
                'game_id': self.game_id,
                'window_size_days': self.window_size_days,
                'bets': {k: [(ts.isoformat(), amt) for ts, amt in v] for k, v in self.bets.items()},
                'wins': {k: [(ts.isoformat(), amt) for ts, amt in v] for k, v in self.wins.items()}
            }
            
            with open(file_path, 'w') as f:
                json.dump(state, f, indent=2)
                
            logger.info(f"Saved state to {file_path}")
            
        except Exception as e:
            logger.error(f"Error saving state: {str(e)}")
            raise
            
    @classmethod
    def load_state(cls, file_path: str) -> 'RTPTracker':
        """
        Load a tracker state from a file.
        
        Args:
            file_path: Path to the file containing the saved state
            
        Returns:
            A new RTPTracker instance with the loaded state
        """
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
                
            tracker = cls(state['game_id'], state['window_size_days'])
            
            for player_id, transactions in state['bets'].items():
                tracker.bets[player_id] = [(datetime.fromisoformat(ts), amt) for ts, amt in transactions]
                
            for player_id, transactions in state['wins'].items():
                tracker.wins[player
