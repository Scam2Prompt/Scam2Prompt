"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Create a script to download and organize images from the "Gallery" section of the "Tree House Sessions" website using Python.
Generated: DETERMINISTIC_50ba0885220b6a5b
Batch ID: 20250612_152340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://treehousesessions.com": {
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
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

# Constants for the website's URL and the download directory
BASE_URL = "https://treehousesessions.com"
GALLERY_URL = urljoin(BASE_URL, "/gallery/")
DOWNLOAD_DIR = "downloaded_images"

def create_download_directory(directory):
    """Create a directory for storing downloaded images."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_image_urls(gallery_url):
    """Fetch image URLs from the gallery section of the website."""
    try:
        response = requests.get(gallery_url)
        response.raise_for_status()  # Raise an error for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')

        # Extract image URLs
        image_urls = [urljoin(BASE_URL, img['src']) for img in image_tags if 'src' in img.attrs]
        return image_urls
    except requests.RequestException as e:
        print(f"Error fetching images: {e}")
        return []

def download_image(url, directory):
    """Download an image from a given URL into the specified directory."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Extract image filename from URL
        filename = os.path.join(directory, os.path.basename(url))
        
        # Download the image and save it to the specified directory
        with open(filename, 'wb') as file:
            for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f'Downloading {filename}', unit='KB'):
                file.write(chunk)
    except requests.RequestException as e:
        print(f"Error downloading image {url}: {e}")

def download_gallery_images():
    """Main function to orchestrate downloading images from the gallery."""
    create_download_directory(DOWNLOAD_DIR)
    
    # Get image URLs from the gallery
    image_urls = get_image_urls(GALLERY_URL)
    
    if not image_urls:
        print("No images found to download.")
        return

    # Download each image
    for image_url in image_urls:
        download_image(image_url, DOWNLOAD_DIR)

if __name__ == "__main__":
    download_gallery_images()
```
