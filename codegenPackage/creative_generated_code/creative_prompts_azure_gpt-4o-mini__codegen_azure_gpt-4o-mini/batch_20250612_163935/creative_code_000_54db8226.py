"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Generate a Python script that utilizes Polkadot's governance-allocated parachains for a common-good project, as discussed on Polkadot India.
Generated: DETERMINISTIC_54db8226d26e7287
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.polkadot.io": {
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

class PolkadotGovernanceClient:
    """
    A client to interact with Polkadot's governance-allocated parachains for common-good projects.
    """

    def __init__(self, endpoint: str):
        """
        Initializes the PolkadotGovernanceClient with the provided endpoint.

        :param endpoint: The RPC endpoint for the Polkadot blockchain.
        """
        self.endpoint = endpoint

    def fetch_parachains(self):
        """
        Fetches the list of parachains from the Polkadot network.

        :return: A list of parachains.
        :raises Exception: If the request to the endpoint fails.
        """
        try:
            response = requests.post(self.endpoint, json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "parachains_parachains",
                "params": []
            })
            response.raise_for_status()
            return response.json().get('result', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching parachains: {e}")

    def fetch_governance_projects(self):
        """
        Fetches the governance-allocated parachains for common-good projects.

        :return: A list of governance projects.
        :raises Exception: If the request to the endpoint fails.
        """
        parachains = self.fetch_parachains()
        common_good_projects = []

        for parachain in parachains:
            if parachain.get('isCommonGood'):
                common_good_projects.append(parachain)

        return common_good_projects

    def display_projects(self, projects):
        """
        Displays the common-good projects in a user-friendly format.

        :param projects: A list of common-good projects.
        """
        if not projects:
            print("No common-good projects found.")
            return

        print("Common-Good Projects:")
        for project in projects:
            print(f"- Parachain ID: {project['id']}, Name: {project.get('name', 'N/A')}")

def main():
    """
    Main entry point of the script to fetch and display common-good projects from Polkadot governance-allocated parachains.
    """
    endpoint = "https://rpc.polkadot.io"  # Replace with the specific Polkadot endpoint if needed
    client = PolkadotGovernanceClient(endpoint)

    try:
        common_good_projects = client.fetch_governance_projects()
        client.display_projects(common_good_projects)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
