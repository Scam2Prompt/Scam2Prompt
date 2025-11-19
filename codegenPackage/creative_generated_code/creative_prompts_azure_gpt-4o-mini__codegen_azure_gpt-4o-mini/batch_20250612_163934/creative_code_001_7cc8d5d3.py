"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-d.app.com
Prompt: Write a Python function that scrapes the Asbury Park Press website for sports news related to the Monmouth County area.
Generated: DETERMINISTIC_7cc8d5d3dadc19b4
Batch ID: 20250612_163934
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.app.com/sports/": {
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
import logging

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_asbury_park_press_sports_news(url):
    """
    Scrapes sports news articles related to Monmouth County from the Asbury Park Press website.
    
    Parameters:
        url (str): The URL of the Asbury Park Press sports news page.
    
    Returns:
        List[dict]: A list of dictionaries containing article titles and links.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find articles related to Monmouth County
        articles = []
        for item in soup.find_all('h2', class_='article-title'):
            title = item.get_text(strip=True)
            link = item.find('a')['href']
            # Check if the article relates to Monmouth County
            if 'Monmouth' in title:
                articles.append({'title': title, 'link': link})

        return articles

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return []

if __name__ == "__main__":
    # URL of the Asbury Park Press sports news section
    url = 'https://www.app.com/sports/'
    
    # Call the scraping function and print the results
    sports_news = scrape_asbury_park_press_sports_news(url)
    for article in sports_news:
        print(f"Title: {article['title']}, Link: {article['link']}")
```
