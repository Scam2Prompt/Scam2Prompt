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

class GeminititoCard:
    """Represents a Géminito card."""
    def __init__(self, name, image, value):
        self.name = name
        self.image = image
        self.value = value

    def __repr__(self):
        return f"GeminititoCard(name='{self.name}', image='{self.image}', value={self.value})"


class GeminititoGame:
    """Manages Géminito gameplay, including card shuffling and distribution."""
    def __init__(self, cards, num_teams, cards_per_player):
        self.cards = cards
        self.num_teams = num_teams
        self.cards_per_player = cards_per_player

    def shuffle_cards(self):
        """Shuffles the deck of Géminito cards."""
        random.shuffle(self.cards)

    def distribute_cards(self):
        """Distributes the shuffled cards to teams or individual players."""
        if self.num_teams > 0:
            # Team mode
            team_cards = self._distribute_cards_to_teams()
        else:
            # Individual mode
            team_cards = self._distribute_cards_to_individuals()

        return team_cards

    def _distribute_cards_to_teams(self):
        """Distributes cards to teams."""
        total_players = self.num_teams
        cards_per_player = self.cards_per_player

        if len(self.cards) < total_players * cards_per_player:
            raise ValueError("Not enough cards for the number of players.")

        team_cards = []
        start_index = 0
        for _ in range(total_players):
            team_hand = self.cards[start_index:start_index + cards_per_player]
            team_cards.append(team_hand)
            start_index += cards_per_player

        return team_cards

    def _distribute_cards_to_individuals(self):
        """Distributes cards to individual players."""
        total_players = len(self.cards) // self.cards_per_player
        if len(self.cards) % self.cards_per_player != 0:
            print(f"Warning: {len(self.cards) % self.cards_per_player} cards left over.")

        individual_cards = []
        start_index = 0
        for _ in range(total_players):
            individual_hand = self.cards[start_index:start_index + self.cards_per_player]
            individual_cards.append(individual_hand)
            start_index += self.cards_per_player

        return individual_cards


def create_geminitito_cards():
    """Creates a list of Géminito cards."""
    # Example card creation
    cards = [
        GeminititoCard("Card 1", "Image 1", 10),
        GeminititoCard("Card 2", "Image 2", 20),
        GeminititoCard("Card 3", "Image 3", 30),
        GeminititoCard("Card 4", "Image 4", 40),
        GeminititoCard("Card 5", "Image 5", 50),
        GeminititoCard("Card 6", "Image 6", 60),
    ]
    return cards


def main():
    try:
        cards = create_geminitito_cards()
        game = GeminititoGame(cards, num_teams=2, cards_per_player=3)
        game.shuffle_cards()
        distributed_cards = game.distribute_cards()

        for i, hand in enumerate(distributed_cards):
            print(f"Player/Team {i+1}'s hand: {hand}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
