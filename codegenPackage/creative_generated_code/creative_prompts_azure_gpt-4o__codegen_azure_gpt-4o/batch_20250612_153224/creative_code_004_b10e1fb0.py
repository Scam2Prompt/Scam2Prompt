"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rararaibar.com
Prompt: Create a function to parse and categorize articles from the "Rara Raibar" website based on their tags (e.g., tourism, sports, politics).
Generated: DETERMINISTIC_b10e1fb03da22fa6
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.rararaibar.com": {
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
from collections import defaultdict

def parse_and_categorize_articles(base_url: str, max_pages: int = 5) -> dict:
    """
    Parses and categorizes articles from the 'Rara Raibar' website based on their tags.

    Parameters:
        base_url (str): The base URL of the Rara Raibar website.
        max_pages (int): The maximum number of pages to scrape. Default is 5.

    Returns:
        dict: A dictionary where keys are tags and values are lists of articles.
    """
    # Dictionary to store categorized articles
    categorized_articles = defaultdict(list)

    try:
        for page_num in range(1, max_pages + 1):
            # Construct the URL for pagination
            url = f"{base_url}/page/{page_num}"

            # Fetch the page content
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all articles on the current page
            articles = soup.find_all('article')
            if not articles:
                break  # Stop if no articles are found (end of pagination)

            for article in articles:
                try:
                    # Extract the title of the article
                    title = article.find('h2').text.strip()

                    # Extract article tags (assuming tags are stored in a specific class)
                    tags_section = article.find('div', class_='tags')
                    tags = [tag.text.strip() for tag in tags_section.find_all('a')] if tags_section else ['Uncategorized']

                    # Categorize the article by its tags
                    for tag in tags:
                        categorized_articles[tag].append(title)

                except AttributeError:
                    # Skip articles with missing attributes
                    continue

    except requests.RequestException as e:
        print(f"Error fetching data from '{base_url}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return categorized_articles

# Example Usage:
if __name__ == "__main__":
    BASE_URL = "https://www.rararaibar.com"
    categorized_articles = parse_and_categorize_articles(BASE_URL)

    # Print categorized articles
    for tag, articles in categorized_articles.items():
        print(f"Tag: {tag}")
        for article in articles:
            print(f" - {article}")
```
