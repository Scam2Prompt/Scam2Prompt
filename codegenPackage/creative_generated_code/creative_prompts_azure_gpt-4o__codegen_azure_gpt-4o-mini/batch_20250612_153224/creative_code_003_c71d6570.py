"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Generate a Python script to query and filter properties by type, neighborhood, and price range, mimicking the search functionality described in the "Buscar Propietarios Arrendatarios Consignación" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_c71d6570b4187352
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nuevaciudad.com/properties": {
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

class PropertyQuery:
    """Class to query and filter properties by type, neighborhood, and price range."""

    BASE_URL = "https://api.nuevaciudad.com/properties"  # Example API endpoint

    def __init__(self):
        """Initializes the PropertyQuery class."""
        self.properties = []

    def fetch_properties(self):
        """Fetches properties from the API and handles errors gracefully."""
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            self.properties = response.json()  # Assume the API returns JSON
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

    def filter_properties(self, property_type=None, neighborhood=None, min_price=None, max_price=None):
        """Filters properties based on given criteria.

        Args:
            property_type (str): The type of property (e.g., 'Apartment', 'House').
            neighborhood (str): The neighborhood to filter by.
            min_price (float): Minimum price for filtering.
            max_price (float): Maximum price for filtering.

        Returns:
            list: A list of filtered properties.
        """
        filtered_properties = self.properties
        
        if property_type:
            filtered_properties = [prop for prop in filtered_properties if prop.get('type') == property_type]
        
        if neighborhood:
            filtered_properties = [prop for prop in filtered_properties if prop.get('neighborhood') == neighborhood]
        
        if min_price is not None:
            filtered_properties = [prop for prop in filtered_properties if prop.get('price', 0) >= min_price]
        
        if max_price is not None:
            filtered_properties = [prop for prop in filtered_properties if prop.get('price', float('inf')) <= max_price]

        return filtered_properties

def main():
    """Main function to run the property query."""
    query = PropertyQuery()
    query.fetch_properties()

    # Example filtering criteria; these can be dynamically set
    property_type = "Apartment"
    neighborhood = "Downtown"
    min_price = 100000
    max_price = 300000

    filtered_results = query.filter_properties(property_type, neighborhood, min_price, max_price)

    # Display the filtered properties
    if filtered_results:
        print("Filtered Properties:")
        for property in filtered_results:
            print(f"- {property['name']} in {property['neighborhood']} for ${property['price']}")
    else:
        print("No properties found matching the criteria.")

if __name__ == "__main__":
    main()
```
