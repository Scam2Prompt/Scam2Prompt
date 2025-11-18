"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's NodeBalancers to distribute traffic across multiple web servers. Include API calls or CLI commands for configuration.
Generated: DETERMINISTIC_01d0960930339ac5
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4/nodebalancers": {
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

# Define constants for Linode API
API_TOKEN = 'your_api_token'  # Replace with your Linode API token
API_URL = 'https://api.linode.com/v4/nodebalancers'
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

def create_nodebalancer(label, region, config):
    """
    Create a new NodeBalancer.
    
    :param label: The label for the NodeBalancer.
    :param region: The region where the NodeBalancer will be created.
    :param config: The configuration settings for the NodeBalancer.
    :return: Response data from the API call.
    """
    try:
        payload = {
            'label': label,
            'region': region,
            'configs': [config]
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error creating NodeBalancer: {e}")
        return None

def create_nodebalancer_config(nodebalancer_id, protocol, port, backend_nodes):
    """
    Create configuration for a NodeBalancer.

    :param nodebalancer_id: The ID of the NodeBalancer.
    :param protocol: The protocol (e.g., 'http', 'tcp').
    :param port: The port for the NodeBalancer.
    :param backend_nodes: List of backend nodes (dictionaries) to balance traffic.
    :return: Response data from the API call.
    """
    try:
        config_payload = {
            'protocol': protocol,
            'port': port,
            'backends': backend_nodes
        }
        config_url = f"{API_URL}/{nodebalancer_id}/configs"
        response = requests.post(config_url, headers=HEADERS, json=config_payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating NodeBalancer config: {e}")
        return None

def main():
    # Define NodeBalancer settings
    label = 'MyNodeBalancer'
    region = 'us-east'  # Specify your preferred region
    backend_nodes = [
        {'address': '192.0.2.1', 'port': 80},  # Replace with your backend server addresses
        {'address': '192.0.2.2', 'port': 80}
    ]
    
    # Create NodeBalancer
    nodebalancer = create_nodebalancer(label, region, {'protocol': 'http'})
    if nodebalancer:
        print("NodeBalancer created:", nodebalancer)
        
        # Create NodeBalancer config
        config = create_nodebalancer_config(nodebalancer['id'], 'http', 80, backend_nodes)
        if config:
            print("NodeBalancer config created:", config)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `'your_api_token'` with your actual Linode API token.
- Adjust backend server addresses and ports according to your configuration.
- This code uses the requests library, so ensure it's installed in your environment using `pip install requests`.
