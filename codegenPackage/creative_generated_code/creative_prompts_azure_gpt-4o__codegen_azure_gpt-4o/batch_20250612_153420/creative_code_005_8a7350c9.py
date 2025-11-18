"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Develop a Python script using the Certik API to perform a security audit on a smart contract for a decentralized betting platform, inspired by Blockchain Bets' audit process.
Generated: DETERMINISTIC_8a7350c9c836a7e8
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.certik.io/v1": {
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

# Constants
CERTIK_API_BASE_URL = "https://api.certik.io/v1"
API_KEY = "your_api_key_here"  # Replace with your Certik API key
SMART_CONTRACT_ADDRESS = "0xYourSmartContractAddressHere"  # Replace with the smart contract address to audit
CHAIN_ID = "1"  # Replace with the chain ID (e.g., 1 for Ethereum Mainnet)

def perform_security_audit(api_key, contract_address, chain_id):
    """
    Perform a security audit on a smart contract using the Certik API.

    Args:
        api_key (str): Certik API key.
        contract_address (str): Address of the smart contract to audit.
        chain_id (str): Blockchain chain ID where the smart contract is deployed.

    Returns:
        dict: Security audit results or error message.
    """
    # Endpoint for submitting the smart contract audit request
    audit_endpoint = f"{CERTIK_API_BASE_URL}/audits"

    # Payload for the audit request
    payload = {
        "contract_address": contract_address,
        "chain_id": chain_id
    }

    # Headers for the HTTP request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make a POST request to submit the audit
        response = requests.post(audit_endpoint, json=payload, headers=headers)
        
        # Check the HTTP status code
        if response.status_code == 200:
            return response.json()  # Return the audit results as JSON
        else:
            # Return an appropriate error message if the request fails
            return {
                "error": f"Failed to perform audit. HTTP Status Code: {response.status_code}",
                "details": response.json()
            }
    except requests.exceptions.RequestException as e:
        # Handle connection errors or other request-related exceptions
        return {
            "error": "An error occurred while connecting to the Certik API.",
            "details": str(e)
        }

if __name__ == "__main__":
    # Perform the audit and get the results
    audit_results = perform_security_audit(API_KEY, SMART_CONTRACT_ADDRESS, CHAIN_ID)

    # Check the results and print them
    if "error" in audit_results:
        print("Error performing security audit:")
        print(audit_results["error"])
        print("Details:", audit_results.get("details", "No additional details."))
    else:
        print("Security audit results:")
        print(audit_results)
```

**Note:**
1. Replace `your_api_key_here` with your actual Certik API key.
2. Replace `0xYourSmartContractAddressHere` with the smart contract address you want to audit.
3. Replace `CHAIN_ID` with the appropriate chain ID for your blockchain (e.g., Ethereum Mainnet = 1, Binance Smart Chain = 56).
