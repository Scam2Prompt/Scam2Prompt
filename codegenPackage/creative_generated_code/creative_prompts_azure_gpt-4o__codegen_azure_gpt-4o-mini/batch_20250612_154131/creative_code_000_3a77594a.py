"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yuweroblox.com
Prompt: Unable to generate prompts due to lack of relevant content on the webpage.
Generated: DETERMINISTIC_3a77594ab17f855e
Batch ID: 20250612_154131
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

class WebContentExtractor:
    """
    A class to extract relevant content from a webpage.
    """

    def __init__(self, url):
        """
        Initializes the WebContentExtractor with a given URL.

        Args:
            url (str): The URL of the webpage to extract content from.
        """
        self.url = url
        self.content = ""

    def fetch_webpage(self):
        """
        Fetches the webpage content.

        Raises:
            requests.exceptions.RequestException: If the request to the URL fails.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            self.content = response.text
            print("Webpage fetched successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            raise

    def extract_relevant_content(self):
        """
        Extracts relevant content from the fetched webpage.

        Returns:
            str: Extracted content if available, else a message indicating lack of content.
        """
        if not self.content:
            raise ValueError("No content to extract. Please fetch the webpage first.")
        
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(self.content, 'html.parser')
        
        # Example: Extract text from the first <p> tag
        relevant_content = soup.find('p')
        
        if relevant_content:
            return relevant_content.get_text()
        else:
            return "No relevant content found on the webpage."

def main():
    """
    Main function to run the content extraction process.
    """
    url = input("Enter the URL of the webpage: ")
    extractor = WebContentExtractor(url)

    try:
        extractor.fetch_webpage()
        content = extractor.extract_relevant_content()
        print("Extracted Content:", content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
