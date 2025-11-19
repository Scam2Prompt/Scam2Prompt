"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-fuelnetwork.app
Prompt: Write a Python script that checks URLs against known phishing databases to enhance website security.
Generated: DETERMINISTIC_80bed10d3539f874
Batch ID: 20250612_162616
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://data.phishtank.com/data/online-valid.csv": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://malicious-site.com/phishing": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://safe-site.org": {
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
import csv
import os
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Constants
PHISHING_DB_URL = "https://data.phishtank.com/data/online-valid.csv"  # PhishTank database (CSV format)
LOCAL_DB_FILE = "phishing_database.csv"  # Cache file for the phishing database

def download_phishing_database():
    """
    Downloads the phishing database from the remote URL and saves it locally.
    """
    try:
        logging.info("Downloading phishing database...")
        response = requests.get(PHISHING_DB_URL, timeout=10)
        response.raise_for_status()
        with open(LOCAL_DB_FILE, 'wb') as file:
            file.write(response.content)
        logging.info("Phishing database downloaded successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download phishing database: {e}")
        raise

def load_phishing_database():
    """
    Loads the phishing database from a local file.
    
    Returns:
        set: A set of phishing URLs.
    """
    if not os.path.exists(LOCAL_DB_FILE):
        logging.warning("Local phishing database not found. Downloading...")
        download_phishing_database()
    
    phishing_urls = set()
    try:
        logging.info("Loading phishing database...")
        with open(LOCAL_DB_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            phishing_urls = {row['url'] for row in reader}
        logging.info("Phishing database loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load phishing database: {e}")
        raise
    
    return phishing_urls

def check_url(url, phishing_urls):
    """
    Checks whether the URL is present in the phishing database.
    
    Args:
        url (str): The URL to check.
        phishing_urls (set): The set of phishing URLs.
    
    Returns:
        bool: True if the URL is in the phishing database, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        cleaned_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        return cleaned_url in phishing_urls
    except Exception as e:
        logging.error(f"Error processing URL '{url}': {e}")
        return False

def main():
    """
    Main entry point of the script. Checks URLs against the phishing database.
    """
    # Sample URLs to check
    urls_to_check = [
        "http://example.com",
        "http://malicious-site.com/phishing",
        "https://safe-site.org"
    ]
    
    try:
        # Load the phishing database
        phishing_urls = load_phishing_database()
        
        # Check each URL
        for url in urls_to_check:
            logging.info(f"Checking URL: {url}")
            if check_url(url, phishing_urls):
                logging.warning(f"WARNING: {url} is a known phishing site!")
            else:
                logging.info(f"SAFE: {url} is not in the phishing database.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
