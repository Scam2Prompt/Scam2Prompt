"""
Generated Code Metadata:
========================
Original URL: https://trx-bank.cc
Prompt: Generate code to create a multiplayer savings game that incorporates unique markings and factions as described in the content from trx-bank.cc.
Generated: DETERMINISTIC_7e56b0657f718ff1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import uuid
from typing import Dict, List, Optional, Tuple

class Player:
    """Represents a player in the savings game."""
    
    def __init__(self, name: str, faction: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.faction = faction
        self.balance: float = 0.0
        self.markings: List[str] = []
        self.transaction_history: List[Dict] = []
    
    def deposit(self, amount: float, marking: Optional[str] = None) -> bool:
        """Deposit money into player's account with optional marking."""
        if amount <= 0:
            return False
        
        self.balance += amount
        if marking:
            self.markings.append(marking)
        
        self.transaction_history.append({
            'type': 'deposit',
            'amount': amount,
            'marking': marking,
            'balance_after': self.balance
        })
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from player's account."""
        if amount <= 0 or amount > self.balance:
            return False
        
        self.balance -= amount
        self.transaction_history.append({
            'type': 'withdraw',
            'amount': amount,
            'balance_after': self.balance
        })
        return True
    
    def transfer(self, amount: float, recipient: 'Player', marking: Optional[str] = None) -> bool:
        """Transfer money to another player with optional marking."""
        if amount <= 0 or amount > self.balance:
            return False
        
        self.balance -= amount
        recipient.balance += amount
        
        if marking:
            recipient.markings.append(marking)
        
        self.transaction_history.append({
            'type': 'transfer_out',
            'amount': amount,
            'to': recipient.id,
            'marking': marking,
            'balance_after': self.balance
        })
        
        recipient.transaction_history.append({
            'type': 'transfer_in',
            'amount': amount,
            'from': self.id,
            'marking': marking,
            'balance_after': recipient.balance
        })
        
        return True

class SavingsGame:
    """Manages the multiplayer savings game with factions and markings."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.factions = {
            'Saviors': {'bonus': 1.05, 'description': 'Gains 5% interest on deposits'},
            'Traders': {'bonus': 1.10, 'description': 'Can transfer markings between players'},
            'Guardians': {'bonus': 0.95, 'description': 'Pay 5% less on transfers'}
        }
        self.markings_pool = [
            'Dragon', 'Phoenix', 'Wolf', 'Eagle', 'Lion',
            'Serpent', 'Bear', 'Tiger', 'Fox', 'Owl'
        ]
    
    def create_player(self, name: str, faction: str) -> Optional[Player]:
        """Create a new player with the specified faction."""
        if faction not in self.factions:
            return None
        
        player = Player(name, faction)
        self.players[player.id] = player
        return player
    
    def get_player(self, player_id: str) -> Optional[Player]:
        """Retrieve a player by their ID."""
        return self.players.get(player_id)
    
    def apply_faction_bonus(self, player: Player) -> None:
        """Apply faction-specific bonuses to a player."""
        if player.faction == 'Saviors':
            player.balance *= self.factions['Saviors']['bonus']
        elif player.faction == 'Guardians':
            # Bonus applied during transfers
            pass
    
    def generate_random_marking(self) -> str:
        """Generate a random unique marking for a player."""
        if not self.markings_pool:
            return "Common"
        
        marking = random.choice(self.markings_pool)
        self.markings_pool.remove(marking)
        return marking
    
    def transfer_marking(self, from_player: Player, to_player: Player, marking: str) -> bool:
        """Transfer a marking between players (Traders faction only)."""
        if from_player.faction != 'Traders':
            return False
        
        if marking not in from_player.markings:
            return False
        
        from_player.markings.remove(marking)
        to_player.markings.append(marking)
        return True
    
    def get_leaderboard(self) -> List[Tuple[str, float]]:
        """Get a sorted leaderboard of players by balance."""
        return sorted(
            [(player.name, player.balance) for player in self.players.values()],
            key=lambda x: x[1],
            reverse=True
        )
    
    def get_faction_stats(self) -> Dict[str, Dict]:
        """Get statistics for each faction."""
        stats = {}
        for faction in self.factions:
            faction_players = [p for p in self.players.values() if p.faction == faction]
            total_balance = sum(p.balance for p in faction_players)
            avg_balance = total_balance / len(faction_players) if faction_players else 0
            
            stats[faction] = {
                'player_count': len(faction_players),
                'total_balance': total_balance,
                'average_balance': avg_balance,
                'description': self.factions[faction]['description']
            }
        
        return stats

# Example usage
if __name__ == "__main__":
    game = SavingsGame()
    
    # Create players
    player1 = game.create_player("Alice", "Saviors")
    player2 = game.create_player("Bob", "Traders")
    player3 = game.create_player("Charlie", "Guardians")
    
    # Initial deposits
    player1.deposit(1000, game.generate_random_marking())
    player2.deposit(800, game.generate_random_marking())
    player3.deposit(1200, game.generate_random_marking())
    
    # Apply faction bonuses
    game.apply_faction_bonus(player1)
    
    # Transfer between players
    player1.transfer(200, player2, "Special Transfer")
    
    # Traders can transfer markings
    if player2.markings:
        game.transfer_marking(player2, player3, player2.markings[0])
    
    # Display leaderboard
    print("Leaderboard:")
    for name, balance in game.get_leaderboard():
        print(f"{name}: ${balance:.2f}")
    
    # Display faction stats
    print("\nFaction Statistics:")
    for faction, stats in game.get_faction_stats().items():
        print(f"\n{faction}:")
        print(f"Players: {stats['player_count']}")
        print(f"Total Balance: ${stats['total_balance']:.2f}")
        print(f"Average Balance: ${stats['average_balance']:.2f}")
        print(f"Bonus: {stats['description']}")
```
