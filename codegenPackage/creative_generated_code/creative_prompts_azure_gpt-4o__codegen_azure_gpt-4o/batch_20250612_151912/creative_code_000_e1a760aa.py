"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://20000.paperplane.io
Prompt: Unable to generate prompts due to lack of relevant technical content on the webpage.
Generated: DETERMINISTIC_e1a760aa14bf5a85
Batch ID: 20250612_151912
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

def extract_technical_content(url):
    """
    Extracts technical content from the webpage at the given URL.
    
    Parameters:
        url (str): The URL of the webpage to scrape.
    
    Returns:
        str: Extracted technical content or a message indicating lack of relevant content.
    """
    try:
        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find technical content by extracting <code>, <pre>, and <p> elements
        technical_content = []
        for tag in soup.find_all(['code', 'pre', 'p']):
            text = tag.get_text(strip=True)
            if text:
                technical_content.append(text)
        
        # Check if we found any technical content
        if technical_content:
            return '\n'.join(technical_content)
        else:
            return "Unable to generate prompts due to lack of relevant technical content on the webpage."
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return f"Error while fetching webpage: {str(e)}"
    except Exception as e:
        # Handle other unforeseen errors
        return f"An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    url = input("Enter the webpage URL: ").strip()
    result = extract_technical_content(url)
    print(result)
```
