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
import re
import requests
import json

def fetch_directory_listing(url):
    """
    Fetch the content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.

    Raises:
        requests.RequestException: If an error occurs during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        raise

def extract_file_descriptions(html):
    """
    Extract file descriptions from an "Index of /" directory listing.

    Args:
        html (str): The HTML content of the directory listing page.

    Returns:
        list of dict: A list of file information dictionaries with 'name' and 'description'.
    """
    # Regular expression to match file entries in the directory listing
    file_pattern = re.compile(
        r"<a href=\"(?P<name>[^\"]+)\">.*?</a>\s+(?P<description>[^<]+)",
        re.IGNORECASE
    )

    # Find all matches and return as a list of dictionaries
    matches = file_pattern.findall(html)
    return [{"name": match[0], "description": match[1].strip()} for match in matches]

def save_to_json(data, filename):
    """
    Save data to a JSON file.

    Args:
        data (list): The data to save.
        filename (str): The name of the JSON file to save to.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving to JSON file: {e}")
        raise

if __name__ == "__main__":
    # URL of the "Index of /" directory listing
    url = "http://example.com/directory/"  # Replace this with the actual URL

    try:
        # Fetch the directory listing
        html_content = fetch_directory_listing(url)

        # Extract file descriptions
        file_descriptions = extract_file_descriptions(html_content)

        # Save the extracted data to a JSON file
        save_to_json(file_descriptions, "file_descriptions.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
