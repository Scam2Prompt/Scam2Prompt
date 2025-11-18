"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Provide step-by-step instructions for integrating Somnia's Layer 1 blockchain into an existing metaverse application to enable cross-platform interactions.
Generated: DETERMINISTIC_91d64b0a0795134e
Batch ID: 20250612_151301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.somnia.io/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a production-ready Python code example for integrating Somnia's Layer 1 blockchain into an existing metaverse application. This code assumes you have access to Somnia's API/SDK and have valid credentials.

```python
# Import required libraries
import requests
import json

# Constants for Somnia Blockchain API
SOMNIA_API_URL = "https://api.somnia.io/v1/"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key
PROJECT_ID = "your_project_id_here"  # Replace with your project ID

# Function to initialize connection to Somnia Blockchain
def initialize_somnia_connection(api_key, project_id):
    """
    Initialize and authenticate with the Somnia Layer 1 blockchain.
    
    Args:
        api_key (str): Your API key for Somnia.
        project_id (str): Your project ID for the metaverse application.
    
    Returns:
        dict: Authentication token and status of initialization.
    """
    try:
        # Prepare authentication payload
        payload = {
            "apiKey": api_key,
            "projectId": project_id
        }
        headers = {
            "Content-Type": "application/json"
        }

        # Send POST request to authenticate
        response = requests.post(SOMNIA_API_URL + "auth", headers=headers, data=json.dumps(payload))

        # Check the response status
        if response.status_code == 200:
            auth_data = response.json()
            print("Successfully authenticated with Somnia Blockchain.")
            return auth_data
        else:
            print(f"Failed to authenticate. Status code: {response.status_code}, Error: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred during authentication: {e}")
        return None

# Function to register a metaverse user on the blockchain
def register_user_on_blockchain(user_id, user_data, auth_token):
    """
    Register a new user to the Somnia blockchain for cross-platform interactions.
    
    Args:
        user_id (str): Unique ID of the user in the metaverse application.
        user_data (dict): Additional data about the user (e.g., username, avatar, preferences).
        auth_token (str): Authentication token from Somnia.
    
    Returns:
        bool: True if registration succeeded, False otherwise.
    """
    try:
        # Prepare registration payload
        payload = {
            "userId": user_id,
            "userData": user_data
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        # Send POST request to register user
        response = requests.post(SOMNIA_API_URL + "users/register", headers=headers, data=json.dumps(payload))

        # Check response status
        if response.status_code == 201:
            print(f"User {user_id} successfully registered on the blockchain.")
            return True
        else:
            print(f"Failed to register user. Status code: {response.status_code}, Error: {response.text}")
            return False

    except Exception as e:
        print(f"An error occurred while registering user: {e}")
        return False

# Function to fetch cross-platform interactions for a user
def fetch_user_interactions(user_id, auth_token):
    """
    Fetch cross-platform interactions for a user from the Somnia blockchain.
    
    Args:
        user_id (str): Unique ID of the user in the metaverse application.
        auth_token (str): Authentication token from Somnia.
    
    Returns:
        dict: Interaction data or an empty dictionary if an error occurred.
    """
    try:
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }

        # Send GET request to fetch interactions
        response = requests.get(SOMNIA_API_URL + f"users/{user_id}/interactions", headers=headers)

        # Check response status
        if response.status_code == 200:
            interactions = response.json()
            print(f"Successfully fetched interactions for user {user_id}.")
            return interactions
        else:
            print(f"Failed to fetch interactions. Status code: {response.status_code}, Error: {response.text}")
            return {}

    except Exception as e:
        print(f"An error occurred while fetching interactions: {e}")
        return {}

# Main function to demonstrate integration
def main():
    """
    Main function to demonstrate integration of Somnia blockchain with a metaverse application.
    """
    # Initialize connection to Somnia Blockchain
    auth_data = initialize_somnia_connection(API_KEY, PROJECT_ID)
    if not auth_data:
        print("Exiting due to failed blockchain initialization.")
        return

    auth_token = auth_data.get("authToken")
    if not auth_token:
        print("Invalid authentication token. Exiting.")
        return

    # Example user data
    user_id = "user123"
    user_data = {
        "username": "metaverse_hero",
        "avatar": "hero_avatar.png",
        "preferences": {"theme": "dark", "language": "en"}
    }

    # Register user on the blockchain
    registration_success = register_user_on_blockchain(user_id, user_data, auth_token)
    if not registration_success:
        print("Exiting due to failed user registration.")
        return

    # Fetch user interactions
    interactions = fetch_user_interactions(user_id, auth_token)
    if interactions:
        print("User interactions:", json.dumps(interactions, indent=4))
    else:
        print("No interactions found or an error occurred.")

# Run the main function
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `SOMNIA_API_URL`, `API_KEY`, and `PROJECT_ID` with your actual details provided by Somnia's documentation or account setup.
- Ensure that you handle sensitive data like API keys securely, using environment variables or a secrets manager.
- Error handling is implemented to ensure the application behaves gracefully during failures.
- The code is structured to be modular and follows Python best practices.
