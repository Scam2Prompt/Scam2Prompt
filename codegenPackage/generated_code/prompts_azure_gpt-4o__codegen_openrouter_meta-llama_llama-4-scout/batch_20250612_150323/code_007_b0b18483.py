"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Develop a Python program that uses the urllib library to check the availability of files listed in an "Index of /" directory and logs any broken links.
Generated: DETERMINISTIC_b0b18483f5494d24
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import urllib.request
import urllib.parse
import logging

# Set up logging configuration
logging.basicConfig(filename='broken_links.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_link_availability(url):
    """
    Checks if a file is available at the given URL.

    Args:
        url (str): The URL of the file to check.

    Returns:
        bool: True if the file is available, False otherwise.
    """
    try:
        # Send a HEAD request to the URL to check if the file exists
        request = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(request)
        # If the response status code is between 200 and 400, the file is available
        return 200 <= response.status < 400
    except urllib.error.HTTPError as e:
        # Log the broken link and return False
        logging.error(f"Broken link: {url} - {e.code} {e.reason}")
        return False
    except Exception as e:
        # Log any other exceptions and return False
        logging.error(f"Error checking link: {url} - {str(e)}")
        return False

def get_index_of_directory(url):
    """
    Retrieves the contents of an "Index of /" directory.

    Args:
        url (str): The URL of the "Index of /" directory.

    Returns:
        list: A list of URLs of files in the directory.
    """
    try:
        # Send a GET request to the URL to retrieve the directory contents
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        # Read the HTML response
        html = response.read().decode('utf-8')
        # Find all links in the HTML
        links = []
        for line in html.splitlines():
            if 'href' in line:
                href = line.split('href="')[1].split('"')[0]
                # If the link is not a directory, add it to the list
                if not href.endswith('/'):
                    links.append(urllib.parse.urljoin(url, href))
        return links
    except Exception as e:
        # Log any exceptions and return an empty list
        logging.error(f"Error retrieving directory contents: {url} - {str(e)}")
        return []

def main():
    url = input("Enter the URL of the 'Index of /' directory: ")
    if not url.endswith('/'):
        url += '/'
    links = get_index_of_directory(url)
    for link in links:
        if not check_link_availability(link):
            print(f"Broken link: {link}")

if __name__ == "__main__":
    main()
```
