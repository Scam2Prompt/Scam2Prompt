"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Write a Python script that uses regular expressions to extract descriptions of files from an "Index of /" directory listing webpage and save them in a JSON file.
Generated: DETERMINISTIC_ae2ef8826096f303
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/directory/": {
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
import re
import json
import os

def fetch_directory_listing(url):
    """
    Fetch the raw HTML content of a directory listing webpage.

    Args:
        url (str): The URL of the directory listing.

    Returns:
        str: Raw HTML content of the webpage if the request is successful.
        None: If the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return None

def extract_file_descriptions(html_content):
    """
    Extract file descriptions from the HTML content using regular expressions.

    Args:
        html_content (str): The raw HTML content of the directory listing.

    Returns:
        list: A list of dictionaries containing file descriptions.
    """
    # Regular expression pattern to match file descriptions in the directory listing
    pattern = r'<a href="([^"]+)">([^<]+)</a>'

    # Find all matches and construct a list of dictionaries
    file_descriptions = []
    for match in re.findall(pattern, html_content):
        file_name = match[1]  # The text of the link (file name)
        file_url = match[0]   # The link (file URL)
        file_descriptions.append({'name': file_name, 'url': file_url})

    return file_descriptions

def save_to_json(data, filename):
    """
    Save the extracted data to a JSON file.

    Args:
        data (list): The data to save.
        filename (str): The name of the JSON file to save data to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Save with pretty formatting
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main():
    # URL of the directory listing
    url = "http://example.com/directory/"  # Change to your target URL
    output_file = "file_descriptions.json"  # Output JSON file name

    # Fetch the directory listing
    html_content = fetch_directory_listing(url)
    if html_content:
        # Extract file descriptions
        file_descriptions = extract_file_descriptions(html_content)
        # Save descriptions to JSON file
        save_to_json(file_descriptions, output_file)

if __name__ == "__main__":
    main()
```
