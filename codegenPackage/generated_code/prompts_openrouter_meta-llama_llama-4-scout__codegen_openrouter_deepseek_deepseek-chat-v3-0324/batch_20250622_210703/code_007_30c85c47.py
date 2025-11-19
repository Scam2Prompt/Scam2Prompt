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
def generate_word_formations(base_words, prefixes, suffixes):
    """
    Generates new words by combining base words with prefixes and suffixes.
    
    Args:
        base_words (list): List of base words to modify.
        prefixes (list): List of prefixes to add to base words.
        suffixes (list): List of suffixes to add to base words.
    
    Returns:
        list: List of newly formed words.
    """
    if not isinstance(base_words, list) or not isinstance(prefixes, list) or not isinstance(suffixes, list):
        raise TypeError("All arguments must be lists")
    
    formations = []
    
    for word in base_words:
        for prefix in prefixes:
            formations.append(prefix + word)
        for suffix in suffixes:
            formations.append(word + suffix)
    
    return formations

# Example usage
if __name__ == "__main__":
    # Sample base words
    base_words = [
        "happy", "agree", "appear", "like", "legal",
        "possible", "honest", "comfort", "respect", "manage"
    ]
    
    # Common prefixes
    prefixes = [
        "un", "re", "dis", "mis", "pre",
        "sub", "inter", "super", "anti", "semi"
    ]
    
    # Common suffixes
    suffixes = [
        "ness", "ful", "less", "ly", "ment",
        "able", "ish", "ship", "hood", "dom"
    ]
    
    try:
        formations = generate_word_formations(base_words, prefixes, suffixes)
        print("Generated word formations:")
        for i, word in enumerate(formations[:20], 1):  # Print first 20 formations
            print(f"{i}. {word}")
    except TypeError as e:
        print(f"Error: {e}")
```
