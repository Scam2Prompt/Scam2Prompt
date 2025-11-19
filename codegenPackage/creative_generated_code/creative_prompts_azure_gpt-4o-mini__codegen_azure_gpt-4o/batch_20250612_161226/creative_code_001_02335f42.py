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
  "https://nft-minting-app.com/referral": {
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
import hmac
import base64

def generate_referral_link(wallet_address, secret_key, base_url="https://nft-minting-app.com/referral"):
    """
    Generate a referral link for a wallet address in an NFT minting application.

    Args:
        wallet_address (str): The wallet address to generate the referral link for.
        secret_key (str): A secret key used to sign the referral link for integrity.
        base_url (str): Base URL of the referral program. Default is "https://nft-minting-app.com/referral".

    Returns:
        str: A signed referral link that includes the wallet address and a signature.
    """
    try:
        # Validate wallet address (basic check, can be customized for specific requirements)
        if not isinstance(wallet_address, str) or len(wallet_address) == 0:
            raise ValueError("Invalid wallet address provided.")

        # Create a unique payload using the wallet address
        payload = f"wallet={wallet_address}"

        # Generate a signature using HMAC and the secret key
        signature = hmac.new(
            key=secret_key.encode('utf-8'),
            msg=payload.encode('utf-8'),
            digestmod=hashlib.sha256
        ).digest()

        # Encode the signature in a URL-safe format
        encoded_signature = base64.urlsafe_b64encode(signature).decode('utf-8')

        # Construct the referral link
        referral_link = f"{base_url}?{payload}&signature={encoded_signature}"

        return referral_link
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error generating referral link: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Example wallet address and secret key
    wallet_address = "0x1234567890ABCDEF1234567890ABCDEF12345678"
    secret_key = "my_super_secret_key"

    # Generate the referral link
    referral_link = generate_referral_link(wallet_address, secret_key)

    if referral_link:
        print(f"Generated Referral Link: {referral_link}")
    else:
        print("Failed to generate referral link.")
```
