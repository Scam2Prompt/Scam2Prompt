"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remix-ipfs-eths.com
Prompt: Write a function to confirm and execute the deletion of objects in a Mailcow domain administration system.
Generated: DETERMINISTIC_bf8119699579b3ec
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class MailcowAPIError(Exception):
    """Custom exception class for Mailcow API errors."""
    pass

class MailcowDomainAdmin:
    def __init__(self, api_url: str, api_token: str):
        """
        Initializes the MailcowDomainAdmin instance.

        :param api_url: The base URL of the Mailcow API.
        :param api_token: The API token for authentication.
        """
        self.api_url = api_url
        self.api_token = api_token

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Makes a request to the Mailcow API.

        :param endpoint: The API endpoint to call.
        :param method: HTTP method (GET or POST).
        :param data: Payload to send with POST requests.
        :return: Response from the API.
        :raises MailcowAPIError: If the API request fails.
        """
        headers = {'X-Api-Key': self.api_token}
        url = f"{self.api_url}/{endpoint}"
        
        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)

            # Raise an error for bad status codes
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise MailcowAPIError(f"API request failed: {e}")

    def confirm_and_delete_object(self, object_id: str, object_type: str):
        """
        Confirms and executes the deletion of an object in the Mailcow domain administration system.

        :param object_id: The identifier of the object to delete.
        :param object_type: The type of the object (e.g., 'domain', 'mailbox').
        :raises ValueError: If an invalid object type is provided.
        :raises MailcowAPIError: If the deletion fails.
        """
        valid_object_types = ['domain', 'mailbox', 'alias']
        
        if object_type not in valid_object_types:
            raise ValueError(f"Invalid object type: {object_type}. Valid types are: {valid_object_types}")

        # Confirm deletion from the user
        confirmation = input(f"Are you sure you want to delete the {object_type} with ID '{object_id}'? (yes/no): ")
        if confirmation.lower() != 'yes':
            print("Deletion aborted.")
            return

        # Prepare the endpoint based on object type
        endpoint = f"{object_type}/delete"

        # Make the API request to delete the object
        data = {'id': object_id}
        response = self._make_request(endpoint, method='POST', data=data)

        # Check if the deletion was successful
        if response.get('status') == 'success':
            print(f"{object_type.capitalize()} with ID '{object_id}' has been successfully deleted.")
        else:
            raise MailcowAPIError(f"Failed to delete {object_type} with ID '{object_id}'. Response: {response}")
```
