"""
Generated Code Metadata:
========================
Original URL: https://fullmoonbird-next.vercel.app
Prompt: Write a Python script that can reset or mint a token ID for a digital character, inspired by the functionality implied on https://fullmoonbird-next.vercel.app.
Generated: DETERMINISTIC_4e95b95d0f55f8f5
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os

class TokenManager:
    """
    A class to manage the minting and resetting of token IDs for digital characters.
    """

    def __init__(self, token_file='tokens.json'):
        """
        Initializes the TokenManager with a specified token file.

        Args:
            token_file (str): The path to the JSON file that stores token data.
        """
        self.token_file = token_file
        self.tokens = self.load_tokens()

    def load_tokens(self):
        """
        Loads tokens from the specified JSON file.

        Returns:
            dict: A dictionary of token IDs and their associated data.
        """
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as file:
                return json.load(file)
        return {}

    def save_tokens(self):
        """
        Saves the current tokens to the specified JSON file.
        """
        with open(self.token_file, 'w') as file:
            json.dump(self.tokens, file, indent=4)

    def mint_token(self, character_name):
        """
        Mints a new token ID for a given character name.

        Args:
            character_name (str): The name of the character to mint a token for.

        Returns:
            str: The newly minted token ID.
        """
        token_id = self.generate_token_id()
        self.tokens[token_id] = {'character_name': character_name}
        self.save_tokens()
        return token_id

    def reset_token(self, token_id):
        """
        Resets the token ID, allowing it to be reused.

        Args:
            token_id (str): The token ID to reset.

        Returns:
            bool: True if the reset was successful, False otherwise.
        """
        if token_id in self.tokens:
            del self.tokens[token_id]
            self.save_tokens()
            return True
        return False

    def generate_token_id(self):
        """
        Generates a unique token ID.

        Returns:
            str: A unique token ID.
        """
        while True:
            token_id = f'TOKEN-{random.randint(1000, 9999)}'
            if token_id not in self.tokens:
                return token_id

def main():
    """
    Main function to demonstrate the TokenManager functionality.
    """
    manager = TokenManager()

    # Mint a new token
    character_name = input("Enter the character name to mint a token: ")
    new_token = manager.mint_token(character_name)
    print(f"Minted new token ID: {new_token} for character: {character_name}")

    # Reset a token
    token_to_reset = input("Enter the token ID to reset: ")
    if manager.reset_token(token_to_reset):
        print(f"Token ID {token_to_reset} has been reset.")
    else:
        print(f"Token ID {token_to_reset} not found.")

if __name__ == "__main__":
    main()
```
