"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzcf.land
Prompt: Provide a step-by-step guide to interact with a mapping portal API that requires user authentication, including handling errors if no maps are visible.
Generated: DETERMINISTIC_58cb343bf246e76f
Batch ID: 20250612_145727
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mappingportal.com": {
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

class MappingPortalAPI:
    """
    A class to interact with a mapping portal API that requires user authentication.
    """

    def __init__(self, base_url, username, password):
        """
        Initialize the API client with the portal's base URL, username, and password.
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.token = None

    def authenticate(self):
        """
        Authenticate the user and obtain an access token.
        """
        auth_url = f"{self.base_url}/auth/login"
        payload = {
            'username': self.username,
            'password': self.password
        }

        try:
            response = requests.post(auth_url, json=payload)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            data = response.json()

            # Check if token is present in the response
            if 'token' in data:
                self.token = data['token']
                print("Authentication successful!")
            else:
                raise ValueError("Authentication failed: No token received")

        except requests.exceptions.RequestException as e:
            print(f"Error during authentication: {e}")
            raise

    def get_visible_maps(self):
        """
        Fetch the list of visible maps for the authenticated user.
        """
        if not self.token:
            raise ValueError("Error: No authentication token. Please authenticate first.")

        maps_url = f"{self.base_url}/maps"
        headers = {
            'Authorization': f"Bearer {self.token}"
        }

        try:
            response = requests.get(maps_url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
            maps = response.json()

            if not maps:
                print("No maps are currently visible for the user.")
            else:
                print("Visible maps retrieved successfully!")
                return maps

        except requests.exceptions.RequestException as e:
            print(f"Error fetching visible maps: {e}")
            raise

    def run(self):
        """
        Main method to execute the process of authenticating and fetching maps.
        """
        try:
            # Step 1: Authenticate the user
            self.authenticate()

            # Step 2: Get the visible maps
            maps = self.get_visible_maps()

            if maps:
                # Output the list of visible maps
                for index, map_item in enumerate(maps, start=1):
                    print(f"{index}. Map Name: {map_item.get('name', 'Unknown')}, ID: {map_item.get('id', 'Unknown')}")

        except Exception as e:
            print(f"An error occurred: {e}")


# Example of how to use the class
if __name__ == "__main__":
    # Replace these with actual credentials and base URL
    BASE_URL = "https://api.mappingportal.com"
    USERNAME = "example_user"
    PASSWORD = "secure_password"

    # Create an instance of the API client
    api_client = MappingPortalAPI(BASE_URL, USERNAME, PASSWORD)

    # Run the process
    api_client.run()
```
