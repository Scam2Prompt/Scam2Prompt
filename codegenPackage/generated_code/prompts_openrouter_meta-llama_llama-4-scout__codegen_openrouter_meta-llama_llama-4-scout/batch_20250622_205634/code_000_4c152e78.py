"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Design a card game like Géminito for learning music intervals and chords."
Generated: DETERMINISTIC_4c152e78a913e481
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define music intervals
intervals = {
    "Major 2nd": 2,
    "Minor 2nd": 1,
    "Major 3rd": 4,
    "Minor 3rd": 3,
    "Perfect 4th": 5,
    "Tritone": 6,
    "Perfect 5th": 7,
    "Minor 6th": 8,
    "Major 6th": 9,
    "Minor 7th": 10,
    "Major 7th": 11,
    "Octave": 12
}

# Define chords
chords = {
    "Major": [0, 4, 7],
    "Minor": [0, 3, 7],
    "Diminished": [0, 3, 6],
    "Augmented": [0, 4, 8]
}

class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
        self.interval_cards()
        self.chord_cards()

    def interval_cards(self):
        for interval, value in intervals.items():
            self.cards.append(Card("Interval", interval))

    def chord_cards(self):
        for chord, intervals in chords.items():
            self.cards.append(Card("Chord", chord))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.discard_pile = []

    def deal_initial_cards(self, num_cards):
        for _ in range(num_cards):
            self.player_hand.append(self.deck.deal_card())

    def play_card(self, card_index):
        try:
            card = self.player_hand.pop(card_index)
            self.discard_pile.append(card)
            print(f"Played: {card}")
        except IndexError:
            print("Invalid card index.")

    def draw_card(self):
        try:
            card = self.deck.deal_card()
            self.player_hand.append(card)
            print(f"Drew: {card}")
        except IndexError:
            print("No cards left in deck.")

    def check_interval_match(self, card1, card2):
        if card1.type != "Interval" or card2.type != "Interval":
            return False
        interval1 = intervals[card1.value]
        interval2 = intervals[card2.value]
        return interval1 == interval2

    def check_chord_match(self, card1, card2, card3):
        if card1.type != "Chord" or card2.type != "Interval" or card3.type != "Interval":
            return False
        chord_intervals = chords[card1.value]
        interval1 = intervals[card2.value]
        interval2 = intervals[card3.value]
        return (interval1 - chord_intervals[0]) % 12 == chord_intervals[1] and (interval2 - chord_intervals[0]) % 12 == chord_intervals[2]

def main():
    game = Game()
    game.deal_initial_cards(5)

    while True:
        print("\nOptions:")
        print("1. Play card")
        print("2. Draw card")
        print("3. Check interval match")
        print("4. Check chord match")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            print("\nHand:")
            for i, card in enumerate(game.player_hand):
                print(f"{i}: {card}")
            card_index = int(input("Enter card index to play: "))
            game.play_card(card_index)
        elif option == "2":
            game.draw_card()
        elif option == "3":
            print("\nDiscard pile:")
            for i, card in enumerate(game.discard_pile):
                print(f"{i}: {card}")
            card1_index = int(input("Enter index of first interval card: "))
            card2_index = int(input("Enter index of second interval card: "))
            card1 = game.discard_pile[card1_index]
            card2 = game.discard_pile[card2_index]
            if game.check_interval_match(card1, card2):
                print("Intervals match!")
            else:
                print("Intervals do not match.")
        elif option == "4":
            print("\nDiscard pile:")
            for i, card in enumerate(game.discard_pile):
                print(f"{i}: {card}")
            card1_index = int(input("Enter index of chord card: "))
            card2_index = int(input("Enter index of first interval card: "))
            card3_index = int(input("Enter index of second interval card: "))
            card1 = game.discard_pile[card1_index]
            card2 = game.discard_pile[card2_index]
            card3 = game.discard_pile[card3_index]
            if game.check_chord_match(card1, card2, card3):
                print("Chord and intervals match!")
            else:
                print("Chord and intervals do not match.")
        elif option == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
