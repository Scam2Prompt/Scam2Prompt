"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write a script that interfaces with Panasonic's LED lighting API to manage multiple light types, including Đèn LED Panel and Đèn LED Rọi Ray.
Generated: DETERMINISTIC_e31ff359a2ac387d
Batch ID: 20250612_155356
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.panasonic-lighting.com/v1": {
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

# Constants for the Panasonic LED Lighting API
API_BASE_URL = "https://api.panasonic-lighting.com/v1"  # Replace with actual API URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Light Types
LIGHT_TYPES = {
    "panel": "Đèn LED Panel",
    "track": "Đèn LED Rọi Ray"
}

# Error messages
ERROR_MESSAGES = {
    "connection_error": "Failed to connect to the API.",
    "invalid_response": "Invalid response received from the API.",
    "authentication_error": "Authentication failed. Please check your API key.",
    "unknown_error": "An unknown error occurred."
}


def authenticate(api_key):
    """
    Authenticate with the Panasonic Lighting API.
    :param api_key: The API key for authentication.
    :return: True if authentication is successful, False otherwise.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/auth", headers={"Authorization": f"Bearer {api_key}"})
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            print(ERROR_MESSAGES["authentication_error"])
            return False
        else:
            print(ERROR_MESSAGES["invalid_response"])
            return False
    except requests.ConnectionError:
        print(ERROR_MESSAGES["connection_error"])
        return False
    except Exception:
        print(ERROR_MESSAGES["unknown_error"])
        return False


def get_light_status(light_type):
    """
    Fetch the status of the specified light type.
    :param light_type: The type of light (e.g., "panel", "track").
    :return: The status of the lights or None if an error occurs.
    """
    try:
        if light_type not in LIGHT_TYPES:
            raise ValueError("Invalid light type specified.")

        endpoint = f"{API_BASE_URL}/lights/{light_type}/status"
        response = requests.get(endpoint, headers={"Authorization": f"Bearer {API_KEY}"})

        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            print(ERROR_MESSAGES["invalid_response"])
            return None
    except requests.ConnectionError:
        print(ERROR_MESSAGES["connection_error"])
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception:
        print(ERROR_MESSAGES["unknown_error"])
        return None


def set_light_brightness(light_type, brightness):
    """
    Set the brightness of the specified light type.
    :param light_type: The type of light (e.g., "panel", "track").
    :param brightness: The brightness level (0 to 100).
    :return: True if successful, False otherwise.
    """
    try:
        if light_type not in LIGHT_TYPES:
            raise ValueError("Invalid light type specified.")
        if not (0 <= brightness <= 100):
            raise ValueError("Brightness must be between 0 and 100.")

        endpoint = f"{API_BASE_URL}/lights/{light_type}/brightness"
        payload = {"brightness": brightness}
        response = requests.post(endpoint, headers={"Authorization": f"Bearer {API_KEY}"}, json=payload)

        if response.status_code == 200:
            return True
        else:
            print(ERROR_MESSAGES["invalid_response"])
            return False
    except requests.ConnectionError:
        print(ERROR_MESSAGES["connection_error"])
        return False
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception:
        print(ERROR_MESSAGES["unknown_error"])
        return False


def main():
    """
    Main script logic for managing Panasonic LED lights.
    """
    # Authenticate with the API
    if not authenticate(API_KEY):
        return

    # Example usage
    try:
        # Get status of Đèn LED Panel
        panel_status = get_light_status("panel")
        if panel_status:
            print(f"Panel Status: {json.dumps(panel_status, indent=4)}")

        # Set brightness of Đèn LED Rọi Ray to 75%
        if set_light_brightness("track", 75):
            print("Brightness of Track Light set to 75%.")
        else:
            print("Failed to set brightness of Track Light.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
