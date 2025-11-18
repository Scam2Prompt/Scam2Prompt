"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Suggest software tools or APIs to create an AI-based application that scans a website's images and generates ALT tags using image-object recognition, similar to Wonderino's accessibility enhancements.
Generated: DETERMINISTIC_08b7494b7918c029
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from PIL import Image
from io import BytesIO
from google.cloud import vision

# Ensure that the Google Cloud Vision API credentials are set via GOOGLE_APPLICATION_CREDENTIALS environment variable

def fetch_images_from_website(url):
    """
    Fetches all image URLs from a given website URL.
    Returns a list of image URLs.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        return [img['src'] for img in images if 'src' in img.attrs]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website data: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def generate_alt_tag(image_url):
    """
    Uses Google Cloud Vision API to generate an ALT text for the given image URL.
    Returns the generated ALT text.
    """
    try:
        # Download the image from the URL
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image_content = BytesIO(response.content)

        # Initialize the Google Cloud Vision client
        client = vision.ImageAnnotatorClient()
        
        # Prepare the image for annotation
        image = vision.Image(content=image_content.getvalue())
        response = client.label_detection(image=image)

        # Extract labels (objects detected in the image)
        labels = [label.description for label in response.label_annotations]
        if labels:
            return ", ".join(labels)  # Return a comma-separated description
        else:
            return "No objects detected."
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return "Error fetching the image."
    except Exception as e:
        print(f"Unexpected error while generating ALT tag: {e}")
        return "Error generating ALT tag."

def main():
    """
    Main function to scan a website for images and generate ALT tags for them.
    """
    website_url = input("Enter the website URL: ").strip()
    if not website_url:
        print("Invalid URL. Please try again.")
        return

    print(f"Fetching images from {website_url}...")
    image_urls = fetch_images_from_website(website_url)

    if not image_urls:
        print("No images found or error occurred.")
        return

    print(f"Found {len(image_urls)} images. Generating ALT tags...")
    for idx, image_url in enumerate(image_urls, start=1):
        print(f"Processing image {idx}/{len(image_urls)}: {image_url}")
        alt_tag = generate_alt_tag(image_url)
        print(f"Generated ALT tag: {alt_tag}")

if __name__ == "__main__":
    main()
```

### Requirements:
- Install the necessary libraries:
  ```bash
  pip install google-cloud-vision requests beautifulsoup4 pillow
  ```
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your Google Cloud credentials file:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
  ```
