"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstractdog.testnet.nfts2.me
Prompt: Write a function to verify ownership of a dog meme NFT on the Abstract Testnet blockchain using NFTs2Me API endpoints.
Generated: DETERMINISTIC_4d5e548c8fcbcc5a
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nfts2me.com/v1/nft": {
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

class NFTVerificationError(Exception):
    """Custom exception for NFT verification errors."""
    pass

def verify_dog_meme_nft(owner_address: str, nft_id: str, api_key: str) -> bool:
    """
    Verify ownership of a dog meme NFT on the Abstract Testnet blockchain using the NFTs2Me API.

    Args:
        owner_address (str): The wallet address of the expected NFT owner.
        nft_id (str): The unique identifier of the NFT.
        api_key (str): The API key for authenticating with the NFTs2Me service.

    Returns:
        bool: True if the ownership is verified, False otherwise.

    Raises:
        NFTVerificationError: If there is an issue with the API request or response.
    """
    # Define the base URL for the NFTs2Me API
    base_url = "https://api.nfts2me.com/v1/nft"

    # Construct the request URL for checking NFT ownership
    request_url = f"{base_url}/{nft_id}/owner"

    # Set up the headers for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the NFTs2Me API
        response = requests.get(request_url, headers=headers)

        # Raise an error if the response was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the ownership matches the expected owner address
        if "owner" in data:
            return data["owner"].lower() == owner_address.lower()
        else:
            raise NFTVerificationError("Owner information not found in the response.")

    except requests.exceptions.RequestException as req_err:
        raise NFTVerificationError(f"API request failed: {req_err}")
    except ValueError as json_err:
        raise NFTVerificationError(f"Failed to parse JSON response: {json_err}")
    except Exception as e:
        raise NFTVerificationError(f"An unexpected error occurred: {e}")

# Example usage (commented out to prevent execution in this context):
# if __name__ == "__main__":
#     try:
#         result = verify_dog_meme_nft("0xYourWalletAddress", "nft12345", "your_api_key_here")
#         print("Ownership verified:", result)
#     except NFTVerificationError as e:
#         print("Error verifying NFT ownership:", e)
```
