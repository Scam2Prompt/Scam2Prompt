"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Write Python code to scrape vehicle data (model, year, mileage, fuel type, and price) from a webpage like the one on Helfen Motors and store it in a CSV file.
Generated: DETERMINISTIC_27a2b6738568289a
Batch ID: 20250612_151408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.helfenmotors.com/vehicles": {
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

def fetch_vehicle_data(url):
    """
    Fetch vehicle data from the given URL and return a list of dictionaries.

    Parameters:
    url (str): The URL of the webpage to scrape.

    Returns:
    list: A list of dictionaries containing vehicle data.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize a list to hold the vehicle data
        vehicles = []

        # Assuming the vehicle data is contained in a table, replace 'table-selector' with the actual selector
        vehicle_rows = soup.select('table-selector tr')  # Update this selector accordingly

        for row in vehicle_rows[1:]:  # Skip header row
            columns = row.find_all('td')
            if len(columns) >= 5:  # Ensure the row has enough columns
                vehicle_data = {
                    'Model': columns[0].text.strip(),
                    'Year': columns[1].text.strip(),
                    'Mileage': columns[2].text.strip(),
                    'Fuel Type': columns[3].text.strip(),
                    'Price': columns[4].text.strip()
                }
                vehicles.append(vehicle_data)

        return vehicles

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def save_to_csv(data, filename):
    """
    Save the vehicle data to a CSV file.

    Parameters:
    data (list): A list of dictionaries containing vehicle data.
    filename (str): The name of the CSV file to save the data.
    """
    try:
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def main():
    """
    Main function to execute the vehicle data scraping and saving process.
    """
    url = 'https://www.helfenmotors.com/vehicles'  # Replace with the actual URL
    filename = 'vehicles_data.csv'

    # Fetch vehicle data
    vehicle_data = fetch_vehicle_data(url)

    # Save the fetched data to a CSV file
    if vehicle_data:
        save_to_csv(vehicle_data, filename)

if __name__ == "__main__":
    main()
```
