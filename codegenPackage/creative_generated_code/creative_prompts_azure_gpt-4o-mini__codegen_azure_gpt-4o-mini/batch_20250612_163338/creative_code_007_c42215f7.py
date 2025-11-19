"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://communitydapps-ochainsync.pages.dev
Prompt: Describe how to reset a wallet password based on the instructions provided in the communitydapps-ochainsync content.
Generated: DETERMINISTIC_c42215f7ac971df1
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class Wallet:
    """
    A class to represent a wallet for managing passwords.
    """

    def __init__(self, wallet_file):
        """
        Initializes the Wallet with the path to the wallet file.
        
        :param wallet_file: Path to the wallet JSON file.
        """
        self.wallet_file = wallet_file
        self.wallet_data = self.load_wallet()

    def load_wallet(self):
        """
        Loads the wallet data from a JSON file.
        
        :return: Dictionary containing wallet data.
        :raises FileNotFoundError: If the wallet file does not exist.
        :raises json.JSONDecodeError: If the wallet file is not valid JSON.
        """
        if not os.path.exists(self.wallet_file):
            raise FileNotFoundError("Wallet file not found.")
        
        with open(self.wallet_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError("Invalid JSON format in wallet file.") from e

    def reset_password(self, old_password, new_password):
        """
        Resets the wallet password if the old password is correct.
        
        :param old_password: The current password of the wallet.
        :param new_password: The new password to set for the wallet.
        :raises ValueError: If the old password is incorrect.
        :raises Exception: If the new password does not meet criteria (e.g., length).
        """
        if self.wallet_data['password'] != old_password:
            raise ValueError("Old password is incorrect.")
        
        if not self.validate_password(new_password):
            raise Exception("New password does not meet criteria.")
        
        self.wallet_data['password'] = new_password
        self.save_wallet()

    def validate_password(self, password):
        """
        Validates the password based on predefined criteria.
        
        :param password: The password to validate.
        :return: True if valid, False otherwise.
        """
        # Example criteria: Password must be at least 8 characters long
        return len(password) >= 8

    def save_wallet(self):
        """
        Saves the updated wallet data back to the JSON file.
        
        :raises Exception: If there is an error writing to the file.
        """
        try:
            with open(self.wallet_file, 'w') as file:
                json.dump(self.wallet_data, file, indent=4)
        except Exception as e:
            raise Exception("Error saving wallet data.") from e

if __name__ == "__main__":
    # Example usage of the Wallet class
    wallet_file_path = 'wallet.json'  # Path to the wallet file
    wallet = Wallet(wallet_file_path)

    old_password = input("Enter your old password: ")
    new_password = input("Enter your new password: ")

    try:
        wallet.reset_password(old_password, new_password)
        print("Password reset successfully.")
    except (ValueError, Exception) as e:
        print(f"Error: {str(e)}")
```
