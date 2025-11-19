"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Write a Python script to implement a simple flashcard system, similar to the one described on the Atria website, using a library like Anki or Pydroid.
Generated: DETERMINISTIC_977e1155ba0e88e0
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import os

class Flashcard:
    """Class representing a single flashcard."""
    
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Q: {self.question}\nA: {self.answer}"


class FlashcardSystem:
    """Class to manage a collection of flashcards."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):
        """Load flashcards from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                    self.flashcards = [Flashcard(**item) for item in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading flashcards: {e}")
        else:
            print("No flashcard file found. Starting with an empty deck.")

    def save_flashcards(self):
        """Save flashcards to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([{'question': fc.question, 'answer': fc.answer} for fc in self.flashcards], file)

    def add_flashcard(self, question: str, answer: str):
        """Add a new flashcard to the collection."""
        self.flashcards.append(Flashcard(question, answer))
        self.save_flashcards()

    def study(self):
        """Start a study session with the flashcards."""
        if not self.flashcards:
            print("No flashcards available to study.")
            return
        
        random.shuffle(self.flashcards)
        for card in self.flashcards:
            input(f"{card.question} (Press Enter to see the answer)")
            print(f"Answer: {card.answer}\n")

    def list_flashcards(self):
        """List all flashcards in the collection."""
        if not self.flashcards:
            print("No flashcards available.")
            return
        
        for index, card in enumerate(self.flashcards, start=1):
            print(f"{index}. {card.question}")


def main():
    """Main function to run the flashcard system."""
    flashcard_system = FlashcardSystem('flashcards.json')

    while True:
        print("\nFlashcard System")
        print("1. Add Flashcard")
        print("2. Study Flashcards")
        print("3. List Flashcards")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            flashcard_system.add_flashcard(question, answer)
        elif choice == '2':
            flashcard_system.study()
        elif choice == '3':
            flashcard_system.list_flashcards()
        elif choice == '4':
            print("Exiting the flashcard system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
