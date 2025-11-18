"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodezdapp.net
Prompt: Unable to generate prompts due to lack of relevant content on the webpage.
Generated: DETERMINISTIC_3a77594ab17f855e
Batch ID: 20250612_154829
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
        return f"Error fetching webpage: {str(e)}"
    except Exception as e:
        return f"An error occurred while processing the webpage: {str(e)}"

if __name__ == '__main__':
    # Example usage
    url = input("Enter the URL of the webpage: ").strip()
    scraped_content = scrape_webpage_content(url)
    print("Extracted Content:")
    print(scraped_content)
```
