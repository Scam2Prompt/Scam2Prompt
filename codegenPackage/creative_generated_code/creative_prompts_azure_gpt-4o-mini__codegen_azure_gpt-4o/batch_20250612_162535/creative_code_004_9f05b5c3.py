"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: What steps are involved in making personal data portable on the Vana Network, and how can I automate this process with code?
Generated: DETERMINISTIC_9f05b5c328a9bd5b
Batch ID: 20250612_162535
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vananetwork.com/v1": {
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
"""
Automating the process of making personal data portable on the Vana Network.

This script assumes the Vana Network provides APIs for data portability
and includes authentication, data retrieval, and format conversion steps.

Requirements:
- Python 3.x
- Libraries: `requests`, `json`.

Steps:
1. Authenticate user.
2. Fetch personal data from the Vana Network.
3. Convert data into portable format (e.g., JSON, CSV).
4. Save the data locally or push to another destination.
"""

import requests
import json
import csv
import os

# Constants
API_BASE_URL = "https://api.vananetwork.com/v1"
AUTH_ENDPOINT = f"{API_BASE_URL}/auth"
DATA_ENDPOINT = f"{API_BASE_URL}/personal-data"
EXPORT_DIR = "./exported_data"  # Directory to save exported files

# Error classes
class VanaNetworkError(Exception):
    """Custom exception for Vana Network errors."""
    pass


def authenticate(api_key):
    """
    Authenticate the user and obtain an access token.

    :param api_key: API key for authentication.
    :return: Access token string.
    :raises VanaNetworkError: If authentication fails.
    """
    payload = {"api_key": api_key}
    response = requests.post(AUTH_ENDPOINT, json=payload)
    
    # Error handling
    if response.status_code != 200:
        raise VanaNetworkError(f"Authentication failed: {response.text}")
    
    return response.json().get("access_token")


def fetch_personal_data(access_token):
    """
    Fetch personal data from the Vana Network.

    :param access_token: Valid access token obtained from authentication.
    :return: JSON data containing personal information.
    :raises VanaNetworkError: If data fetching fails.
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(DATA_ENDPOINT, headers=headers)
    
    # Error handling
    if response.status_code != 200:
        raise VanaNetworkError(f"Failed to fetch personal data: {response.text}")
    
    return response.json()


def save_data_as_json(data, filepath):
    """
    Save data in JSON format.

    :param data: Data to save.
    :param filepath: File path for the saved data.
    """
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def save_data_as_csv(data, filepath):
    """
    Save data in CSV format.

    :param data: Data to save (JSON object or list of dictionaries).
    :param filepath: File path for the saved data.
    """
    if not isinstance(data, list):
        data = [data]  # Convert single object to list for CSV compatibility
    
    # Writing data to CSV
    with open(filepath, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def export_personal_data(api_key, export_format="json"):
    """
    Automate the process of exporting personal data.

    :param api_key: User's API key for authentication.
    :param export_format: Format for exporting data ('json' or 'csv').
    """
    try:
        # Step 1: Authenticate user
        access_token = authenticate(api_key)
        print("Authentication successful.")

        # Step 2: Fetch personal data
        personal_data = fetch_personal_data(access_token)
        print("Personal data fetched successfully.")

        # Step 3: Export data to specified format
        if not os.path.exists(EXPORT_DIR):
            os.makedirs(EXPORT_DIR)  # Create export directory if it doesn't exist
        
        if export_format == "json":
            json_path = os.path.join(EXPORT_DIR, "personal_data.json")
            save_data_as_json(personal_data, json_path)
            print(f"Personal data saved as JSON: {json_path}")
        elif export_format == "csv":
            csv_path = os.path.join(EXPORT_DIR, "personal_data.csv")
            save_data_as_csv(personal_data, csv_path)
            print(f"Personal data saved as CSV: {csv_path}")
        else:
            raise ValueError("Invalid export format. Use 'json' or 'csv'.")
    
    except (VanaNetworkError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    # Replace 'your-api-key-here' with a valid API key
    USER_API_KEY = "your-api-key-here"
    
    # Export data in JSON format
    export_personal_data(USER_API_KEY, export_format="json")
    
    # To export in CSV format, change export_format="csv"
    # export_personal_data(USER_API_KEY, export_format="csv")
```
