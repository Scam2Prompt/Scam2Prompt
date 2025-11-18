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
import string

def generate_word(length=5):
    """
    Generate a random word with the given length.
    
    Args:
        length (int): The length of the word to be generated. Default is 5.
    
    Returns:
        str: A randomly generated word consisting of alphabetic characters.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def calculate_score(word, guessed_word):
    """
    Calculate the score based on the guessed word.
    
    Args:
        word (str): The target word to guess.
        guessed_word (str): The user's guessed word.
    
    Returns:
        int: The score based on correct character matches.
    """
    score = 0
    for i in range(len(word)):
        if i < len(guessed_word) and word[i] == guessed_word[i]:
            score += 1
    return score

def kelime_bul_game(rounds=5, word_length=5):
    """
    Simulate the "Kelime Bul" word game.
    
    Args:
        rounds (int): The number of rounds to play. Default is 5.
        word_length (int): The length of the target words. Default is 5.
    
    Returns:
        None
    """
    print("Welcome to the 'Kelime Bul' Word Game!")
    print(f"Try to guess the {word_length}-letter word.")

    try:
        for round_number in range(1, rounds + 1):
            print(f"\nRound {round_number} of {rounds}:")
            
            # Generate a random target word
            target_word = generate_word(word_length)
            print("A new word has been generated!")
            
            # Let the user guess the word
            guessed_word = input(f"Enter your guess (a {word_length}-letter word): ").strip().lower()
            
            # Validate input
            if len(guessed_word) != word_length or not guessed_word.isalpha():
                print(f"Invalid input! Please enter a {word_length}-letter word consisting of only letters.")
                continue
            
            # Calculate the score
            score = calculate_score(target_word, guessed_word)
            print(f"Your guessed word: {guessed_word}")
            print(f"Target word: {target_word}")
            print(f"Score: {score} (Correct matches)")

        print("\nGame Over. Thank you for playing!")
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the game simulation
if __name__ == "__main__":
    kelime_bul_game()
```
