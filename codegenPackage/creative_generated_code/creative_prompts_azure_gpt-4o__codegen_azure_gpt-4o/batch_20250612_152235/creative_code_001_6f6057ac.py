"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decrypt-nft.pages.dev
Prompt: Generate code to verify user eligibility for claiming an NFT, ensuring the process adheres to the one-NFT-per-user restriction mentioned on the Decrypt NFT page.
Generated: DETERMINISTIC_6f6057ac5ae35e70
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
from typing import Optional, Dict, Set

class NFTEligibilityVerifier:
    def __init__(self):
        # Stores user data as a hash for privacy (e.g., hashed email or user ID)
        self.claimed_users: Set[str] = set()

    @staticmethod
    def hash_user_data(user_data: str) -> str:
        """
        Hash the user data using SHA-256 for privacy and consistency.
        :param user_data: Unique user identifier (e.g., email or user ID).
        :return: Hashed user data.
        """
        return hashlib.sha256(user_data.encode('utf-8')).hexdigest()

    def check_eligibility(self, user_data: str) -> bool:
        """
        Check if a user is eligible to claim an NFT.
        :param user_data: Unique user identifier (e.g., email or user ID).
        :return: True if eligible, False otherwise.
        """
        hashed_user = self.hash_user_data(user_data)
        return hashed_user not in self.claimed_users

    def claim_nft(self, user_data: str) -> Optional[str]:
        """
        Allows a user to claim an NFT if eligible.
        :param user_data: Unique user identifier (e.g., email or user ID).
        :return: Success message if eligible, None otherwise.
        """
        try:
            hashed_user = self.hash_user_data(user_data)
            
            # Check eligibility
            if hashed_user in self.claimed_users:
                return None  # User already claimed an NFT
            
            # Mark user as having claimed an NFT
            self.claimed_users.add(hashed_user)
            return "NFT successfully claimed!"
        except Exception as e:
            # Log error (in production, use a logger)
            print(f"An error occurred: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    verifier = NFTEligibilityVerifier()
    
    user_id = "user@example.com"  # Replace with unique user identifier
    
    # Check NFT eligibility
    if verifier.check_eligibility(user_id):
        print(verifier.claim_nft(user_id))  # Attempt to claim NFT
    else:
        print("User has already claimed an NFT.")
```
