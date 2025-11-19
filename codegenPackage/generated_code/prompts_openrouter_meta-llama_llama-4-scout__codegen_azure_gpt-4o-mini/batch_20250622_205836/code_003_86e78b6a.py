"""
Generated Code Metadata:
========================
Original URL: https://connect-amlprotect.elacas.edu.pk
Prompt: Write a script to list the directory index of a website using a programming language, similar to the output shown on connect-amlprotect.elacas.edu.pk.
Generated: DETERMINISTIC_86e78b6aa624ee8b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import os

def fetch_directory_index(url):
    """
    Fetches the directory index of a given URL.

    Args:
        url (str): The URL of the website to fetch the directory index from.

    Returns:
        list: A list of directory items (files and folders) found in the index.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links in the directory index
        links = soup.find_all('a')

        # Extract the href attributes and return as a list
        directory_items = [link.get('href') for link in links if link.get('href')]
        return directory_items

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the directory index: {e}")
        return []

def display_directory_index(directory_items):
    """
    Displays the directory items in a formatted manner.

    Args:
        directory_items (list): A list of directory items to display.
    """
    if not directory_items:
        print("No items found in the directory index.")
        return

    print("Directory Index:")
    for item in directory_items:
        print(f"- {item}")

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL of the website to list the directory index: ")
    
    # Fetch the directory index
    directory_items = fetch_directory_index(url)
    
    # Display the fetched directory index
    display_directory_index(directory_items)

if __name__ == "__main__":
    main()
```

### Requirements:
- Install the required libraries using pip:
```bash
pip install requests beautifulsoup4
```
