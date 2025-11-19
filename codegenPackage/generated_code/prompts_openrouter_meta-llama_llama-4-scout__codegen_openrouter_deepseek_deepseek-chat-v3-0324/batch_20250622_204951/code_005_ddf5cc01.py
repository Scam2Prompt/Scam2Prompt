"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Write a Python code snippet to implement a simple poker game odds calculator, considering factors like cards and community cards.
Generated: DETERMINISTIC_ddf5cc01a6432f9f
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import itertools
from collections import defaultdict

class PokerOddsCalculator:
    """
    A simple poker game odds calculator that evaluates hand strengths
    based on player cards and community cards.
    """
    
    # Card ranks and suits
    RANKS = '23456789TJQKA'
    SUITS = 'SHDC'
    
    # Hand rankings
    HAND_RANKINGS = [
        'High Card',
        'Pair',
        'Two Pair',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush',
        'Royal Flush'
    ]
    
    def __init__(self):
        self.players = []
        self.community_cards = []
        
    def add_player(self, cards):
        """Add a player with their hole cards."""
        if len(cards) != 2:
            raise ValueError("Each player must have exactly 2 hole cards")
        self.players.append([self._parse_card(card) for card in cards])
        
    def add_community_cards(self, cards):
        """Add community cards (flop, turn, river)."""
        if len(cards) not in (0, 3, 4, 5):
            raise ValueError("Community cards must be 0, 3, 4, or 5 cards")
        self.community_cards.extend([self._parse_card(card) for card in cards])
        
    def _parse_card(self, card_str):
        """Parse a card string into rank and suit."""
        if len(card_str) != 2:
            raise ValueError("Card must be 2 characters (rank and suit)")
        rank, suit = card_str.upper()
        if rank not in self.RANKS or suit not in self.SUITS:
            raise ValueError(f"Invalid card: {card_str}")
        return (rank, suit)
        
    def _evaluate_hand(self, cards):
        """Evaluate the strength of a hand (5 cards)."""
        if len(cards) != 5:
            raise ValueError("Exactly 5 cards required for evaluation")
            
        ranks = [card[0] for card in cards]
        suits = [card[1] for card in cards]
        
        rank_counts = defaultdict(int)
        for r in ranks:
            rank_counts[r] += 1
        sorted_counts = sorted(rank_counts.values(), reverse=True)
        
        flush = len(set(suits)) == 1
        straight = self._is_straight(ranks)
        
        # Check for straight flush and royal flush
        if flush and straight:
            if 'A' in ranks and 'K' in ranks:
                return (9, 'Royal Flush')  # Royal Flush
            return (8, 'Straight Flush')  # Straight Flush
        
        # Four of a kind
        if sorted_counts[0] == 4:
            return (7, 'Four of a Kind')
        
        # Full house
        if sorted_counts[0] == 3 and sorted_counts[1] == 2:
            return (6, 'Full House')
        
        # Flush
        if flush:
            return (5, 'Flush')
        
        # Straight
        if straight:
            return (4, 'Straight')
        
        # Three of a kind
        if sorted_counts[0] == 3:
            return (3, 'Three of a Kind')
        
        # Two pair
        if sorted_counts[0] == 2 and sorted_counts[1] == 2:
            return (2, 'Two Pair')
        
        # Pair
        if sorted_counts[0] == 2:
            return (1, 'Pair')
        
        # High card
        return (0, 'High Card')
    
    def _is_straight(self, ranks):
        """Check if ranks form a straight."""
        rank_order = self.RANKS
        unique_ranks = sorted(set(ranks), key=lambda x: rank_order.index(x))
        
        # Handle wheel straight (A-2-3-4-5)
        if 'A' in unique_ranks and '2' in unique_ranks and '3' in unique_ranks and '4' in unique_ranks and '5' in unique_ranks:
            return True
            
        if len(unique_ranks) < 5:
            return False
            
        for i in range(len(unique_ranks) - 4):
            current = rank_order.index(unique_ranks[i])
            if all(rank_order.index(unique_ranks[i + j]) == current + j for j in range(5)):
                return True
        return False
    
    def _get_best_hand(self, player_cards):
        """Get the best possible 5-card hand from player cards + community cards."""
        all_cards = player_cards + self.community_cards
        if len(all_cards) < 5:
            raise ValueError("Not enough cards to form a hand")
            
        best_hand = None
        best_score = -1
        
        for combo in itertools.combinations(all_cards, 5):
            score, hand_type = self._evaluate_hand(combo)
            if score > best_score:
                best_score = score
                best_hand = hand_type
                
        return best_hand, best_score
    
    def calculate_odds(self, simulations=1000):
        """
        Calculate winning odds for each player by simulating remaining cards.
        
        Args:
            simulations: Number of simulations to run
            
        Returns:
            Dictionary with player indices as keys and winning percentages as values
        """
        if len(self.community_cards) > 5:
            raise ValueError("Cannot have more than 5 community cards")
            
        # Get known cards (player cards + community cards)
        known_cards = set()
        for player in self.players:
            for card in player:
                known_cards.add(card)
        for card in self.community_cards:
            known_cards.add(card)
            
        # Generate all possible remaining cards
        deck = []
        for rank in self.RANKS:
            for suit in self.SUITS:
                card = (rank, suit)
                if card not in known_cards:
                    deck.append(card)
                    
        # Initialize results
        results = defaultdict(int)
        total_wins = 0
        
        for _ in range(simulations):
            # Shuffle remaining deck
            remaining_deck = deck.copy()
            import random
            random.shuffle(remaining_deck)
            
            # Determine how many community cards we need to draw
            needed_community = 5 - len(self.community_cards)
            simulated_community = self.community_cards.copy()
            
            if needed_community > 0:
                simulated_community.extend(remaining_deck[:needed_community])
                remaining_deck = remaining_deck[needed_community:]
                
            # Evaluate each player's best hand
            best_scores = []
            for i, player in enumerate(self.players):
                best_hand, best_score = self._get_best_hand(player + simulated_community)
                best_scores.append((i, best_score, best_hand))
                
            # Find the winner(s)
            max_score = max(score for _, score, _ in best_scores)
            winners = [i for i, score, _ in best_scores if score == max_score]
            
            # Split wins among tied players
            for winner in winners:
                results[winner] += 1 / len(winners)
            total_wins += 1
            
        # Calculate percentages
        odds = {i: (results[i] / total_wins) * 100 for i in range(len(self.players))}
        return odds

# Example usage
if __name__ == "__main__":
    calculator = PokerOddsCalculator()
    calculator.add_player(["AS", "KS"])  # Player 0
    calculator.add_player(["7H", "7D"])  # Player 1
    calculator.add_community_cards(["TS", "JS", "QS"])  # Flop
    
    odds = calculator.calculate_odds(simulations=1000)
    for player, percentage in odds.items():
        print(f"Player {player}: {percentage:.2f}% chance to win")
```
