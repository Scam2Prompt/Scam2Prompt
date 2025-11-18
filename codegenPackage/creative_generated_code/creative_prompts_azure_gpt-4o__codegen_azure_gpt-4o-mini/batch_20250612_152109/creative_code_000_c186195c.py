"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpkad.lamongankab.go.id
Prompt: Write Python code to interact with the "e-APBD" application for preparing RKA, APBD, and DPA documents for regional government organizations, as described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_c186195c9c3e6885
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bpkad.lamongan.go.id/e-apbd": {
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

class EAPBDClient:
    """
    A client class to interact with the e-APBD application for preparing RKA, APBD, and DPA documents.
    """
    
    BASE_URL = "https://api.bpkad.lamongan.go.id/e-apbd"

    def __init__(self, username: str, password: str):
        """
        Initializes the EAPBDClient with user credentials.

        Parameters:
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.token = None

    def authenticate(self):
        """
        Authenticates the user and obtains an access token.
        Raises:
            Exception: If authentication fails.
        """
        auth_url = f"{self.BASE_URL}/auth/login"
        try:
            response = self.session.post(auth_url, json={"username": self.username, "password": self.password})
            response.raise_for_status()
            self.token = response.json().get("token")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Authentication failed: {e}")

    def prepare_document(self, document_type: str, data: dict):
        """
        Prepares the specified document type with the provided data.

        Parameters:
            document_type (str): The type of document to prepare (RKA, APBD, or DPA).
            data (dict): The data required for document preparation.

        Raises:
            ValueError: If the document type is invalid.
            Exception: If document preparation fails.
        """
        valid_document_types = ['RKA', 'APBD', 'DPA']
        if document_type not in valid_document_types:
            raise ValueError(f"Invalid document type. Choose from {valid_document_types}.")

        prepare_url = f"{self.BASE_URL}/documents/{document_type}/prepare"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = self.session.post(prepare_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()  # Return the response containing document preparation result
        except requests.exceptions.RequestException as e:
            raise Exception(f"Document preparation failed: {e}")

    def logout(self):
        """
        Logs out the current session and invalidates the token.
        """
        logout_url = f"{self.BASE_URL}/auth/logout"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = self.session.post(logout_url, headers=headers)
            response.raise_for_status()
            self.token = None  # Invalidate the token
        except requests.exceptions.RequestException as e:
            print(f"Logout failed: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual username and password
    USERNAME = "your_username"
    PASSWORD = "your_password"

    client = EAPBDClient(USERNAME, PASSWORD)
    try:
        client.authenticate()
        document_data = {
            "field1": "value1",  # Fill with actual data
            "field2": "value2",
            # Other required fields...
        }
        result = client.prepare_document("RKA", document_data)
        print("Document prepared successfully:", result)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client.logout()
```
