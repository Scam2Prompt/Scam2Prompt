"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.predaiaarteenatura.eu
Prompt: Create a script to parse and organize the catalog data for different symposium editions (e.g., Edizione 2023, Edizione 2024) from the Predaia Arte e Natura website into a structured JSON format.
Generated: DETERMINISTIC_82ec2d2b91166ffb
Batch ID: 20250612_151539
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.predaiaarteenatura.com/catalogo/": {
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
import os

# Define the base URL for the symposium catalog
BASE_URL = "https://www.predaiaarteenatura.com/catalogo/"  # Placeholder URL

def fetch_catalog_data(year):
    """
    Fetches and parses catalog data for a specific symposium edition.

    Args:
        year (str): The year of the symposium edition.

    Returns:
        dict: A dictionary containing the parsed catalog data.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
    """
    url = f"{BASE_URL}{year}"
    response = requests.get(url)
    
    # Raise an exception for HTTP errors
    response.raise_for_status()
    
    # Parse the content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize a dictionary to hold the catalog data
    catalog_data = {
        "year": year,
        "exhibits": []
    }
    
    # Extract exhibit information (assuming there's a consistent HTML structure)
    exhibits = soup.find_all(class_="exhibit")  # Placeholder class name for exhibits
    for exhibit in exhibits:
        title = exhibit.find(class_="title").get_text(strip=True)  # Placeholder class name for title
        artist = exhibit.find(class_="artist").get_text(strip=True)  # Placeholder class name for artist
        description = exhibit.find(class_="description").get_text(strip=True)  # Placeholder class name for description
        
        # Append exhibit information to the catalog data
        catalog_data["exhibits"].append({
            "title": title,
            "artist": artist,
            "description": description
        })
    
    return catalog_data

def save_catalog_to_json(catalog_data, output_dir="catalogs"):
    """
    Saves the catalog data to a JSON file.

    Args:
        catalog_data (dict): The catalog data to be saved.
        output_dir (str): The directory where the JSON file will be saved.
    """
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    file_path = os.path.join(output_dir, f"catalog_{catalog_data['year']}.json")
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(catalog_data, json_file, ensure_ascii=False, indent=4)

def main():
    """
    Main function to execute the script.
    """
    years = ["2023", "2024"]  # List of years to fetch data for

    for year in years:
        try:
            # Fetch and save catalog data for each year
            catalog_data = fetch_catalog_data(year)
            save_catalog_to_json(catalog_data)
            print(f"Catalog data for {year} saved successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for year {year}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
