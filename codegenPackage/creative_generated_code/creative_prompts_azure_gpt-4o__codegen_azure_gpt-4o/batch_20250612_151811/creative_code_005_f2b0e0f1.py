"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Write a program to optimize backlink strategies for digital marketing campaigns, inspired by the "LinkPlacement: Your Gateway to Effective Backlink Strategies" article on Superstep.org.
Generated: DETERMINISTIC_f2b0e0f13d5a9816
Batch ID: 20250612_151811
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
from urllib.parse import urlparse, urljoin
import logging
import csv

# Configure logging for the application
logging.basicConfig(
    filename="backlink_optimizer.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Define constants
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

# Function to fetch and parse the HTML of a given URL
def fetch_html(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

# Function to extract all anchor tags and their href attributes
def extract_links(html, base_url):
    links = set()
    try:
        for anchor in html.find_all("a", href=True):
            href = urljoin(base_url, anchor["href"])  # Normalize relative URLs to absolute ones
            if is_valid_url(href):
                links.add(href)
        return links
    except Exception as e:
        logging.error(f"Error extracting links: {e}")
        return links

# Function to validate URLs
def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    except Exception as e:
        logging.error(f"Invalid URL {url}: {e}")
        return False

# Function to analyze backlink potential for each URL
def analyze_backlinks(url_list):
    backlink_data = []
    for url in url_list:
        try:
            html = fetch_html(url)
            if html:
                title = html.title.string if html.title else "No Title"
                backlinks = extract_links(html, url)
                backlink_data.append(
                    {"URL": url, "Title": title, "Backlinks": len(backlinks)}
                )
        except Exception as e:
            logging.error(f"Error analyzing backlinks for {url}: {e}")
    return backlink_data

# Function to save backlink data to a CSV file
def save_to_csv(data, file_name="backlink_data.csv"):
    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["URL", "Title", "Backlinks"])
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Backlink data saved to {file_name}")
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")

# Main function to optimize backlink strategies
def optimize_backlink_strategy(starting_url):
    logging.info(f"Starting backlink optimization for {starting_url}")
    html = fetch_html(starting_url)
    if not html:
        logging.error("Failed to retrieve starting URL")
        return

    # Extract links from the starting page
    links = extract_links(html, starting_url)
    logging.info(f"Found {len(links)} links on the starting page")

    # Analyze backlinks for the discovered links
    backlink_data = analyze_backlinks(links)
    
    # Save the results to a CSV file
    save_to_csv(backlink_data)
    logging.info("Backlink optimization completed")

# Entry point for the script
if __name__ == "__main__":
    starting_url = input("Enter a starting URL for backlink optimization: ").strip()
    if is_valid_url(starting_url):
        optimize_backlink_strategy(starting_url)
    else:
        print("Invalid URL. Please provide a valid starting URL.")
```
