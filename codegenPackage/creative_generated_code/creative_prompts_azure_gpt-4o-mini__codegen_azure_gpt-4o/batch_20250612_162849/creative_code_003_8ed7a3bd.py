"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Generate a code snippet that creates a referral link for NFT mints, inspired by the Unichain-Rooster referral system.
Generated: DETERMINISTIC_8ed7a3bd079fd44e
Batch ID: 20250612_162849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://nftmintingplatform.com/referral": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
import datetime

# Constants
BASE_URL = "https://nftmintingplatform.com/referral"  # Base URL for referral links
EXPIRATION_DAYS = 30  # Number of days before the referral link expires

class ReferralLinkGenerator:
    def __init__(self):
        # Dictionary to store referral links and metadata
        self.referral_links = {}

    def generate_referral_link(self, user_id, nft_collection):
        """
        Generate a unique referral link for NFT minting.
        
        Parameters:
            user_id (str): Unique identifier for the user generating the referral.
            nft_collection (str): Name or ID of the NFT collection being referred to.
        
        Returns:
            str: The unique referral link.
        """
        try:
            # Generate a unique token using UUID and user-specific data
            unique_token = hashlib.sha256(f"{user_id}-{nft_collection}-{uuid.uuid4()}".encode()).hexdigest()

            # Construct the referral link
            referral_link = f"{BASE_URL}?token={unique_token}"

            # Calculate expiration date
            expiration_date = datetime.datetime.now() + datetime.timedelta(days=EXPIRATION_DAYS)

            # Store metadata
            self.referral_links[unique_token] = {
                "user_id": user_id,
                "nft_collection": nft_collection,
                "created_at": datetime.datetime.now(),
                "expires_at": expiration_date
            }

            return referral_link
        except Exception as e:
            print(f"Error generating referral link: {e}")
            raise

    def validate_referral_link(self, token):
        """
        Validate a referral link to ensure it is valid and not expired.
        
        Parameters:
            token (str): The token part of the referral link.
        
        Returns:
            bool: True if the referral link is valid, False otherwise.
        """
        try:
            link_data = self.referral_links.get(token)
            
            if not link_data:
                return False  # Token not found

            # Check if the referral link has expired
            if datetime.datetime.now() > link_data['expires_at']:
                return False  # Referral link expired

            return True  # Referral link is valid
        except Exception as e:
            print(f"Error validating referral link: {e}")
            return False

# Example usage
if __name__ == "__main__":
    generator = ReferralLinkGenerator()

    # Generate a referral link
    user_id = "user123"
    nft_collection = "CoolNFTCollection"

    referral_link = generator.generate_referral_link(user_id, nft_collection)
    print(f"Generated Referral Link: {referral_link}")

    # Validate the referral link
    token = referral_link.split("?token=")[1]
    is_valid = generator.validate_referral_link(token)
    print(f"Is referral link valid? {is_valid}")
```
