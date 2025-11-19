"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Generate a Python script that utilizes flashcard techniques to enhance memory retention for medical exam preparation, similar to the methods described on Atria's learning platform.
Generated: DETERMINISTIC_702bda32409bd648
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
import time

class Flashcard:
    """Class to represent a flashcard with a question and answer."""

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __str__(self) -> str:
        return f"Q: {self.question}\nA: {self.answer}"


class FlashcardDeck:
    """Class to manage a deck of flashcards."""

    def __init__(self):
        self.cards = []

    def add_card(self, card: Flashcard):
        """Add a flashcard to the deck."""
        self.cards.append(card)

    def shuffle(self):
        """Shuffle the flashcards in the deck."""
        random.shuffle(self.cards)

    def get_random_card(self):
        """Return a random flashcard from the deck."""
        if not self.cards:
            raise ValueError("No flashcards in the deck.")
        return random.choice(self.cards)


def load_flashcards_from_file(file_path: str) -> FlashcardDeck:
    """Load flashcards from a JSON file."""
    deck = FlashcardDeck()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                deck.add_card(Flashcard(item['question'], item['answer']))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return deck


def study_flashcards(deck: FlashcardDeck):
    """Start the flashcard study session."""
    print("Starting your flashcard study session. Type 'exit' to quit.")
    deck.shuffle()
    while True:
        card = deck.get_random_card()
        print(card.question)
        user_input = input("Your answer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == card.answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {card.answer}\n")
        time.sleep(1)  # Pause before showing the next card


def main():
    """Main function to run the flashcard application."""
    file_path = 'flashcards.json'  # Specify the path to your JSON file
    deck = load_flashcards_from_file(file_path)
    if deck.cards:
        study_flashcards(deck)
    else:
        print("No flashcards available for study.")


if __name__ == "__main__":
    main()
```

### Example JSON File Structure (flashcards.json):
```json
[
    {"question": "What is the primary function of red blood cells?", "answer": "Transport oxygen."},
    {"question": "What hormone regulates blood sugar?", "answer": "Insulin."},
    {"question": "What organ is responsible for detoxification?", "answer": "Liver."}
]
```
