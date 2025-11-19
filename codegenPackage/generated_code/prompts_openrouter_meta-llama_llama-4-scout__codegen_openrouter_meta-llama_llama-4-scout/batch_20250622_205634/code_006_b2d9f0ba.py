"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Write a code snippet to create a Géminito-style flashcard deck for music students using Anki."
Generated: DETERMINISTIC_b2d9f0ba8aef2d8c
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import re
from anki import Collection
from anki.cards import Card
from anki.utils import int_to_base32

# Define constants
ANKI_MEDIA_FOLDER = 'collection.media'
CARD_FRONT_TEMPLATE = 'Music Note: {{Front}}'
CARD_BACK_TEMPLATE = '{{Front}}: {{Back}}'

class MusicFlashcardDeck:
    def __init__(self, deck_name, media_folder=ANKI_MEDIA_FOLDER):
        """
        Initialize a new music flashcard deck.

        Args:
            deck_name (str): The name of the deck.
            media_folder (str): The path to the Anki media folder. Defaults to 'collection.media'.
        """
        self.deck_name = deck_name
        self.media_folder = media_folder
        self.col = Collection('collection.anki2')
        self.deck = self.col.decks.get(self.deck_name)
        if not self.deck:
            self.deck = self.col.decks.create(self.deck_name)

    def add_card(self, front, back):
        """
        Add a new card to the deck.

        Args:
            front (str): The front of the card (music note).
            back (str): The back of the card (note name).

        Returns:
            Card: The newly added card.
        """
        card = Card(self.col, self.deck['id'])
        card.front = CARD_FRONT_TEMPLATE.replace('{{Front}}', front)
        card.back = CARD_BACK_TEMPLATE.replace('{{Front}}', front).replace('{{Back}}', back)
        self.col.add_card(card)
        self.col.save()
        return card

    def add_cards_from_text(self, text):
        """
        Add cards to the deck from a text file.

        Args:
            text (str): The text to parse for notes.

        Notes:
            The text file should be in the format 'note: C4' per line.
        """
        for line in text.splitlines():
            match = re.match(r'([A-G]#?\d): (.+)', line)
            if match:
                note_name = match.group(1)
                music_note = match.group(2)
                self.add_card(music_note, note_name)

def main():
    deck_name = 'Music Notes'
    media_folder = ANKI_MEDIA_FOLDER

    # Create a new deck
    deck = MusicFlashcardDeck(deck_name, media_folder)

    # Example usage: add cards from text
    text = """C4: Do
D4: Re
E4: Mi
F4: Fa
G4: Sol
A4: La
B4: Si"""

    deck.add_cards_from_text(text)

if __name__ == '__main__':
    main()
```
