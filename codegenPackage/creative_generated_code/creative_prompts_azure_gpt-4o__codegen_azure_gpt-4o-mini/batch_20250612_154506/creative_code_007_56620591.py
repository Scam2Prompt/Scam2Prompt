"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Suggest APIs or libraries for integrating Gmail email aliases into a domain management system, as mentioned in the resources section of norion.loan.
Generated: DETERMINISTIC_5662059128a05fa8
Batch ID: 20250612_154506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/gmail/v1/users": {
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

class GmailAPI:
    """
    A class to interact with the Gmail API for managing email aliases.
    """

    BASE_URL = "https://www.googleapis.com/gmail/v1/users"

    def __init__(self, user_id, access_token):
        """
        Initializes the GmailAPI with user ID and access token.

        :param user_id: The user's email address or 'me' for the authenticated user.
        :param access_token: OAuth2 access token for authentication.
        """
        self.user_id = user_id
        self.access_token = access_token

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes an HTTP request to the Gmail API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method (GET, POST, DELETE).
        :param data: The data to send with the request (if applicable).
        :return: Response object from the API.
        """
        url = f"{self.BASE_URL}/{self.user_id}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method specified.")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def list_aliases(self):
        """
        Lists all email aliases for the authenticated user.
        
        :return: A list of email aliases.
        """
        endpoint = "settings/forwardingAddresses"
        return self._make_request(endpoint)

    def add_alias(self, alias_email):
        """
        Adds a new email alias for the user.

        :param alias_email: The new alias email address to add.
        :return: Response from the Gmail API.
        """
        endpoint = "settings/forwardingAddresses"
        data = {
            "forwardingEmail": alias_email
        }
        return self._make_request(endpoint, method='POST', data=data)

    def delete_alias(self, alias_email):
        """
        Deletes an existing email alias for the user.

        :param alias_email: The alias email address to delete.
        :return: Response from the Gmail API.
        """
        endpoint = f"settings/forwardingAddresses/{alias_email}"
        return self._make_request(endpoint, method='DELETE')

# Example usage:
if __name__ == "__main__":
    # Replace with actual user ID and access token
    USER_ID = "me"  # or specific user email
    ACCESS_TOKEN = "your_access_token_here"

    gmail_api = GmailAPI(USER_ID, ACCESS_TOKEN)

    # List current aliases
    aliases = gmail_api.list_aliases()
    print("Current Aliases:", aliases)

    # Add a new alias
    new_alias = "newalias@example.com"
    response = gmail_api.add_alias(new_alias)
    print("Add Alias Response:", response)

    # Delete an alias
    response = gmail_api.delete_alias(new_alias)
    print("Delete Alias Response:", response)
```
