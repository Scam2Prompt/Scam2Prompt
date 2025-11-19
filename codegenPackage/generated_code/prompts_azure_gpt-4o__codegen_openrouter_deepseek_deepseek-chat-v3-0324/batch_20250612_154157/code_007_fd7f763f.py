"""
Generated Code Metadata:
========================
Original URL: https://eigen-labs-287829331544c3a3caa5f5b77a00.webflow.io
Prompt: Develop a simulation model in Python to demonstrate the infinite horizon game concept described by Eigen Labs, using EigenLayer as the core protocol.
Generated: DETERMINISTIC_fd7f763fa0b37ee1
Batch ID: 20250612_154157
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto
import random
import matplotlib.pyplot as plt
from collections import defaultdict

class PlayerAction(Enum):
    """Possible actions a player can take in the game."""
    COOPERATE = auto()
    DEFECT = auto()

@dataclass
class Player:
    """Represents a player in the infinite horizon game."""
    id: int
    strategy: str  # 'tit_for_tat', 'always_cooperate', 'always_defect', 'random'
    reputation: float = 1.0  # Initial reputation score
    stake: float = 100.0  # Initial stake amount
    rewards: float = 0.0  # Accumulated rewards
    
    def decide_action(self, opponent_history: List[PlayerAction]) -> PlayerAction:
        """Determine the player's action based on their strategy."""
        if self.strategy == 'tit_for_tat':
            if not opponent_history:
                return PlayerAction.COOPERATE
            return opponent_history[-1]
        elif self.strategy == 'always_cooperate':
            return PlayerAction.COOPERATE
        elif self.strategy == 'always_defect':
            return PlayerAction.DEFECT
        elif self.strategy == 'random':
            return random.choice(list(PlayerAction))
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")

@dataclass
class GameRound:
    """Represents a single round of interaction between two players."""
    player1: Player
    player2: Player
    action1: PlayerAction
    action2: PlayerAction
    rewards: Tuple[float, float]

class InfiniteHorizonGame:
    """Simulates the infinite horizon game using EigenLayer concepts."""
    
    def __init__(self, players: List[Player], stake_multiplier: float = 1.1, 
                 reputation_decay: float = 0.95, base_reward: float = 10.0):
        self.players = players
        self.stake_multiplier = stake_multiplier
        self.reputation_decay = reputation_decay
        self.base_reward = base_reward
        self.history: Dict[Tuple[int, int], List[GameRound]] = defaultdict(list)
        self.current_round = 0
        
    def _calculate_rewards(self, action1: PlayerAction, action2: PlayerAction, 
                          player1: Player, player2: Player) -> Tuple[float, float]:
        """Calculate rewards based on actions and player stakes."""
        if action1 == PlayerAction.COOPERATE and action2 == PlayerAction.COOPERATE:
            reward = self.base_reward * player1.stake * player1.reputation
            return (reward, reward)
        elif action1 == PlayerAction.COOPERATE and action2 == PlayerAction.DEFECT:
            return (0, self.base_reward * player2.stake * player2.reputation * 2)
        elif action1 == PlayerAction.DEFECT and action2 == PlayerAction.COOPERATE:
            return (self.base_reward * player1.stake * player1.reputation * 2, 0)
        else:  # Both defect
            return (0, 0)
    
    def _update_player_states(self, player1: Player, player2: Player, 
                             action1: PlayerAction, action2: PlayerAction):
        """Update player stakes and reputations based on actions."""
        # Update reputations
        if action1 == PlayerAction.COOPERATE:
            player1.reputation = min(1.0, player1.reputation * self.stake_multiplier)
        else:
            player1.reputation *= self.reputation_decay
            
        if action2 == PlayerAction.COOPERATE:
            player2.reputation = min(1.0, player2.reputation * self.stake_multiplier)
        else:
            player2.reputation *= self.reputation_decay
            
        # Update stakes based on rewards
        rewards = self._calculate_rewards(action1, action2, player1, player2)
        player1.stake += rewards[0]
        player2.stake += rewards[1]
        player1.rewards += rewards[0]
        player2.rewards += rewards[1]
        
        return rewards
    
    def play_round(self, player1: Player, player2: Player) -> GameRound:
        """Execute a single round between two players."""
        # Get player actions
        history1 = [r.action2 for r in self.history[(player1.id, player2.id)]]
        history2 = [r.action1 for r in self.history[(player2.id, player1.id)]]
        
        action1 = player1.decide_action(history2)
        action2 = player2.decide_action(history1)
        
        # Calculate and distribute rewards
        rewards = self._update_player_states(player1, player2, action1, action2)
        
        # Record the round
        round_result = GameRound(player1, player2, action1, action2, rewards)
        self.history[(player1.id, player2.id)].append(round_result)
        self.current_round += 1
        
        return round_result
    
    def simulate(self, rounds: int = 1000, match_every: int = 10) -> Dict[int, float]:
        """Run the simulation for a given number of rounds."""
        results = defaultdict(list)
        
        for _ in range(rounds):
            # Randomly match players periodically
            if self.current_round % match_every == 0:
                random.shuffle(self.players)
                
            # Play rounds between adjacent players
            for i in range(0, len(self.players), 2):
                if i+1 < len(self.players):
                    self.play_round(self.players[i], self.players[i+1])
            
            # Record stakes for visualization
            for player in self.players:
                results[player.id].append(player.stake)
        
        return results
    
    def visualize_results(self, results: Dict[int, float]):
        """Plot the stake evolution over time for all players."""
        plt.figure(figsize=(12, 6))
        for player_id, stakes in results.items():
            player = next(p for p in self.players if p.id == player_id)
            plt.plot(stakes, label=f"Player {player_id} ({player.strategy})")
        
        plt.title("Stake Evolution in Infinite Horizon Game")
        plt.xlabel("Round")
        plt.ylabel("Stake Amount")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    """Run the simulation with example players."""
    # Create players with different strategies
    players = [
        Player(id=1, strategy='tit_for_tat'),
        Player(id=2, strategy='always_cooperate'),
        Player(id=3, strategy='always_defect'),
        Player(id=4, strategy='random'),
        Player(id=5, strategy='tit_for_tat'),
        Player(id=6, strategy='always_defect')
    ]
    
    # Initialize and run the game
    game = InfiniteHorizonGame(players)
    results = game.simulate(rounds=500)
    
    # Display results
    game.visualize_results(results)
    
    # Print final rewards
    print("\nFinal Rewards:")
    for player in sorted(game.players, key=lambda p: p.rewards, reverse=True):
        print(f"Player {player.id} ({player.strategy}): {player.rewards:.2f}")

if __name__ == "__main__":
    main()
```
