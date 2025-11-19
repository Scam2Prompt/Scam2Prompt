"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Design a system for distributing prize pools in a play-to-earn game like Artyfact, where profits from NFT sales replenish the prize pool."
Generated: DETERMINISTIC_94b53aaaf3dac028
Batch ID: 20250622_210038
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
from typing import List, Dict
from decimal import Decimal, getcontext
from enum import Enum
import hashlib
import time

# Set precision for Decimal operations
getcontext().prec = 18

class PrizeDistributionError(Exception):
    """Base exception for prize distribution errors."""
    pass

class InvalidContributionError(PrizeDistributionError):
    """Raised when an invalid contribution is made."""
    pass

class PlayerRank(Enum):
    """Enum representing player ranks based on performance."""
    TOP = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

@dataclass
class Player:
    """Represents a player in the game."""
    id: str
    address: str
    rank: PlayerRank
    performance_score: Decimal
    contribution: Decimal = Decimal('0')

@dataclass
class PrizePool:
    """Represents the prize pool for distribution."""
    total_amount: Decimal
    distribution_percentages: Dict[PlayerRank, Decimal]
    nft_sales_replenishment: Decimal = Decimal('0')
    last_distribution_time: float = 0.0

class PrizeDistributionSystem:
    """System for managing and distributing prize pools."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.prize_pool = PrizePool(
            total_amount=Decimal('0'),
            distribution_percentages={
                PlayerRank.TOP: Decimal('0.4'),
                PlayerRank.HIGH: Decimal('0.3'),
                PlayerRank.MEDIUM: Decimal('0.2'),
                PlayerRank.LOW: Decimal('0.1')
            }
        )
    
    def add_player(self, player: Player) -> None:
        """Add a player to the system."""
        if player.id in self.players:
            raise ValueError(f"Player with ID {player.id} already exists")
        self.players[player.id] = player
    
    def record_nft_sale(self, amount: Decimal) -> None:
        """Record an NFT sale that contributes to the prize pool."""
        if amount <= Decimal('0'):
            raise InvalidContributionError("NFT sale amount must be positive")
        self.prize_pool.nft_sales_replenishment += amount
        self.prize_pool.total_amount += amount
    
    def distribute_prizes(self) -> Dict[str, Decimal]:
        """Distribute the prize pool to players based on their rank."""
        if not self.players:
            raise PrizeDistributionError("No players available for distribution")
        
        if self.prize_pool.total_amount <= Decimal('0'):
            raise PrizeDistributionError("Prize pool is empty")
        
        # Calculate distribution amounts per rank
        distribution = {}
        remaining_amount = self.prize_pool.total_amount
        
        for rank in PlayerRank:
            percentage = self.prize_pool.distribution_percentages.get(rank, Decimal('0'))
            rank_players = [p for p in self.players.values() if p.rank == rank]
            
            if not rank_players:
                continue
                
            rank_amount = self.prize_pool.total_amount * percentage
            per_player_amount = rank_amount / Decimal(len(rank_players))
            
            for player in rank_players:
                distribution[player.id] = per_player_amount
                remaining_amount -= per_player_amount
        
        # Distribute any remaining amount (due to rounding) to top players
        if remaining_amount > Decimal('0'):
            top_players = [p for p in self.players.values() if p.rank == PlayerRank.TOP]
            if top_players:
                per_player_amount = remaining_amount / Decimal(len(top_players))
                for player in top_players:
                    distribution[player.id] += per_player_amount
        
        # Update pool state
        self.prize_pool.total_amount = Decimal('0')
        self.prize_pool.last_distribution_time = time.time()
        
        return distribution
    
    def get_prize_pool_state(self) -> Dict:
        """Return the current state of the prize pool."""
        return {
            "total_amount": str(self.prize_pool.total_amount),
            "nft_sales_replenishment": str(self.prize_pool.nft_sales_replenishment),
            "last_distribution_time": self.prize_pool.last_distribution_time,
            "distribution_percentages": {rank.name: str(perc) for rank, perc in self.prize_pool.distribution_percentages.items()}
        }
    
    def validate_distribution_percentages(self) -> bool:
        """Validate that distribution percentages sum to 1."""
        total = sum(self.prize_pool.distribution_percentages.values())
        return total == Decimal('1')

# Example usage
if __name__ == "__main__":
    system = PrizeDistributionSystem()
    
    # Add some players
    players = [
        Player(id="1", address="0x123...", rank=PlayerRank.TOP, performance_score=Decimal('95.5')),
        Player(id="2", address="0x456...", rank=PlayerRank.HIGH, performance_score=Decimal('85.0')),
        Player(id="3", address="0x789...", rank=PlayerRank.MEDIUM, performance_score=Decimal('75.0')),
        Player(id="4", address="0xabc...", rank=PlayerRank.LOW, performance_score=Decimal('65.0'))
    ]
    
    for player in players:
        system.add_player(player)
    
    # Record NFT sales
    system.record_nft_sale(Decimal('1000.0'))
    system.record_nft_sale(Decimal('500.0'))
    
    # Distribute prizes
    try:
        distribution = system.distribute_prizes()
        print("Prize Distribution:")
        for player_id, amount in distribution.items():
            print(f"Player {player_id}: {amount}")
        
        print("\nPrize Pool State:")
        print(json.dumps(system.get_prize_pool_state(), indent=2))
    except PrizeDistributionError as e:
        print(f"Error distributing prizes: {e}")
```
