"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Create a web scraping script in Python to extract health insurance plan details from a website like Health Insurance Shop, ensuring compliance with GDPR regulations.
Generated: DETERMINISTIC_e44204494780d762
Batch ID: 20250612_154820
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/health-insurance-shop": {
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
import logging
from datetime import datetime

# Configure logging for debugging and error handling
logging.basicConfig(
    filename="health_insurance_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# User-agent header to mimic a browser request (important for GDPR compliance)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Base URL of the target website
BASE_URL = "https://www.example.com/health-insurance-shop"

def fetch_page(url):
    """
    Fetches the web page content using the provided URL.
    Includes error handling for HTTP requests.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

def parse_plan_details(html_content):
    """
    Parses the HTML content to extract health insurance plan details.
    Returns a list of dictionaries containing plan data.
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        plans = []
        
        # Example: Assuming plans are in a div with class `plan-card`
        plan_cards = soup.find_all("div", class_="plan-card")
        
        for card in plan_cards:
            plan = {
                "name": card.find("h2", class_="plan-name").get_text(strip=True),
                "price": card.find("span", class_="plan-price").get_text(strip=True),
                "coverage": card.find("p", class_="plan-coverage").get_text(strip=True),
            }
            plans.append(plan)
        
        return plans
    except Exception as e:
        logging.error(f"Error parsing HTML content: {e}")
        return []

def save_to_json(data, file_name):
    """
    Saves the extracted data into a JSON file.
    """
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data successfully saved to {file_name}")
    except Exception as e:
        logging.error(f"Error saving data to JSON file: {e}")

def main():
    """
    Main function to orchestrate the web scraping process.
    Ensures compliance with GDPR by not collecting sensitive user data.
    """
    logging.info("Starting web scraping script...")
    
    # Fetch HTML content from the website
    html_content = fetch_page(BASE_URL)
    
    if not html_content:
        logging.error("Failed to retrieve HTML content. Exiting...")
        return
    
    # Extract health insurance plan details
    plans = parse_plan_details(html_content)
    
    if not plans:
        logging.warning("No plans found. Exiting...")
        return
    
    # Save extracted data to JSON file
    file_name = f"health_insurance_plans_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_to_json(plans, file_name)
    
    logging.info("Web scraping script completed successfully.")

if __name__ == "__main__":
    main()
```
