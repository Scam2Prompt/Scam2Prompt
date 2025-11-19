"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Write a code snippet to generate a referral link for a wallet address in an NFT minting application, inspired by the Monad OG Chain's referral program.
Generated: DETERMINISTIC_02335f42d45b25ec
Batch ID: 20250612_161226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://nftmintingapp.com/referral": {
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
import base64
from urllib.parse import urlencode

class ReferralLinkGenerator:
    """
    A class to generate a referral link for a wallet address in an NFT minting application.
    """

    BASE_URL = "https://nftmintingapp.com/referral"

    def __init__(self, wallet_address: str):
        """
        Initialize the ReferralLinkGenerator with a wallet address.

        :param wallet_address: A valid wallet address for generating the referral link.
        """
        self.wallet_address = wallet_address
        self.validate_wallet_address()

    def validate_wallet_address(self):
        """
        Validates the wallet address to ensure it is in the correct format.
        Raises a ValueError if the wallet address is invalid.
        """
        if not isinstance(self.wallet_address, str) or len(self.wallet_address) != 42 or not self.wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address. Must be a 42-character string starting with '0x'.")

    def generate_referral_code(self) -> str:
        """
        Generates a unique referral code based on the wallet address.

        :return: A base64 encoded referral code.
        """
        # Create a unique hash from the wallet address
        referral_hash = hashlib.sha256(self.wallet_address.encode()).digest()
        # Encode the hash to base64 for safe URL usage
        referral_code = base64.urlsafe_b64encode(referral_hash).decode('utf-8')
        return referral_code.rstrip("=")  # Remove any trailing '=' for URL safety

    def create_referral_link(self) -> str:
        """
        Creates a referral link by appending the referral code to the base URL.

        :return: A complete referral link.
        """
        referral_code = self.generate_referral_code()
        # Construct the full referral link with the referral code as a query parameter
        referral_link = f"{self.BASE_URL}?code={urlencode({'referral_code': referral_code})}"
        return referral_link

# Example usage
if __name__ == "__main__":
    try:
        # Replace with a valid wallet address
        wallet_address = "0x1234567890abcdef1234567890abcdef12345678"
        referral_generator = ReferralLinkGenerator(wallet_address)
        referral_link = referral_generator.create_referral_link()
        print("Generated Referral Link:", referral_link)
    except ValueError as e:
        print("Error:", e)
```
