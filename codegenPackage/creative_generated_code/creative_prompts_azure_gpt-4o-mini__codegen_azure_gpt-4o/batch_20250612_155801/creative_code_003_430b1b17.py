"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Create a script that downloads images from the 360Fuel network's img directory using its API.
Generated: DETERMINISTIC_430b1b177937ae12
Batch ID: 20250612_155801
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.360fuel.net/img/": {
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
import os
from pathlib import Path

# Constants
API_BASE_URL = "https://api.360fuel.net/img/"
DOWNLOAD_DIRECTORY = "downloaded_images"
TIMEOUT = 10  # Timeout for API requests in seconds

def fetch_image_list():
    """
    Fetches the list of images available on the 360Fuel API.

    Returns:
        list: A list of image file names.
    """
    try:
        response = requests.get(API_BASE_URL, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP error responses
        return response.json()  # Assumes the API returns a JSON list of image filenames
    except requests.RequestException as e:
        print(f"Error fetching image list: {e}")
        return []

def download_image(image_name):
    """
    Downloads a single image from the 360Fuel API.

    Args:
        image_name (str): The name of the image file to download.
    """
    image_url = f"{API_BASE_URL}{image_name}"
    try:
        response = requests.get(image_url, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP error responses

        # Ensure the download directory exists
        Path(DOWNLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)
        
        # Save the image to the download directory
        file_path = os.path.join(DOWNLOAD_DIRECTORY, image_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {image_name}")
    except requests.RequestException as e:
        print(f"Error downloading image {image_name}: {e}")

def main():
    """
    Main function to orchestrate downloading images from the 360Fuel API.
    """
    print("Fetching image list...")
    image_list = fetch_image_list()
    
    if not image_list:
        print("No images found or error fetching image list.")
        return

    print(f"Found {len(image_list)} images. Starting download...")
    for image_name in image_list:
        download_image(image_name)
    print("Download complete.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
