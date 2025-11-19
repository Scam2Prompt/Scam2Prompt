"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Generate a list of 20 word formations using the Formation of Words section from Learn English Simply, and provide a Python function to create new words by adding prefixes or suffixes.
Generated: DETERMINISTIC_30c85c471de2e145
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

# List of prefixes and suffixes commonly used in English word formation
PREFIXES = ["un", "re", "in", "dis", "pre", "mis", "over", "under", "sub", "inter"]
SUFFIXES = ["ing", "ed", "er", "ly", "ness", "ment", "tion", "able", "ful", "less"]

# Base words to form new words
BASE_WORDS = [
    "happy", "play", "work", "read", "write", "help", "move", "run", "jump", "think",
    "act", "build", "clean", "drive", "grow", "learn", "love", "make", "paint", "talk"
]

def generate_word_formations(base_words, prefixes, suffixes, count=20):
    """
    Generate a list of new word formations by adding prefixes or suffixes to base words.

    Args:
        base_words (list): List of base words to form new words.
        prefixes (list): List of prefixes to add to base words.
        suffixes (list): List of suffixes to add to base words.
        count (int): Number of word formations to generate.

    Returns:
        list: List of newly formed words.
    """
    if not base_words or not prefixes or not suffixes:
        raise ValueError("Base words, prefixes, and suffixes must be non-empty lists.")

    formed_words = set()  # Use a set to avoid duplicates

    while len(formed_words) < count:
        base_word = random.choice(base_words)
        if random.choice([True, False]):  # Randomly decide to add a prefix or suffix
            new_word = random.choice(prefixes) + base_word
        else:
            new_word = base_word + random.choice(suffixes)
        formed_words.add(new_word)

    return list(formed_words)

# Example usage
if __name__ == "__main__":
    try:
        word_formations = generate_word_formations(BASE_WORDS, PREFIXES, SUFFIXES, count=20)
        print("Generated Word Formations:")
        for word in word_formations:
            print(word)
    except Exception as e:
        print(f"An error occurred: {e}")
```
