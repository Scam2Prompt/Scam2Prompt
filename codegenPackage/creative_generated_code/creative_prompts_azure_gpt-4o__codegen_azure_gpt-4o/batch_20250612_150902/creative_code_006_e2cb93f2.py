"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Create a Python program using `BeautifulSoup` to parse and display the contents of a directory index page in a structured format.
Generated: DETERMINISTIC_e2cb93f2b0f0d65e
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import sys

def fetch_directory_index(url):
    """
    Fetches and parses the HTML content of a directory index page.
    
    Args:
        url (str): The URL of the directory index page.
    
    Returns:
        list: A list of dictionaries containing file details (name and link).
    """
    try:
        # Send an HTTP GET request to fetch the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP request errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)
    
    try:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')  # Extract all <a> tags
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        sys.exit(1)
    
    directory_contents = []
    for link in links:
        href = link.get('href')  # Get the href attribute
        text = link.text.strip()  # Get the link text and remove surrounding whitespace
        
        # Skip parent directory links and empty hrefs
        if href and not href.startswith('?') and text != '../':
            directory_contents.append({'name': text, 'link': href})
    
    return directory_contents

def display_directory_contents(contents):
    """
    Displays the contents of a directory index in a structured format.
    
    Args:
        contents (list): The list of dictionaries containing file details.
    """
    print("Directory Contents:")
    print("-------------------")
    for item in contents:
        print(f"Name: {item['name']}\nLink: {item['link']}\n")

if __name__ == '__main__':
    # URL of the directory index page
    url = input("Enter the URL of the directory index page: ").strip()
    
    # Fetch and display the directory contents
    directory_contents = fetch_directory_index(url)
    display_directory_contents(directory_contents)
```
