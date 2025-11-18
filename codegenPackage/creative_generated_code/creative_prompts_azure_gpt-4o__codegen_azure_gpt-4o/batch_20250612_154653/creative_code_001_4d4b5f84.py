"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakevaultsdrop.pages.dev
Prompt: Generate code to verify a wallet by entering a 12-word or 24-word seed phrase, as described on StakeVault.Network.
Generated: DETERMINISTIC_4d4b5f843cb38ea7
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def verify_wallet_seed(seed_phrase: str) -> bool:
    """
    Verifies if the provided seed phrase is a valid 12-word or 24-word phrase.
    
    Args:
        seed_phrase (str): The seed phrase to verify, consisting of words separated by spaces.
    
    Returns:
        bool: True if the seed phrase is valid, False otherwise.
    """
    
    # Define minimum and maximum word count for a valid seed phrase
    MIN_WORD_COUNT = 12
    MAX_WORD_COUNT = 24
    
    try:
        # Split the seed phrase by spaces to extract individual words
        words = seed_phrase.strip().split()
        
        # Check if the number of words is either 12 or 24
        if len(words) not in (MIN_WORD_COUNT, MAX_WORD_COUNT):
            return False
        
        # Check if each word consists of valid characters (letters only, no digits/special characters)
        # Assuming seed phrase words should conform to BIP-39 standard
        pattern = re.compile(r"^[a-zA-Z]+$")
        for word in words:
            if not pattern.match(word):
                return False
        
        # If all checks pass, the seed phrase is valid
        return True
    
    except Exception as e:
        # Log the error and return False for any unexpected issues
        print(f"An error occurred during seed phrase verification: {e}")
        return False


# Example usage
if __name__ == "__main__":
    seed_phrase_input = input("Enter your wallet seed phrase (12 or 24 words): ").strip()
    
    if verify_wallet_seed(seed_phrase_input):
        print("The seed phrase is valid.")
    else:
        print("The seed phrase is invalid.")
```
