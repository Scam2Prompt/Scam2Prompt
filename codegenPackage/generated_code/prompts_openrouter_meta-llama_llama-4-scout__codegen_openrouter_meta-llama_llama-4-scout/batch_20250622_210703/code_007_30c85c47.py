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
# word_formations.py

import random

# List of prefixes
prefixes = [
    "un", "re", "anti", "non", "co", "ex", "sub", "trans", "super", "post"
]

# List of suffixes
suffixes = [
    "able", "al", "ful", "ic", "ive", "less", "ly", "ous", "ness", "ship"
]

# List of base words
base_words = [
    "act", "form", "port", "code", "graph", "log", "path", "script", "struct", "system"
]

def generate_word_formations(num_formations: int) -> list:
    """
    Generate a list of word formations by adding prefixes or suffixes to base words.

    Args:
        num_formations (int): The number of word formations to generate.

    Returns:
        list: A list of word formations.
    """
    word_formations = []
    for _ in range(num_formations):
        base_word = random.choice(base_words)
        prefix = random.choice(prefixes) if random.random() < 0.5 else ""
        suffix = random.choice(suffixes) if random.random() < 0.5 else ""
        
        # Ensure that the word formation is not empty
        if not prefix and not suffix:
            suffix = random.choice(suffixes)

        word_formation = prefix + base_word + suffix
        word_formations.append(word_formation)

    return word_formations

def create_new_word(base_word: str, prefix: str = "", suffix: str = "") -> str:
    """
    Create a new word by adding a prefix or suffix to a base word.

    Args:
        base_word (str): The base word.
        prefix (str, optional): The prefix to add. Defaults to "".
        suffix (str, optional): The suffix to add. Defaults to "".

    Returns:
        str: The new word.
    """
    return prefix + base_word + suffix

def main():
    num_formations = 20
    word_formations = generate_word_formations(num_formations)
    print("Word Formations:")
    for i, word_formation in enumerate(word_formations):
        print(f"{i+1}. {word_formation}")

    # Example usage of create_new_word function
    base_word = "act"
    prefix = "un"
    suffix = "able"
    new_word = create_new_word(base_word, prefix, suffix)
    print(f"\nNew Word: {new_word}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
