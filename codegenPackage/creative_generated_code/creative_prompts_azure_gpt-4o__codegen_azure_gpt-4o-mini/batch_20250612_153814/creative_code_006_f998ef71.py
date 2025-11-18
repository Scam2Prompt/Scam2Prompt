"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Write a script to generate and manage the "招待コード残数" for users providing invite codes, ensuring the system updates dynamically as described on https://wc.innovie-corp.com.
Generated: DETERMINISTIC_f998ef71498ecb46
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import string
from typing import Dict, List

# Define the maximum number of invite codes and their usage limits
MAX_INVITE_CODES = 100
INVITE_CODE_LENGTH = 8

class InviteCodeManager:
    def __init__(self):
        """
        Initialize the InviteCodeManager with an empty code store and load existing codes.
        """
        self.codes: Dict[str, int] = {}
        self.load_codes()

    def load_codes(self) -> None:
        """
        Load invite codes from a JSON file. If the file does not exist, initialize an empty code store.
        """
        try:
            with open('invite_codes.json', 'r') as file:
                self.codes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.codes = {}

    def save_codes(self) -> None:
        """
        Save the current invite codes to a JSON file.
        """
        with open('invite_codes.json', 'w') as file:
            json.dump(self.codes, file)

    def generate_invite_code(self) -> str:
        """
        Generate a unique invite code.
        
        Returns:
            str: A unique invite code.
        """
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=INVITE_CODE_LENGTH))
            if code not in self.codes:
                self.codes[code] = 0
                self.save_codes()
                return code

    def use_invite_code(self, code: str) -> bool:
        """
        Use an invite code. Increments the usage count if the code is valid and has remaining usage.

        Args:
            code (str): The invite code to use.

        Returns:
            bool: True if the code was successfully used, False otherwise.
        """
        if code in self.codes:
            if self.codes[code] < MAX_INVITE_CODES:
                self.codes[code] += 1
                self.save_codes()
                return True
            else:
                print(f"Invite code {code} has reached its maximum usage limit.")
        else:
            print(f"Invite code {code} is invalid or does not exist.")
        return False

    def get_invite_code_status(self) -> Dict[str, int]:
        """
        Get the current status of all invite codes and their usage counts.

        Returns:
            dict: A dictionary with invite codes as keys and their usage counts as values.
        """
        return self.codes

def main():
    """
    Main function to demonstrate the functionality of the InviteCodeManager.
    """
    manager = InviteCodeManager()

    # Generate a new invite code
    new_code = manager.generate_invite_code()
    print(f"Generated invite code: {new_code}")

    # Use the invite code
    if manager.use_invite_code(new_code):
        print(f"Successfully used invite code: {new_code}")

    # Fetch and display all invite codes and their usage counts
    status = manager.get_invite_code_status()
    print("Current invite code status:")
    for code, count in status.items():
        print(f"Code: {code}, Used: {count}")

if __name__ == "__main__":
    main()
```
