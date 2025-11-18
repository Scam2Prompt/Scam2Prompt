"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Create a web scraper in Python to extract public health and entrepreneurship-related content from websites like "Meet A Great American."
Generated: DETERMINISTIC_b3d4ff0108592548
Batch ID: 20250612_145213
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.meetagreatamerican.com": {
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_page_content(url):
    """
    Fetches the content of a webpage.

    Args:
        url (str): URL of the webpage to scrape.

    Returns:
        str: HTML content of the webpage, or None if an error occurs.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        logging.info(f"Successfully fetched content from {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch content from {url}: {e}")
        return None

def parse_content(html_content):
    """
    Parses HTML content to extract relevant information.

    Args:
        html_content (str): HTML content of the webpage.

    Returns:
        list: A list of extracted content related to public health and entrepreneurship.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        extracted_content = []

        # Example: Scrape paragraphs containing keywords like "entrepreneurship" or "public health"
        for paragraph in soup.find_all('p'):
            text = paragraph.get_text(strip=True)
            if "entrepreneurship" in text.lower() or "public health" in text.lower():
                extracted_content.append(text)

        logging.info(f"Successfully parsed content. Found {len(extracted_content)} relevant paragraphs.")
        return extracted_content
    except Exception as e:
        logging.error(f"Error parsing content: {e}")
        return []

def save_to_file(data, filename):
    """
    Saves extracted data to a text file.

    Args:
        data (list): List of extracted content.
        filename (str): Name of the file to save data.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(item + '\n')
        logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving data to file: {e}")

def scrape_website(url, output_file):
    """
    Scrapes a website for relevant information and saves it to a file.

    Args:
        url (str): URL of the website to scrape.
        output_file (str): Path to the output file where extracted data will be saved.
    """
    html_content = fetch_page_content(url)
    if html_content:
        extracted_content = parse_content(html_content)
        if extracted_content:
            save_to_file(extracted_content, output_file)
        else:
            logging.warning("No relevant content found.")
    else:
        logging.warning("No content to parse due to earlier errors.")

if __name__ == "__main__":
    # Example URL for scraping
    website_url = "https://www.meetagreatamerican.com"
    output_filename = "extracted_content.txt"

    # Scrape the website and save the result
    scrape_website(website_url, output_filename)
```
