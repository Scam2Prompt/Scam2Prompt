"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ray-wl.web.app
Prompt: Write a function to calculate the total number of minted RAY NFTs and display the remaining mint rights using Solana blockchain data.
Generated: DETERMINISTIC_1bbf630f75afafdb
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import requests

class SolanaNFT:
    def __init__(self, nft_address: str):
        """
        Initialize the SolanaNFT class with the given NFT address.

        :param nft_address: The Solana address of the NFT collection.
        """
        self.nft_address = nft_address
        self.api_url = f"https://api.mainnet-beta.solana.com"

    def get_minted_nfts(self) -> int:
        """
        Fetch the total number of minted NFTs for the given address.

        :return: Total number of minted NFTs.
        """
        try:
            # Prepare the request payload for the Solana API
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getTokenSupply",
                "params": [self.nft_address],
            }
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Extract the total supply from the response
            total_supply = response.json().get('result', {}).get('value', {}).get('uiAmount', 0)
            return int(total_supply)
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching minted NFTs: {e}")
            return 0

    def calculate_remaining_mint_rights(self, max_mint: int) -> int:
        """
        Calculate the remaining mint rights based on the maximum allowed mints.

        :param max_mint: The maximum number of NFTs that can be minted.
        :return: The number of remaining mint rights.
        """
        minted_nfts = self.get_minted_nfts()
        remaining_mints = max_mint - minted_nfts
        return max(remaining_mints, 0)  # Ensure remaining mints aren't negative

    def display_remaining_mint_rights(self, max_mint: int):
        """
        Display the remaining mint rights for the NFT collection.

        :param max_mint: The maximum number of NFTs that can be minted.
        """
        remaining_mints = self.calculate_remaining_mint_rights(max_mint)
        print(f"Remaining mint rights: {remaining_mints}")


# Example usage:
if __name__ == "__main__":
    # Replace with the actual NFT address and maximum mint rights
    nft_address = "Your_NFT_Collection_Address"
    max_mint = 1000  # Replace with the max mint limit for your NFT collection

    nft = SolanaNFT(nft_address)
    nft.display_remaining_mint_rights(max_mint)
```
