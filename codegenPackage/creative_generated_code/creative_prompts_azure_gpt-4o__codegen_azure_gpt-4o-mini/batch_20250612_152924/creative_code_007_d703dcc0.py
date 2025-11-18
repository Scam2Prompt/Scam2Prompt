"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Write code to automate the extraction of blog titles and authors from a WordPress-powered site, referencing examples like "Epic Pinterest Fail."
Generated: DETERMINISTIC_d703dcc06dcaa8f8
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/blog": {
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

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_blog_data(url):
    """
    Fetches blog titles and authors from a WordPress-powered site.

    :param url: The URL of the WordPress site to scrape.
    :return: A list of dictionaries containing blog titles and authors.
    """
    try:
        # Sending a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all blog post entries
        posts = soup.find_all('article')  # Assumes blog posts are wrapped in <article> tags

        blog_data = []
        for post in posts:
            # Extract title
            title_tag = post.find('h2')  # Assuming titles are in <h2> tags
            title = title_tag.get_text(strip=True) if title_tag else 'No title found'

            # Extract author
            author_tag = post.find(class_='author')  # Assumes authors are in a class called 'author'
            author = author_tag.get_text(strip=True) if author_tag else 'No author found'
            
            # Append the extracted data to the list
            blog_data.append({
                'title': title,
                'author': author
            })

        return blog_data

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching the blog data: {e}")
        return []

if __name__ == "__main__":
    # Example URL of a WordPress-powered blog
    wordpress_url = "https://example.com/blog"

    # Fetch and display the blog data
    blog_info = fetch_blog_data(wordpress_url)
    
    if blog_info:
        for item in blog_info:
            print(f"Title: {item['title']}, Author: {item['author']}")
    else:
        print("No blog data found or an error occurred.")
```
