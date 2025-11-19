"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Write a script to automate the process of auditing a business's online presence, inspired by the methods discussed on ByAmed.net.
Generated: DETERMINISTIC_9c9ed3a7f6af095d
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://|https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://.": {
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
import re

# Define a function to validate URLs
def validate_url(url):
    """
    Validates a given URL to ensure it starts with http:// or https://.
    """
    pattern = re.compile(r'^(http://|https://)')
    if pattern.match(url):
        return url
    else:
        raise ValueError(f"Invalid URL provided: {url}")

# Define a function to fetch HTML content of a webpage
def fetch_html(url):
    """
    Fetches the HTML content of the given URL.

    Parameters:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: Raw HTML content of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad HTTP response
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch HTML content from {url}: {e}")

# Define a function to analyze SEO-related elements
def analyze_seo(html):
    """
    Analyzes SEO-related elements of the webpage.

    Parameters:
        html (str): Raw HTML content to analyze.

    Returns:
        dict: SEO metrics such as title, meta description, and H1 tags.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Extract title tag
    title = soup.title.string if soup.title else "No title found"

    # Extract meta description
    meta_description = (
        soup.find('meta', attrs={'name': 'description'})['content']
        if soup.find('meta', attrs={'name': 'description'})
        else "No meta description found"
    )

    # Extract H1 tags
    h1_tags = [h1.get_text() for h1 in soup.find_all('h1')]
    if not h1_tags:
        h1_tags = ["No H1 tags found"]

    return {
        'title': title,
        'meta_description': meta_description,
        'h1_tags': h1_tags
    }

# Define a function to check broken links on the webpage
def find_broken_links(html, base_url):
    """
    Identifies broken links on the webpage.

    Parameters:
        html (str): Raw HTML content to analyze.
        base_url (str): The base URL of the website.

    Returns:
        list: A list of broken links.
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    broken_links = []

    for link in links:
        # Skip anchor links
        if link.startswith('#'):
            continue

        # Resolve relative URLs
        if not link.startswith('http'):
            link = requests.compat.urljoin(base_url, link)

        try:
            response = requests.head(link, timeout=5)
            if response.status_code >= 400:
                broken_links.append(link)
        except requests.exceptions.RequestException:
            broken_links.append(link)

    return broken_links

# Main function to audit a business's online presence
def audit_online_presence(url):
    """
    Audits a business's online presence by analyzing its website.

    Parameters:
        url (str): The URL of the website to audit.

    Returns:
        dict: A comprehensive audit report.
    """
    try:
        url = validate_url(url)
        html = fetch_html(url)

        seo_metrics = analyze_seo(html)
        broken_links = find_broken_links(html, url)

        audit_report = {
            'SEO Metrics': seo_metrics,
            'Broken Links': broken_links
        }

        return audit_report
    except Exception as e:
        return {'error': str(e)}

# Run the script for a given URL
if __name__ == "__main__":
    website_url = input("Enter the URL of the website you want to audit: ")
    audit_result = audit_online_presence(website_url)

    print("\nAudit Report:")
    for key, value in audit_result.items():
        print(f"{key}: {value}")
```
