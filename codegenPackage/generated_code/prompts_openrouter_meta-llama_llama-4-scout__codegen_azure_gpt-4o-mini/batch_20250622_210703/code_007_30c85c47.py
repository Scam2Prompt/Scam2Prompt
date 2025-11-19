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

class WordFormation:
    """
    A class to handle word formations by adding prefixes or suffixes.
    """

    def __init__(self):
        # List of base words for word formation
        self.base_words = [
            "act", "play", "create", "form", "inform", 
            "manage", "develop", "educate", "communicate", "motivate",
            "decide", "produce", "analyze", "organize", "participate",
            "improve", "transform", "inspire", "explore", "innovate"
        ]
        
        # Prefixes and suffixes to be used for word formation
        self.prefixes = ["re", "un", "dis", "pre", "mis"]
        self.suffixes = ["ing", "ed", "tion", "ment", "able"]

    def generate_word_formations(self, count=20):
        """
        Generate a list of word formations by combining base words with prefixes and suffixes.

        :param count: Number of word formations to generate
        :return: List of generated word formations
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        formations = set()  # Use a set to avoid duplicates

        while len(formations) < count:
            base_word = random.choice(self.base_words)
            prefix = random.choice(self.prefixes)
            suffix = random.choice(self.suffixes)

            # Create new words by adding prefixes and suffixes
            new_word_with_prefix = prefix + base_word
            new_word_with_suffix = base_word + suffix

            formations.add(new_word_with_prefix)
            formations.add(new_word_with_suffix)

        return list(formations)

def main():
    """
    Main function to execute the word formation generation.
    """
    try:
        word_formation = WordFormation()
        formations = word_formation.generate_word_formations(20)
        print("Generated Word Formations:")
        for word in formations:
            print(word)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
