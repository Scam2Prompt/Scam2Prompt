"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnfymrm14.ukit.me
Prompt: Unable to generate prompts due to lack of relevant technical content on the webpage.
Generated: DETERMINISTIC_e1a760aa14bf5a85
Batch ID: 20250612_145309
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

def extract_relevant_content(url):
    """
    Extracts and returns relevant technical content from a webpage.
    
    Parameters:
        url (str): The URL of the webpage to scrape.
    
    Returns:
        str: Extracted text content if found, else an error message.
    """
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to extract relevant technical content (e.g., <code>, <pre>, or <article> tags)
        technical_content = []
        for tag_name in ['code', 'pre', 'article']:
            elements = soup.find_all(tag_name)
            for element in elements:
                technical_content.append(element.get_text(strip=True))
        
        # If no technical content is found, return an error message
        if not technical_content:
            return "No relevant technical content found on the webpage."
        
        # Join and return the content as a unified string
        return "\n".join(technical_content)
    
    except requests.exceptions.RequestException as e:
        # Handle network-related or HTTP issues
        return f"Error fetching webpage: {e}"
    except Exception as e:
        # Handle any other unforeseen errors
        return f"An unexpected error occurred: {e}"

# Example Usage
if __name__ == "__main__":
    # Replace with the URL of the webpage you want to extract content from
    test_url = "https://example.com"
    
    # Get the relevant content
    result = extract_relevant_content(test_url)
    
    # Print the result
    print(result)
```
