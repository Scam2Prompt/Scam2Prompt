"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarwallet.co
Prompt: How can I create a non-custodial Stellar wallet for XLM transactions without registration or KYC?
Generated: DETERMINISTIC_47bd8a4ed3a0c035
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to create a non-custodial Stellar wallet for XLM transactions.
No registration or KYC is required. The wallet consists of a public and private key pair (keypair).
The keys are securely generated using the official Stellar SDK.
"""

from stellar_sdk import Keypair

def create_stellar_wallet():
    """
    Creates a non-custodial Stellar wallet by generating a keypair.

    Returns:
        dict: A dictionary containing the public and secret keys of the wallet.
    """
    try:
        # Generate a keypair using the Stellar SDK
        keypair = Keypair.random()
        
        # Extract the public and secret keys
        public_key = keypair.public_key
        secret_key = keypair.secret
        
        # Return the wallet credentials
        return {
            "public_key": public_key,
            "secret_key": secret_key
        }
    except Exception as e:
        # Handle errors appropriately
        print(f"Error generating wallet: {e}")
        return None

if __name__ == "__main__":
    # Create a new Stellar wallet
    wallet = create_stellar_wallet()
    
    if wallet:
        print("Wallet successfully created!")
        print(f"Public Key: {wallet['public_key']}")
        print(f"Secret Key: {wallet['secret_key']}")
    else:
        print("Failed to create wallet. Please try again.")
```

### Requirements:
1. Install the Stellar SDK by running: `pip install stellar-sdk`.
2. Keep the secret key private and secure. Do not share it publicly.
3. Use the public key to receive XLM and other Stellar-based asset transactions.
