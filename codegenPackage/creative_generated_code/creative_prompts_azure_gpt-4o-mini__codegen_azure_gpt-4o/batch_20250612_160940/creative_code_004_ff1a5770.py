"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbffa3pntrrd6o7gbifdctk2ingttjnunx3qdqyzr27guaqcdgbi.ipfs.dweb.link
Prompt: Explain how to rent AI nodes on Node AI and the pricing structure for different GPU types.
Generated: DETERMINISTIC_ff1a5770de47233c
Batch ID: 20250612_160940
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nodeai.com/v1": {
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

class NodeAIRentalService:
    """
    NodeAIRentalService allows users to fetch AI node rental details and pricing structure.
    This code demonstrates how to interact with the Node AI API to retrieve information about renting AI nodes.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.nodeai.com/v1"):
        """
        Initializes the rental service with the API key and base URL.

        :param api_key: Your API key for accessing Node AI services.
        :param base_url: The base URL of the Node AI API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_gpu_pricing(self) -> dict:
        """
        Fetches the pricing structure for different GPU types from Node AI.

        :return: Dictionary containing GPU types and their prices.
        :raises: Exception if the API call fails.
        """
        endpoint = f"{self.base_url}/pricing/gpu"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch GPU pricing: {e}")

    def get_available_nodes(self) -> dict:
        """
        Fetches the list of available AI nodes for rent.

        :return: Dictionary containing details of available AI nodes.
        :raises: Exception if the API call fails.
        """
        endpoint = f"{self.base_url}/nodes/available"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch available nodes: {e}")

def main():
    """
    Main function to demonstrate fetching GPU pricing and available AI nodes.
    Replace 'your_api_key_here' with your actual API key for testing.
    """
    api_key = "your_api_key_here"  # Replace with your Node AI API key
    rental_service = NodeAIRentalService(api_key)

    try:
        # Fetch and display GPU pricing structure
        gpu_pricing = rental_service.get_gpu_pricing()
        print("GPU Pricing Structure:")
        for gpu_type, price in gpu_pricing.items():
            print(f"  {gpu_type}: ${price}/hour")

        # Fetch and display available AI nodes
        available_nodes = rental_service.get_available_nodes()
        print("\nAvailable AI Nodes:")
        for node in available_nodes:
            print(f"  Node ID: {node['id']}, GPU Type: {node['gpu_type']}, Status: {node['status']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
