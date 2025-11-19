"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Create a Python program to simulate the "Géminito-Junior" deck with 26 cards, ensuring it adheres to the described educational level (end of 1st cycle of Conservatoire).
Generated: DETERMINISTIC_4f9918fe052ed5ff
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
from collections import defaultdict

class GeminitoJuniorDeck:
    """
    A class to simulate the "Géminito-Junior" deck with 26 cards.
    The deck is designed for educational purposes (end of 1st cycle of Conservatoire).
    """
    
    def __init__(self):
        """
        Initialize the deck with 26 cards following the Géminito-Junior specifications.
        Cards are represented as tuples (suit, value).
        """
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = []
        self.initialize_deck()
        self.shuffle()
    
    def initialize_deck(self):
        """Create the initial deck of 26 cards (7-10, J, Q, K from 4 suits)."""
        for suit in self.suits:
            for value in self.values:
                self.deck.append((suit, value))
    
    def shuffle(self):
        """Shuffle the deck using Fisher-Yates algorithm."""
        for i in range(len(self.deck) - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
    
    def deal_card(self):
        """Deal one card from the top of the deck."""
        if not self.deck:
            raise ValueError("Deck is empty, no cards left to deal.")
        return self.deck.pop()
    
    def deal_hand(self, num_cards=5):
        """
        Deal a hand of cards from the deck.
        
        Args:
            num_cards (int): Number of cards to deal. Default is 5.
        
        Returns:
            list: List of cards dealt.
        
        Raises:
            ValueError: If num_cards exceeds available cards.
        """
        if num_cards > len(self.deck):
            raise ValueError(f"Not enough cards in deck. Requested: {num_cards}, Available: {len(self.deck)}")
        return [self.deal_card() for _ in range(num_cards)]
    
    def reset_deck(self):
        """Reset the deck to its initial state and shuffle."""
        self.deck = []
        self.initialize_deck()
        self.shuffle()
    
    def count_cards_by_suit(self):
        """Count how many cards remain in the deck for each suit."""
        suit_counts = defaultdict(int)
        for suit, _ in self.deck:
            suit_counts[suit] += 1
        return dict(suit_counts)
    
    def count_cards_by_value(self):
        """Count how many cards remain in the deck for each value."""
        value_counts = defaultdict(int)
        for _, value in self.deck:
            value_counts[value] += 1
        return dict(value_counts)
    
    def __str__(self):
        """Return a string representation of the current deck state."""
        return f"Géminito-Junior Deck: {len(self.deck)} cards remaining"

# Example usage
if __name__ == "__main__":
    deck = GeminitoJuniorDeck()
    print(deck)
    
    hand = deck.deal_hand(5)
    print("Dealt hand:", hand)
    
    print("Remaining cards by suit:", deck.count_cards_by_suit())
    print("Remaining cards by value:", deck.count_cards_by_value())
    
    deck.reset_deck()
    print("\nDeck reset and shuffled:", deck)
```
