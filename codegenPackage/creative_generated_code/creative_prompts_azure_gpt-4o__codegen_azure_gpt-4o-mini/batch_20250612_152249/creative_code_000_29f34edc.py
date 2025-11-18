"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Write a Python script to scrape contact information and service details from the Budi Bromo Tour website for jeep rentals and homestay accommodations.
Generated: DETERMINISTIC_29f34edcd13224ee
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://budi-bromo-tour-website-url.com": {
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

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_webpage(url):
    """
    Fetch the content of the webpage at the specified URL.

    :param url: The URL of the webpage to scrape.
    :return: The HTML content of the webpage, or None if an error occurred.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def scrape_contact_info(soup):
    """
    Scrape contact information from the BeautifulSoup object.

    :param soup: A BeautifulSoup object representing the webpage's HTML.
    :return: A dictionary containing contact information.
    """
    contact_info = {}
    
    # Example selectors - these would need to be adjusted based on actual HTML structure
    contact_section = soup.find('div', class_='contact-info')
    if contact_section:
        phone = contact_section.find('span', class_='phone').text.strip()
        email = contact_section.find('span', class_='email').text.strip()
        contact_info['phone'] = phone
        contact_info['email'] = email
    else:
        logging.warning("Contact section not found on the page.")
    
    return contact_info

def scrape_service_details(soup):
    """
    Scrape service details for jeep rentals and homestay from the BeautifulSoup object.

    :param soup: A BeautifulSoup object representing the webpage's HTML.
    :return: A list of dictionaries containing service details.
    """
    services = []
    
    # Example selectors - these would need to be adjusted based on actual HTML structure
    services_section = soup.find_all('div', class_='service-item')
    for service in services_section:
        service_name = service.find('h3').text.strip()
        service_details = service.find('p').text.strip()
        
        services.append({
            'name': service_name,
            'details': service_details
        })
        
    if not services:
        logging.warning("No services found on the page.")
    
    return services

def main():
    url = 'https://budi-bromo-tour-website-url.com'  # Replace with the actual URL
    
    # Fetch webpage content
    html_content = fetch_webpage(url)
    if html_content is None:
        logging.error("Failed to retrieve webpage content.")
        return
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Scrape contact information
    contact_info = scrape_contact_info(soup)
    logging.info(f"Contact Information: {contact_info}")

    # Scrape service details
    service_details = scrape_service_details(soup)
    logging.info(f"Service Details: {service_details}")

if __name__ == "__main__":
    main()
```
