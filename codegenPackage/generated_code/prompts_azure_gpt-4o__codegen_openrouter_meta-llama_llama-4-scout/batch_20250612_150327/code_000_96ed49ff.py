"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Write Python code to create a flashcard system for active recall, incorporating keywords and concepts relevant to UKMPPD preparation as described on the Atria website.
Generated: DETERMINISTIC_96ed49fff0bf5f6a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flashcard_system.py

import random
import json
import os

class Flashcard:
    """Represents a flashcard with a question and an answer."""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardSystem:
    """Manages a collection of flashcards for active recall."""

    def __init__(self, data_file):
        self.data_file = data_file
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        """Loads flashcards from a JSON file."""
        if not os.path.exists(self.data_file):
            return []

        with open(self.data_file, 'r') as file:
            data = json.load(file)
            return [Flashcard(card['question'], card['answer']) for card in data]

    def save_flashcards(self):
        """Saves flashcards to a JSON file."""
        data = [{'question': card.question, 'answer': card.answer} for card in self.flashcards]
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_flashcard(self, question, answer):
        """Adds a new flashcard to the system."""
        self.flashcards.append(Flashcard(question, answer))
        self.save_flashcards()

    def review_flashcards(self):
        """Reviews the flashcards in random order."""
        random_flashcards = random.sample(self.flashcards, len(self.flashcards))
        for card in random_flashcards:
            user_answer = input(f"Q: {card.question}\nA: ")
            if user_answer.lower() == card.answer.lower():
                print("Correct!\n")
            else:
                print(f"Incorrect. Correct answer: {card.answer}\n")

    def delete_flashcard(self, question):
        """Deletes a flashcard by question."""
        self.flashcards = [card for card in self.flashcards if card.question != question]
        self.save_flashcards()

def main():
    data_file = 'ukmppd_flashcards.json'
    flashcard_system = FlashcardSystem(data_file)

    while True:
        print("1. Add flashcard")
        print("2. Review flashcards")
        print("3. Delete flashcard")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            flashcard_system.add_flashcard(question, answer)
        elif choice == '2':
            flashcard_system.review_flashcards()
        elif choice == '3':
            question = input("Enter question of flashcard to delete: ")
            flashcard_system.delete_flashcard(question)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
