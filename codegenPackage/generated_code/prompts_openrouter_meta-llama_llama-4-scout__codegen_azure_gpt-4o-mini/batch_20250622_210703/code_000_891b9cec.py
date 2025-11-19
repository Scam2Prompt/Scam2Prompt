"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Write a Python script to create a vocabulary quiz using the word lists from Learn English Simply's Vocabulary section.
Generated: DETERMINISTIC_891b9cecd13228ca
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class VocabularyQuiz:
    def __init__(self, word_list):
        """
        Initializes the VocabularyQuiz with a list of words.

        :param word_list: List of tuples containing words and their definitions.
        """
        self.word_list = word_list
        self.score = 0
        self.total_questions = 0

    def ask_question(self):
        """
        Randomly selects a word from the word list and asks the user for its definition.
        """
        word, definition = random.choice(self.word_list)
        user_answer = input(f"What is the definition of '{word}'? ")

        # Check if the user's answer matches the definition
        if user_answer.strip().lower() == definition.strip().lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct definition is: {definition}")

        self.total_questions += 1

    def start_quiz(self):
        """
        Starts the vocabulary quiz, asking a set number of questions.
        """
        print("Welcome to the Vocabulary Quiz!")
        num_questions = int(input("How many questions would you like to answer? "))

        for _ in range(num_questions):
            self.ask_question()

        self.display_results()

    def display_results(self):
        """
        Displays the final score and percentage of correct answers.
        """
        if self.total_questions > 0:
            percentage = (self.score / self.total_questions) * 100
            print(f"\nQuiz completed! Your score: {self.score}/{self.total_questions} "
                  f"({percentage:.2f}%)")
        else:
            print("No questions were answered.")

def load_word_list():
    """
    Loads a predefined list of vocabulary words and their definitions.

    :return: List of tuples containing words and their definitions.
    """
    return [
        ("abate", "to lessen in intensity or degree"),
        ("benevolent", "well-meaning and kindly"),
        ("candid", "truthful and straightforward"),
        ("defer", "to postpone or delay"),
        ("emulate", "to match or surpass a person or achievement"),
        ("frugal", "sparing or economical with regard to money or food"),
        ("garrulous", "excessively talkative, especially on trivial matters"),
        ("hasten", "to be quick to do something"),
        ("inevitable", "certain to happen; unavoidable"),
        ("jubilant", "feeling or expressing great happiness and triumph"),
    ]

def main():
    """
    Main function to run the vocabulary quiz.
    """
    try:
        word_list = load_word_list()
        quiz = VocabularyQuiz(word_list)
        quiz.start_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
