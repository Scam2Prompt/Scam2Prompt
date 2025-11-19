"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abracadabra.top
Prompt: How can I set up a virtual server with Timeweb for my online store, including configuration options and pricing details?
Generated: DETERMINISTIC_40e7799bd530ed72
Batch ID: 20250612_155842
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.timeweb.com/v1": {
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

class TimewebVirtualServer:
    """
    A class to interact with the Timeweb API for creating and managing a virtual server.

    Attributes:
        api_url (str): The base URL for the Timeweb API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str):
        """
        Initializes the TimewebVirtualServer with an API key.

        Parameters:
            api_key (str): The API key for the Timeweb API.
        """
        self.api_url = "https://api.timeweb.com/v1"
        self.api_key = api_key

    def create_server(self, server_name: str, plan_id: int, region: str) -> dict:
        """
        Creates a virtual server with specified configuration options.

        Parameters:
            server_name (str): The name of the server.
            plan_id (int): The ID of the server plan.
            region (str): The region where the server will be hosted.

        Returns:
            dict: The response from the Timeweb API containing server details.
        """
        endpoint = f"{self.api_url}/servers"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": server_name,
            "plan_id": plan_id,
            "region": region
        }

        try:
            response = requests.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(f"HTTP error occurred: {err}")
        except Exception as e:
            raise SystemExit(f"An error occurred: {e}")

    def get_plans(self) -> list:
        """
        Retrieves available server plans and their pricing details.

        Returns:
            list: A list of server plans with pricing details.
        """
        endpoint = f"{self.api_url}/plans"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(f"HTTP error occurred: {err}")
        except Exception as e:
            raise SystemExit(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Timeweb API key
    api_key = 'your_api_key'
    
    timeweb_server = TimewebVirtualServer(api_key)
    
    # Fetch and display available plans
    try:
        plans = timeweb_server.get_plans()
        print("Available Plans:")
        for plan in plans:
            print(f"Plan ID: {plan['id']}, Name: {plan['name']}, Price: {plan['price']}")
        
        # Create a server (example values)
        server_name = "MyOnlineStoreServer"
        plan_id = plans[0]['id']  # Use the first available plan
        region = "us-central"  # Example region, replace with desired region

        server_details = timeweb_server.create_server(server_name, plan_id, region)
        print("Server Created Successfully:", server_details)
    
    except Exception as e:
        print(f"Error: {e}")
```
