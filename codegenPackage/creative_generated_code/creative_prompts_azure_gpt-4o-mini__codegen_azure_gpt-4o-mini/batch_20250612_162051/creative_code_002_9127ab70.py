"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Create a Python script that scrapes the Navkar Furniture website to collect information about their office furniture offerings.
Generated: DETERMINISTIC_9127ab703c2aaba7
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://navkarfurniture.com/office-furniture": {
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

# Define the URL of the Navkar Furniture website
URL = "https://navkarfurniture.com/office-furniture"

def fetch_page(url):
    """
    Fetch the HTML content of the given URL.
    
    Args:
        url (str): The URL to fetch.
    
    Returns:
        BeautifulSoup: Parsed HTML of the page.
    
    Raises:
        HTTPError: If the HTTP request returns an unsuccessful status code.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.content, 'html.parser')
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Print any other errors

def parse_office_furniture(soup):
    """
    Parse the office furniture information from the BeautifulSoup object.
    
    Args:
        soup (BeautifulSoup): Parsed HTML of the office furniture page.
    
    Returns:
        list: A list of dictionaries containing furniture details.
    """
    furniture_list = []

    # Locate the furniture items on the page
    items = soup.find_all('div', class_='furniture-item')
    
    for item in items:
        # Extract relevant details for each piece of furniture
        name = item.find('h3', class_='furniture-name').get_text(strip=True)
        price = item.find('span', class_='furniture-price').get_text(strip=True)
        description = item.find('p', class_='furniture-description').get_text(strip=True)

        furniture_list.append({
            'Name': name,
            'Price': price,
            'Description': description
        })
    
    return furniture_list

def save_to_csv(data, filename='office_furniture.csv'):
    """
    Save the scraped data to a CSV file.
    
    Args:
        data (list): List of dictionaries containing furniture details.
        filename (str): The name of the file to save data into.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data saved to {filename}")

def main():
    """
    Main function to orchestrate the web scraping process.
    """
    # Fetch the page content
    soup = fetch_page(URL)
    if soup:
        # Parse the office furniture details
        furniture_data = parse_office_furniture(soup)
        
        if furniture_data:
            # Save the data to a CSV file
            save_to_csv(furniture_data)
        else:
            print("No furniture data found.")
    else:
        print("Failed to retrieve the webpage.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

This Python script will scrape the Navkar Furniture website for office furniture offerings, parse the relevant data, and save it to a CSV file. Make sure you have the `requests`, `BeautifulSoup`, and `pandas` libraries installed for this script to run successfully.
