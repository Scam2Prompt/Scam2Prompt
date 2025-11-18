"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridges-sonicslab.com
Prompt: Unable to generate prompts due to lack of accessible content on the webpage.
Generated: DETERMINISTIC_7641f23ffe9285c7
Batch ID: 20250612_154147
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

def extract_content_from_webpage(url):
    """
    Extracts text content from a given webpage URL.
    
    Args:
        url (str): URL of the webpage to scrape.
        
    Returns:
        str: The extracted text content from the webpage.
        
    Raises:
        ValueError: If the URL is invalid or content cannot be retrieved.
        Exception: For other unforeseen errors during request or parsing.
    """
    try:
        # Validate the URL
        if not url.startswith("http"):
            raise ValueError("Invalid URL. Ensure the URL starts with 'http' or 'https'")
        
        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

        # Parse the webpage content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text content
        text_content = soup.get_text(strip=True)
        
        # Ensure the content is not empty
        if not text_content:
            raise ValueError("No accessible content found on the webpage.")
        
        return text_content

    except requests.exceptions.Timeout:
        raise Exception("The request timed out. Please check the URL or your network connection.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        url = input("Enter the URL of the webpage: ").strip()
        content = extract_content_from_webpage(url)
        print("Extracted Content:")
        print(content)
    except Exception as e:
        print(f"Error: {e}")
```
