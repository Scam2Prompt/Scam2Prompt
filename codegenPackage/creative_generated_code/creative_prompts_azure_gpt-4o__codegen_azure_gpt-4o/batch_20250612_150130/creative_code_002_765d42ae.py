"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinanciales.com
Prompt: Create a Python script to detect and extract server information (e.g., Apache version, Debian details, port number) from an Apache directory listing webpage.
Generated: DETERMINISTIC_765d42ae3734dad4
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import re
from bs4 import BeautifulSoup

def extract_server_info(url):
    """
    Extract server information from an Apache directory listing webpage.

    Args:
        url (str): The URL of the Apache directory listing page.

    Returns:
        dict: A dictionary containing extracted server information.
    """
    try:
        # Send HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract server information from the 'Server' header (if available)
        server_header = response.headers.get('Server', 'Unknown')
        
        # Extract Apache version from webpage content (if present)
        apache_version = None
        apache_version_match = re.search(r'Apache/([\d.]+)', response.text)
        if apache_version_match:
            apache_version = apache_version_match.group(1)
        
        # Extract Debian details from webpage content (if present)
        debian_version = None
        debian_match = re.search(r'Debian(?: GNU/Linux)? (\d+)', response.text)
        if debian_match:
            debian_version = debian_match.group(1)

        # Extract port number from the URL (if present)
        port_number = None
        port_match = re.search(r':(\d+)', url)
        if port_match:
            port_number = port_match.group(1)

        # Return extracted server information as a dictionary
        server_info = {
            'Server Header': server_header,
            'Apache Version': apache_version,
            'Debian Version': debian_version,
            'Port Number': port_number
        }
        return server_info

    except requests.exceptions.RequestException as e:
        # Handle network errors
        print(f"Error fetching the URL: {e}")
        return {}

    except Exception as e:
        # Handle other exceptions gracefully
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    # Example usage
    url = input("Enter the URL of the Apache directory listing: ").strip()
    server_info = extract_server_info(url)
    print("Extracted Server Information:")
    for key, value in server_info.items():
        print(f"{key}: {value or 'Not Found'}")
```
