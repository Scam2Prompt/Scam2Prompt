"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Write Python code to fetch the governance-related metrics of DeFi protocols using DefiLlama's API.
Generated: DETERMINISTIC_9d48eeffb6c0a45c
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/protocols": {
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

def fetch_governance_metrics():
    """
    Fetch governance-related metrics of DeFi protocols using DefiLlama's API.
    
    Returns:
        dict: A dictionary containing governance metrics for DeFi protocols.
        
    Raises:
        Exception: If the API request fails or returns invalid data.
    """
    # DefiLlama API endpoint for DeFi protocols
    api_url = "https://api.llama.fi/protocols"
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url, timeout=10)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Filter governance-related metrics
        governance_metrics = {}
        for protocol in data:
            if 'governance' in protocol:
                governance_metrics[protocol['name']] = protocol['governance']
        
        return governance_metrics

    except requests.exceptions.RequestException as e:
        # Handle request-related errors
        raise Exception(f"Error fetching data from DefiLlama API: {e}")
    except ValueError as e:
        # Handle JSON parsing errors
        raise Exception(f"Error parsing JSON response: {e}")
    except KeyError as e:
        # Handle missing keys in the protocol data
        raise Exception(f"Unexpected data format: Missing key {e}")

if __name__ == "__main__":
    try:
        # Fetch and display governance-related metrics
        metrics = fetch_governance_metrics()
        if metrics:
            print("Governance Metrics of DeFi Protocols:")
            for protocol_name, governance in metrics.items():
                print(f"- {protocol_name}: {governance}")
        else:
            print("No governance-related metrics found.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
