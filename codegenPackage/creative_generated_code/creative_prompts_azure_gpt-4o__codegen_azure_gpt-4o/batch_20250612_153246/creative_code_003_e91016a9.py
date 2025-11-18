"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Write a Python script to scrape product data from Marine Kiosk's webpage, including details of "Lost Mary QM600" vape flavors and "A. Le Coq" cocktails, and store them in a structured JSON format.
Generated: DETERMINISTIC_e91016a97771900d
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://marinekiosk.example.com": {
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

def fetch_webpage(url):
    """
    Fetch the HTML content of the given webpage.
    Args:
        url (str): URL of the webpage to fetch.
    Returns:
        str: HTML content of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def parse_product_data(html_content):
    """
    Parse product details for "Lost Mary QM600" and "A. Le Coq" from the HTML content.
    Args:
        html_content (str): HTML content of the webpage.
    Returns:
        dict: A dictionary containing product data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    product_data = {
        "Lost Mary QM600": [],
        "A. Le Coq": []
    }

    # Extract Lost Mary QM600 flavors
    lost_mary_section = soup.find('div', id='lost-mary-qm600')  # Adjust selector as needed
    if lost_mary_section:
        flavors = lost_mary_section.find_all('div', class_='flavor-item')  # Adjust selector as needed
        for flavor in flavors:
            flavor_name = flavor.find('h3').text.strip()
            description = flavor.find('p').text.strip()
            product_data["Lost Mary QM600"].append({
                "Flavor": flavor_name,
                "Description": description
            })

    # Extract A. Le Coq cocktails
    le_coq_section = soup.find('div', id='a-le-coq')  # Adjust selector as needed
    if le_coq_section:
        cocktails = le_coq_section.find_all('div', class_='cocktail-item')  # Adjust selector as needed
        for cocktail in cocktails:
            cocktail_name = cocktail.find('h3').text.strip()
            description = cocktail.find('p').text.strip()
            product_data["A. Le Coq"].append({
                "Cocktail": cocktail_name,
                "Description": description
            })

    return product_data

def save_to_json(data, filename):
    """
    Save the structured data to a JSON file.
    Args:
        data (dict): The data to save.
        filename (str): File name for the JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving data to JSON file: {e}")

def main():
    """
    Main function to scrape product data and save it in JSON format.
    """
    url = 'https://marinekiosk.example.com'  # Replace with the actual webpage URL
    html_content = fetch_webpage(url)

    if html_content:
        product_data = parse_product_data(html_content)
        save_to_json(product_data, 'product_data.json')
        print("Product data has been successfully saved to 'product_data.json'.")
    else:
        print("Failed to retrieve the webpage content.")

if __name__ == "__main__":
    main()
```

Note: You need to update the `url` and the HTML element selectors (`id` and `class` attributes) based on the actual structure of Marine Kiosk's webpage to ensure accurate scraping.
