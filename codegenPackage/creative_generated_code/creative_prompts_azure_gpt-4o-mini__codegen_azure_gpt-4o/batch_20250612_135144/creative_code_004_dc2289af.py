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
    """
    Represents a single flashcard with a question and answer.
    Tracks review history to implement active recall strategies.
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.last_reviewed = None  # Timestamp of the last review
        self.review_count = 0      # Number of times the flashcard has been reviewed
        self.correct_count = 0     # Number of times the answer was correct

    def mark_reviewed(self, correct):
        """
        Updates review statistics based on user performance.
        :param correct: Boolean indicating if the answer was correct.
        """
        self.last_reviewed = datetime.now()
        self.review_count += 1
        if correct:
            self.correct_count += 1

    def __repr__(self):
        return f"Flashcard(question='{self.question}', answer='{self.answer}')"


class FlashcardApp:
    """
    Flashcard application that supports active recall and tracks user progress.
    """
    def __init__(self):
        self.flashcards = []  # List to store flashcards
        self.load_flashcards()  # Load existing flashcards from storage

    def add_flashcard(self, question, answer):
        """
        Adds a new flashcard to the collection.
        :param question: The question for the flashcard.
        :param answer: The answer for the flashcard.
        """
        new_flashcard = Flashcard(question, answer)
        self.flashcards.append(new_flashcard)
        self.save_flashcards()  # Save the updated flashcard list

    def review_flashcards(self):
        """
        Selects flashcards for review based on active recall principles.
        Prioritizes cards that were reviewed less recently or answered incorrectly.
        """
        # Sort flashcards by review priority
        self.flashcards.sort(key=lambda card: (
            card.last_reviewed or datetime.min,  # Older reviews first
            card.correct_count / max(card.review_count, 1)  # Lower accuracy first
        ))

        # Review selected flashcards
        for card in self.flashcards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ")
            correct = user_answer.strip().lower() == card.answer.strip().lower()
            if correct:
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is: {card.answer}")
            card.mark_reviewed(correct)

        # Save updated flashcards to storage
        self.save_flashcards()

    def save_flashcards(self):
        """
        Saves flashcards to a JSON file for persistent storage.
        """
        try:
            data = [{
                'question': card.question,
                'answer': card.answer,
                'last_reviewed': card.last_reviewed.isoformat() if card.last_reviewed else None,
                'review_count': card.review_count,
                'correct_count': card.correct_count
            } for card in self.flashcards]

            with open('flashcards.json', 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving flashcards: {e}")

    def load_flashcards(self):
        """
        Loads flashcards from a JSON file.
        """
        try:
            with open('flashcards.json', 'r') as file:
                data = json.load(file)
                self.flashcards = [
                    Flashcard(
                        question=entry['question'],
                        answer=entry['answer'],
                    ) for entry in data
                ]
                for card, entry in zip(self.flashcards, data):
                    card.last_reviewed = datetime.fromisoformat(entry['last_reviewed']) if entry['last_reviewed'] else None
                    card.review_count = entry['review_count']
                    card.correct_count = entry['correct_count']
        except FileNotFoundError:
            # If no file exists, start with an empty collection
            self.flashcards = []
        except Exception as e:
            print(f"Error loading flashcards: {e}")
            self.flashcards = []

    def run(self):
        """
        Main method to run the flashcard application.
        """
        while True:
            print("\nFlashcard Application")
            print("1. Add flashcard")
            print("2. Review flashcards")
            print("3. Exit")
            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    question = input("Enter the question: ")
                    answer = input("Enter the answer: ")
                    self.add_flashcard(question, answer)
                elif choice == 2:
                    self.review_flashcards()
                elif choice == 3:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")


# Start the flashcard application
if __name__ == "__main__":
    app = FlashcardApp()
    app.run()
```
