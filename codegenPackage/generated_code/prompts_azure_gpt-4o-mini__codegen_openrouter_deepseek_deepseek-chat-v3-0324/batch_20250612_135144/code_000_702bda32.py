"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Generate a Python script that utilizes flashcard techniques to enhance memory retention for medical exam preparation, similar to the methods described on Atria's learning platform.
Generated: DETERMINISTIC_702bda32409bd648
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os
from datetime import datetime, timedelta

class Flashcard:
    """Represents a single flashcard with question, answer, and learning metrics."""
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category
        self.streak = 0
        self.last_reviewed = None
        self.next_review = datetime.now()
    
    def to_dict(self):
        """Convert flashcard to dictionary for serialization."""
        return {
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'streak': self.streak,
            'last_reviewed': self.last_reviewed.isoformat() if self.last_reviewed else None,
            'next_review': self.next_review.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create flashcard from dictionary."""
        card = cls(data['question'], data['answer'], data['category'])
        card.streak = data['streak']
        card.last_reviewed = datetime.fromisoformat(data['last_reviewed']) if data['last_reviewed'] else None
        card.next_review = datetime.fromisoformat(data['next_review'])
        return card

class FlashcardDeck:
    """Manages a collection of flashcards with spaced repetition functionality."""
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.categories = set()
    
    def add_card(self, question, answer, category):
        """Add a new flashcard to the deck."""
        card = Flashcard(question, answer, category)
        self.cards.append(card)
        self.categories.add(category)
        return card
    
    def get_due_cards(self):
        """Retrieve cards that are due for review."""
        now = datetime.now()
        return [card for card in self.cards if card.next_review <= now]
    
    def review_card(self, card, performance):
        """
        Update card metrics based on review performance.
        Performance: 0 (incorrect), 1 (correct with difficulty), 2 (correct easily)
        """
        card.last_reviewed = datetime.now()
        
        if performance == 0:
            card.streak = 0
            card.next_review = datetime.now() + timedelta(minutes=10)
        elif performance == 1:
            card.streak += 1
            interval = timedelta(days=1) * card.streak
            card.next_review = datetime.now() + interval
        else:
            card.streak += 2
            interval = timedelta(days=3) * card.streak
            card.next_review = datetime.now() + interval
    
    def save_to_file(self, filename):
        """Save the deck to a JSON file."""
        data = {
            'name': self.name,
            'cards': [card.to_dict() for card in self.cards]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename):
        """Load a deck from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        deck = cls(data['name'])
        deck.cards = [Flashcard.from_dict(card_data) for card_data in data['cards']]
        deck.categories = {card.category for card in deck.cards}
        return deck

class FlashcardApp:
    """Main application for managing and reviewing flashcards."""
    def __init__(self):
        self.decks = {}
        self.current_deck = None
    
    def create_deck(self, name):
        """Create a new flashcard deck."""
        if name in self.decks:
            raise ValueError(f"Deck '{name}' already exists.")
        self.decks[name] = FlashcardDeck(name)
        return self.decks[name]
    
    def load_deck(self, filename):
        """Load a deck from file."""
        deck = FlashcardDeck.load_from_file(filename)
        if deck.name in self.decks:
            raise ValueError(f"Deck '{deck.name}' already loaded.")
        self.decks[deck.name] = deck
        return deck
    
    def save_all_decks(self, directory='decks'):
        """Save all decks to files in the specified directory."""
        os.makedirs(directory, exist_ok=True)
        for name, deck in self.decks.items():
            filename = os.path.join(directory, f"{name.replace(' ', '_')}.json")
            deck.save_to_file(filename)
    
    def review_session(self, deck_name=None, category=None, limit=None):
        """Conduct a review session with the specified deck."""
        deck = self.decks[deck_name] if deck_name else self.current_deck
        if not deck:
            raise ValueError("No deck selected for review.")
        
        due_cards = deck.get_due_cards()
        if category:
            due_cards = [card for card in due_cards if card.category == category]
        
        if limit:
            due_cards = due_cards[:limit]
        
        if not due_cards:
            print("No cards due for review at this time.")
            return
        
        random.shuffle(due_cards)
        print(f"\nStarting review session with {len(due_cards)} cards...\n")
        
        for i, card in enumerate(due_cards, 1):
            print(f"Card {i}/{len(due_cards)}")
            print(f"Category: {card.category}")
            print(f"Question: {card.question}")
            input("Press Enter to reveal answer...")
            print(f"Answer: {card.answer}\n")
            
            while True:
                try:
                    performance = int(input("How well did you know this? (0=Incorrect, 1=Hard, 2=Easy): "))
                    if 0 <= performance <= 2:
                        break
                    print("Please enter 0, 1, or 2.")
                except ValueError:
                    print("Please enter a number.")
            
            deck.review_card(card, performance)
            print(f"Next review scheduled for: {card.next_review.strftime('%Y-%m-%d %H:%M')}\n")
        
        print("Review session completed!")

def main():
    """Main entry point for the flashcard application."""
    app = FlashcardApp()
    
    # Sample medical flashcards (could be loaded from file in real usage)
    try:
        deck = app.create_deck("Medical Terminology")
        deck.add_card("What does 'CNS' stand for?", "Central Nervous System", "Abbreviations")
        deck.add_card("What is the medical term for high blood pressure?", "Hypertension", "Conditions")
        deck.add_card("What does 'STAT' mean in medical orders?", "Immediately", "Abbreviations")
        deck.add_card("What is the normal range for blood pH?", "7.35-7.45", "Physiology")
        deck.add_card("What does 'PRN' stand for in prescriptions?", "As needed", "Abbreviations")
    except ValueError as e:
        print(f"Error creating sample deck: {e}")
    
    # Start review session
    try:
        app.current_deck = deck
        app.review_session(category="Abbreviations", limit=3)
    except Exception as e:
        print(f"Error during review session: {e}")
    
    # Save decks
    try:
        app.save_all_decks()
    except Exception as e:
        print(f"Error saving decks: {e}")

if __name__ == "__main__":
    main()
```
