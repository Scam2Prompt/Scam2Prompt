"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gyariasy.fromsmash.com
Prompt: Write a Python script that utilizes Smash to upload and share large files online.
Generated: DETERMINISTIC_6d8d7eea6e2d5cac
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fromsmash.com/v1/transfers": {
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
import os
import requests

def upload_large_file(file_path):
    """
    Uploads a large file to Smash and returns the shareable link.

    Args:
        file_path (str): Path to the file to be uploaded.

    Returns:
        str: Shareable link for the uploaded file.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: If the upload fails or an error occurs.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    smash_base_url = "https://api.fromsmash.com/v1/transfers"
    headers = {
        "Accept": "application/json",
        # Add authentication headers if available (for premium Smash accounts)
        # "Authorization": "Bearer <your_access_token>"
    }

    try:
        # Open the file in binary mode for uploading
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(smash_base_url, headers=headers, files=files)

        # Check if the request was successful
        if response.status_code != 201:
            raise Exception(f"Failed to upload file. Status code: {response.status_code}, Response: {response.text}")

        # Parse the JSON response to extract the shareable link
        response_data = response.json()
        shareable_link = response_data.get("url")

        if not shareable_link:
            raise Exception("Failed to retrieve the shareable link from the response.")

        return shareable_link

    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while making the request: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Replace with the path to your file
        file_path = "path/to/your/large/file"
        shareable_link = upload_large_file(file_path)
        print(f"File uploaded successfully! Shareable link: {shareable_link}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as error:
        print(f"Error: {error}")
```

Note: Replace `"path/to/your/large/file"` in the example usage with the actual path to your file. Additionally, if you have an authentication token for Smash API, include it in the headers section. Ensure you comply with Smash API's terms of use and documentation for production environments.
