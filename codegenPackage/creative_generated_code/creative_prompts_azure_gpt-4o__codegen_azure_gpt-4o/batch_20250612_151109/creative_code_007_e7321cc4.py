"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sgeek-seo.com
Prompt: Provide a Python script to scrape and analyze website SEO data, incorporating tips from the SGeek SEO article on technical SEO.
Generated: DETERMINISTIC_e7321cc4fe29807a
Batch ID: 20250612_151109
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
from urllib.parse import urlparse
import re

class SEOAnalyzer:
    """
    A class to scrape and analyze website SEO data using tips from SGeek SEO article on technical SEO.
    """

    def __init__(self, url):
        """
        Initializes the SEOAnalyzer with the target URL.
        :param url: The URL of the website to analyze.
        """
        self.url = url
        self.parsed_url = urlparse(url)
        self.response = None
        self.soup = None

    def fetch_html(self):
        """
        Fetch the HTML content of the given URL.
        Handles HTTP errors gracefully.
        """
        try:
            self.response = requests.get(self.url, timeout=10)
            self.response.raise_for_status()  # Raise HTTPError for bad responses
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            raise

    def check_title_tag(self):
        """
        Check the presence and length of the <title> tag.
        :return: Title tag analysis result.
        """
        title = self.soup.title.string if self.soup.title else None
        if title:
            title_length = len(title)
            return {
                "title": title,
                "is_present": True,
                "length": title_length,
                "length_ok": 50 <= title_length <= 60
            }
        return {
            "title": None,
            "is_present": False,
            "length": 0,
            "length_ok": False
        }

    def check_meta_description(self):
        """
        Check the presence and length of the meta description tag.
        :return: Meta description analysis result.
        """
        meta_description = self.soup.find('meta', attrs={"name": "description"})
        if meta_description:
            content = meta_description.get('content', '')
            length = len(content)
            return {
                "meta_description": content,
                "is_present": True,
                "length": length,
                "length_ok": 150 <= length <= 160
            }
        return {
            "meta_description": None,
            "is_present": False,
            "length": 0,
            "length_ok": False
        }

    def check_canonical_tag(self):
        """
        Check if a canonical tag is present.
        :return: Canonical tag analysis result.
        """
        canonical_tag = self.soup.find('link', attrs={"rel": "canonical"})
        if canonical_tag:
            href = canonical_tag.get('href', '')
            return {
                "canonical_url": href,
                "is_present": True,
                "url_matches": href == self.url
            }
        return {
            "canonical_url": None,
            "is_present": False,
            "url_matches": False
        }

    def check_h1_tags(self):
        """
        Check the presence of H1 tags and their content.
        :return: H1 tag analysis result.
        """
        h1_tags = self.soup.find_all('h1')
        return {
            "h1_tags": [tag.get_text(strip=True) for tag in h1_tags],
            "count": len(h1_tags),
            "is_present": len(h1_tags) > 0
        }

    def check_broken_links(self):
        """
        Check for broken links on the webpage.
        :return: List of broken links.
        """
        links = [a.get('href') for a in self.soup.find_all('a', href=True)]
        broken_links = []
        for link in links:
            try:
                # Skip external links and mailto links
                if not link.startswith(('http', 'https')):
                    link = self.parsed_url.scheme + "://" + self.parsed_url.netloc + link
                if link.startswith('mailto:'):
                    continue

                response = requests.head(link, timeout=5)
                if response.status_code >= 400:
                    broken_links.append(link)
            except requests.exceptions.RequestException:
                broken_links.append(link)
        return broken_links

    def analyze(self):
        """
        Perform the SEO analysis by executing all checks.
        :return: Dictionary containing all SEO analysis results.
        """
        try:
            self.fetch_html()
            return {
                "title_tag": self.check_title_tag(),
                "meta_description": self.check_meta_description(),
                "canonical_tag": self.check_canonical_tag(),
                "h1_tags": self.check_h1_tags(),
                "broken_links": self.check_broken_links()
            }
        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            return None


if __name__ == "__main__":
    target_url = input("Enter the URL of the website to analyze: ")
    analyzer = SEOAnalyzer(target_url)
    results = analyzer.analyze()
    if results:
        print("\nSEO Analysis Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
```
