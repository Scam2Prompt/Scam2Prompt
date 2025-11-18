"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python script to automate membership registration for a tennis club using the "easyVerein" API, ensuring the username format follows the convention "nachname_vorname" in lowercase.
Generated: DETERMINISTIC_5f6df0197dce1c7e
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.easyverein.com/v1": {
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

# Constants
API_BASE_URL = "https://api.easyverein.com/v1"
API_KEY = "your_api_key_here"  # Replace with your API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_username(last_name: str, first_name: str) -> str:
    """
    Generate a username following the convention 'nachname_vorname' in lowercase.
    Args:
        last_name (str): Last name of the member.
        first_name (str): First name of the member.
    Returns:
        str: Generated username.
    """
    return f"{last_name.lower()}_{first_name.lower()}"

def register_member(first_name: str, last_name: str, email: str, phone: str) -> dict:
    """
    Automates membership registration by sending data to the easyVerein API.
    Args:
        first_name (str): First name of the member.
        last_name (str): Last name of the member.
        email (str): Email address of the member.
        phone (str): Phone number of the member.
    Returns:
        dict: API response data.
    Raises:
        Exception: If the API request fails or returns an error.
    """
    # Generate username
    username = generate_username(last_name, first_name)

    # Prepare payload
    payload = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }

    try:
        # Send POST request to the API
        response = requests.post(f"{API_BASE_URL}/members", headers=HEADERS, data=json.dumps(payload))

        # Raise an exception if the response status code indicates an error
        response.raise_for_status()

        # Return the response data
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any errors during the API call
        print(f"An error occurred while registering the member: {e}")
        raise

def main():
    """
    Main function to interact with the user and automate membership registration.
    """
    print("Welcome to the Tennis Club Membership Registration")

    # Collect user input
    first_name = input("Enter the first name: ").strip()
    last_name = input("Enter the last name: ").strip()
    email = input("Enter the email: ").strip()
    phone = input("Enter the phone number: ").strip()

    # Register the member
    try:
        response = register_member(first_name, last_name, email, phone)
        print(f"Member registered successfully! Response: {response}")
    except Exception as e:
        print(f"Failed to register the member: {str(e)}")

if __name__ == "__main__":
    main()
```
