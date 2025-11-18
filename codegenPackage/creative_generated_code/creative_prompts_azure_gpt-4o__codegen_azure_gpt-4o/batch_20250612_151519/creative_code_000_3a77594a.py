"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfree.info
Prompt: Unable to generate prompts due to lack of relevant content on the webpage.
Generated: DETERMINISTIC_3a77594ab17f855e
Batch ID: 20250612_151519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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

def scrape_webpage_content(url):
    """
    Scrapes content from the given webpage URL.
    
    Args:
        url (str): The URL of the webpage to scrape content from.

    Returns:
        str: The raw text content of the webpage.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.exceptions.RequestException: For network-related errors.
        Exception: For other unexpected errors.
    """
    # Validate the input URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided. Please provide a non-empty string URL.")

    try:
        # Send a GET request to the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the text content from the webpage
        webpage_text = soup.get_text(strip=True)

        if not webpage_text:
            # If the webpage has no relevant content, raise an error
            raise ValueError("Unable to generate prompts due to lack of relevant content on the webpage.")
        
        return webpage_text

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise requests.exceptions.RequestException(f"Network error occurred: {e}")
    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"An error occurred while processing the webpage: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'http://example.com' with the actual URL you want to scrape
        content = scrape_webpage_content("http://example.com")
        print("Webpage content successfully retrieved:")
        print(content)
    except Exception as error:
        print(f"Error: {error}")
```
