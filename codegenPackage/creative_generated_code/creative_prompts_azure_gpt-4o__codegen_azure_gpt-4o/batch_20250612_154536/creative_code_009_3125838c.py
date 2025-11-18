"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstclass222.w3spaces.com
Prompt: Generate a tutorial for beginners on how to use W3 Spaces to build and publish a static website.
Generated: DETERMINISTIC_3125838c0e0e6ea8
Batch ID: 20250612_154536
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://nyc3.digitaloceanspaces.com": {
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
# Tutorial: Build and Publish a Static Website on W3 Spaces
# This script automates the process of creating and uploading a static website to W3 Spaces.

import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configuration Variables (Update these with your specific values)
SPACE_NAME = "your-space-name"  # Replace with your W3 Spaces name
ACCESS_KEY = "your-access-key"  # Replace with your W3 Spaces access key
SECRET_KEY = "your-secret-key"  # Replace with your W3 Spaces secret key
ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"  # Replace with the endpoint URL for your region
LOCAL_DIRECTORY = "./website"  # Replace with the path to your static website files (HTML, CSS, JS, etc.)

def upload_files_to_space(local_directory, space_name, client):
    """
    Recursively upload files from a local directory to a W3 Spaces bucket.
    
    :param local_directory: Path to the local directory containing static website files
    :param space_name: Name of the W3 Spaces bucket
    :param client: Initialized boto3 client for Spaces
    """
    try:
        # Traverse the local directory
        for root, dirs, files in os.walk(local_directory):
            for file in files:
                # Construct full local file path
                local_file_path = os.path.join(root, file)
                
                # Construct the key (path) for the file in the Spaces bucket
                relative_path = os.path.relpath(local_file_path, local_directory)
                bucket_key = relative_path.replace("\\", "/")  # Ensure correct path format
                
                # Upload the file
                print(f"Uploading {local_file_path} to {space_name}/{bucket_key}...")
                client.upload_file(local_file_path, space_name, bucket_key)
                print(f"Uploaded {file} successfully.")
    except FileNotFoundError as fnf_error:
        print(f"Error: File not found - {fnf_error}")
    except NoCredentialsError:
        print("Error: No credentials provided. Check your access key and secret key.")
    except PartialCredentialsError:
        print("Error: Incomplete credentials provided. Check your access key and secret key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        # Ensure the local directory exists
        if not os.path.exists(LOCAL_DIRECTORY):
            raise FileNotFoundError(f"The directory '{LOCAL_DIRECTORY}' does not exist. Please create your website files first.")

        # Initialize the boto3 client for W3 Spaces
        spaces_client = boto3.client('s3',
                                     aws_access_key_id=ACCESS_KEY,
                                     aws_secret_access_key=SECRET_KEY,
                                     endpoint_url=ENDPOINT_URL)
        
        # Upload local files to the W3 Space
        print(f"Uploading static website files from '{LOCAL_DIRECTORY}' to W3 Space '{SPACE_NAME}'...")
        upload_files_to_space(LOCAL_DIRECTORY, SPACE_NAME, spaces_client)
        print("Website deployment completed successfully!")
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Notes:
- Replace placeholders (`your-space-name`, `your-access-key`, etc.) with actual credentials and details from your W3 Spaces account.
- Ensure `boto3` is installed (`pip install boto3`) before running the script.
- Place your static website files (HTML, CSS, JavaScript, etc.) in the directory specified by `LOCAL_DIRECTORY`.
- You may need to configure the bucket (Space) for public access depending on your use case.
