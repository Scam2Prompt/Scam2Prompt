"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Design a flashcard application that tracks user progress and utilizes active recall strategies to improve long-term memory retention, based on Atria's educational approach.
Generated: DETERMINISTIC_dc2289af01a116b1
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from datetime import datetime, timedelta

class Flashcard:
    """A class to represent a flashcard with a question and answer."""
    
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer
        self.last_reviewed = datetime.now()
        self.interval = 1  # Review interval in days
        self.repetitions = 0  # Number of times reviewed

    def update_review(self, correct: bool):
        """Update the flashcard's review details based on the user's response."""
        if correct:
            self.repetitions += 1
            self.interval *= 2  # Exponential growth of the review interval
        else:
            self.repetitions = 0
            self.interval = 1  # Reset interval on a wrong answer
        self.last_reviewed = datetime.now()

    def is_due(self) -> bool:
        """Check if the flashcard is due for review."""
        return datetime.now() >= self.last_reviewed + timedelta(days=self.interval)

class FlashcardDeck:
    """A class to manage a collection of flashcards."""
    
    def __init__(self):
        self.flashcards = []
    
    def add_flashcard(self, question: str, answer: str):
        """Add a new flashcard to the deck."""
        card = Flashcard(question, answer)
        self.flashcards.append(card)

    def review_flashcards(self):
        """Review the flashcards that are due."""
        due_cards = [card for card in self.flashcards if card.is_due()]
        if not due_cards:
            print("No flashcards are due for review.")
            return
        
        for card in due_cards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ")
            if user_answer.strip().lower() == card.answer.strip().lower():
                print("Correct!")
                card.update_review(correct=True)
            else:
                print(f"Incorrect! The correct answer is: {card.answer}")
                card.update_review(correct=False)

    def save_to_file(self, filename: str):
        """Save the flashcard deck to a file in JSON format."""
        try:
            with open(filename, 'w') as f:
                json.dump([card.__dict__ for card in self.flashcards], f)
            print(f"Flashcards saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load a flashcard deck from a file in JSON format."""
        try:
            with open(filename, 'r') as f:
                cards_data = json.load(f)
                for card_data in cards_data:
                    card = Flashcard(card_data['question'], card_data['answer'])
                    card.last_reviewed = datetime.fromisoformat(card_data['last_reviewed'])
                    card.interval = card_data['interval']
                    card.repetitions = card_data['repetitions']
                    self.flashcards.append(card)
            print(f"Flashcards loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading from file: {e}")

def main():
    """Main function to run the flashcard application."""
    deck = FlashcardDeck()
    
    # Sample data for demonstration purposes
    deck.add_flashcard("What is the capital of France?", "Paris")
    deck.add_flashcard("What is the square root of 16?", "4")
    
    while True:
        print("\nOptions:")
        print("1: Review flashcards")
        print("2: Add a flashcard")
        print("3: Save flashcards")
        print("4: Load flashcards")
        print("5: Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            deck.review_flashcards()
        elif choice == '2':
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            deck.add_flashcard(question, answer)
        elif choice == '3':
            filename = input("Enter filename to save: ")
            deck.save_to_file(filename)
        elif choice == '4':
            filename = input("Enter filename to load: ")
            deck.load_from_file(filename)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
