"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Generate a list of 10 different solitaire games (e.g., Forty Thieves, Yukon, Scorpion) and their unique rules using a programming language of your choice.
Generated: DETERMINISTIC_9885f1376b6ccd9e
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List

@dataclass
class SolitaireGame:
    name: str
    rules: List[str]

def generate_solitaire_games() -> List[SolitaireGame]:
    """Generate a list of 10 different solitaire games with their rules."""
    return [
        SolitaireGame(
            name="Klondike",
            rules=[
                "Standard 52-card deck",
                "7 tableau piles with increasing number of face-down cards",
                "Build down in alternating colors",
                "Move sequences of cards if they are in order",
                "Foundation piles built up by suit from Ace to King"
            ]
        ),
        SolitaireGame(
            name="Spider",
            rules=[
                "Two decks (104 cards)",
                "10 tableau piles with 54 cards dealt (6 cards in first 4 piles, 5 in last 6)",
                "Build down in suit (sequences can be moved together)",
                "Complete sequences from King to Ace are removed",
                "No foundation piles - goal is to remove all cards"
            ]
        ),
        SolitaireGame(
            name="FreeCell",
            rules=[
                "Standard 52-card deck",
                "4 free cells (can hold any single card)",
                "8 tableau piles (4 with 7 cards, 4 with 6 cards)",
                "Build down in alternating colors",
                "Foundation piles built up by suit from Ace to King"
            ]
        ),
        SolitaireGame(
            name="Pyramid",
            rules=[
                "Standard 52-card deck",
                "Cards arranged in pyramid shape (28 cards)",
                "Remove pairs of cards that add up to 13 (King=13, Queen=12, Jack=11, Ace=1)",
                "Top card of waste pile can be used",
                "Goal is to remove all cards from pyramid"
            ]
        ),
        SolitaireGame(
            name="Forty Thieves",
            rules=[
                "Two decks (104 cards)",
                "10 tableau piles with 4 cards each (all face-up)",
                "Build down by suit",
                "Only top card can be moved",
                "Foundation piles built up by suit from Ace to King"
            ]
        ),
        SolitaireGame(
            name="Yukon",
            rules=[
                "Standard 52-card deck",
                "7 tableau piles (similar to Klondike but all cards face-up)",
                "Build down in alternating colors",
                "Can move any sequence of properly ordered cards",
                "Foundation piles built up by suit from Ace to King"
            ]
        ),
        SolitaireGame(
            name="Scorpion",
            rules=[
                "Standard 52-card deck",
                "7 tableau piles (3 with 7 cards, 4 with 6 cards)",
                "Build down in suit (sequences can be moved together)",
                "No foundation piles - goal is to arrange cards in descending order by suit",
                "Empty tableau piles can be filled with any card or sequence"
            ]
        ),
        SolitaireGame(
            name="Golf",
            rules=[
                "Standard 52-card deck",
                "7 tableau piles with 5 cards each (all face-up)",
                "Stock pile with remaining cards",
                "Build up or down regardless of suit",
                "Goal is to remove all cards by matching with waste pile"
            ]
        ),
        SolitaireGame(
            name="Canfield",
            rules=[
                "Standard 52-card deck",
                "Reserve pile of 13 cards (only top card playable)",
                "4 tableau piles starting with one card each",
                "Build down in alternating colors",
                "Foundation piles built up by suit starting from a randomly chosen card"
            ]
        ),
        SolitaireGame(
            name="TriPeaks",
            rules=[
                "Standard 52-card deck",
                "Three peaks of cards (28 cards total in layout)",
                "Build up or down regardless of suit",
                "Only cards one rank higher or lower than waste pile can be removed",
                "Goal is to remove all cards from the peaks"
            ]
        )
    ]

if __name__ == "__main__":
    games = generate_solitaire_games()
    for i, game in enumerate(games, 1):
        print(f"{i}. {game.name}")
        for rule in game.rules:
            print(f"   - {rule}")
        print()
```
