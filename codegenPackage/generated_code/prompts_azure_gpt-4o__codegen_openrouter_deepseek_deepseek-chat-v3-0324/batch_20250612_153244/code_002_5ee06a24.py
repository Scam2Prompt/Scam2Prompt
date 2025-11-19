"""
Generated Code Metadata:
========================
Original URL: https://galagames-rewards.com
Prompt: Develop a function in Python to simulate the "Kelime Bul" word game as described on Mynet's platform.
Generated: DETERMINISTIC_5ee06a24864cc494
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class KelimeBulGame:
    """
    A class to simulate the "Kelime Bul" word game.
    
    Attributes:
        word_length (int): Length of the target word.
        max_attempts (int): Maximum number of attempts allowed.
        target_word (str): The word to be guessed.
        attempts (List[str]): List of previous attempts.
        correct_letters (Dict[int, str]): Dictionary of correctly guessed letters and their positions.
        misplaced_letters (Dict[int, List[str]]): Dictionary of letters that are in the word but misplaced.
        wrong_letters (List[str]): List of letters not in the word.
    """
    
    def __init__(self, word_list: List[str], word_length: int = 5, max_attempts: int = 6):
        """
        Initialize the game with a word list, word length, and max attempts.
        
        Args:
            word_list (List[str]): List of possible target words.
            word_length (int): Length of the target word. Defaults to 5.
            max_attempts (int): Maximum number of attempts. Defaults to 6.
            
        Raises:
            ValueError: If word_length is invalid or word_list is empty.
        """
        if word_length <= 0:
            raise ValueError("Word length must be a positive integer.")
        if not word_list:
            raise ValueError("Word list cannot be empty.")
            
        self.word_length = word_length
        self.max_attempts = max_attempts
        self.target_word = self._select_target_word(word_list)
        self.attempts = []
        self.correct_letters = {}
        self.misplaced_letters = {}
        self.wrong_letters = []
        
    def _select_target_word(self, word_list: List[str]) -> str:
        """
        Select a random word from the word list with the specified length.
        
        Args:
            word_list (List[str]): List of possible words.
            
        Returns:
            str: Randomly selected word.
            
        Raises:
            ValueError: If no word of the specified length exists in the list.
        """
        valid_words = [word for word in word_list if len(word) == self.word_length]
        if not valid_words:
            raise ValueError(f"No words of length {self.word_length} found in the word list.")
        return random.choice(valid_words).upper()
    
    def submit_guess(self, guess: str) -> Dict[str, List[int]]:
        """
        Submit a guess and update game state.
        
        Args:
            guess (str): The guessed word.
            
        Returns:
            Dict[str, List[int]]: Dictionary with 'correct' and 'misplaced' letter positions.
            
        Raises:
            ValueError: If guess length is invalid or guess is not alphabetic.
            RuntimeError: If game is already over.
        """
        if len(guess) != self.word_length:
            raise ValueError(f"Guess must be {self.word_length} letters long.")
        if not guess.isalpha():
            raise ValueError("Guess must contain only alphabetic characters.")
        if self.is_game_over():
            raise RuntimeError("Game is already over.")
            
        guess = guess.upper()
        self.attempts.append(guess)
        
        result = {'correct': [], 'misplaced': []}
        
        for i in range(self.word_length):
            if guess[i] == self.target_word[i]:
                self.correct_letters[i] = guess[i]
                result['correct'].append(i)
            elif guess[i] in self.target_word:
                if i not in self.misplaced_letters:
                    self.misplaced_letters[i] = []
                if guess[i] not in self.misplaced_letters[i]:
                    self.misplaced_letters[i].append(guess[i])
                result['misplaced'].append(i)
            else:
                if guess[i] not in self.wrong_letters:
                    self.wrong_letters.append(guess[i])
                    
        return result
    
    def is_game_over(self) -> bool:
        """
        Check if the game is over (either won or out of attempts).
        
        Returns:
            bool: True if game is over, False otherwise.
        """
        return self.is_won() or len(self.attempts) >= self.max_attempts
    
    def is_won(self) -> bool:
        """
        Check if the game is won.
        
        Returns:
            bool: True if the last guess was correct, False otherwise.
        """
        return len(self.attempts) > 0 and self.attempts[-1] == self.target_word
    
    def get_hint(self) -> Optional[str]:
        """
        Provide a hint by revealing one correct letter.
        
        Returns:
            Optional[str]: A hint with one revealed letter, or None if no letters left to reveal.
        """
        unrevealed_positions = [i for i in range(self.word_length) if i not in self.correct_letters]
        if not unrevealed_positions:
            return None
            
        hint_pos = random.choice(unrevealed_positions)
        hint_letter = self.target_word[hint_pos]
        hint = ['_'] * self.word_length
        hint[hint_pos] = hint_letter
        return ''.join(hint)
    
    def get_game_state(self) -> Dict:
        """
        Get the current game state.
        
        Returns:
            Dict: Dictionary containing game state information.
        """
        return {
            'word_length': self.word_length,
            'max_attempts': self.max_attempts,
            'attempts': self.attempts,
            'correct_letters': self.correct_letters,
            'misplaced_letters': self.misplaced_letters,
            'wrong_letters': self.wrong_letters,
            'target_word': self.target_word if self.is_game_over() else None,
            'is_won': self.is_won(),
            'remaining_attempts': self.max_attempts - len(self.attempts)
        }

# Example usage
if __name__ == "__main__":
    word_list = ["apple", "grape", "melon", "peach", "mango", "lemon"]
    game = KelimeBulGame(word_list)
    
    while not game.is_game_over():
        print(f"\nAttempts left: {game.max_attempts - len(game.attempts)}")
        print(f"Correct letters: {game.correct_letters}")
        print(f"Misplaced letters: {game.misplaced_letters}")
        print(f"Wrong letters: {game.wrong_letters}")
        
        guess = input("Enter your guess: ").strip()
        try:
            result = game.submit_guess(guess)
            print(f"Correct positions: {result['correct']}")
            print(f"Misplaced positions: {result['misplaced']}")
            
            if game.is_won():
                print(f"Congratulations! You guessed the word: {game.target_word}")
            elif game.is_game_over():
                print(f"Game over! The word was: {game.target_word}")
                
        except ValueError as e:
            print(f"Invalid guess: {e}")
```
