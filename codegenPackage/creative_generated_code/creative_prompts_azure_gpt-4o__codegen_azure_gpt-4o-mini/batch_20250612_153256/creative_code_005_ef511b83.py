"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Develop a code snippet that uses Skillchain's API to protect an artist's JPG file by storing it on the blockchain and affirming authorship.
Generated: DETERMINISTIC_ef511b834575d392
Batch ID: 20250612_153256
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.skillchain.io/v1": {
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

class SkillchainAPI:
    """
    A class to interact with the Skillchain API for storing JPG files on the blockchain
    and affirming authorship.
    """

    BASE_URL = "https://api.skillchain.io/v1"  # Update with the actual Skillchain API endpoint
    
    def __init__(self, api_key):
        """
        Initializes the SkillchainAPI with the provided API key.

        :param api_key: The API key to authenticate requests.
        """
        self.api_key = api_key

    def upload_file(self, file_path):
        """
        Uploads a JPG file to the Skillchain API and returns the file ID.

        :param file_path: The local path to the JPG file.
        :return: The file ID if upload is successful, else raises an Exception.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        # Prepare the headers and data for the request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{self.BASE_URL}/upload", headers=headers, files=files)

        # Check for successful response
        if response.status_code == 200:
            file_info = response.json()
            return file_info['id']  # Assuming the API returns a file ID
        else:
            raise Exception(f"Failed to upload file: {response.text}")

    def affirm_authorship(self, file_id, artist_name):
        """
        Affirms authorship of the uploaded file on the blockchain.

        :param file_id: The ID of the uploaded file.
        :param artist_name: The name of the artist to affirm authorship for.
        :return: Response from the API if successful, else raises an Exception.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "file_id": file_id,
            "artist_name": artist_name
        }
        
        response = requests.post(f"{self.BASE_URL}/affirm-authorship", headers=headers, json=payload)

        # Check for successful response
        if response.status_code == 200:
            return response.json()  # Return the response data
        else:
            raise Exception(f"Failed to affirm authorship: {response.text}")


def main():
    """
    Main function to demonstrate the use of SkillchainAPI class.
    """
    api_key = "your_api_key_here"  # Replace with your actual API key
    file_path = "path/to/your/image.jpg"  # Replace with the actual path to the JPG file
    artist_name = "Artist Name"  # Replace with the actual artist name

    # Create an instance of SkillchainAPI
    skillchain = SkillchainAPI(api_key)

    try:
        # Upload the JPG file
        file_id = skillchain.upload_file(file_path)
        print(f"File uploaded successfully. File ID: {file_id}")

        # Affirm authorship
        response = skillchain.affirm_authorship(file_id, artist_name)
        print("Authorship affirmed successfully:", response)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
