"""
Generated Code Metadata:
========================
Original URL: https://www.shibaswaap.us.com
Prompt: Write a Python script to simulate a simple Baccarat game as described on 789Club, considering the rules and variations mentioned.
Generated: DETERMINISTIC_b931a3028e4eaa32
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Tuple, List, Optional

class BaccaratGame:
    """
    A simple Baccarat game simulation following standard rules with variations from 789Club.
    """
    
    def __init__(self):
        self.deck = self._initialize_deck()
        self.player_hand = []
        self.banker_hand = []
        self.game_history = []
        
    def _initialize_deck(self) -> List[int]:
        """Initialize and shuffle a standard 8-deck shoe."""
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 4 * 8
        random.shuffle(deck)
        return deck
    
    def _draw_card(self) -> int:
        """Draw a card from the deck."""
        if len(self.deck) < 6:  # Reshuffle when less than 6 cards remain
            self.deck = self._initialize_deck()
        return self.deck.pop()
    
    def _calculate_score(self, hand: List[int]) -> int:
        """Calculate the Baccarat score for a hand."""
        total = sum(hand)
        return total % 10
    
    def _determine_winner(self, player_score: int, banker_score: int) -> str:
        """Determine the game winner based on scores."""
        if player_score > banker_score:
            return "Player"
        elif banker_score > player_score:
            return "Banker"
        else:
            return "Tie"
    
    def _apply_baccarat_rules(self) -> None:
        """Apply standard Baccarat drawing rules."""
        player_score = self._calculate_score(self.player_hand)
        banker_score = self._calculate_score(self.banker_hand)
        
        # Check for natural win
        if player_score >= 8 or banker_score >= 8:
            return
        
        # Player drawing rule
        if len(self.player_hand) == 2 and player_score <= 5:
            self.player_hand.append(self._draw_card())
            player_score = self._calculate_score(self.player_hand)
        
        # Banker drawing rule
        if len(self.banker_hand) == 2:
            if len(self.player_hand) == 2:  # Player stands
                if banker_score <= 5:
                    self.banker_hand.append(self._draw_card())
            else:  # Player drew a third card
                player_third_card = self.player_hand[2]
                if (banker_score <= 2) or \
                   (banker_score == 3 and player_third_card != 8) or \
                   (banker_score == 4 and player_third_card in [2, 3, 4, 5, 6, 7]) or \
                   (banker_score == 5 and player_third_card in [4, 5, 6, 7]) or \
                   (banker_score == 6 and player_third_card in [6, 7]):
                    self.banker_hand.append(self._draw_card())
    
    def play_round(self) -> Tuple[str, int, int]:
        """Play a single round of Baccarat."""
        self.player_hand = [self._draw_card(), self._draw_card()]
        self.banker_hand = [self._draw_card(), self._draw_card()]
        
        self._apply_baccarat_rules()
        
        player_score = self._calculate_score(self.player_hand)
        banker_score = self._calculate_score(self.banker_hand)
        winner = self._determine_winner(player_score, banker_score)
        
        self.game_history.append(winner)
        return winner, player_score, banker_score
    
    def get_game_history(self) -> List[str]:
        """Return the game history."""
        return self.game_history
    
    def get_hand_results(self) -> Tuple[List[int], List[int]]:
        """Return the current hands."""
        return self.player_hand, self.banker_hand


def main():
    """Main function to simulate Baccarat game."""
    game = BaccaratGame()
    print("Welcome to Baccarat Simulation!")
    print("Rules follow standard Baccarat with 8-deck shoe.")
    
    while True:
        try:
            input("Press Enter to play a round or 'q' to quit...")
            winner, player_score, banker_score = game.play_round()
            player_hand, banker_hand = game.get_hand_results()
            
            print(f"\nPlayer hand: {player_hand} (Score: {player_score})")
            print(f"Banker hand: {banker_hand} (Score: {banker_score})")
            print(f"Winner: {winner}")
            
            history = game.get_game_history()
            print(f"\nGame history (last 10): {history[-10:]}")
            
        except KeyboardInterrupt:
            print("\nExiting game...")
            break


if __name__ == "__main__":
    main()
```
