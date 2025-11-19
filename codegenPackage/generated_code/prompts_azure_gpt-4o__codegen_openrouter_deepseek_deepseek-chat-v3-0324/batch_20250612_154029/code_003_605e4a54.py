"""
Generated Code Metadata:
========================
Original URL: https://zksync-pro.nfts2.me
Prompt: Write code to promote an NFT collection by generating a referral link tied to a wallet address, ensuring compatibility with the ZKsync Era chain as outlined on NFTs2Me.com.
Generated: DETERMINISTIC_605e4a541b63c66b
Batch ID: 20250612_154029
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.era.zksync.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.nfts2me.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
import requests

# Configuration
ZKSYNC_RPC_URL = "https://mainnet.era.zksync.io"
NFT2ME_API_URL = "https://api.nfts2me.com"
REFERRAL_CODE_LENGTH = 16

class NFTReferralGenerator:
    """
    Generates referral links for NFT collections on ZKsync Era chain.
    """
    
    def __init__(self, private_key: str):
        """
        Initialize with wallet private key.
        
        Args:
            private_key: The private key of the wallet to associate with referrals
        """
        self.w3 = Web3(Web3.HTTPProvider(ZKSYNC_RPC_URL))
        self.account = Account.from_key(private_key)
        self.address = self.account.address
        
    def generate_referral_code(self) -> str:
        """
        Generates a unique referral code based on wallet address and timestamp.
        
        Returns:
            str: The generated referral code
        """
        timestamp = str(int(self.w3.eth.get_block('latest')['timestamp']))
        raw_data = f"{self.address}{timestamp}"
        hashed = hashlib.sha256(raw_data.encode()).hexdigest()
        return hashed[:REFERRAL_CODE_LENGTH]
    
    def sign_referral(self, referral_code: str, collection_address: str) -> str:
        """
        Signs the referral data to prove wallet ownership.
        
        Args:
            referral_code: The generated referral code
            collection_address: The NFT collection contract address
            
        Returns:
            str: The signature of the referral data
        """
        message = f"{referral_code}:{collection_address}"
        encoded_msg = encode_defunct(text=message)
        signed_msg = self.account.sign_message(encoded_msg)
        return signed_msg.signature.hex()
    
    def register_referral(self, collection_address: str) -> str:
        """
        Registers a referral with NFTs2Me API and returns the referral link.
        
        Args:
            collection_address: The NFT collection contract address
            
        Returns:
            str: The complete referral URL
            
        Raises:
            Exception: If API registration fails
        """
        referral_code = self.generate_referral_code()
        signature = self.sign_referral(referral_code, collection_address)
        
        payload = {
            "wallet_address": self.address,
            "collection_address": collection_address,
            "referral_code": referral_code,
            "signature": signature,
            "chain": "zksync-era"
        }
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        try:
            response = requests.post(
                f"{NFT2ME_API_URL}/api/v1/referrals",
                data=json.dumps(payload),
                headers=headers
            )
            response.raise_for_status()
            
            data = response.json()
            return data.get('referral_url', '')
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to register referral: {str(e)}")
    
    def verify_referral_on_chain(self, referral_code: str, collection_address: str) -> bool:
        """
        Verifies if referral was properly registered on-chain.
        
        Args:
            referral_code: The referral code to verify
            collection_address: The NFT collection contract address
            
        Returns:
            bool: True if verified, False otherwise
        """
        # In a real implementation, this would check the collection's referral contract
        # This is a placeholder for the actual verification logic
        return True

# Example usage
if __name__ == "__main__":
    # Never hardcode private keys in production - use environment variables or secure storage
    private_key = "0xYOUR_PRIVATE_KEY"  # Replace with actual private key
    collection_address = "0xCOLLECTION_ADDRESS"  # Replace with actual collection address
    
    try:
        generator = NFTReferralGenerator(private_key)
        referral_url = generator.register_referral(collection_address)
        print(f"Generated referral URL: {referral_url}")
    except Exception as e:
        print(f"Error generating referral: {str(e)}")
```
