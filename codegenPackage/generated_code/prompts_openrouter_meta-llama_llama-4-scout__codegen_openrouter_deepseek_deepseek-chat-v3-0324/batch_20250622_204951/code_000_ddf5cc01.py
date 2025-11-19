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
import collections

class PokerOddsCalculator:
    """
    A simple poker game odds calculator that evaluates hand strengths
    based on private cards and community cards.
    """
    
    # Card ranks and suits
    RANKS = '23456789TJQKA'
    SUITS = 'CDHS'
    
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
        self.deck = self._create_deck()
        
    def _create_deck(self):
        """Create a standard 52-card deck."""
        return [rank + suit for suit in self.SUITS for rank in self.RANKS]
    
    def _get_remaining_deck(self, known_cards):
        """Return remaining deck after removing known cards."""
        return [card for card in self.deck if card not in known_cards]
    
    def _evaluate_hand(self, cards):
        """Evaluate the strength of a poker hand."""
        if len(cards) != 5:
            raise ValueError("A poker hand must consist of exactly 5 cards")
            
        ranks = [self.RANKS.index(card[0]) for card in cards]
        suits = [card[1] for card in cards]
        
        rank_counter = collections.Counter(ranks)
        suit_counter = collections.Counter(suits)
        
        # Check for flush
        flush = len(suit_counter) == 1
        
        # Check for straight
        unique_ranks = sorted(rank_counter.keys())
        straight = (
            len(unique_ranks) == 5 and 
            unique_ranks[-1] - unique_ranks[0] == 4
        ) or (
            set(unique_ranks) == {0, 1, 2, 3, 12}  # Ace-low straight (A-2-3-4-5)
        )
        
        # Determine hand strength
        if straight and flush:
            if unique_ranks[-1] == 12 and unique_ranks[-2] == 11:  # Royal Flush
                return (9,)
            return (8, unique_ranks[-1])  # Straight Flush
        elif 4 in rank_counter.values():
            return (7, rank_counter.most_common(1)[0][0])  # Four of a Kind
        elif sorted(rank_counter.values()) == [2, 3]:
            return (6, rank_counter.most_common(2)[0][0], rank_counter.most_common(2)[1][0])  # Full House
        elif flush:
            return (5, sorted(ranks, reverse=True))  # Flush
        elif straight:
            return (4, unique_ranks[-1])  # Straight
        elif 3 in rank_counter.values():
            return (3, rank_counter.most_common(1)[0][0])  # Three of a Kind
        elif list(rank_counter.values()).count(2) == 2:
            pairs = sorted([r for r, count in rank_counter.items() if count == 2], reverse=True)
            return (2, pairs[0], pairs[1])  # Two Pair
        elif 2 in rank_counter.values():
            return (1, rank_counter.most_common(1)[0][0])  # Pair
        else:
            return (0, sorted(ranks, reverse=True))  # High Card
    
    def calculate_odds(self, player_cards, community_cards=None, num_opponents=1, simulations=1000):
        """
        Calculate winning odds for a player's hand against opponents.
        
        Args:
            player_cards: List of player's private cards (e.g., ['AS', 'KD'])
            community_cards: List of community cards (e.g., ['TS', 'JH', 'QC'])
            num_opponents: Number of opponents to simulate
            simulations: Number of simulations to run
            
        Returns:
            Dictionary with win/tie probabilities and hand strength distribution
        """
        if community_cards is None:
            community_cards = []
            
        if len(player_cards) != 2:
            raise ValueError("Player must have exactly 2 cards")
            
        if len(community_cards) > 5:
            raise ValueError("Community cards cannot exceed 5")
            
        known_cards = player_cards + community_cards
        remaining_deck = self._get_remaining_deck(known_cards)
        
        wins = 0
        ties = 0
        hand_strengths = {i: 0 for i in range(len(self.HAND_RANKINGS))}
        
        for _ in range(simulations):
            # Shuffle remaining deck
            import random
            random.shuffle(remaining_deck)
            
            # Deal community cards if needed
            needed_community = 5 - len(community_cards)
            simulated_community = community_cards + remaining_deck[:needed_community]
            
            # Deal opponent cards
            opponent_cards = []
            for _ in range(num_opponents):
                start = needed_community + _ * 2
                opponent_cards.append(remaining_deck[start:start+2])
            
            # Evaluate player's hand
            player_hand = player_cards + simulated_community
            player_best = self._get_best_hand(player_hand)
            player_strength = self._evaluate_hand(player_best)
            hand_strengths[player_strength[0]] += 1
            
            # Evaluate opponents' hands
            opponents_best = []
            for cards in opponent_cards:
                opponent_hand = cards + simulated_community
                opponents_best.append(self._evaluate_hand(self._get_best_hand(opponent_hand)))
            
            # Compare hands
            player_wins = True
            player_ties = False
            
            for opponent_strength in opponents_best:
                if opponent_strength > player_strength:
                    player_wins = False
                    break
                elif opponent_strength == player_strength:
                    player_ties = True
            
            if player_wins and not player_ties:
                wins += 1
            elif player_ties:
                ties += 1
        
        return {
            'win_probability': wins / simulations,
            'tie_probability': ties / simulations,
            'hand_strengths': {self.HAND_RANKINGS[k]: v/simulations 
                              for k, v in hand_strengths.items()}
        }
    
    def _get_best_hand(self, cards):
        """Get the best possible 5-card hand from 5-7 cards."""
        if len(cards) < 5:
            raise ValueError("Need at least 5 cards to make a hand")
            
        if len(cards) == 5:
            return cards
            
        # Try all combinations of 5 cards
        best_hand = None
        best_strength = None
        
        for combo in itertools.combinations(cards, 5):
            strength = self._evaluate_hand(combo)
            if best_strength is None or strength > best_strength:
                best_strength = strength
                best_hand = combo
                
        return best_hand
```
