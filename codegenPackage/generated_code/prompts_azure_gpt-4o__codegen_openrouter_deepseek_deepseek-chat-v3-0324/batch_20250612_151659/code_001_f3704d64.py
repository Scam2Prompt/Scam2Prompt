"""
Generated Code Metadata:
========================
Original URL: https://smeth.pages.dev
Prompt: Generate code for verifying the authenticity of an NFT image by calculating its SHA256 hash and comparing it to a hash embedded in a smart contract, as described for CryptoPunks.
Generated: DETERMINISTIC_f3704d64eaf44d85
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import requests
from web3 import Web3
from typing import Optional, Tuple

class NFTImageAuthenticator:
    """
    Verifies the authenticity of an NFT image by comparing its SHA256 hash
    with a hash stored in a smart contract.
    """
    
    def __init__(self, web3_provider_url: str, contract_address: str, contract_abi: list):
        """
        Initialize the authenticator with blockchain connection details.
        
        Args:
            web3_provider_url: URL of the Ethereum node provider
            contract_address: Address of the smart contract storing the hashes
            contract_abi: ABI of the smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")
        
        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )
    
    def calculate_image_hash(self, image_url: str) -> Optional[str]:
        """
        Calculate SHA256 hash of an image fetched from a URL.
        
        Args:
            image_url: URL of the image to verify
            
        Returns:
            Hex string of the SHA256 hash, or None if download fails
        """
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            image_data = response.content
            return hashlib.sha256(image_data).hexdigest()
        except (requests.RequestException, ValueError) as e:
            print(f"Error downloading image: {e}")
            return None
    
    def get_contract_hash(self, token_id: int) -> Optional[str]:
        """
        Retrieve the stored hash for a given token ID from the smart contract.
        
        Args:
            token_id: The NFT token ID to check
            
        Returns:
            Hex string of the stored hash, or None if retrieval fails
        """
        try:
            hash_bytes = self.contract.functions.imageHash(token_id).call()
            return hash_bytes.hex()
        except Exception as e:
            print(f"Error retrieving hash from contract: {e}")
            return None
    
    def verify_authenticity(self, token_id: int, image_url: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Verify if an NFT image matches the hash stored in the contract.
        
        Args:
            token_id: The NFT token ID to verify
            image_url: URL of the image to verify
            
        Returns:
            Tuple of (is_authentic, image_hash, contract_hash)
            Returns (False, None, None) if any step fails
        """
        image_hash = self.calculate_image_hash(image_url)
        if not image_hash:
            return False, None, None
            
        contract_hash = self.get_contract_hash(token_id)
        if not contract_hash:
            return False, None, None
            
        return image_hash == contract_hash, image_hash, contract_hash
```
