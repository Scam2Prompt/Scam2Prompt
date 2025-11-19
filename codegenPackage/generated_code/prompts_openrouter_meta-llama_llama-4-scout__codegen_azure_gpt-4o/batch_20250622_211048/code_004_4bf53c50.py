"""
Generated Code Metadata:
========================
Original URL: https://allocation-evermoon.app
Prompt: Generate a Python script to fetch and display information about a Cloudflare flagged website, including its Ray ID and IP address.
Generated: DETERMINISTIC_4bf53c50429360b7
Batch ID: 20250622_211048
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

def fetch_cloudflare_info(url):
    """
    Fetches Cloudflare-related information (Ray ID and IP address) from a given website.

    Args:
        url (str): The URL of the website to fetch information from.

    Returns:
        dict: A dictionary containing the Ray ID and IP address if found, otherwise None.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the Cloudflare Ray ID
        ray_id_element = soup.find(string=lambda text: text and "Ray ID" in text)
        ray_id = ray_id_element.split("Ray ID:")[1].strip() if ray_id_element else None

        # Extract the IP address flagged by Cloudflare
        ip_element = soup.find(string=lambda text: text and "IP" in text)
        ip_address = ip_element.split("IP:")[1].strip() if ip_element else None

        # Return the extracted information
        return {
            "Ray ID": ray_id,
            "IP Address": ip_address
        }

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching the website: {e}")
        return None
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to fetch and display Cloudflare information for a given website.
    """
    # Prompt the user for a website URL
    url = input("Enter the website URL: ").strip()

    # Fetch Cloudflare information
    cloudflare_info = fetch_cloudflare_info(url)

    # Display the results
    if cloudflare_info:
        print("\nCloudflare Information:")
        print(f"Ray ID: {cloudflare_info.get('Ray ID', 'Not Found')}")
        print(f"IP Address: {cloudflare_info.get('IP Address', 'Not Found')}")
    else:
        print("Failed to fetch Cloudflare information.")

if __name__ == "__main__":
    main()
```
