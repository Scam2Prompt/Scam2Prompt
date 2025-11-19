"""
Generated Code Metadata:
========================
Original URL: https://braavosstg.wpenginepowered.com
Prompt: Generate a code snippet that demonstrates how to integrate the Braavos Starknet Wallet API for managing NFTs, including music and video files.
Generated: DETERMINISTIC_e9020c7c2c29a957
Batch ID: 20250612_135121
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/cover.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.braavos.app": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/music.mp3": {
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
import requests
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

@dataclass
class NFTMetadata:
    name: str
    description: str
    image_url: str
    animation_url: Optional[str] = None  # For video/music NFTs
    attributes: Optional[List[Dict[str, Union[str, int, float]]]] = None

class BraavosWalletAPI:
    """
    A client for interacting with the Braavos Starknet Wallet API for NFT management.
    Handles music and video NFTs along with standard image NFTs.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.braavos.app"):
        """
        Initialize the Braavos API client.
        
        Args:
            api_key: Your Braavos API key
            base_url: Base URL for the API (defaults to production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        """
        Internal method to make API requests with error handling.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise Exception(f"API request failed: {e.response.text}") from e
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}") from e
    
    def mint_nft(
        self,
        contract_address: str,
        recipient: str,
        metadata: NFTMetadata,
        chain_id: str = "SN_MAIN"
    ) -> dict:
        """
        Mint a new NFT (including music/video NFTs).
        
        Args:
            contract_address: NFT contract address
            recipient: Wallet address to receive the NFT
            metadata: NFT metadata including media URLs
            chain_id: Starknet chain ID (default: mainnet)
            
        Returns:
            Transaction receipt
        """
        endpoint = "/v1/nfts/mint"
        payload = {
            "contract_address": contract_address,
            "recipient": recipient,
            "metadata": {
                "name": metadata.name,
                "description": metadata.description,
                "image": metadata.image_url,
                "animation_url": metadata.animation_url,
                "attributes": metadata.attributes or []
            },
            "chain_id": chain_id
        }
        return self._make_request("POST", endpoint, payload)
    
    def transfer_nft(
        self,
        contract_address: str,
        token_id: str,
        sender: str,
        recipient: str,
        chain_id: str = "SN_MAIN"
    ) -> dict:
        """
        Transfer an NFT to another wallet.
        
        Args:
            contract_address: NFT contract address
            token_id: ID of the NFT to transfer
            sender: Current owner's wallet address
            recipient: New owner's wallet address
            chain_id: Starknet chain ID (default: mainnet)
            
        Returns:
            Transaction receipt
        """
        endpoint = "/v1/nfts/transfer"
        payload = {
            "contract_address": contract_address,
            "token_id": token_id,
            "sender": sender,
            "recipient": recipient,
            "chain_id": chain_id
        }
        return self._make_request("POST", endpoint, payload)
    
    def get_nft_metadata(
        self,
        contract_address: str,
        token_id: str,
        chain_id: str = "SN_MAIN"
    ) -> NFTMetadata:
        """
        Retrieve metadata for a specific NFT.
        
        Args:
            contract_address: NFT contract address
            token_id: ID of the NFT
            chain_id: Starknet chain ID (default: mainnet)
            
        Returns:
            NFTMetadata object with the NFT's metadata
        """
        endpoint = f"/v1/nfts/{contract_address}/{token_id}"
        params = {"chain_id": chain_id}
        response = self._make_request("GET", endpoint, params)
        
        return NFTMetadata(
            name=response["name"],
            description=response["description"],
            image_url=response["image"],
            animation_url=response.get("animation_url"),
            attributes=response.get("attributes", [])
        )
    
    def list_owned_nfts(self, wallet_address: str, chain_id: str = "SN_MAIN") -> List[Dict]:
        """
        List all NFTs owned by a wallet address.
        
        Args:
            wallet_address: Wallet address to query
            chain_id: Starknet chain ID (default: mainnet)
            
        Returns:
            List of NFT dictionaries with basic info
        """
        endpoint = f"/v1/nfts/owned/{wallet_address}"
        params = {"chain_id": chain_id}
        return self._make_request("GET", endpoint, params).get("nfts", [])

# Example usage
if __name__ == "__main__":
    # Initialize client
    api_key = "your_api_key_here"
    braavos = BraavosWalletAPI(api_key)
    
    # Example NFT metadata for a music NFT
    music_nft_metadata = NFTMetadata(
        name="Starknet Symphony",
        description="An exclusive music NFT for Starknet enthusiasts",
        image_url="https://example.com/cover.jpg",
        animation_url="https://example.com/music.mp3",
        attributes=[
            {"trait_type": "Genre", "value": "Electronic"},
            {"trait_type": "Duration", "value": 180}
        ]
    )
    
    # Mint the NFT
    try:
        mint_result = braavos.mint_nft(
            contract_address="0x123...",
            recipient="0xabc...",
            metadata=music_nft_metadata
        )
        print(f"NFT minted: {mint_result}")
    except Exception as e:
        print(f"Error minting NFT: {str(e)}")
    
    # Get NFT metadata
    try:
        nft_metadata = braavos.get_nft_metadata(
            contract_address="0x123...",
            token_id="42"
        )
        print(f"Retrieved NFT metadata: {nft_metadata}")
    except Exception as e:
        print(f"Error fetching NFT metadata: {str(e)}")
```
