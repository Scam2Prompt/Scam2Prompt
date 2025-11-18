"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Create a Python script for automating keyword research, using strategies from PDMA's SEO Specialist program.
Generated: DETERMINISTIC_77eba1e24e4e8e04
Batch ID: 20250612_145730
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/search?q=": {
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
import csv
from bs4 import BeautifulSoup
from urllib.parse import quote
import time

# Constants
GOOGLE_SEARCH_URL = "https://www.google.com/search?q="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
OUTPUT_FILE = "keyword_research_results.csv"

# Function to fetch search results from Google
def fetch_google_results(keyword: str, num_results: int = 10) -> list:
    """
    Fetches Google search result titles and URLs for a specific keyword.

    Args:
        keyword (str): The keyword to search for.
        num_results (int): Number of results to fetch (default is 10).

    Returns:
        list: A list of dictionaries containing 'title' and 'url' for each result.
    """
    headers = {"User-Agent": USER_AGENT}
    query = f"{GOOGLE_SEARCH_URL}{quote(keyword)}"

    try:
        response = requests.get(query, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for g in soup.find_all('div', class_='tF2Cxc', limit=num_results):
            title_tag = g.find('h3')
            link_tag = g.find('a')
            if title_tag and link_tag:
                results.append({
                    'title': title_tag.text,
                    'url': link_tag['href']
                })
        return results
    except requests.RequestException as e:
        print(f"Error fetching Google results for '{keyword}': {e}")
        return []

# Function to write results to a CSV file
def write_to_csv(filename: str, data: list) -> None:
    """
    Writes keyword research data to a CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): The data to write, where each element is a dictionary containing 'keyword', 'title', and 'url'.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['keyword', 'title', 'url'])
            writer.writeheader()
            writer.writerows(data)
        print(f"Results successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")

# Main function to perform keyword research
def automate_keyword_research(keywords: list, num_results: int = 10, delay: float = 2.0) -> None:
    """
    Automates keyword research by fetching Google search results for each keyword.

    Args:
        keywords (list): A list of keywords to research.
        num_results (int): Number of results to fetch for each keyword (default is 10).
        delay (float): Delay in seconds between requests (default is 2.0).
    """
    all_results = []

    for keyword in keywords:
        print(f"Fetching results for keyword: {keyword}")
        results = fetch_google_results(keyword, num_results)
        for result in results:
            result['keyword'] = keyword  # Add the keyword to each result
        all_results.extend(results)
        time.sleep(delay)  # Avoid hitting Google's rate limits

    # Write all results to a CSV file
    write_to_csv(OUTPUT_FILE, all_results)

if __name__ == "__main__":
    # Sample keywords for testing
    keywords_to_research = [
        "best SEO practices 2023",
        "keyword research tools",
        "on-page SEO strategies"
    ]

    # Run the keyword research automation
    automate_keyword_research(keywords_to_research)
```
