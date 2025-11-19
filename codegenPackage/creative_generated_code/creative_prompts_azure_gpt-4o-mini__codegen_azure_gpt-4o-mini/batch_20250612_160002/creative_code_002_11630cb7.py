"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakes.pages.dev
Prompt: Write a code snippet that automates the retrieval of files for "Materi bahasa inggris kelas 7 bab 1 kurikulum 2013" from the Pancakes webpage.
Generated: DETERMINISTIC_11630cb7be631eab
Batch ID: 20250612_160002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/pancakes": {
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
from bs4 import BeautifulSoup
import os

def download_file(url, folder_path):
    """
    Downloads a file from a given URL and saves it in a specified folder.
    
    :param url: The URL of the file to download
    :param folder_path: The local folder path where the file will be saved
    :raises Exception: Raises an exception if the download fails
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        file_name = os.path.join(folder_path, url.split("/")[-1])  # Extract the file name from the URL
        
        # Write the content to a file
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

def fetch_material_links(base_url):
    """
    Fetches links to the material files from the Pancakes webpage.
    
    :param base_url: The base URL of the Pancakes webpage
    :return: List of file URLs related to the specified topic
    """
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links that contain the topic specified
        links = soup.find_all('a', href=True)
        material_links = [link['href'] for link in links if "Materi bahasa inggris kelas 7 bab 1 kurikulum 2013" in link.text]
        
        return material_links
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching material links: {e}")
        return []

def main():
    """
    Main function to execute the file retrieval automation.
    """
    base_url = "https://example.com/pancakes"  # Replace with the actual URL of the Pancakes webpage
    folder_path = "downloads"  # Folder to save downloaded files
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    material_links = fetch_material_links(base_url)
    
    if material_links:
        for link in material_links:
            download_file(link, folder_path)
    else:
        print("No material links found.")

if __name__ == "__main__":
    main()
```
