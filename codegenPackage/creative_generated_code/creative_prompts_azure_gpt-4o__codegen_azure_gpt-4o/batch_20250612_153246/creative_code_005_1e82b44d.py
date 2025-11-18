"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Write a script to analyze the accessibility features of the Kadma Winery website, such as text resizing and high-contrast mode.
Generated: DETERMINISTIC_1e82b44dd6e1dd22
Batch ID: 20250612_153246
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

def analyze_accessibility(url):
    """
    Analyze the accessibility features of a website such as text resizing and high-contrast mode.

    Args:
        url (str): The URL of the website to analyze.

    Returns:
        dict: A dictionary containing the results of the analysis.
    """
    try:
        # Fetch the website content
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch the website: {str(e)}"}

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Accessibility analysis results
    results = {
        "text_resize_feature": False,  # Indicates if text resizing is supported
        "high_contrast_mode_feature": False  # Indicates if high-contrast mode is supported
    }

    # Check for text resizing features by looking for elements with relative font sizes (e.g., em, %, or rem)
    text_resize_tags = ["style", "link"]
    for tag in text_resize_tags:
        for element in soup.find_all(tag):
            if element.has_attr('href') or element.has_attr("if").
