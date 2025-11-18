"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markandecastro.com
Prompt: Unable to generate prompts due to lack of relevant content on the webpage.
Generated: DETERMINISTIC_3a77594ab17f855e
Batch ID: 20250612_150947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
        str: Extracted content from the webpage. Returns an error message if the scraping fails.
    """
    try:
        # Send a GET request to the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant text content from the webpage
        # Select text from <p> tags, assuming prompts are located in paragraph tags
        content = soup.find_all('p')
        if content:
            return ' '.join([p.get_text(strip=True) for p in content])
        else:
            return "No relevant content found on the webpage."
    
    except requests.exceptions.RequestException as e:
        # Handle network exceptions
        return f"An error occurred while accessing the webpage: {e}"
    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = "https://example.com"  # Replace with the actual URL
    content = scrape_webpage_content(url)
    print(content)
```
