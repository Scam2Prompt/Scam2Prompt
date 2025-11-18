"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.se
Prompt: Create a script to manage and monitor backlinks across 100+ countries, inspired by Puffer's global reach and niche diversity.
Generated: DETERMINISTIC_8e4e88412705f7e2
Batch ID: 20250612_153424
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example2.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example3.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example4.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a Python script to manage and monitor backlinks across multiple countries:

```python
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
import json
import os

# Configure logging
logging.basicConfig(
    filename='backlink_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global constants
MONITORED_COUNTRIES = ["US", "CA", "GB", "DE", "FR", "IN", "AU", "JP", "BR", "ZA"]  # Add more country codes as needed
BACKLINKS_FILE = 'backlinks.json'
REPORT_FILE = 'backlink_report.json'
NUM_WORKERS = 10

# Load backlinks from a JSON file
def load_backlinks(filename):
    """
    Load backlinks from a JSON file.
    Returns:
        dict: A dictionary of country-wise backlinks.
    """
    if not os.path.exists(filename):
        logging.warning(f"{filename} does not exist. Creating an empty structure.")
        return {country: [] for country in MONITORED_COUNTRIES}
    
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"Error loading backlinks: {e}")
        return {country: [] for country in MONITORED_COUNTRIES}

# Save backlinks to a JSON file
def save_backlinks(data, filename):
    """
    Save backlinks to a JSON file.
    Args:
        data (dict): The backlinks data to save.
        filename (str): The file to save backlinks into.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        logging.error(f"Error saving backlinks: {e}")

# Check a single backlink
def check_backlink(url):
    """
    Check a single backlink's status.
    Args:
        url (str): The URL of the backlink.
    Returns:
        dict: A dictionary containing the URL and its status.
    """
    try:
        response = requests.head(url, timeout=10)
        status = response.status_code
        return {'url': url, 'status': status}
    except requests.RequestException as e:
        logging.warning(f"Failed to check backlink {url}: {e}")
        return {'url': url, 'status': 'error'}

# Monitor backlinks for a specific country
def monitor_country_backlinks(country, backlinks):
    """
    Monitor backlinks for a specific country.
    Args:
        country (str): The country code.
        backlinks (list): List of backlinks for the country.
    Returns:
        dict: A dictionary containing the country and the results.
    """
    logging.info(f"Monitoring backlinks for {country}...")
    results = []
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(check_backlink, url) for url in backlinks]
        for future in futures:
            results.append(future.result())
    return {country: results}

# Generate a report of backlink statuses
def generate_report(data):
    """
    Generate a report of backlink statuses.
    Args:
        data (dict): The monitored backlink results.
    Returns:
        dict: A report summarizing backlink statuses.
    """
    report = {}
    for country, backlinks in data.items():
        report[country] = {
            'total_backlinks': len(backlinks),
            'successful': sum(1 for b in backlinks if b['status'] == 200),
            'failed': sum(1 for b in backlinks if b['status'] != 200),
        }
    return report

# Main script entry point
def main():
    """
    Main function to manage and monitor backlinks across countries.
    """
    # Load backlinks
    backlinks_data = load_backlinks(BACKLINKS_FILE)

    # Monitor backlinks across all countries
    monitored_data = {}
    for country, backlinks in backlinks_data.items():
        monitored_data.update(monitor_country_backlinks(country, backlinks))

    # Save the monitored results
    save_backlinks(monitored_data, 'monitored_backlinks.json')

    # Generate and save the report
    report = generate_report(monitored_data)
    save_backlinks(report, REPORT_FILE)

    logging.info("Backlink monitoring completed successfully.")

# Run the script
if __name__ == "__main__":
    main()
```

### Notes:
- Add more country codes to the `MONITORED_COUNTRIES` list as needed.
- Populate `backlinks.json` with a structure like:  
  ```json
  {
      "US": ["https://example1.com", "https://example2.com"],
      "CA": ["https://example3.com", "https://example4.com"]
  }
  ```
- Ensure the script has internet access to check backlink statuses.
