"""
Generated Code Metadata:
========================
Original URL: https://degen-4g1.pages.dev
Prompt: "Write a Python script to mint an NFT on the Base blockchain using the Highlight platform's API, specifically for a generative series like Phototropism."
Generated: DETERMINISTIC_daf0bf2ea18bcfcc
Batch ID: 20250622_210803
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.highlight.xyz": {
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
import json
from typing import Dict, Optional

class HighlightNFTMinter:
    """
    A class to handle NFT minting on the Base blockchain using Highlight's API.
    Specifically designed for generative series like Phototropism.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://api.highlight.xyz"):
        """
        Initialize the NFT minter with API credentials.
        
        Args:
            api_key: Your Highlight API key
            base_url: Base URL for Highlight API (defaults to production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    
    def mint_nft(
        self,
        series_id: str,
        recipient_address: str,
        quantity: int = 1,
        metadata: Optional[Dict] = None
    ) -> Dict:
        """
        Mint an NFT from a generative series on Base blockchain.
        
        Args:
            series_id: The ID of the generative series (e.g., Phototropism)
            recipient_address: Ethereum address to receive the NFT
            quantity: Number of NFTs to mint (default: 1)
            metadata: Optional metadata to attach to the NFT
            
        Returns:
            Dictionary containing the API response
            
        Raises:
            Exception: If API request fails
        """
        endpoint = f"{self.base_url}/v1/mint/base"
        
        payload = {
            "seriesId": series_id,
            "recipientAddress": recipient_address,
            "quantity": quantity,
            "chain": "base"
        }
        
        if metadata:
            payload["metadata"] = metadata
        
        try:
            response = requests.post(
                endpoint,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to mint NFT: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with your actual API key
    minter = HighlightNFTMinter(api_key="your_highlight_api_key_here")
    
    try:
        # Mint a Phototropism NFT
        result = minter.mint_nft(
            series_id="phototropism-series-id",  # Replace with actual series ID
            recipient_address="0xRecipientAddressHere",
            quantity=1,
            metadata={
                "custom_attribute": "value"
            }
        )
        print("NFT minted successfully:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error minting NFT: {e}")
```
