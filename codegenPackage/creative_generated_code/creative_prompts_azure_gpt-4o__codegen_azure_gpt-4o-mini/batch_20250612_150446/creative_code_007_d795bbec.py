"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apphubs.pages.dev
Prompt: Write code to implement a multichain bridging solution for transferring tokens and NFTs across chains using Wormhole, referencing the "Bridge Unlimited transfers across chains" feature.
Generated: DETERMINISTIC_d795bbec4d52fd4c
Batch ID: 20250612_150446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wormhole.com": {
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
import json
import requests

class WormholeBridge:
    """Class to facilitate token and NFT transfers across blockchain networks using the Wormhole protocol."""
    
    def __init__(self, api_url, private_key):
        """
        Initialize the WormholeBridge instance.
        
        Parameters:
            api_url (str): The base URL for the Wormhole API.
            private_key (str): The private key for signing transactions.
        """
        self.api_url = api_url
        self.private_key = private_key

    def send_token(self, from_chain, to_chain, amount, recipient):
        """
        Send tokens from one blockchain to another.
        
        Parameters:
            from_chain (str): The source blockchain.
            to_chain (str): The destination blockchain.
            amount (float): The amount of tokens to transfer.
            recipient (str): The recipient address on the destination chain.
        
        Returns:
            dict: Response from the Wormhole API.
        """
        try:
            payload = {
                "from_chain": from_chain,
                "to_chain": to_chain,
                "amount": amount,
                "recipient": recipient
            }
            response = requests.post(f"{self.api_url}/transfer", json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            return {"error": str(err)}

    def send_nft(self, from_chain, to_chain, nft_id, recipient):
        """
        Send an NFT from one blockchain to another.
        
        Parameters:
            from_chain (str): The source blockchain.
            to_chain (str): The destination blockchain.
            nft_id (str): The identifier of the NFT to transfer.
            recipient (str): The recipient address on the destination chain.
        
        Returns:
            dict: Response from the Wormhole API.
        """
        try:
            payload = {
                "from_chain": from_chain,
                "to_chain": to_chain,
                "nft_id": nft_id,
                "recipient": recipient
            }
            response = requests.post(f"{self.api_url}/nft_transfer", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            return {"error": str(err)}

# Example usage
if __name__ == "__main__":
    # Replace with your actual Wormhole API URL and private key
    API_URL = "https://api.wormhole.com"
    PRIVATE_KEY = "your_private_key"

    bridge = WormholeBridge(API_URL, PRIVATE_KEY)

    # Sending tokens example
    token_response = bridge.send_token("Ethereum", "Solana", 10.0, "recipient_address_here")
    print(json.dumps(token_response, indent=4))

    # Sending NFT example
    nft_response = bridge.send_nft("Ethereum", "Solana", "nft_id_here", "recipient_address_here")
    print(json.dumps(nft_response, indent=4))
```
