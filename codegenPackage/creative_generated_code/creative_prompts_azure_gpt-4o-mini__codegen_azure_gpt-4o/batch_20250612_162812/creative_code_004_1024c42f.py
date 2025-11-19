"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://b24.medianation.ru
Prompt: What API methods are available for user authorization in "1С-Битрикс24"?
Generated: DETERMINISTIC_1024c42f53e9ccb3
Batch ID: 20250612_162812
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://yourcompanyname.bitrix24.com/rest/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourcompanyname.bitrix24.com/oauth/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourcompanyname.bitrix24.com/oauth/authorize": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourredirecturl.com": {
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

# Constants
BITRIX24_BASE_URL = "https://yourcompanyname.bitrix24.com/rest/"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "https://yourredirecturl.com"
AUTHORIZATION_URL = f"https://yourcompanyname.bitrix24.com/oauth/authorize"
TOKEN_URL = f"https://yourcompanyname.bitrix24.com/oauth/token"

def get_authorization_url():
    """
    Construct the authorization URL for user login.

    Returns:
        str: Authorization URL.
    """
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
    }
    return f"{AUTHORIZATION_URL}?{requests.compat.urlencode(params)}"

def exchange_code_for_token(auth_code: str):
    """
    Exchange authorization code for access and refresh tokens.

    Args:
        auth_code (str): Authorization code returned after user login.

    Returns:
        dict: Response containing access and refresh tokens.
    """
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
    }
    try:
        response = requests.post(TOKEN_URL, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error exchanging code for token: {e}")
        return None

def refresh_access_token(refresh_token: str):
    """
    Refresh the access token using a valid refresh token.

    Args:
        refresh_token (str): Refresh token.

    Returns:
        dict: Response containing new access and refresh tokens.
    """
    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token,
    }
    try:
        response = requests.post(TOKEN_URL, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error refreshing access token: {e}")
        return None

def test_api_call(access_token: str):
    """
    Test an API call using the obtained access token.

    Args:
        access_token (str): Valid access token.

    Returns:
        dict: API response data.
    """
    endpoint = f"{BITRIX24_BASE_URL}/user.current.json"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error making API call: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Step 1: User visits this URL to authorize access
    print("Visit this URL to authorize access:")
    print(get_authorization_url())

    # Step 2: After user authorizes, they receive a code. Exchange it for tokens.
    auth_code = input("Enter the authorization code: ").strip()
    tokens = exchange_code_for_token(auth_code)

    if tokens:
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")
        print("Access token:", access_token)
        print("Refresh token:", refresh_token)

        # Test API call
        user_info = test_api_call(access_token)
        print("User Info:", user_info)

        # Refresh the access token when needed
        new_tokens = refresh_access_token(refresh_token)
        print("Refreshed tokens:", new_tokens)
```
