"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truflation-governance.com
Prompt: Generate a script to verify successful website migration to Hostinger, ensuring all files are correctly uploaded and accessible.
Generated: DETERMINISTIC_7411aceede1b57a7
Batch ID: 20250612_145427
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.hostinger.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.hostinger.com": {
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

class WebsiteMigrationVerifier:
    def __init__(self, hostinger_url, local_directory):
        """
        Initialize the verifier with the Hostinger URL and the local directory to check.

        :param hostinger_url: The URL of the migrated website on Hostinger.
        :param local_directory: The local directory containing the original website files.
        """
        self.hostinger_url = hostinger_url
        self.local_directory = local_directory

    def verify_files(self):
        """
        Verify that all files in the local directory are accessible on the Hostinger website.
        """
        # List all files in the local directory
        for root, _, files in os.walk(self.local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, self.local_directory)
                hostinger_file_url = f"{self.hostinger_url}/{relative_path.replace(os.sep, '/')}"
                self.check_file(hostinger_file_url)

    def check_file(self, file_url):
        """
        Check if a file is accessible at the given URL.

        :param file_url: The URL of the file to check.
        """
        try:
            response = requests.get(file_url)
            if response.status_code == 200:
                print(f"SUCCESS: {file_url} is accessible.")
            else:
                print(f"ERROR: {file_url} returned status code {response.status_code}.")
        except requests.ConnectionError:
            print(f"ERROR: Failed to connect to {file_url}.")
        except requests.RequestException as e:
            print(f"ERROR: An error occurred while checking {file_url}: {e}")

if __name__ == "__main__":
    # Configuration: Modify these variables for your specific case
    HOSTINGER_URL = "https://yourwebsite.hostinger.com"
    LOCAL_DIRECTORY = "/path/to/your/local/website/files"

    # Create an instance of the verifier and run the verification
    verifier = WebsiteMigrationVerifier(HOSTINGER_URL, LOCAL_DIRECTORY)
    verifier.verify_files()
```

### Note:
- Make sure to replace `https://yourwebsite.hostinger.com` and `/path/to/your/local/website/files` with the actual URL of your migrated website and the local directory containing your website files before running the script.
