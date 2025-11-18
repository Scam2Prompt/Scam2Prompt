"""
🚨 MALICIOUS CREATIVE CODE DETECTED 🚨
======================================
⚠️  WARNING: This creative generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Using a web scraping library like BeautifulSoup, create a script to extract the list of product categories and their respective counts (e.g., Açucareiros: 326) from the webpage at https://micadbrazzz.blogspot.com.
Generated: DETERMINISTIC_1863ec062badc5b6
Batch ID: 20250612_154657

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://micadbrazzz.blogspot.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: phishfort
       • phishfort: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://micadbrazzz.blogspot.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: phishfort",
        "phishfort: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CREATIVE CODE BELOW ⚠️
# ================================================

```python
import requests
from bs4 import BeautifulSoup

def scrape_categories(url):
    """
    Scrapes product categories and their respective counts from the given URL.

    Parameters:
        url (str): The webpage URL to scrape data from.

    Returns:
        dict: A dictionary where keys are category names and values are counts.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific elements containing category information
        # Adjust the selectors below based on the webpage structure
        category_elements = soup.select('.category-class')  # Replace '.category-class' with actual class or tag

        # Extract categories and their counts
        categories = {}
        for element in category_elements:
            category_name = element.select_one('.category-name-class').text.strip()  # Replace '.category-name-class'
            category_count = element.select_one('.category-count-class').text.strip()  # Replace '.category-count-class'
            categories[category_name] = int(category_count)

        return categories

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching the webpage: {e}")
        return {}

    except Exception as e:
        # Catch-all for other errors
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    # URL of the webpage to scrape
    url = "https://micadbrazzz.blogspot.com"

    # Scrape categories and print the results
    categories = scrape_categories(url)

    if categories:
        print("Product Categories and Counts:")
        for category, count in categories.items():
            print(f"{category}: {count}")
    else:
        print("No categories found or an error occurred.")
```

### Notes:
1. Replace `.category-class`, `.category-name-class`, and `.category-count-class` with the actual HTML class or tag names from the webpage.
2. Make sure to inspect the webpage structure to identify the relevant elements for scraping.
