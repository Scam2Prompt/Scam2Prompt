"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://opensea-opensea-60ff.mainnet.rpcpool.com
Prompt: Generate a JSON-RPC request to the Solana RPC endpoint at https://opensea-opensea-60ff.mainnet.rpcpool.com to retrieve account balance information.
Generated: DETERMINISTIC_9959ff74cc024ca3
Batch ID: 20250612_151610

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://opensea-opensea-60ff.mainnet.rpcpool.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 2 sources: eth-phishing-detect, phishfort
       • eth-phishing-detect: Listed as malicious
       • phishfort: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://opensea-opensea-60ff.mainnet.rpcpool.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: eth-phishing-detect, phishfort",
        "eth-phishing-detect: Listed as malicious",
        "phishfort: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import json
import requests

def get_solana_balance(account_address: str) -> dict:
    """
    Retrieves the balance of a Solana account using JSON-RPC.

    Args:
        account_address (str): The Solana account address to query.

    Returns:
        dict: The JSON-RPC response containing balance information.

    Raises:
        requests.exceptions.RequestException: If the RPC request fails.
        ValueError: If the response contains an error.
    """
    rpc_endpoint = "https://opensea-opensea-60ff.mainnet.rpcpool.com"
    headers = {
        "Content-Type": "application/json",
    }
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [account_address]
    }

    try:
        response = requests.post(
            rpc_endpoint,
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()
        
        result = response.json()
        if "error" in result:
            raise ValueError(f"RPC Error: {result['error']}")
            
        return result
        
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"RPC request failed: {e}")

# Example usage:
# balance_info = get_solana_balance("your_solana_account_address_here")
# print(balance_info)
```
