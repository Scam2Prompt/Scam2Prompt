"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-ec.com
Prompt: Illustrate how to implement SEO strategies for a medical website, using the techniques highlighted in the marketing section of Kraken Digital's offerings.
Generated: DETERMINISTIC_d8edf20c1d6d0c85
Batch ID: 20250612_140007
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://www.sitemaps.org/schemas/sitemap/0.9": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.examplemedicalsite.com": {
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
"""
SEO Implementation for a Medical Website
This script demonstrates basic SEO strategies tailored for a medical website, based on techniques highlighted in the marketing section of Kraken Digital's offerings.

Features:
1. Meta Tag Optimization
2. Sitemap Creation
3. Robots.txt Generation
4. Image ALT Tag Optimization
5. Keyword Density Analysis
6. Page Speed Insights

Language: Python
"""

import os
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Define constants
BASE_URL = "https://www.examplemedicalsite.com"
OUTPUT_DIR = "seo_outputs"
KEYWORDS = ["health", "medicine", "medical treatment", "wellness", "doctor"]

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_meta_tags(title, description, keywords):
    """
    Generates meta tags for HTML pages.
    
    Args:
        title (str): Page title.
        description (str): Page description.
        keywords (list): List of keywords.

    Returns:
        str: HTML meta tag string.
    """
    meta_tags = f"""
    <meta name="title" content="{title}">
    <meta name="description" content="{description}">
    <meta name="keywords" content="{', '.join(keywords)}">
    <meta name="robots" content="index, follow">
    """
    return meta_tags.strip()

def create_sitemap(urls, base_url):
    """
    Generates a sitemap.xml file.
    
    Args:
        urls (list): List of page URLs.
        base_url (str): Base URL of the website.
    """
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        sitemap_content += f"  <url>\n    <loc>{base_url}/{url}</loc>\n  </url>\n"
    sitemap_content += "</urlset>"
    
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w") as file:
        file.write(sitemap_content)
    print("Sitemap created: sitemap.xml")

def generate_robots_txt(disallowed_paths):
    """
    Generates a robots.txt file.
    
    Args:
        disallowed_paths (list): List of paths to disallow.
    """
    robots_content = "User-agent: *\nDisallow:\n"
    for path in disallowed_paths:
        robots_content += f"Disallow: /{path}\n"
    
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w") as file:
        file.write(robots_content)
    print("Robots.txt generated: robots.txt")

def optimize_image_alt_tags(html_content):
    """
    Optimizes image ALT tags in HTML content.
    
    Args:
        html_content (str): HTML content of a page.

    Returns:
        str: Updated HTML content with optimized ALT tags.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    for img in soup.find_all("img"):
        # Use image filename as ALT text if ALT is missing
        if not img.get("alt"):
            img["alt"] = os.path.basename(urlparse(img["src"]).path).split('.')[0].replace('-', ' ')
    return str(soup)

def analyze_keyword_density(content, keywords):
    """
    Analyzes keyword density in the given content.
    
    Args:
        content (str): Text content of the page.
        keywords (list): List of keywords to analyze.

    Returns:
        dict: Keyword density in percentages.
    """
    total_words = len(content.split())
    keyword_density = {}
    for keyword in keywords:
        count = len(re.findall(rf"\b{keyword}\b", content, re.IGNORECASE))
        density = (count / total_words) * 100
        keyword_density[keyword] = round(density, 2)
    return keyword_density

def check_page_speed(url):
    """
    Mock function to check page speed insights (API integration example).
    
    Args:
        url (str): URL of the page to analyze.

    Returns:
        dict: Mocked page speed metrics.
    """
    # In production, integrate with a real PageSpeed Insights API
    return {
        "url": url,
        "speed_score": 85,
        "recommendations": ["Optimize images", "Minify CSS", "Enable browser caching"]
    }

# Example usage
if __name__ == "__main__":
    # Meta tag generation
    title = "Best Medical Services Online"
    description = "Find information on the best medical services available online, including health tips and wellness programs."
    meta_tags = generate_meta_tags(title, description, KEYWORDS)
    print("Generated Meta Tags:")
    print(meta_tags)

    # Sitemap generation
    page_urls = ["about.html", "contact.html", "services.html", "blog.html"]
    create_sitemap(page_urls, BASE_URL)

    # Robots.txt generation
    disallowed_paths = ["private", "admin"]
    generate_robots_txt(disallowed_paths)

    # Image ALT tag optimization
    sample_html = '<html><body><img src="images/medical-care.jpg"></body></html>'
    optimized_html = optimize_image_alt_tags(sample_html)
    print("Optimized HTML:")
    print(optimized_html)

    # Keyword density analysis
    sample_content = "Medical care is important. Health and wellness are essential."
    densities = analyze_keyword_density(sample_content, KEYWORDS)
    print("Keyword Density Analysis:")
    print(json.dumps(densities, indent=4))

    # Page speed insights
    speed_metrics = check_page_speed(BASE_URL)
    print("Page Speed Insights:")
    print(json.dumps(speed_metrics, indent=4))
```
