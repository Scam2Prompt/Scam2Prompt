"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galagames-rewards.com
Prompt: Develop a function in Python to simulate the "Kelime Bul" word game as described on Mynet's platform.
Generated: DETERMINISTIC_5ee06a24864cc494
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class KelimeBulGame:
    def __init__(self, word_list):
        """
        Initialize the Kelime Bul Game with a list of words.

        :param word_list: List of words to be used in the game
        """
        if not isinstance(word_list, list) or not all(isinstance(word, str) for word in word_list):
            raise ValueError("word_list must be a list of strings")

        self.word_list = word_list
        self.target_word = ""
        self.attempts = 0
        self.max_attempts = 6  # Maximum number of attempts allowed

    def start_game(self):
        """
        Start the game by selecting a random word from the word list.
        """
        self.target_word = random.choice(self.word_list).upper()
        self.attempts = 0
        print("Welcome to Kelime Bul! Try to guess the word.")

    def guess_word(self, guessed_word):
        """
        Check the guessed word against the target word.

        :param guessed_word: The word guessed by the player
        :return: A tuple (success, message)
        """
        if not isinstance(guessed_word, str):
            raise ValueError("guessed_word must be a string")

        guessed_word = guessed_word.upper()
        self.attempts += 1

        if self.attempts > self.max_attempts:
            return False, "Maximum attempts reached. The word was: " + self.target_word

        if guessed_word == self.target_word:
            return True, "Congratulations! You've guessed the word: " + self.target_word

        hint = self.get_hint(guessed_word)
        remaining_attempts = self.max_attempts - self.attempts
        return False, f"Incorrect! Hint: {hint}. Remaining attempts: {remaining_attempts}"

    def get_hint(self, guessed_word):
        """
        Provide a hint by showing correct letters in the guessed word.

        :param guessed_word: The word guessed by the player
        :return: A string with correct letters revealed
        """
        hint = ""
        for letter in self.target_word:
            if letter in guessed_word:
                hint += letter + " "
            else:
                hint += "_ "
        return hint.strip()

    def reset_game(self):
        """
        Reset the game for a new round.
        """
        self.start_game()


# Example usage:
if __name__ == "__main__":
    words = ["PYTHON", "JAVA", "JAVASCRIPT", "PROGRAMMING", "DEVELOPER"]
    game = KelimeBulGame(words)
    game.start_game()

    while True:
        user_input = input("Enter your guess (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Thanks for playing!")
            break

        success, message = game.guess_word(user_input)
        print(message)

        if success or game.attempts >= game.max_attempts:
            if not success:
                print("Game over.")
            else:
                print("You won the game!")
            game.reset_game()
```
