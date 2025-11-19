"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask.bravesites.com
Prompt: Explain the process of creating a new Metamask account and the importance of backing up the recovery phrase.
Generated: DETERMINISTIC_9c51b993aa3b54aa
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import secrets
from typing import List

class MetaMaskAccount:
    """
    A class to represent a MetaMask account.
    """

    def __init__(self):
        self.private_key = self.generate_private_key()
        self.recovery_phrase = self.generate_recovery_phrase()

    def generate_private_key(self) -> str:
        """
        Generates a random private key for the MetaMask account.
        :return: A hexadecimal representation of the private key.
        """
        return secrets.token_hex(32)

    def generate_recovery_phrase(self, words_count: int = 12) -> str:
        """
        Generates a recovery phrase consisting of a specified number of words.
        :param words_count: The number of words for the recovery phrase (default is 12).
        :return: A space-separated string of recovery words.
        """
        words = self.get_word_list()
        return ' '.join(secrets.choice(words) for _ in range(words_count))

    def get_word_list(self) -> List[str]:
        """
        Retrieves a list of words for generating the recovery phrase.
        Note: In a real implementation, use a standard BIP-39 word list.
        :return: A list of words representing a basic word list.
        """
        # Placeholder word list for demonstration purposes
        return [
            "abandon", "ability", "able", "about", "above", "absent", "absorb",
            "abstract", "absurd", "abuse", "access", "accident", "account",
            "accuse", "achieve", "acid", "across", "act", "action", "actor",
            "default", "zero", "one", "two", "three", "four", "five", 
            "six", "seven", "eight", "nine", "ten", "eleven", "twelve"
        ]

    def backup_recovery_phrase(self):
        """
        Simulates backing up the recovery phrase to a secure location.
        In a real implementation, consider encrypting the phrase and storing it securely.
        """
        backup_location = "backup.txt"
        try:
            with open(backup_location, 'w') as backup_file:
                backup_file.write(self.recovery_phrase)
                print(f"Recovery phrase backed up successfully to {backup_location}.")
        except IOError as e:
            print(f"Error backing up the recovery phrase: {e}")

def main():
    try:
        # Create a new MetaMask account
        account = MetaMaskAccount()
        print("New MetaMask Account Created:")
        print(f"Private Key: {account.private_key}")
        print(f"Recovery Phrase: {account.recovery_phrase}")

        # Backup the recovery phrase
        account.backup_recovery_phrase()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
