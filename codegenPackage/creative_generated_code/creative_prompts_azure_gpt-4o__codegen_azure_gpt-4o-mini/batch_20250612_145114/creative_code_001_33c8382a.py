"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Generate code to simulate the process of claiming an NFT reward from the Habbo platform, ensuring the user enters a valid Habbo username and accepts the terms of use.
Generated: DETERMINISTIC_33c8382ab6d0b3f2
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class HabboNFTClaim:
    def __init__(self, username: str):
        self.username = username
        self.terms_accepted = False

    def validate_username(self) -> bool:
        """Validate the Habbo username."""
        # Assuming a valid Habbo username is alphanumeric and between 1 to 15 characters
        return bool(re.match(r'^[A-Za-z0-9]{1,15}$', self.username))

    def accept_terms_of_use(self):
        """Simulate acceptance of terms of use."""
        self.terms_accepted = True
        print("Terms of use accepted.")

    def claim_nft(self):
        """Simulate claiming an NFT reward."""
        if not self.validate_username():
            raise ValueError("Invalid Habbo username. Please enter a valid username (1-15 alphanumeric characters).")
        
        if not self.terms_accepted:
            raise PermissionError("You must accept the terms of use before claiming the NFT.")

        # Simulate claiming the NFT
        print(f"NFT reward successfully claimed for user: {self.username}")

def main():
    """Main function to run the NFT claiming simulation."""
    try:
        # Input from user
        username = input("Enter your Habbo username: ")
        habbo_claim = HabboNFTClaim(username)
        
        # User must accept the terms of use
        accept_terms = input("Do you accept the terms of use? (yes/no): ").strip().lower()
        if accept_terms == 'yes':
            habbo_claim.accept_terms_of_use()
        else:
            print("You must accept the terms to claim your NFT.")
            return
        
        # Claim the NFT
        habbo_claim.claim_nft()

    except ValueError as ve:
        print(f"Error: {ve}")
    except PermissionError as pe:
        print(f"Error: {pe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
