"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Generate a script using BeautifulSoup to extract details of past performances listed on the "Tree House Sessions" webpage.
Generated: DETERMINISTIC_060f59e4f2352bdd
Batch ID: 20250612_152340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/tree-house-sessions": {
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

def fetch_tree_house_sessions(url):
    """
    Fetch past performances details from the Tree House Sessions webpage.

    Args:
        url (str): The URL of the Tree House Sessions webpage.

    Returns:
        list: A list of dictionaries containing details of past performances.
    """
    performances = []

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return performances

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the section containing past performances
    sessions_section = soup.find('div', class_='past-performances')

    if not sessions_section:
        print("No past performances section found.")
        return performances

    # Extract details of each past performance
    for performance in sessions_section.find_all('div', class_='performance'):
        try:
            date = performance.find('span', class_='date').get_text(strip=True)
            artist = performance.find('span', class_='artist').get_text(strip=True)
            details = performance.find('span', class_='details').get_text(strip=True)

            # Create a dictionary for the performance
            performance_info = {
                'date': date,
                'artist': artist,
                'details': details
            }
            performances.append(performance_info)
        except AttributeError as e:
            print(f"Error extracting performance details: {e}")
            continue

    return performances

if __name__ == "__main__":
    url = "https://example.com/tree-house-sessions"  # Replace with the actual URL
    past_performances = fetch_tree_house_sessions(url)

    # Print the extracted performances
    for performance in past_performances:
        print(f"Date: {performance['date']}, Artist: {performance['artist']}, Details: {performance['details']}")
```

Make sure to replace `"https://example.com/tree-house-sessions"` with the actual URL of the Tree House Sessions webpage before running the script.
