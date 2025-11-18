"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.reaper.farmm.towerfish.tw
Prompt: Write code to implement a wallet phrase input system supporting 12, 15, 18, 21, and 24-word phrases, similar to the wallet connection options on Reaper.Farm.
Generated: DETERMINISTIC_63dae715359fe286
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# wallet_phrase_input.py
import re

class WalletPhraseInput:
    def __init__(self):
        # Supported phrase sizes
        self.supported_sizes = [12, 15, 18, 21, 24]
        # Regular expression to validate individual words in the wallet phrase
        self.word_pattern = re.compile(r"^[a-zA-Z]+$")  # Allow only alphabetic characters

    def validate_wallet_phrase(self, phrase: str) -> bool:
        """
        Validates the wallet phrase.
        
        Args:
            phrase (str): The wallet phrase entered by the user.

        Returns:
            bool: True if the wallet phrase is valid, False otherwise.
        """
        try:
            # Split the phrase into individual words
            words = phrase.strip().split()
            
            # Check if the phrase length matches any of the supported sizes
            if len(words) not in self.supported_sizes:
                print(f"Error: Wallet phrase must contain one of the following word counts: {self.supported_sizes}")
                return False
            
            # Validate each word against the regular expression
            for word in words:
                if not self.word_pattern.match(word):
                    print(f"Error: Invalid word in wallet phrase: '{word}'. Words must contain only alphabetic characters.")
                    return False
            
            # If all validations pass, the phrase is valid
            return True
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred while validating the wallet phrase: {e}")
            return False

    def input_wallet_phrase(self):
        """
        Prompts the user to input a wallet phrase and validates it.
        """
        try:
            print("Enter your wallet phrase (12, 15, 18, 21, or 24 words):")
            phrase = input(">>> ").strip()
            
            if self.validate_wallet_phrase(phrase):
                print("Wallet phrase is valid.")
            else:
                print("Wallet phrase is invalid.")
        except KeyboardInterrupt:
            # Gracefully handle user interrupt (Ctrl+C)
            print("\nOperation cancelled by the user.")
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the wallet phrase input system
    wallet_phrase_input = WalletPhraseInput()
    wallet_phrase_input.input_wallet_phrase()
```
