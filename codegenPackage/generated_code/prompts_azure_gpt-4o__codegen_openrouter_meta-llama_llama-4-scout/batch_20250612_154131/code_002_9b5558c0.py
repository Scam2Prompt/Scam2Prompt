"""
Generated Code Metadata:
========================
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Provide a Python script using `requests` and `BeautifulSoup` to scrape the directory structure from a LiteSpeed Web Server index page.
Generated: DETERMINISTIC_9b5558c04c6070ac
Batch ID: 20250612_154131
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_directory_structure(url):
    """
    Scrapes the directory structure from a LiteSpeed Web Server index page.

    Args:
        url (str): The URL of the index page to scrape.

    Returns:
        list: A list of directory and file entries.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            logging.error(f"Failed to retrieve page. Status code: {response.status_code}")
            return []

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all list items (which represent directory and file entries)
        list_items = soup.find_all('li')

        # Initialize an empty list to store the directory and file entries
        entries = []

        # Iterate over each list item
        for item in list_items:
            # Find the anchor tag within the list item
            anchor = item.find('a')

            # If an anchor tag is found, extract the text and URL
            if anchor:
                text = anchor.text.strip()
                href = anchor.get('href')

                # Add the entry to the list
                entries.append({
                    'text': text,
                    'href': href
                })

        return entries

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return []

def main():
    url = input("Enter the URL of the index page to scrape: ")
    entries = scrape_directory_structure(url)

    if entries:
        print("Directory Structure:")
        for entry in entries:
            print(f"- {entry['text']} ({entry['href']})")
    else:
        print("No entries found.")

if __name__ == "__main__":
    main()
```
