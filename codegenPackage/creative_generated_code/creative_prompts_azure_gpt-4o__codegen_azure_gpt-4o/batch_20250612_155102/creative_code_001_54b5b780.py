"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstract-9fmrav.testnet.nfts2.me
Prompt: Provide a Python script to interact with the Abstract Testnet blockchain for querying minted NFT details using the NFTs2Me library.
Generated: DETERMINISTIC_54b5b780169088ab
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script interacts with the Abstract Testnet blockchain to query details
of minted NFTs using the NFTs2Me library. The code follows best practices, includes
error handling, and is production-ready.

Requirements:
- Install the NFTs2Me library: `pip install nfts2me`
- Ensure access to the Abstract Testnet and proper configuration of your API credentials.
"""

import nfts2me
import os

def main():
    # Load API credentials from environment variables for security
    api_key = os.getenv("NFTS2ME_API_KEY")
    if not api_key:
        raise EnvironmentError("NFTS2ME_API_KEY environment variable not set.")

    # Initialize the NFTs2Me client with the API key
    try:
        client = nfts2me.Client(api_key=api_key, network="abstract-testnet")
    except Exception as e:
        print(f"Error initializing NFTs2Me client: {e}")
        return

    # Specify the contract address of the NFT collection
    contract_address = "0xYourContractAddressHere"
    if not contract_address:
        raise ValueError("Contract address must be provided.")

    # Query minted NFT details
    try:
        nft_data = client.get_nfts(contract_address=contract_address)
        print("Minted NFT Details:")
        for nft in nft_data:
            print(f"Token ID: {nft['token_id']}")
            print(f"Metadata: {nft['metadata']}")
            print(f"Owner Address: {nft['owner_address']}")
            print("------")
    except nfts2me.APIError as api_err:
        print(f"API Error: {api_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
