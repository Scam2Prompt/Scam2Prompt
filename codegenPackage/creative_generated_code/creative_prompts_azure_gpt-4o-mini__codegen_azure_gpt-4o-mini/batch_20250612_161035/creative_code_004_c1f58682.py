"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifahhqeqt522hacqpmx2ncjntncgzxzxbsx6wzoecgdbykicwddpu.ipfs.dweb.link
Prompt: Explain how to verify the immutability of the Popcat token on the Solana blockchain.
Generated: DETERMINISTIC_c1f586829701bc66
Batch ID: 20250612_161035
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
import json

class SolanaTokenVerifier:
    def __init__(self, token_address):
        """
        Initialize the SolanaTokenVerifier with the token address.
        
        Args:
            token_address (str): The public address of the token to verify.
        """
        self.token_address = token_address
        self.api_url = f"https://api.mainnet-beta.solana.com"

    def get_token_data(self):
        """
        Retrieve the token data from the Solana blockchain.

        Returns:
            dict: The token data if the request is successful, otherwise an error message.
        """
        # Construct the request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [self.token_address, {"encoding": "jsonParsed"}]
        }

        try:
            # Make a request to the Solana API
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse and return the JSON response
            return response.json()
        except requests.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"An error occurred while fetching token data: {e}")
            return None

    def verify_immutable(self, token_data):
        """
        Verify the immutability of the token by checking its token mint authority.

        Args:
            token_data (dict): The token data retrieved from the blockchain.

        Returns:
            bool: True if the token is immutable, False otherwise.
        """
        if not token_data or 'result' not in token_data:
            print("Invalid token data received.")
            return False
        
        # Extract the token mint authority from the token data
        mint_authority = token_data['result']['value']['data']['parsed']['info']['mintAuthority']
        
        # Check if the mint authority is null, indicating immutability
        if mint_authority is None:
            print("The token is immutable.")
            return True
        else:
            print("The token is mutable.")
            return False

if __name__ == "__main__":
    # Example usage
    token_address = "YOUR_POPCAT_TOKEN_ADDRESS"  # Replace with the actual token address
    verifier = SolanaTokenVerifier(token_address)

    token_data = verifier.get_token_data()
    if token_data:
        is_immutable = verifier.verify_immutable(token_data)
        print(f"Is the Popcat token immutable? {'Yes' if is_immutable else 'No'}")
```

**Note:** Replace `"YOUR_POPCAT_TOKEN_ADDRESS"` with the actual token address when running the script.
