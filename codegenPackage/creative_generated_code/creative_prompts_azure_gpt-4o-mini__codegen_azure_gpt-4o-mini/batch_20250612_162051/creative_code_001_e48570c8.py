"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casadelospastes.com
Prompt: Write a Python script that calculates the nutritional values of a paste based on the ingredients listed on the La Casa de los Pastes website.
Generated: DETERMINISTIC_e48570c8937f424a
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.lacasadelospastes.com/ingredients": {
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

class NutritionalCalculator:
    def __init__(self, url):
        """Initialize with the URL of the website containing ingredient information."""
        self.url = url
        self.ingredients_data = self.fetch_ingredients_data()
        self.nutritional_values = {}

    def fetch_ingredients_data(self):
        """Fetch the ingredient data from the provided URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.content, 'html.parser')
            # Parse the soup to extract ingredient information
            ingredients = self.parse_ingredients(soup)
            return ingredients
        except requests.RequestException as e:
            print(f"Error fetching ingredients data: {e}")
            return {}

    def parse_ingredients(self, soup):
        """Parse the ingredients from the BeautifulSoup object."""
        ingredients = {}
        # Assume the ingredients are in a specific HTML structure
        for item in soup.select('.ingredient-item'):
            name = item.select_one('.ingredient-name').get_text(strip=True)
            value = float(item.select_one('.ingredient-value').get_text(strip=True).replace('g', ''))
            ingredients[name] = value
        return ingredients

    def calculate_nutritional_values(self):
        """Calculate nutritional values based on ingredients."""
        # Placeholder: Replace with actual calculations based on nutritional data
        # Example calculation: sum up all ingredient values for demonstration purposes
        total_nutrition = sum(self.ingredients_data.values())
        self.nutritional_values['Total Weight (g)'] = total_nutrition
        # Add more nutritional calculations as needed

    def display_nutritional_values(self):
        """Display the calculated nutritional values."""
        if not self.nutritional_values:
            print("No nutritional values calculated.")
            return
        print("Nutritional Values:")
        for key, value in self.nutritional_values.items():
            print(f"{key}: {value}")

def main():
    """Main function to run the nutritional calculator."""
    url = "https://www.lacasadelospastes.com/ingredients"  # Example URL
    calculator = NutritionalCalculator(url)
    calculator.calculate_nutritional_values()
    calculator.display_nutritional_values()

if __name__ == "__main__":
    main()
```
