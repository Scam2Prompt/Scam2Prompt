"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Write code for synchronizing offline data collected on a mobile app with a web platform, ensuring seamless integration as highlighted in Azagros' solution.
Generated: DETERMINISTIC_0c79d8acd7b9f320
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.webplatform.com": {
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
import os

# Configuration for the web platform API
API_BASE_URL = "https://api.webplatform.com"
API_ENDPOINT_SYNC = "/sync"
API_KEY = "your_api_key_here"

# File path for offline data storage
OFFLINE_DATA_FILE = "offline_data.json"

def load_offline_data(file_path):
    """
    Load offline data from the specified JSON file.
    If the file does not exist, return an empty list.

    :param file_path: Path to the offline data file
    :return: List of offline data records
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Return empty list if file does not exist
        return []
    except json.JSONDecodeError as e:
        # Log the error and return empty list
        print(f"Error decoding JSON: {e}")
        return []

def save_offline_data(file_path, data):
    """
    Save offline data to the specified JSON file.

    :param file_path: Path to the offline data file
    :param data: List of offline data records to save
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving offline data: {e}")

def sync_data_with_server(api_url, api_key, data):
    """
    Synchronize offline data with the web platform server.

    :param api_url: API URL for data synchronization
    :param api_key: API key for authentication
    :param data: List of offline data records to sync
    :return: Response from the server
    """
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    try:
        response = requests.post(api_url, headers=headers, json={"records": data})
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()      # Return server response as JSON
    except requests.exceptions.RequestException as e:
        print(f"Error syncing data with server: {e}")
        return {"success": False, "error": str(e)}

def main():
    """
    Main function for synchronizing offline data with the web platform.
    """
    # Load offline data
    offline_data = load_offline_data(OFFLINE_DATA_FILE)

    # If no offline data is available, exit the function
    if not offline_data:
        print("No offline data to sync.")
        return

    # Sync data with server
    print("Synchronizing data with server...")
    server_response = sync_data_with_server(f"{API_BASE_URL}{API_ENDPOINT_SYNC}", API_KEY, offline_data)

    # Handle server response
    if server_response.get("success"):
        print("Data synchronization successful.")
        # Clear offline data after successful sync
        save_offline_data(OFFLINE_DATA_FILE, [])
    else:
        print(f"Data synchronization failed: {server_response.get('error')}")

if __name__ == "__main__":
    # Execute the main function
    main()
```
