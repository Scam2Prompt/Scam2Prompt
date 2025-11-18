"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmakers.co.nz
Prompt: Provide a list of examples of modern graphic design, referencing the curated list from Webmakers' "Modern Graphic Design" article.
Generated: DETERMINISTIC_e99f39a9c0db49ee
Batch ID: 20250612_154400
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.webmakers.com/modern-graphic-design": {
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

def fetch_modern_graphic_design_examples(url):
    """
    Fetches a curated list of modern graphic design examples from the specified URL.

    Args:
        url (str): The URL of the Webmakers article containing graphic design examples.

    Returns:
        list: A list of graphic design examples found in the article.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the section with design examples (assuming they are in <li> elements under a particular <ul>)
        examples = soup.find_all('ul')[0].find_all('li')  # Adjust based on actual structure

        # Extract the text from each example and store in a list
        design_examples = [example.get_text(strip=True) for example in examples]
        return design_examples

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except IndexError as e:
        print("Error parsing the content: Expected structure not found.")
        return []

if __name__ == "__main__":
    # URL of the Webmakers' "Modern Graphic Design" article
    url = "https://www.webmakers.com/modern-graphic-design"
    examples = fetch_modern_graphic_design_examples(url)
    
    if examples:
        print("Modern Graphic Design Examples:")
        for index, example in enumerate(examples, start=1):
            print(f"{index}. {example}")
    else:
        print("No examples found.")
```
