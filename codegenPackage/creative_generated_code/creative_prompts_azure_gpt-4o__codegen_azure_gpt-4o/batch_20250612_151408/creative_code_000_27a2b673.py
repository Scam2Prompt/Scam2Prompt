"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Write Python code to scrape vehicle data (model, year, mileage, fuel type, and price) from a webpage like the one on Helfen Motors and store it in a CSV file.
Generated: DETERMINISTIC_27a2b6738568289a
Batch ID: 20250612_151408
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
import csv

def scrape_vehicle_data(url, output_csv_file):
    """
    Scrapes vehicle data from the given URL and stores it in a CSV file.

    Args:
        url (str): The URL of the webpage to scrape.
        output_csv_file (str): The path to the output CSV file.
    """
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find vehicle listings on the page
        vehicle_listings = soup.find_all('div', class_='vehicle-listing')  # Update class name based on actual site structure
        
        # Prepare data for CSV
        vehicle_data = []
        for listing in vehicle_listings:
            # Extract data from each listing
            model = listing.find('span', class_='model').get_text(strip=True)  # Update class name based on actual site structure
            year = listing.find('span', class_='year').get_text(strip=True)
            mileage = listing.find('span', class_='mileage').get_text(strip=True)
            fuel_type = listing.find('span', class_='fuel-type').get_text(strip=True)
            price = listing.find('span', class_='price').get_text(strip=True)
            
            # Append data to the list
            vehicle_data.append([model, year, mileage, fuel_type, price])
        
        # Write data to CSV
        with open(output_csv_file, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Write header row
            writer.writerow(['Model', 'Year', 'Mileage', 'Fuel Type', 'Price'])
            # Write data rows
            writer.writerows(vehicle_data)
        
        print(f"Data successfully scraped and saved to {output_csv_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == '__main__':
    # Replace 'URL_HERE' with the actual URL and 'output.csv' with desired output file name
    scrape_vehicle_data('URL_HERE', 'output.csv')
```
