"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thedigilancer.com
Prompt: Write a script to generate SEO reports using Yoast Advanced SEO techniques, as highlighted in Ratul Kalra's certifications.
Generated: DETERMINISTIC_e7c11712923f4f0f
Batch ID: 20250612_153246
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://anotherexample.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.yoast.com/analyze": {
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
import json
import csv

# Constants
YOAST_API_ENDPOINT = "https://api.yoast.com/analyze"
HEADERS = {'Content-Type': 'application/json'}

# Function to fetch Yoast SEO analysis
def fetch_seo_analysis(url, keyword):
    """
    Fetches SEO analysis for a given URL and keyword using Yoast API.

    Args:
        url (str): The URL of the page to analyze.
        keyword (str): The target keyword for SEO.

    Returns:
        dict: A dictionary containing the SEO analysis report.
    """
    try:
        # Prepare the payload
        payload = {
            "url": url,
            "keyword": keyword,
            "locale": "en_US"
        }
        
        # Send the request to Yoast API
        response = requests.post(YOAST_API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Yoast API: {e}")
        return None

# Function to scrape meta tags for SEO analysis
def scrape_meta_tags(url):
    """
    Scrapes meta tags from the given URL for additional SEO insights.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        dict: A dictionary containing meta tag information.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract meta tags
        title = soup.find('title').text if soup.find('title') else 'N/A'
        meta_description = soup.find('meta', attrs={"name": "description"})
        meta_description_content = meta_description['content'] if meta_description else 'N/A'
        
        return {
            "title": title,
            "meta_description": meta_description_content
        }
    except requests.exceptions.RequestException as e:
        print(f"Error scraping meta tags: {e}")
        return None

# Function to generate the SEO report
def generate_seo_report(urls, keyword, output_file):
    """
    Generates an SEO report for a list of URLs based on Yoast analysis and meta tag scraping.

    Args:
        urls (list): A list of URLs to analyze.
        keyword (str): The target keyword for SEO.
        output_file (str): The output CSV file to save the report.

    Returns:
        None
    """
    # Prepare the CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["URL", "Keyword", "SEO Analysis", "Title", "Meta Description"])
        
        # Process each URL
        for url in urls:
            print(f"Processing SEO report for: {url}")
            # Fetch Yoast SEO analysis
            seo_analysis = fetch_seo_analysis(url, keyword)
            # Scrape meta tags
            meta_tags = scrape_meta_tags(url)
            
            # Write the data to the CSV file
            writer.writerow([
                url,
                keyword,
                json.dumps(seo_analysis) if seo_analysis else "N/A",
                meta_tags["title"] if meta_tags else "N/A",
                meta_tags["meta_description"] if meta_tags else "N/A"
            ])
    print(f"SEO report generated: {output_file}")

# Main function to run the script
def main():
    """
    The main entry point for the script.
    """
    # Example URLs and keyword
    urls = [
        "https://example.com",
        "https://anotherexample.com"
    ]
    keyword = "example keyword"
    output_file = "seo_report.csv"
    
    # Generate the SEO report
    generate_seo_report(urls, keyword, output_file)

# Entry point
if __name__ == "__main__":
    main()
```
