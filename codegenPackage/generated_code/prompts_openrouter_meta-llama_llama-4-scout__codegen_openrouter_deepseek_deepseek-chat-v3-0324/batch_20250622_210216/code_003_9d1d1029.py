"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: "Design a simple game mechanism for a play-to-earn (P2E) game on the Bitcoin blockchain, inspired by the 'Duel Race' feature mentioned on the Bitcoin Dogs Club website."
Generated: DETERMINISTIC_9d1d102909efb931
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import random
import time
from typing import Dict, List, Tuple, Optional

class BitcoinDuelRace:
    """
    A simple play-to-earn game mechanism for a Bitcoin blockchain game inspired by 'Duel Race'.
    Players compete in races to earn rewards in satoshis.
    """
    
    def __init__(self, min_bet: int = 1000, max_bet: int = 10000):
        """
        Initialize the Duel Race game with configurable betting limits.
        
        Args:
            min_bet: Minimum bet amount in satoshis
            max_bet: Maximum bet amount in satoshis
        """
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.active_duels: Dict[str, Dict] = {}  # duel_id: {player1, player2, bet_amount, status}
        self.completed_duels: Dict[str, Dict] = {}
        self.player_balances: Dict[str, int] = {}  # player_address: balance
        
    def create_player(self, player_address: str, initial_balance: int = 100000) -> bool:
        """
        Register a new player with an initial balance.
        
        Args:
            player_address: Player's Bitcoin address
            initial_balance: Starting balance in satoshis
            
        Returns:
            bool: True if player was created successfully
        """
        if player_address in self.player_balances:
            return False
        self.player_balances[player_address] = initial_balance
        return True
    
    def create_duel(self, player_address: str, bet_amount: int) -> Optional[str]:
        """
        Create a new duel race waiting for an opponent.
        
        Args:
            player_address: Creator's Bitcoin address
            bet_amount: Amount to bet in satoshis
            
        Returns:
            Optional[str]: Duel ID if created successfully, None otherwise
        """
        if bet_amount < self.min_bet or bet_amount > self.max_bet:
            return None
        if self.player_balances.get(player_address, 0) < bet_amount:
            return None
            
        duel_id = self._generate_duel_id(player_address)
        self.active_duels[duel_id] = {
            'player1': player_address,
            'player2': None,
            'bet_amount': bet_amount,
            'status': 'waiting',
            'created_at': int(time.time())
        }
        return duel_id
    
    def join_duel(self, player_address: str, duel_id: str) -> bool:
        """
        Join an existing duel race.
        
        Args:
            player_address: Joining player's Bitcoin address
            duel_id: ID of the duel to join
            
        Returns:
            bool: True if joined successfully
        """
        if duel_id not in self.active_duels:
            return False
        if self.active_duels[duel_id]['player2'] is not None:
            return False
        if self.player_balances.get(player_address, 0) < self.active_duels[duel_id]['bet_amount']:
            return False
            
        self.active_duels[duel_id]['player2'] = player_address
        self.active_duels[duel_id]['status'] = 'active'
        return True
    
    def run_duel(self, duel_id: str) -> Optional[Tuple[str, int]]:
        """
        Execute the duel race and determine the winner.
        
        Args:
            duel_id: ID of the duel to run
            
        Returns:
            Optional[Tuple[str, int]]: (winner_address, prize_amount) or None if failed
        """
        if duel_id not in self.active_duels:
            return None
        if self.active_duels[duel_id]['status'] != 'active':
            return None
            
        duel = self.active_duels[duel_id]
        player1 = duel['player1']
        player2 = duel['player2']
        bet_amount = duel['bet_amount']
        
        # Deduct bets from both players
        self.player_balances[player1] -= bet_amount
        self.player_balances[player2] -= bet_amount
        
        # Determine winner randomly (simplified for demo)
        winner = random.choice([player1, player2])
        prize = bet_amount * 2 * 0.9  # 10% house fee
        prize = int(prize)
        
        # Award prize to winner
        self.player_balances[winner] += prize
        
        # Record completed duel
        self.completed_duels[duel_id] = {
            **duel,
            'winner': winner,
            'prize': prize,
            'completed_at': int(time.time()),
            'status': 'completed'
        }
        
        # Remove from active duels
        del self.active_duels[duel_id]
        
        return (winner, prize)
    
    def get_player_balance(self, player_address: str) -> int:
        """
        Get a player's current balance.
        
        Args:
            player_address: Player's Bitcoin address
            
        Returns:
            int: Current balance in satoshis
        """
        return self.player_balances.get(player_address, 0)
    
    def get_active_duels(self) -> List[Dict]:
        """
        Get list of all active duels waiting for opponents.
        
        Returns:
            List[Dict]: List of active duel dictionaries
        """
        return [duel for duel in self.active_duels.values() if duel['status'] == 'waiting']
    
    def _generate_duel_id(self, player_address: str) -> str:
        """
        Generate a unique duel ID based on player address and timestamp.
        
        Args:
            player_address: Player's Bitcoin address
            
        Returns:
            str: Generated duel ID
        """
        timestamp = str(int(time.time()))
        return hashlib.sha256((player_address + timestamp).encode()).hexdigest()[:16]
```
