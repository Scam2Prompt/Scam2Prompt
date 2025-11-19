"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Develop an algorithm to randomly shuffle and distribute Géminito cards for gameplay in teams or individual modes, ensuring all cards remain visible to players as per the rules.
Generated: DETERMINISTIC_6712842f49517021
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple, Union

class GeminitoCardGame:
    """
    A class to handle the distribution and shuffling of Géminito cards for gameplay.
    Supports both team and individual modes while ensuring all cards remain visible.
    """
    
    def __init__(self, num_players: int, team_mode: bool = False):
        """
        Initialize the game with the number of players and game mode.
        
        Args:
            num_players: Number of players in the game.
            team_mode: Whether the game is in team mode (True) or individual mode (False).
        """
        self.num_players = num_players
        self.team_mode = team_mode
        self.cards = self._generate_cards()
        self.players = self._initialize_players()
        
    def _generate_cards(self) -> List[str]:
        """
        Generate a standard deck of Géminito cards (40 cards).
        
        Returns:
            List of card strings representing the deck.
        """
        suits = ['Oros', 'Copas', 'Espadas', 'Bastos']
        ranks = ['1', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
        return [f"{rank} de {suit}" for suit in suits for rank in ranks]
    
    def _initialize_players(self) -> Dict[Union[int, str], List[str]]:
        """
        Initialize player or team structures based on game mode.
        
        Returns:
            Dictionary mapping player/team IDs to their card lists.
        """
        if self.team_mode:
            # Teams are labeled as 'Team A', 'Team B', etc.
            return {f'Team {chr(65 + i)}': [] for i in range(self.num_players // 2)}
        else:
            # Individual players are numbered 1 to num_players
            return {i + 1: [] for i in range(self.num_players)}
    
    def shuffle_and_distribute(self) -> Dict[Union[int, str], List[str]]:
        """
        Shuffle the deck and distribute cards evenly among players/teams.
        Ensures all cards are distributed and visible.
        
        Returns:
            Dictionary mapping players/teams to their cards.
            
        Raises:
            ValueError: If the number of players is invalid for team mode.
        """
        if self.team_mode and self.num_players % 2 != 0:
            raise ValueError("Team mode requires an even number of players.")
        
        # Shuffle the deck
        random.shuffle(self.cards)
        
        # Calculate cards per player/team
        total_cards = len(self.cards)
        cards_per_entity = total_cards // len(self.players)
        
        # Distribute cards
        for i, card in enumerate(self.cards):
            entity = list(self.players.keys())[i % len(self.players)]
            self.players[entity].append(card)
        
        return self.players
    
    def get_player_cards(self, player_id: Union[int, str]) -> List[str]:
        """
        Retrieve cards for a specific player or team.
        
        Args:
            player_id: Player number or team name.
            
        Returns:
            List of cards for the specified player/team.
            
        Raises:
            KeyError: If player/team ID is invalid.
        """
        if player_id not in self.players:
            raise KeyError(f"Invalid player/team ID: {player_id}")
        return self.players[player_id]
    
    def get_all_cards(self) -> Dict[Union[int, str], List[str]]:
        """
        Get all distributed cards for all players/teams.
        
        Returns:
            Dictionary of all players/teams and their cards.
        """
        return self.players


# Example usage
if __name__ == "__main__":
    try:
        # Individual mode with 4 players
        game = GeminitoCardGame(num_players=4, team_mode=False)
        distributed_cards = game.shuffle_and_distribute()
        print("Individual Mode Distribution:")
        for player, cards in distributed_cards.items():
            print(f"Player {player}: {cards}")
        
        # Team mode with 4 players (2 teams)
        team_game = GeminitoCardGame(num_players=4, team_mode=True)
        team_distributed = team_game.shuffle_and_distribute()
        print("\nTeam Mode Distribution:")
        for team, cards in team_distributed.items():
            print(f"{team}: {cards}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
