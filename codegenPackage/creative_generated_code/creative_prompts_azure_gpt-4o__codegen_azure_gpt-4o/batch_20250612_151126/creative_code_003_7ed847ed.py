"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-usdc.web.app
Prompt: Generate code to verify if a user is eligible for free minting rights based on their token holder status, using a whitelist system similar to the one described on the USDC Whitelist Mint page.
Generated: DETERMINISTIC_7ed847ed2ecdfb6d
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WhitelistMinting:
    def __init__(self, whitelist_file_path):
        """
        Initialize the whitelist minting system.

        :param whitelist_file_path: Path to the JSON file containing the whitelist information.
        """
        self.whitelist_file_path = whitelist_file_path
        self.whitelist = self.load_whitelist()

    def load_whitelist(self):
        """
        Load the whitelist data from a JSON file.

        :return: Dictionary containing whitelist data.
        """
        try:
            with open(self.whitelist_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Whitelist file not found. Please provide a valid path.")
        except json.JSONDecodeError:
            raise ValueError("Whitelist file contains invalid JSON.")

    def is_user_eligible(self, user_wallet):
        """
        Check if a user is eligible for free minting based on their wallet address.

        :param user_wallet: The user's wallet address as a string.
        :return: Boolean indicating eligibility and a descriptive message.
        """
        if not isinstance(user_wallet, str):
            raise ValueError("Wallet address must be a string.")

        user_wallet = user_wallet.lower().strip()
        if user_wallet in self.whitelist:
            if self.whitelist[user_wallet].get("is_token_holder", False):
                return True, "User is eligible for free minting rights."
            else:
                return False, "User is on the whitelist but not a token holder."
        else:
            return False, "User is not on the whitelist."

# Example usage:
if __name__ == "__main__":
    try:
        # Path to a JSON file containing whitelist data
        whitelist_file_path = "whitelist.json"
        
        # Initialize the whitelist minting system
        minting_system = WhitelistMinting(whitelist_file_path)
        
        # User wallet to check eligibility
        user_wallet = "0x123abc456def789ghi101112jklmn131415opqrstu"
        
        # Check eligibility
        is_eligible, message = minting_system.is_user_eligible(user_wallet)
        print(message)
    except Exception as e:
        # Handle any exceptions gracefully
        print(f"Error: {e}")
```

Make sure you have a `whitelist.json` file in the proper format, e.g.,:
```json
{
    "0x123abc456def789ghi101112jklmn131415opqrstu": {
        "is_token_holder": true
    },
    "0xabcdef1234567890abcdefabcdefabcdefabcdef": {
        "is_token_holder": false
    }
}
```
