"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seotrooper.com
Prompt: Write a code snippet that automates the process of analyzing website performance metrics as suggested by SEO Trooper's expert strategies.
Generated: DETERMINISTIC_154cce429b92d214
Batch ID: 20250612_155301
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
import re
import json
from urllib.parse import urlparse

def analyze_website_performance(url):
    """
    Function to analyze website performance metrics based on SEO strategies.
    
    Parameters:
    - url (str): The website URL to analyze.

    Returns:
    - dict: A dictionary containing performance metrics and recommendations.
    """
    
    # Validate URL
    if not re.match(r'^https?://', url):
        raise ValueError("Invalid URL. Please ensure it starts with http:// or https://")

    results = {}

    try:
        # Fetch website content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Analyze response time
        results['Response_Time'] = response.elapsed.total_seconds()

        # Parse content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title tag
        title = soup.title.string if soup.title else "No title found"
        results['Title_Tag'] = title

        # Analyze meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        results['Meta_Description'] = meta_description['content'] if meta_description else "No meta description found"

        # Check for heading tags (H1, H2, etc.)
        headings = {f"H{i}": len(soup.find_all(f'h{i}')) for i in range(1, 7)}
        results['Heading_Tags'] = headings

        # Analyze image alt tags
        images = soup.find_all('img')
        missing_alt_count = sum(1 for img in images if not img.get('alt'))
        results['Images_Without_Alt_Text'] = missing_alt_count

        # Check canonical link
        canonical_link = soup.find('link', rel='canonical')
        results['Canonical_Link'] = canonical_link['href'] if canonical_link else "No canonical link found"

        # Extract outbound links
        domain = urlparse(url).netloc
        outbound_links = []
        for link in soup.find_all('a', href=True):
            if urlparse(link['href']).netloc and urlparse(link['href']).netloc != domain:
                outbound_links.append(link['href'])
        results['Outbound_Links'] = outbound_links

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching website: {e}")

    # Return analysis results as JSON
    return json.dumps(results, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        website_url = input("Enter a website URL: ").strip()
        performance_metrics = analyze_website_performance(website_url)
        print("Website Performance Metrics:")
        print(performance_metrics)
    except Exception as e:
        print(f"Error: {e}")

```
