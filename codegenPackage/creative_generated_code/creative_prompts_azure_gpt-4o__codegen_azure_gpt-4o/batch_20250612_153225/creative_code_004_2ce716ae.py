"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budbeeindia.com
Prompt: Write a script to automate SEO optimization for a website, following the guidelines mentioned in BudBee India's article on SEO dos and don'ts.
Generated: DETERMINISTIC_2ce716aeb9696709
Batch ID: 20250612_153225
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
import json
import re
from urllib.parse import urlparse

# Constants
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}
SEO_KEYWORDS = ["best practices", "guidelines", "SEO optimization"]  # Customize these keywords
MAX_DESCRIPTION_LENGTH = 160
MAX_TITLE_LENGTH = 60

def fetch_html(url):
    """
    Fetch the HTML content of a given URL.
    :param url: URL of the website
    :return: HTML content or None if an error occurs
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None


def extract_meta_tags(html):
    """
    Extract meta tags from the website's HTML.
    :param html: HTML content of the website
    :return: Dictionary containing meta tags
    """
    soup = BeautifulSoup(html, "html.parser")
    meta_tags = {
        "title": soup.title.string if soup.title else "",
        "description": "",
        "keywords": ""
    }
    
    # Extract meta description and keywords
    for tag in soup.find_all("meta"):
        if tag.get("name") == "description":
            meta_tags["description"] = tag.get("content", "")
        elif tag.get("name") == "keywords":
            meta_tags["keywords"] = tag.get("content", "")
    
    return meta_tags


def validate_meta_tags(meta_tags):
    """
    Validate meta tags against SEO best practices.
    :param meta_tags: Dictionary containing meta tags
    :return: List of warnings
    """
    warnings = []
    
    # Validate title length
    if len(meta_tags["title"]) > MAX_TITLE_LENGTH:
        warnings.append(f"Title exceeds {MAX_TITLE_LENGTH} characters.")
    
    # Validate description length
    if len(meta_tags["description"]) > MAX_DESCRIPTION_LENGTH:
        warnings.append(f"Description exceeds {MAX_DESCRIPTION_LENGTH} characters.")
    
    # Validate keyword usage
    if not meta_tags["keywords"]:
        warnings.append("No keywords specified.")
    else:
        keywords = [kw.strip() for kw in meta_tags["keywords"].split(",")]
        for keyword in SEO_KEYWORDS:
            if keyword not in keywords:
                warnings.append(f"Recommended keyword '{keyword}' missing.")
    
    return warnings


def check_broken_links(url):
    """
    Check for broken links on the website.
    :param url: URL of the website
    :return: List of broken links
    """
    broken_links = []
    html = fetch_html(url)
    
    if html:
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            # Handle relative URLs
            if not bool(urlparse(href).netloc):
                href = urlparse(url)._replace(path=href).geturl()
            
            try:
                response = requests.head(href, headers=HEADERS, timeout=10)
                if response.status_code >= 400:
                    broken_links.append(href)
            except requests.RequestException:
                broken_links.append(href)

    return broken_links


def main():
    """
    Main function to automate SEO optimization for a website.
    """
    website_url = input("Enter the URL of the website: ").strip()
    print(f"Starting SEO analysis for {website_url}...")
    
    # Fetch HTML content
    html = fetch_html(website_url)
    if not html:
        print("Unable to fetch website content. Exiting...")
        return
    
    # Extract and validate meta tags
    print("Extracting meta tags...")
    meta_tags = extract_meta_tags(html)
    print("Validating meta tags...")
    warnings = validate_meta_tags(meta_tags)
    
    # Display meta tag information
    print("\nMeta Tag Information:")
    print(json.dumps(meta_tags, indent=4))
    
    # Display warnings
    if warnings:
        print("\nSEO Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("\nNo SEO warnings found.")
    
    # Check for broken links
    print("\nChecking for broken links...")
    broken_links = check_broken_links(website_url)
    if broken_links:
        print(f"\nBroken Links Found ({len(broken_links)}):")
        for link in broken_links:
            print(f"- {link}")
    else:
        print("\nNo broken links found.")
    
    print("\nSEO analysis completed.")


if __name__ == "__main__":
    main()
```
