"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a Python script to interact with the MDEX API for conducting cross-chain transactions between HECO and BSC.
Generated: DETERMINISTIC_102e2dd92b1cb08b
Batch ID: 20250612_140436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com": {
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

# MDEX API base URL
BASE_URL = "https://api.mdex.com"

# Function to send a request to the MDEX API
def send_mdex_request(endpoint, payload):
    """
    Sends a request to the MDEX API.

    Parameters:
    - endpoint (str): API endpoint to call.
    - payload (dict): The request payload.

    Returns:
    - dict: The JSON response from the API.
    """
    url = f"{BASE_URL}/{endpoint}"

    try:
        # Sending POST request
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad HTTP responses
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and handle connection errors or invalid responses
        print(f"Error interacting with MDEX API: {e}")
        return None

# Function to initiate a cross-chain transaction
def initiate_cross_chain_transaction(from_chain, to_chain, token_address, amount, wallet_address):
    """
    Initiates a cross-chain transaction using the MDEX API.

    Parameters:
    - from_chain (str): Source chain (e.g., 'HECO').
    - to_chain (str): Destination chain (e.g., 'BSC').
    - token_address (str): Contract address of the token.
    - amount (float): Amount to transfer.
    - wallet_address (str): Wallet address to receive the tokens.

    Returns:
    - dict: The response from the API indicating the success or failure of the transaction.
    """
    endpoint = "crosschain/transfer"  # Example endpoint for cross-chain transactions
    
    # Prepare the request payload
    payload = {
        "fromChain": from_chain,
        "toChain": to_chain,
        "tokenAddress": token_address,
        "amount": str(amount),  # Amount should be sent as a string
        "walletAddress": wallet_address
    }

    # Send the request
    response = send_mdex_request(endpoint, payload)
    
    if response:
        # Check for success in the response
        if response.get("success", False):
            print("Cross-chain transaction initiated successfully!")
        else:
            print(f"Failed to initiate transaction: {response.get('message', 'Unknown error')}")
    
    return response

if __name__ == "__main__":
    # Example inputs
    from_chain = "HECO"
    to_chain = "BSC"
    token_address = "0xTokenAddressHere"  # Replace with actual token address
    amount = 10.0  # Replace with desired amount
    wallet_address = "0xYourWalletAddressHere"  # Replace with your wallet address

    # Initiate the cross-chain transaction
    response = initiate_cross_chain_transaction(from_chain, to_chain, token_address, amount, wallet_address)
    
    # Print response for debugging
    print(json.dumps(response, indent=2))
```

**Note**: Replace placeholder values with your actual inputs (`token_address`, `wallet_address`, etc.). Ensure you have proper authorization to interact with MDEX's API and verify the correct endpoint URL and payload structure based on their official documentation.
