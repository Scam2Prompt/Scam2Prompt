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
import json
import random

class Flashcard:
    """Class representing a single flashcard."""
    
    def __init__(self, keyword, concept):
        """
        Initialize a flashcard with a keyword and its corresponding concept.
        
        :param keyword: The keyword for the flashcard.
        :param concept: The concept associated with the keyword.
        """
        self.keyword = keyword
        self.concept = concept

    def __str__(self):
        """Return a string representation of the flashcard."""
        return f"Keyword: {self.keyword}\nConcept: {self.concept}"


class FlashcardSystem:
    """Class to manage a collection of flashcards."""
    
    def __init__(self):
        """Initialize the flashcard system with an empty list of flashcards."""
        self.flashcards = []

    def add_flashcard(self, keyword, concept):
        """
        Add a new flashcard to the system.
        
        :param keyword: The keyword for the flashcard.
        :param concept: The concept associated with the keyword.
        """
        self.flashcards.append(Flashcard(keyword, concept))

    def load_flashcards(self, filename):
        """
        Load flashcards from a JSON file.
        
        :param filename: The name of the JSON file containing flashcards.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.add_flashcard(item['keyword'], item['concept'])
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_flashcards(self, filename):
        """
        Save the current flashcards to a JSON file.
        
        :param filename: The name of the JSON file to save flashcards.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([{'keyword': fc.keyword, 'concept': fc.concept} for fc in self.flashcards], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def quiz(self):
        """Start a quiz session with the flashcards."""
        if not self.flashcards:
            print("No flashcards available. Please add some flashcards first.")
            return
        
        random.shuffle(self.flashcards)
        score = 0
        
        for flashcard in self.flashcards:
            print(f"Keyword: {flashcard.keyword}")
            answer = input("What is the concept? ")
            if answer.strip().lower() == flashcard.concept.lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer is: {flashcard.concept}\n")
        
        print(f"Quiz completed! Your score: {score}/{len(self.flashcards)}")


def main():
    """Main function to run the flashcard system."""
    flashcard_system = FlashcardSystem()
    
    # Load flashcards from a file (if exists)
    flashcard_system.load_flashcards('flashcards.json')
    
    while True:
        print("Flashcard System Menu:")
        print("1. Add Flashcard")
        print("2. Quiz")
        print("3. Save Flashcards")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            keyword = input("Enter the keyword: ")
            concept = input("Enter the concept: ")
            flashcard_system.add_flashcard(keyword, concept)
            print("Flashcard added successfully!\n")
        elif choice == '2':
            flashcard_system.quiz()
        elif choice == '3':
            flashcard_system.save_flashcards('flashcards.json')
            print("Flashcards saved successfully!\n")
        elif choice == '4':
            print("Exiting the flashcard system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
```
