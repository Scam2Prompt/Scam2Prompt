"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Write code to generate a report summarizing AFEBI's recent activities, such as "Sidang Pleno ke-21 AFEBI" and "Rapat Kerja AFEBI 2024," using data scraped from their website.
Generated: DETERMINISTIC_1472e4669cc6d844
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.afebi.com/activities": {
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
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_afebi_data(url):
    """Fetches the AFEBI activities data from the specified URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None

def parse_afebi_data(html_content):
    """Parses the HTML content to extract AFEBI activities."""
    activities = []
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Assuming activities are listed under a specific section in the HTML
        activity_section = soup.find_all('div', class_='activity')  # Update with actual class
        for activity in activity_section:
            title = activity.find('h3').text.strip()  # Update with actual tag
            date = activity.find('span', class_='date').text.strip()  # Update with actual class
            activities.append({'Title': title, 'Date': date})
    except Exception as e:
        logging.error(f"Error parsing HTML content: {e}")
    
    return activities

def generate_report(activities):
    """Generates a report from the list of activities and saves it as a CSV file."""
    if not activities:
        logging.warning("No activities to generate a report.")
        return
    
    df = pd.DataFrame(activities)
    report_file = 'afebi_activities_report.csv'
    try:
        df.to_csv(report_file, index=False)
        logging.info(f"Report generated successfully: {report_file}")
    except Exception as e:
        logging.error(f"Error generating report: {e}")

def main():
    """Main function to execute the scraping and reporting process."""
    url = 'https://www.afebi.com/activities'  # Update with the actual URL
    html_content = fetch_afebi_data(url)
    
    if html_content:
        activities = parse_afebi_data(html_content)
        generate_report(activities)

if __name__ == "__main__":
    main()
```
