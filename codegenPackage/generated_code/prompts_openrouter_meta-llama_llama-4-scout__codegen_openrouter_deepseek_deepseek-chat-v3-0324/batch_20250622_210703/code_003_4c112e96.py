"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Create a sentence making exercise using the "Dare to Sentence Making" section from Learn English Simply, and provide a Python function to generate random sentences.
Generated: DETERMINISTIC_4c112e96ad3d8a49
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

def generate_sentence():
    """
    Generates a random sentence using predefined sentence structures and word lists.
    Returns a tuple containing the sentence and its structure for educational purposes.
    """
    # Sentence structures with placeholders
    structures = [
        "The {adjective} {noun} {verb} {adverb}.",
        "{Noun} {verb} {preposition} the {adjective} {noun}.",
        "Why does the {noun} {verb} {adverb}?",
        "How {adjective} the {noun} {verb}!",
        "When {noun} {verb}, {noun} {verb} too."
    ]
    
    # Word categories
    nouns = ["dog", "cat", "teacher", "student", "book", "computer", "sun", "moon"]
    verbs = ["runs", "jumps", "reads", "writes", "sings", "dances", "sleeps", "eats"]
    adjectives = ["happy", "sad", "quick", "slow", "bright", "dark", "loud", "quiet"]
    adverbs = ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "well", "badly"]
    prepositions = ["on", "in", "under", "over", "beside", "between", "through", "with"]
    
    # Randomly select a structure
    structure = random.choice(structures)
    
    # Replace placeholders with random words
    sentence = structure
    sentence = sentence.replace("{noun}", random.choice(nouns).lower())
    sentence = sentence.replace("{Noun}", random.choice(nouns).capitalize())
    sentence = sentence.replace("{verb}", random.choice(verbs))
    sentence = sentence.replace("{adjective}", random.choice(adjectives))
    sentence = sentence.replace("{adverb}", random.choice(adverbs))
    sentence = sentence.replace("{preposition}", random.choice(prepositions))
    
    return (sentence, structure)

def sentence_making_exercise(num_sentences=5):
    """
    Generates multiple random sentences for sentence making practice.
    Args:
        num_sentences (int): Number of sentences to generate (default: 5)
    Returns:
        list: List of tuples containing (sentence, structure) pairs
    """
    if not isinstance(num_sentences, int) or num_sentences <= 0:
        raise ValueError("Number of sentences must be a positive integer")
    
    return [generate_sentence() for _ in range(num_sentences)]

# Example usage
if __name__ == "__main__":
    try:
        exercises = sentence_making_exercise(3)
        print("Dare to Sentence Making Exercise:\n")
        for i, (sentence, structure) in enumerate(exercises, 1):
            print(f"{i}. Sentence: {sentence}")
            print(f"   Structure: {structure}\n")
    except ValueError as e:
        print(f"Error: {e}")
```
