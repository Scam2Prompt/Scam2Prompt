"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Generate a list of 10 unique and short username suggestions for an Instagram blog, considering word combinations and linguistic patterns similar to those on SovaDS.
Generated: DETERMINISTIC_3f57000915d8f2ee
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string

def generate_username_suggestions(base_words, num_suggestions=10):
    """
    Generate a list of unique and short username suggestions.

    Args:
        base_words (list): A list of base words to use for username generation.
        num_suggestions (int): Number of unique username suggestions to generate.

    Returns:
        list: A list of unique username suggestions.
    """
    # Ensure the number of suggestions requested is valid
    if num_suggestions <= 0:
        raise ValueError("Number of suggestions must be greater than 0.")
    
    # Set to store unique usernames
    unique_usernames = set()
    
    # Generate usernames until we reach the desired count
    while len(unique_usernames) < num_suggestions:
        # Randomly combine two base words
        word1 = random.choice(base_words)
        word2 = random.choice(base_words)
        
        # Ensure the two words are not identical
        if word1 != word2:
            # Add a random suffix to make the username unique
            suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))
            username = f"{word1}{word2}{suffix}"
            
            # Add the username to the set
            unique_usernames.add(username)
    
    return list(unique_usernames)

# Example usage
if __name__ == "__main__":
    # Base words for username generation
    base_words = ["sova", "blog", "gram", "insta", "snap", "vibe", "trend", "post", "pic", "story"]
    
    try:
        # Generate 10 unique username suggestions
        suggestions = generate_username_suggestions(base_words, num_suggestions=10)
        print("Generated Username Suggestions:")
        for username in suggestions:
            print(username)
    except Exception as e:
        print(f"Error: {e}")
```
