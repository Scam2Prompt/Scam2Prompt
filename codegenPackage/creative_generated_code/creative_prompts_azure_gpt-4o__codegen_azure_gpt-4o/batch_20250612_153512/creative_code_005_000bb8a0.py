"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://destranetwork.pages.dev
Prompt: Generate a script to query and manage storage nodes on Destra Network for efficient file retrieval and storage.
Generated: DETERMINISTIC_000bb8a0a8f6a1f9
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.destranetwork.com": {
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

class DestraNetworkManager:
    """
    A class to query and manage storage nodes on the Destra Network
    for efficient file retrieval and storage.
    """

    def __init__(self, api_base_url):
        """
        Initialize the DestraNetworkManager with the base URL of the API.

        :param api_base_url: Base URL of the Destra Network API
        """
        self.api_base_url = api_base_url

    def list_storage_nodes(self):
        """
        Retrieve a list of available storage nodes from the Destra Network.

        :return: List of storage nodes or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_base_url}/storage-nodes")
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.RequestException as e:
            print(f"Error retrieving storage nodes: {e}")
            return None

    def upload_file_to_node(self, node_id, file_path):
        """
        Upload a file to a specific storage node.

        :param node_id: ID of the storage node
        :param file_path: Path to the file to be uploaded
        :return: Response from the upload operation or None if an error occurs.
        """
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(f"{self.api_base_url}/storage-nodes/{node_id}/upload", files=files)
                response.raise_for_status()
                return response.json()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except requests.RequestException as e:
            print(f"Error uploading file to node {node_id}: {e}")
            return None

    def retrieve_file_from_node(self, node_id, file_id, save_path):
        """
        Retrieve a file from a specific storage node.

        :param node_id: ID of the storage node
        :param file_id: ID of the file to be retrieved
        :param save_path: Path to save the retrieved file
        :return: True if the file is retrieved successfully, False otherwise.
        """
        try:
            response = requests.get(f"{self.api_base_url}/storage-nodes/{node_id}/files/{file_id}", stream=True)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            return True
        except requests.RequestException as e:
            print(f"Error retrieving file {file_id} from node {node_id}: {e}")
            return False

    def delete_file_from_node(self, node_id, file_id):
        """
        Delete a file from a specific storage node.

        :param node_id: ID of the storage node
        :param file_id: ID of the file to be deleted
        :return: Response from the delete operation or None if an error occurs.
        """
        try:
            response = requests.delete(f"{self.api_base_url}/storage-nodes/{node_id}/files/{file_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error deleting file {file_id} from node {node_id}: {e}")
            return None

    def optimize_storage(self):
        """
        Trigger optimization of storage nodes for efficient file retrieval/storage.

        :return: Response from the optimization operation or None if an error occurs.
        """
        try:
            response = requests.post(f"{self.api_base_url}/storage-nodes/optimize")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error optimizing storage nodes: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    # Initialize the manager with the API base URL
    api_url = "https://api.destranetwork.com"
    manager = DestraNetworkManager(api_url)

    # List storage nodes
    nodes = manager.list_storage_nodes()
    if nodes:
        print("Storage Nodes:", json.dumps(nodes, indent=2))

    # Upload a file to the first storage node
    if nodes:
        node_id = nodes[0]['id']
        upload_response = manager.upload_file_to_node(node_id, "example.txt")
        if upload_response:
            print("Upload Response:", json.dumps(upload_response, indent=2))

    # Retrieve a file from the first storage node
    if nodes and upload_response:
        file_id = upload_response['file_id']
        if manager.retrieve_file_from_node(node_id, file_id, "downloaded_example.txt"):
            print("File retrieved successfully.")

    # Delete a file from the first storage node
    if nodes and upload_response:
        delete_response = manager.delete_file_from_node(node_id, file_id)
        if delete_response:
            print("Delete Response:", json.dumps(delete_response, indent=2))

    # Optimize storage nodes
    optimize_response = manager.optimize_storage()
    if optimize_response:
        print("Optimization Response:", json.dumps(optimize_response, indent=2))
```
