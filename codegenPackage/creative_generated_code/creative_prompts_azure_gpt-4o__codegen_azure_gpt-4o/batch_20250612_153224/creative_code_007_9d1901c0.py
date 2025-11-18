"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Develop a script to implement a location-based property search feature that filters listings by neighborhoods or cities (e.g., Santa Marta, Villavicencio, Neiva), as seen on Félix Trujillo Falla's website.
Generated: DETERMINISTIC_9d1901c0a160ca47
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class PropertySearch:
    """
    A class to represent a location-based property search feature.
    """

    def __init__(self, properties_file):
        """
        Initializes the PropertySearch class with the properties data.
        
        Args:
            properties_file (str): Path to the JSON file containing property data.
        """
        self.properties_file = properties_file
        self.properties = self.load_properties()

    def load_properties(self):
        """
        Loads property data from a JSON file.
        
        Returns:
            list: List of property dictionaries.
            
        Raises:
            FileNotFoundError: If the specified JSON file is not found.
            json.JSONDecodeError: If the JSON file is not properly formatted.
        """
        try:
            with open(self.properties_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON - {e}")
            return []

    def search_by_location(self, location):
        """
        Filters properties based on the specified location (e.g., neighborhood or city).
        
        Args:
            location (str): The location to filter properties by.
        
        Returns:
            list: List of properties matching the specified location.
        """
        if not self.properties:
            print("Warning: No properties available to search.")
            return []

        # Filter properties matching the specified location
        filtered_properties = [
            property for property in self.properties if property.get("location", "").lower() == location.lower()
        ]
        return filtered_properties

    def display_properties(self, properties):
        """
        Displays the filtered properties in a readable format.
        
        Args:
            properties (list): List of property dictionaries to display.
        """
        if not properties:
            print("No properties found for the specified location.")
            return

        print(f"Found {len(properties)} properties:")
        for prop in properties:
            print(f"- {prop.get('name', 'Unnamed Property')} in {prop.get('location', 'Unknown Location')}")
            print(f"  Price: ${prop.get('price', 'N/A')} | Bedrooms: {prop.get('bedrooms', 'N/A')} | Bathrooms: {prop.get('bathrooms', 'N/A')}")
            print("")

# Main execution block
if __name__ == "__main__":
    # Specify the path to the properties data file
    properties_file = "properties.json"

    # Initialize PropertySearch with the data file
    search_tool = PropertySearch(properties_file)

    print("Welcome to the Property Search Tool!")
    user_location = input("Enter a neighborhood or city to filter properties: ")

    # Perform the search
    matching_properties = search_tool.search_by_location(user_location)

    # Display the results
    search_tool.display_properties(matching_properties)
```

### Notes:
1. The script assumes a JSON file named `properties.json` containing property data in the following format:
   ```json
   [
       {"name": "Property A", "location": "Santa Marta", "price": 120000, "bedrooms": 3, "bathrooms": 2},
       {"name": "Property B", "location": "Villavicencio", "price": 90000, "bedrooms": 2, "bathrooms": 1},
       {"name": "Property C", "location": "Neiva", "price": 150000, "bedrooms": 4, "bathrooms": 3}
   ]
   ```
2. Proper error handling has been incorporated for file loading and JSON decoding issues.
3. The script displays results in a clean and readable format.
4. Additional features can be added, such as sorting or filtering by price or number of bedrooms.
