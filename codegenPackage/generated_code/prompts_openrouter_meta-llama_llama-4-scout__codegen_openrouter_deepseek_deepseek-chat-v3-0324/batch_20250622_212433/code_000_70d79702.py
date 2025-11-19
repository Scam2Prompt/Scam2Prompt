"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the SIMemes game economy, where players collect and trade poop, and the goal is to accumulate wealth and resources.
Generated: DETERMINISTIC_70d7970272687047
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os
from typing import Dict, List, Optional

class Player:
    """Represents a player in the SIMemes game economy."""
    
    def __init__(self, player_id: str, name: str):
        """Initialize a player with default resources."""
        self.player_id = player_id
        self.name = name
        self.poop_count = 0
        self.money = 100  # Starting money
        self.inventory: Dict[str, int] = {}
        self.trades_completed = 0
        
    def collect_poop(self, amount: int = 1) -> None:
        """Collect poop and add to player's inventory."""
        self.poop_count += amount
        
    def sell_poop(self, price_per_unit: float) -> float:
        """
        Sell collected poop for money.
        Returns the total money earned from the sale.
        """
        if self.poop_count <= 0:
            raise ValueError("No poop to sell")
            
        total = self.poop_count * price_per_unit
        self.money += total
        self.poop_count = 0
        return total
        
    def buy_item(self, item_name: str, cost: float, quantity: int = 1) -> None:
        """Purchase an item if player has enough money."""
        if self.money < cost * quantity:
            raise ValueError("Insufficient funds")
            
        self.money -= cost * quantity
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
        
    def trade(self, other_player: 'Player', give_item: str, give_qty: int, 
              receive_item: str, receive_qty: int) -> None:
        """Trade items with another player."""
        if give_item not in self.inventory or self.inventory[give_item] < give_qty:
            raise ValueError(f"Not enough {give_item} to trade")
            
        if receive_item not in other_player.inventory or other_player.inventory[receive_item] < receive_qty:
            raise ValueError(f"Other player doesn't have enough {receive_item}")
            
        # Execute the trade
        self.inventory[give_item] -= give_qty
        other_player.inventory[give_item] = other_player.inventory.get(give_item, 0) + give_qty
        
        other_player.inventory[receive_item] -= receive_qty
        self.inventory[receive_item] = self.inventory.get(receive_item, 0) + receive_qty
        
        self.trades_completed += 1
        other_player.trades_completed += 1
        
    def to_dict(self) -> Dict:
        """Serialize player data to dictionary."""
        return {
            'player_id': self.player_id,
            'name': self.name,
            'poop_count': self.poop_count,
            'money': self.money,
            'inventory': self.inventory,
            'trades_completed': self.trades_completed
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Deserialize player data from dictionary."""
        player = cls(data['player_id'], data['name'])
        player.poop_count = data['poop_count']
        player.money = data['money']
        player.inventory = data['inventory']
        player.trades_completed = data['trades_completed']
        return player

class GameEconomy:
    """Manages the SIMemes game economy."""
    
    def __init__(self):
        """Initialize the game economy with empty player list."""
        self.players: Dict[str, Player] = {}
        self.market_prices: Dict[str, float] = {
            'poop': 1.0,
            'golden_poop': 10.0,
            'legendary_poop': 50.0
        }
        self.save_file = 'game_economy_save.json'
        
    def add_player(self, player_id: str, name: str) -> Player:
        """Add a new player to the economy."""
        if player_id in self.players:
            raise ValueError("Player ID already exists")
            
        player = Player(player_id, name)
        self.players[player_id] = player
        return player
        
    def remove_player(self, player_id: str) -> None:
        """Remove a player from the economy."""
        if player_id not in self.players:
            raise ValueError("Player ID not found")
            
        del self.players[player_id]
        
    def get_player(self, player_id: str) -> Player:
        """Get a player by ID."""
        if player_id not in self.players:
            raise ValueError("Player ID not found")
            
        return self.players[player_id]
        
    def generate_random_poop(self, player_id: str) -> str:
        """
        Player collects random poop with different rarity.
        Returns the type of poop collected.
        """
        if player_id not in self.players:
            raise ValueError("Player ID not found")
            
        player = self.players[player_id]
        rand = random.random()
        
        if rand < 0.7:  # 70% chance for regular poop
            player.collect_poop()
            return 'regular_poop'
        elif rand < 0.9:  # 20% chance for golden poop
            player.inventory['golden_poop'] = player.inventory.get('golden_poop', 0) + 1
            return 'golden_poop'
        else:  # 10% chance for legendary poop
            player.inventory['legendary_poop'] = player.inventory.get('legendary_poop', 0) + 1
            return 'legendary_poop'
            
    def update_market_prices(self) -> None:
        """Randomly update market prices to simulate market fluctuations."""
        for item in self.market_prices:
            # Random price change between -20% and +20%
            change = 1 + (random.random() * 0.4 - 0.2)
            self.market_prices[item] = max(0.1, self.market_prices[item] * change)
            
    def save_game(self) -> None:
        """Save the game state to a file."""
        data = {
            'players': {pid: p.to_dict() for pid, p in self.players.items()},
            'market_prices': self.market_prices
        }
        
        with open(self.save_file, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_game(self) -> bool:
        """
        Load the game state from a file.
        Returns True if successful, False otherwise.
        """
        if not os.path.exists(self.save_file):
            return False
            
        try:
            with open(self.save_file, 'r') as f:
                data = json.load(f)
                
            self.players = {pid: Player.from_dict(pdata) for pid, pdata in data['players'].items()}
            self.market_prices = data['market_prices']
            return True
        except (json.JSONDecodeError, KeyError, TypeError):
            return False
            
    def get_leaderboard(self, by: str = 'money') -> List[Dict]:
        """
        Get a leaderboard sorted by specified metric.
        Valid metrics: 'money', 'poop_count', 'trades_completed'
        """
        if by not in ['money', 'poop_count', 'trades_completed']:
            raise ValueError("Invalid leaderboard metric")
            
        players = sorted(
            self.players.values(),
            key=lambda p: getattr(p, by),
            reverse=True
        )
        
        return [{
            'name': p.name,
            'metric': getattr(p, by),
            'rank': i+1
        } for i, p in enumerate(players)]

# Example usage
if __name__ == "__main__":
    economy = GameEconomy()
    
    # Try to load saved game
    if not economy.load_game():
        print("Starting new game...")
        
    # Create some players
    try:
        player1 = economy.add_player("1", "Alice")
        player2 = economy.add_player("2", "Bob")
    except ValueError as e:
        print(f"Error creating players: {e}")
    
    # Simulate some gameplay
    for _ in range(5):
        economy.generate_random_poop("1")
        economy.generate_random_poop("2")
    
    # Update market prices
    economy.update_market_prices()
    
    # Print leaderboard
    print("\nMoney Leaderboard:")
    for entry in economy.get_leaderboard('money'):
        print(f"{entry['rank']}. {entry['name']}: ${entry['metric']:.2f}")
    
    # Save the game
    economy.save_game()
```
