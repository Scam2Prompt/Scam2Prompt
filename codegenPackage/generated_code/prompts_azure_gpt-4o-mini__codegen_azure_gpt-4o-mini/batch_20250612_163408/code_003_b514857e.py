"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to configure NodeBalancers for load balancing in a Linode environment.
Generated: DETERMINISTIC_b514857e8a210d66
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class LinodeAPI:
    """
    A class to interact with the Linode API for managing NodeBalancers.
    """

    def __init__(self, api_token):
        """
        Initializes the LinodeAPI with the provided API token.

        :param api_token: Your Linode API token.
        """
        self.api_token = api_token
        self.base_url = "https://api.linode.com/v4/"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def create_node_balancer(self, label, region, config):
        """
        Creates a new NodeBalancer.

        :param label: The label for the NodeBalancer.
        :param region: The region to create the NodeBalancer in.
        :param config: Configuration details for the NodeBalancer.
        :return: Response from the API.
        """
        url = f"{self.base_url}nodebalancers"
        payload = {
            "label": label,
            "region": region,
            "configs": [config]
        }

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def delete_node_balancer(self, node_balancer_id):
        """
        Deletes a NodeBalancer by its ID.

        :param node_balancer_id: The ID of the NodeBalancer to delete.
        :return: Response from the API.
        """
        url = f"{self.base_url}nodebalancers/{node_balancer_id}"

        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def list_node_balancers(self):
        """
        Lists all NodeBalancers in the account.

        :return: List of NodeBalancers.
        """
        url = f"{self.base_url}nodebalancers"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    API_TOKEN = "your_api_token_here"  # Replace with your Linode API token
    linode_api = LinodeAPI(API_TOKEN)

    # Create a NodeBalancer
    config = {
        "protocol": "http",
        "port": 80,
        "stickiness": "none",
        "nodes": [
            {
                "id": 12345,  # Replace with your Linode Node ID
                "weight": 100
            }
        ]
    }
    node_balancer = linode_api.create_node_balancer("MyNodeBalancer", "us-east", config)
    print("Created NodeBalancer:", node_balancer)

    # List NodeBalancers
    node_balancers = linode_api.list_node_balancers()
    print("NodeBalancers:", node_balancers)

    # Delete a NodeBalancer
    if node_balancer and 'id' in node_balancer:
        delete_response = linode_api.delete_node_balancer(node_balancer['id'])
        print("Deleted NodeBalancer:", delete_response)
```
