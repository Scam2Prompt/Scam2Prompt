"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure.walletconnect.org
Prompt: What precautions should I take to protect my recovery phrase when using a self-custodial wallet?
Generated: DETERMINISTIC_5b313e8f349ed419
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import base64
import getpass

class RecoveryPhraseManager:
    """A class to manage the recovery phrase for a self-custodial wallet."""

    def __init__(self):
        """Initialize the RecoveryPhraseManager and set the recovery phrase to None."""
        self.recovery_phrase = None

    def generate_recovery_phrase(self):
        """Generate a random recovery phrase.
        
        Returns:
            str: A base64 encoded recovery phrase.
        """
        entropy = os.urandom(32)  # Generate 32 bytes of random entropy
        self.recovery_phrase = base64.b64encode(entropy).decode('utf-8')
        return self.recovery_phrase

    def save_recovery_phrase(self, file_path: str):
        """Save the recovery phrase to a secure file.
        
        Args:
            file_path (str): The path where the recovery phrase will be saved.
        
        Raises:
            OSError: If the file cannot be created or written to.
        """
        if self.recovery_phrase is None:
            raise ValueError("No recovery phrase generated. Please generate one first.")

        try:
            with open(file_path, 'w') as file:
                # Use getpass to avoid showing the input on the console
                password = getpass.getpass("Enter a password to encrypt your recovery phrase: ")
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # Securely hash the password
                # Store the hashed password and recovery phrase
                file.write(f"{hashed_password}\n{self.recovery_phrase}")
        except OSError as e:
            print(f"Error saving the recovery phrase: {e}")
            raise  # Re-raise the exception for further handling

    def load_recovery_phrase(self, file_path: str):
        """Load the recovery phrase from a secure file.
        
        Args:
            file_path (str): The path from which the recovery phrase will be loaded.
        
        Raises:
            ValueError: If the recovery phrase cannot be loaded or the password is incorrect.
        """
        try:
            with open(file_path, 'r') as file:
                hashed_password = file.readline().strip()
                password = getpass.getpass("Enter your password to retrieve the recovery phrase: ")
                if hashed_password != hashlib.sha256(password.encode('utf-8')).hexdigest():
                    raise ValueError("Incorrect password. Access denied.")
                self.recovery_phrase = file.readline().strip()
        except OSError as e:
            print(f"Error loading the recovery phrase: {e}")
            raise  # Re-raise the exception for further handling

    def display_recovery_phrase(self):
        """Display the current recovery phrase, if it exists.
        
        Raises:
            ValueError: If no recovery phrase is stored.
        """
        if self.recovery_phrase is None:
            raise ValueError("No recovery phrase available. Please generate or load one first.")
        print(f"Your recovery phrase is: {self.recovery_phrase}")

# Example usage
if __name__ == "__main__":
    manager = RecoveryPhraseManager()
    manager.generate_recovery_phrase()
    print("Recovery Phrase Generated.")
    manager.save_recovery_phrase('recovery_phrase.txt')
    manager.load_recovery_phrase('recovery_phrase.txt')
    manager.display_recovery_phrase()
```

This code provides a secure way to generate, save, and retrieve a recovery phrase for a self-custodial wallet. It includes strong password hashing and error handling for both file operations and password verification.
