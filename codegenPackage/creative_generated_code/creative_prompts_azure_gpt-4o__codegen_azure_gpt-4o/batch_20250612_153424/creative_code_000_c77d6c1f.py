"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetcomputer.cc
Prompt: Unable to generate relevant prompts due to lack of content on the provided webpage.
Generated: DETERMINISTIC_c77d6c1fa0cf3fc6
Batch ID: 20250612_153424
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

def fetch_webpage_content(url):
    """
    Fetches the HTML content of a webpage.
    
    Parameters:
        url (str): The URL of the webpage to fetch.
    
    Returns:
        str: The HTML content of the webpage if successful, else None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        # Log the error and return None
        print(f"Error fetching content from {url}: {e}")
        return None

def extract_prompts_from_webpage(html_content):
    """
    Extracts relevant prompts (or meaningful text) from the HTML content of a webpage.
    
    Parameters:
        html_content (str): The HTML content of the webpage.
    
    Returns:
        list: A list of extracted prompts or meaningful text.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Example: extract text from <p> tags as potential prompts
        paragraphs = soup.find_all('p')
        prompts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
        return prompts if prompts else ["No relevant content found on the webpage."]
    except Exception as e:
        # Log the error and return a default message
        print(f"Error parsing HTML content: {e}")
        return ["Failed to extract prompts due to an error."]

def main():
    """
    Main function to fetch webpage content and extract relevant prompts.
    """
    url = input("Enter the URL of the webpage: ").strip()
    html_content = fetch_webpage_content(url)
    
    if html_content:
        prompts = extract_prompts_from_webpage(html_content)
        print("\nExtracted Prompts:")
        for idx, prompt in enumerate(prompts, start=1):
            print(f"{idx}. {prompt}")

if __name__ == "__main__":
    main()
```
