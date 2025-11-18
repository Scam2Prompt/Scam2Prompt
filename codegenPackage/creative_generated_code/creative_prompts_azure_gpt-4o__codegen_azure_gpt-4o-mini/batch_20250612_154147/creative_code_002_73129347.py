"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m2bob.shop
Prompt: Generate code to interact with M2Bob's features for automating tasks in Metin2, ensuring compatibility with the server list provided on the M2Bob website.
Generated: DETERMINISTIC_73129347c30b0e99
Batch ID: 20250612_154147
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://m2bob.com/api": {
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

class M2BobAutomation:
    """
    A class to interact with M2Bob's features for automating tasks in Metin2.
    This class encapsulates methods for fetching server lists and performing
    operations on them.
    """

    BASE_URL = "https://m2bob.com/api"  # Base URL for M2Bob API

    def __init__(self):
        self.servers = self.get_servers()
    
    def get_servers(self):
        """
        Fetch the list of servers from M2Bob API.

        Returns:
            list: A list of available servers.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/servers")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('servers', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching servers: {e}")
            return []

    def perform_task_on_server(self, server_id, task):
        """
        Perform a specific task on a given server.

        Args:
            server_id (str): The ID of the server to act upon.
            task (str): The task to perform.

        Returns:
            bool: True if the task was successfully performed, False otherwise.
        """
        if server_id not in [server['id'] for server in self.servers]:
            print(f"Server ID {server_id} is not valid.")
            return False

        try:
            task_payload = {
                'server_id': server_id,
                'task': task
            }
            response = requests.post(f"{self.BASE_URL}/perform_task", json=task_payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('success', False)
        except requests.exceptions.RequestException as e:
            print(f"Error performing task on server {server_id}: {e}")
            return False

if __name__ == "__main__":
    # Example usage of the M2BobAutomation class
    automation = M2BobAutomation()

    # Iterate through the list of servers and perform a test task
    for server in automation.servers:
        success = automation.perform_task_on_server(server['id'], "test_task")
        if success:
            print(f"Task completed successfully on server {server['name']}.")
        else:
            print(f"Failed to complete task on server {server['name']}.")
```
