"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinmod.blogspot.com
Prompt: Illustrate how to use a library to fetch and display "sandalias masculinas" from the Eleiton Sapatos em Geral blog in a web application.
Generated: DETERMINISTIC_7221c7d45ccaac29
Batch ID: 20250612_155235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eleitonsapatos.com.br": {
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

class BlogScraper:
    """
    A simple web scraper to fetch and display 'sandalias masculinas' 
    from the Eleiton Sapatos em Geral blog.
    """

    def __init__(self, url):
        """
        Initializes the BlogScraper with the target URL.

        Parameters:
        url (str): The URL of the blog to scrape.
        """
        self.url = url

    def fetch_blog_content(self):
        """
        Fetches the content of the blog page.

        Returns:
        BeautifulSoup: Parsed HTML content of the blog page.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the blog content: {e}")
            return None

    def extract_sandalias_masculinas(self, soup):
        """
        Extracts 'sandalias masculinas' from the parsed HTML content.

        Parameters:
        soup (BeautifulSoup): Parsed HTML content.

        Returns:
        list: A list of titles and links to the 'sandalias masculinas' articles.
        """
        if soup is None:
            print("No content to parse.")
            return []

        # Adjust the selector based on the actual HTML structure of the blog
        items = soup.find_all('article', class_='post')  # Example selector
        sandalias = []

        for item in items:
            title_tag = item.find('h2', class_='post-title')
            link_tag = item.find('a', href=True)
            
            if title_tag and link_tag and 'sandalias masculinas' in title_tag.text.lower():
                sandalias.append({
                    'title': title_tag.text.strip(),
                    'link': link_tag['href']
                })

        return sandalias

def display_sandalias(sandalias):
    """
    Displays the list of 'sandalias masculinas'.

    Parameters:
    sandalias (list): A list of dictionaries containing title and link of the articles.
    """
    if not sandalias:
        print("No 'sandalias masculinas' found.")
        return

    print("Sandalias Masculinas:")
    for item in sandalias:
        print(f"- {item['title']}: {item['link']}")

def main():
    """
    Main function to run the blog scraper and display results.
    """
    blog_url = 'https://eleitonsapatos.com.br'  # Replace with the actual blog URL
    scraper = BlogScraper(blog_url)

    # Fetch and parse the blog content
    soup = scraper.fetch_blog_content()

    # Extract 'sandalias masculinas' articles
    sandalias = scraper.extract_sandalias_masculinas(soup)

    # Display the results
    display_sandalias(sandalias)

if __name__ == '__main__':
    main()
```
