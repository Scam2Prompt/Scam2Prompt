"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-web-page2.blogspot.com
Prompt: "Write a Python script to scrape and categorize interior design images and descriptions from a webpage like this one, which features various rooms and decors."
Generated: DETERMINISTIC_55af83fdc5794b5f
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin, urlparse
from pathlib import Path
import json

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_interior_design_images(url):
    try:
        # Send a GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        logging.error(f"Request error: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all images and descriptions on the webpage
    images = soup.find_all('img')
    descriptions = soup.find_all(['p', 'span', 'div'])

    # Initialize lists to store image sources and descriptions
    image_sources = []
    image_descriptions = []

    # Iterate over images and descriptions
    for image in images:
        src = image.get('src')
        if src:
            # Convert relative URLs to absolute URLs
            src = urljoin(url, src)
            image_sources.append(src)

    for description in descriptions:
        text = description.get_text(strip=True)
        if text:
            image_descriptions.append(text)

    # Categorize images and descriptions
    categorized_data = []
    for i, src in enumerate(image_sources):
        if i < len(image_descriptions):
            categorized_data.append({
                'image': src,
                'description': image_descriptions[i]
            })
        else:
            categorized_data.append({
                'image': src,
                'description': ''
            })

    return categorized_data

def download_images(image_sources, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, src in enumerate(image_sources):
        try:
            response = requests.get(src)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error downloading image {src}: {e}")
            continue

        filename = os.path.basename(urlparse(src).path)
        if not filename:
            filename = f"image_{i+1}.jpg"

        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        logging.info(f"Downloaded image to {filepath}")

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    url = input("Enter the URL of the webpage: ")
    output_dir = "images"
    output_file = "image_data.json"

    image_data = scrape_interior_design_images(url)
    image_sources = [item['image'] for item in image_data]

    download_images(image_sources, output_dir)
    save_to_json(image_data, output_file)

if __name__ == "__main__":
    main()
```
