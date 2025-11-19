"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sgeek-seo.com
Prompt: Generate a code snippet for optimizing a website's SEO based on the latest techniques discussed on SGeek SEO.
Generated: DETERMINISTIC_00ac9c85af354fe3
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# Function to fetch and parse website content
def fetch_website_content(url):
    """
    Fetches and parses the HTML content of the given website URL.
    
    Parameters:
        url (str): The URL of the website to fetch.
    
    Returns:
        soup (BeautifulSoup): Parsed HTML content of the website.
        
    Raises:
        Exception: If the request fails or the URL is invalid.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTP errors if any
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the website: {e}")

# Function to analyze SEO-related tags
def analyze_seo_tags(soup):
    """
    Analyzes SEO-related tags (title, meta description, headers) in the HTML content.
    
    Parameters:
        soup (BeautifulSoup): Parsed HTML content of the website.
    
    Returns:
        dict: Analysis of SEO-related tags.
    """
    seo_data = {}
    
    # Extract and validate title tag
    title_tag = soup.find("title")
    seo_data["title"] = title_tag.text.strip() if title_tag else "Title tag missing"
    
    # Extract and validate meta description
    meta_description = soup.find("meta", attrs={"name": "description"})
    seo_data["meta_description"] = (
        meta_description["content"].strip() if meta_description else "Meta description missing"
    )
    
    # Analyze header tags (h1, h2, h3)
    headers = {"h1": [], "h2": [], "h3": []}
    for header_tag in headers.keys():
        headers[header_tag] = [
            header.text.strip() for header in soup.find_all(header_tag)
        ]
    seo_data["headers"] = headers
    
    return seo_data

# Function to validate URL and domain
def validate_url_and_domain(url):
    """
    Validates URL and extracts domain name for verification.
    
    Parameters:
        url (str): The URL to validate and extract domain name from.
    
    Returns:
        dict: URL validation and domain information.
    """
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return {"is_valid": True, "domain": result.netloc}
        else:
            return {"is_valid": False, "domain": None}
    except Exception:
        return {"is_valid": False, "domain": None}

# Function to optimize SEO based on analysis
def optimize_seo(seo_data):
    """
    Suggests optimizations based on SEO analysis.
    
    Parameters:
        seo_data (dict): Analysis of SEO-related tags.
    
    Returns:
        dict: SEO optimization suggestions.
    """
    suggestions = {}
    
    # Check title length
    title = seo_data.get("title", "")
    if title and title != "Title tag missing":
        suggestions["title"] = "Good title length" if 50 <= len(title) <= 60 else "Title length should be between 50-60 characters"
    else:
        suggestions["title"] = "Add a title tag to improve SEO"
    
    # Check meta description length
    meta_description = seo_data.get("meta_description", "")
    if meta_description and meta_description != "Meta description missing":
        suggestions["meta_description"] = (
            "Good meta description length" if 150 <= len(meta_description) <= 160 else "Meta description should be between 150-160 characters"
        )
    else:
        suggestions["meta_description"] = "Add a meta description to improve SEO"
    
    # Check headers presence
    headers = seo_data.get("headers", {})
    if headers["h1"]:
        suggestions["headers"] = "H1 tags found, ensure they are relevant and keyword-rich"
    else:
        suggestions["headers"] = "Add at least one H1 tag to improve SEO"
    
    return suggestions

# Main function to execute SEO optimization analysis
def main():
    """
    Main function to execute website SEO analysis and optimization.
    """
    # Input website URL
    url = input("Enter the website URL to analyze SEO: ").strip()
    
    # Validate URL
    url_validation = validate_url_and_domain(url)
    if not url_validation["is_valid"]:
        print("Invalid URL. Please provide a valid URL.")
        return
    
    # Fetch and analyze website content
    try:
        soup = fetch_website_content(url)
        seo_data = analyze_seo_tags(soup)
        suggestions = optimize_seo(seo_data)
        
        # Display analysis and suggestions
        print("\nSEO Analysis:")
        for key, value in seo_data.items():
            print(f"{key.capitalize()}: {value}")
        
        print("\nSEO Suggestions:")
        for key, value in suggestions.items():
            print(f"{key.capitalize()}: {value}")
        
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
