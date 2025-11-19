"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Provide a step-by-step guide to implement a digital card game using Géminito's rules, focusing on educational features for music theory training.
Generated: DETERMINISTIC_cc0d5e64c0eb9606
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_card_game.py

import random

class Card:
    """Represents a card in the Géminito deck."""
    
    def __init__(self, pitch, rhythm, notation):
        """
        Initializes a Card object.

        Args:
            pitch (str): The pitch of the card (e.g., C, D, E).
            rhythm (str): The rhythm of the card (e.g., quarter, half, whole).
            notation (str): The musical notation of the card (e.g., C4, D5).
        """
        self.pitch = pitch
        self.rhythm = rhythm
        self.notation = notation

    def __repr__(self):
        return f"Card(pitch={self.pitch}, rhythm={self.rhythm}, notation={self.notation})"


class Deck:
    """Represents a deck of Géminito cards."""
    
    def __init__(self):
        """
        Initializes a Deck object with 120 cards.
        """
        self.cards = []
        self.pitches = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.rhythms = ['quarter', 'half', 'whole']
        self.notations = [f"{pitch}{i}" for pitch in self.pitches for i in range(1, 8) for _ in range(3)]

        for _ in range(40):
            for rhythm in self.rhythms:
                for notation in self.notations:
                    pitch = notation[0]
                    self.cards.append(Card(pitch, rhythm, notation))

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """
        Deals a card from the deck.

        Returns:
            Card: The dealt card.

        Raises:
            ValueError: If the deck is empty.
        """
        if not self.cards:
            raise ValueError("The deck is empty.")
        return self.cards.pop()


class Player:
    """Represents a player in the Géminito game."""
    
    def __init__(self, name):
        """
        Initializes a Player object.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        """
        Draws a card from the deck.

        Args:
            deck (Deck): The deck to draw from.
        """
        self.hand.append(deck.deal_card())

    def play_card(self, index):
        """
        Plays a card from the player's hand.

        Args:
            index (int): The index of the card to play.

        Returns:
            Card: The played card.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            return self.hand.pop(index)
        except IndexError:
            raise IndexError("Invalid card index.")


class Game:
    """Represents a game of Géminito."""
    
    def __init__(self, player1, player2):
        """
        Initializes a Game object.

        Args:
            player1 (Player): The first player.
            player2 (Player): The second player.
        """
        self.player1 = player1
        self.player2 = player2
        self.deck = Deck()
        self.deck.shuffle()

    def deal_initial_cards(self):
        """Deals the initial 10 cards to each player."""
        for _ in range(10):
            self.player1.draw_card(self.deck)
            self.player2.draw_card(self.deck)

    def play_game(self):
        """
        Plays the game.

        Returns:
            str: The winner's name.
        """
        self.deal_initial_cards()

        while self.deck.cards:
            # Player 1's turn
            print(f"\n{self.player1.name}'s turn:")
            for i, card in enumerate(self.player1.hand):
                print(f"{i}: {card}")
            index = int(input("Enter the index of the card to play: "))
            played_card = self.player1.play_card(index)
            print(f"Played card: {played_card}")

            # Player 2's turn
            print(f"\n{self.player2.name}'s turn:")
            for i, card in enumerate(self.player2.hand):
                print(f"{i}: {card}")
            index = int(input("Enter the index of the card to play: "))
            played_card = self.player2.play_card(index)
            print(f"Played card: {played_card}")

        # Determine the winner
        if len(self.player1.hand) > len(self.player2.hand):
            return self.player1.name
        elif len(self.player2.hand) > len(self.player1.hand):
            return self.player2.name
        else:
            return "It's a tie!"


def main():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    game = Game(player1, player2)
    winner = game.play_game()
    print(f"\nThe winner is: {winner}")


if __name__ == "__main__":
    main()
```
