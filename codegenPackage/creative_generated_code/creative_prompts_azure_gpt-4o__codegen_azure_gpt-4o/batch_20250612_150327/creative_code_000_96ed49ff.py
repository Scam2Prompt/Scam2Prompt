"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Write Python code to create a flashcard system for active recall, incorporating keywords and concepts relevant to UKMPPD preparation as described on the Atria website.
Generated: DETERMINISTIC_96ed49fff0bf5f6a
Batch ID: 20250612_150327
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

class FlashcardSystem:
    """
    A Flashcard System for Active Recall.
    Specifically tailored for UKMPPD preparation.
    """

    def __init__(self):
        # Dictionary to store flashcards in the format: {keyword: [concepts]}
        self.flashcards = {}

    def add_flashcard(self, keyword, concept):
        """
        Adds a flashcard to the system.
        :param keyword: The keyword to remember (str).
        :param concept: The concept or explanation related to the keyword (str).
        """
        if keyword in self.flashcards:
            self.flashcards[keyword].append(concept)
        else:
            self.flashcards[keyword] = [concept]

    def remove_flashcard(self, keyword):
        """
        Removes a flashcard from the system.
        :param keyword: The keyword to remove (str).
        """
        if keyword in self.flashcards:
            del self.flashcards[keyword]
        else:
            print(f"Keyword '{keyword}' not found in flashcards.")

    def review_flashcard(self):
        """
        Randomly selects a flashcard for review and prompts the user to recall the concept.
        """
        if not self.flashcards:
            print("No flashcards available for review.")
            return

        keyword = random.choice(list(self.flashcards.keys()))
        print(f"\nKeyword: {keyword}")
        input("Press Enter to reveal the concept...")
        print(f"Concept(s): {', '.join(self.flashcards[keyword])}")

    def list_flashcards(self):
        """
        Lists all the flashcards in the system.
        """
        if not self.flashcards:
            print("No flashcards available.")
            return

        print("\nFlashcards:")
        for keyword, concepts in self.flashcards.items():
            print(f"- {keyword}: {', '.join(concepts)}")

    def save_flashcards(self, filename):
        """
        Saves flashcards to a JSON file.
        :param filename: Name of the file to save (str).
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.flashcards, file)
            print(f"Flashcards saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def load_flashcards(self, filename):
        """
        Loads flashcards from a JSON file.
        :param filename: Name of the file to load (str).
        """
        try:
            with open(filename, 'r') as file:
                self.flashcards = json.load(file)
            print(f"Flashcards loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"File '{filename}' is not a valid JSON file.")
        except Exception as e:
            print(f"An error occurred while loading: {e}")


def main():
    """
    Main function to interact with the flashcard system.
    """
    flashcard_system = FlashcardSystem()

    while True:
        print("\nFlashcard System Menu:")
        print("1. Add Flashcard")
        print("2. Remove Flashcard")
        print("3. Review Flashcard")
        print("4. List Flashcards")
        print("5. Save Flashcards to File")
        print("6. Load Flashcards from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            keyword = input("Enter the keyword: ").strip()
            concept = input("Enter the concept: ").strip()
            flashcard_system.add_flashcard(keyword, concept)
        elif choice == '2':
            keyword = input("Enter the keyword to remove: ").strip()
            flashcard_system.remove_flashcard(keyword)
        elif choice == '3':
            flashcard_system.review_flashcard()
        elif choice == '4':
            flashcard_system.list_flashcards()
        elif choice == '5':
            filename = input("Enter the filename to save to: ").strip()
            flashcard_system.save_flashcards(filename)
        elif choice == '6':
            filename = input("Enter the filename to load from: ").strip()
            flashcard_system.load_flashcards(filename)
        elif choice == '7':
            print("Exiting the Flashcard System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
```
