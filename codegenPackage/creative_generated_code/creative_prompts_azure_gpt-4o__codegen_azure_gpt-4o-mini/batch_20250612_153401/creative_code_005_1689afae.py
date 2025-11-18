"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity2.pages.dev
Prompt: Develop a Python program to interact with OpenCog Hyperon’s Atomspace knowledge metagraph for collaborative AI strategies.
Generated: DETERMINISTIC_1689afae5958cbfc
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:12345/api": {
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

class AtomspaceClient:
    """
    A client to interact with OpenCog Hyperon’s Atomspace for knowledge management.
    """

    def __init__(self, base_url):
        """
        Initializes the AtomspaceClient with the provided base URL.

        Args:
            base_url (str): The base URL of the Atomspace API.
        """
        self.base_url = base_url

    def _send_request(self, endpoint, method='GET', data=None):
        """
        Sends an HTTP request to the Atomspace API.

        Args:
            endpoint (str): The specific API endpoint to hit.
            method (str): The HTTP method ('GET', 'POST', etc.).
            data (dict): The data to send with the request, if applicable.

        Returns:
            dict: The response from the API parsed as JSON.

        Raises:
            Exception: If the response is not successful.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url, json=data)
            else:
                raise ValueError("Unsupported HTTP method.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def get_atoms(self):
        """
        Retrieves all atoms from the Atomspace.

        Returns:
            list: A list of atoms in the Atomspace.
        """
        return self._send_request('atoms')

    def add_atom(self, atom_data):
        """
        Adds a new atom to the Atomspace.

        Args:
            atom_data (dict): A dictionary containing the atom's data.

        Returns:
            dict: The response from the API after adding the atom.
        """
        return self._send_request('atoms', method='POST', data=atom_data)

    def query_metagraph(self, query):
        """
        Queries the metagraph for specific patterns or relationships.

        Args:
            query (dict): The query to be executed on the metagraph.

        Returns:
            list: The result of the metagraph query.
        """
        return self._send_request('metagraph/query', method='POST', data=query)

if __name__ == "__main__":
    # Example usage of the AtomspaceClient
    atomspace_url = "http://localhost:12345/api"  # Replace with your Atomspace API URL

    client = AtomspaceClient(atomspace_url)

    try:
        # Fetch and print all atoms from the Atomspace
        atoms = client.get_atoms()
        print("Atoms in Atomspace:", atoms)

        # Example: Adding a new atom
        new_atom = {
            "type": "ConceptNode",
            "name": "CollaborativeAI",
            "description": "A concept representing collaborative AI strategies."
        }
        response = client.add_atom(new_atom)
        print("Added atom response:", response)

        # Example: Query the metagraph
        query = {
            "type": "Relation",
            "subject": "CollaborativeAI",
            "predicate": "relatedTo"
        }
        results = client.query_metagraph(query)
        print("Query results:", results)

    except Exception as e:
        print(f"An error occurred during Atomspace interaction: {e}")
```
