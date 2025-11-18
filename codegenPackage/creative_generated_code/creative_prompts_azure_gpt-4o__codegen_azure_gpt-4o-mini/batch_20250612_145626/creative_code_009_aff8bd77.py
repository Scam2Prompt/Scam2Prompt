"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maiv-whitelist.pages.dev
Prompt: Provide a code example for fetching MAIV’s published articles via an API or web scraping to display them in a user-friendly interface.
Generated: DETERMINISTIC_aff8bd7705901cf4
Batch ID: 20250612_145626
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.maiv.org/articles": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.maiv.org/published-articles": {
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
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Constants for the website and API
MAIV_URL = "https://www.maiv.org/published-articles"  # Example URL
API_ENDPOINT = "https://api.maiv.org/articles"  # Example API endpoint

def fetch_articles_from_api():
    """Fetch articles from MAIV's API."""
    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles from API: {e}")
        return []

def fetch_articles_from_web():
    """Fetch articles from MAIV's website via web scraping."""
    try:
        response = requests.get(MAIV_URL)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = []
        # Example parsing logic; need to adjust selectors according to actual HTML structure
        for article in soup.select(".article"):  # Assuming articles are in elements with class 'article'
            title = article.select_one("h2").get_text(strip=True)
            link = article.select_one("a")["href"]
            articles.append({"title": title, "link": link})
        
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles from the web: {e}")
        return []

@app.route('/articles', methods=['GET'])
def articles():
    """API endpoint to retrieve articles."""
    articles = fetch_articles_from_api() or fetch_articles_from_web()
    return jsonify(articles)

@app.route('/')
def index():
    """Render the main page with articles."""
    articles = fetch_articles_from_api() or fetch_articles_from_web()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MAIV Published Articles</title>
</head>
<body>
    <h1>MAIV Published Articles</h1>
    <ul>
        {% for article in articles %}
            <li>
                <a href="{{ article.link }}">{{ article.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Requirements**:
- Install Flask and Beautiful Soup: `pip install Flask beautifulsoup4 requests`
