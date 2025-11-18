"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Develop a Python script to parse and categorize extensions from Crx搜搜 based on tags like "工具," "教育," and "开发者工具."
Generated: DETERMINISTIC_d38cee1c3963c05d
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.crxso.com/": {
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
import json
from collections import defaultdict

# Define the URL for Crx搜搜 extensions
BASE_URL = "https://www.crxso.com/"
TAG_CATEGORIES = ["工具", "教育", "开发者工具"]

def fetch_extension_data(tag):
    """
    Fetches extension data from Crx搜搜 based on the given tag.

    :param tag: The tag to filter extensions (e.g., "工具", "教育", "开发者工具").
    :return: A list of dictionaries containing extension details.
    """
    try:
        response = requests.get(f"{BASE_URL}/search/{tag}", timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return parse_extensions(response.text)
    except requests.RequestException as e:
        print(f"Error fetching data for tag '{tag}': {e}")
        return []

def parse_extensions(html_content):
    """
    Parses the HTML content and extracts extension details.

    :param html_content: The raw HTML content of the page.
    :return: A list of dictionaries with extension name and URL.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    extensions = []

    # Locate the relevant section in the HTML structure
    extension_elements = soup.find_all('div', class_='extension-item')
    
    for element in extension_elements:
        try:
            name = element.find('h3').text.strip()
            url = element.find('a')['href']
            extensions.append({'name': name, 'url': url})
        except (AttributeError, KeyError) as e:
            print(f"Error parsing extension details: {e}")

    return extensions

def categorize_extensions(extensions):
    """
    Categorizes extensions based on predefined tags.

    :param extensions: A list of extension dictionaries.
    :return: A dictionary categorized by tags.
    """
    categorized = defaultdict(list)

    for ext in extensions:
        for tag in TAG_CATEGORIES:
            if tag in ext['name']:
                categorized[tag].append(ext)
                break  # Stop checking after the first match

    return categorized

def main():
    """
    Main function to orchestrate fetching and categorizing extensions.
    """
    all_extensions = []
    
    for tag in TAG_CATEGORIES:
        extensions = fetch_extension_data(tag)
        all_extensions.extend(extensions)

    if all_extensions:
        categorized_extensions = categorize_extensions(all_extensions)

        # Save categorized data to a JSON file
        with open('categorized_extensions.json', 'w', encoding='utf-8') as f:
            json.dump(categorized_extensions, f, ensure_ascii=False, indent=4)
        print("Extensions categorized and saved to 'categorized_extensions.json'.")
    else:
        print("No extensions found.")

if __name__ == '__main__':
    main()
```
