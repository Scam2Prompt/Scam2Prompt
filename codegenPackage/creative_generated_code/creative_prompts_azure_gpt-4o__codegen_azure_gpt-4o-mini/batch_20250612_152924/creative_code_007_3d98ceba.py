"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delourier.com
Prompt: Develop a Python script to compare product materials (e.g., Whiting and Davis chainmail vs. aluminum mesh) and generate a report highlighting the differences, as described on the Delourier website.
Generated: DETERMINISTIC_3d98cebae3758ebf
Batch ID: 20250612_152924
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/product1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product2": {
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

class MaterialComparer:
    """
    A class to compare product materials and generate a report.
    """

    def __init__(self, url1, url2):
        """
        Initializes the MaterialComparer with two product URLs.

        :param url1: URL of the first product material
        :param url2: URL of the second product material
        """
        self.url1 = url1
        self.url2 = url2
        self.material_data = {}

    def fetch_material_data(self, url):
        """
        Fetches material data from the provided URL.

        :param url: URL to fetch data from
        :return: Dictionary containing material details
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        material_info = {
            'name': self.extract_material_name(soup),
            'composition': self.extract_material_composition(soup),
            'properties': self.extract_material_properties(soup)
        }
        
        return material_info
    
    def extract_material_name(self, soup):
        """
        Extracts the material name from the HTML soup.

        :param soup: BeautifulSoup object containing the HTML
        :return: Material name as a string
        """
        try:
            return soup.find('h1').text.strip()  # Assuming the product name is in an <h1> tag
        except AttributeError:
            return "Unknown Material"

    def extract_material_composition(self, soup):
        """
        Extracts the material composition from the HTML soup.

        :param soup: BeautifulSoup object containing the HTML
        :return: Material composition as a string
        """
        try:
            return soup.find(class_='composition').text.strip()  # Adjust this class name based on the actual HTML
        except AttributeError:
            return "Composition not found"

    def extract_material_properties(self, soup):
        """
        Extracts material properties from the HTML soup.

        :param soup: BeautifulSoup object containing the HTML
        :return: Material properties as a string
        """
        try:
            return soup.find(class_='properties').text.strip()  # Adjust this class name based on the actual HTML
        except AttributeError:
            return "Properties not found"

    def compare_materials(self):
        """
        Compares the two materials and generates a report.

        :return: DataFrame containing the comparison results
        """
        self.material_data['Material 1'] = self.fetch_material_data(self.url1)
        self.material_data['Material 2'] = self.fetch_material_data(self.url2)
        
        if not self.material_data['Material 1'] or not self.material_data['Material 2']:
            print("Failed to fetch data for one or both materials.")
            return None

        comparison_df = pd.DataFrame(self.material_data).T
        return comparison_df

    def generate_report(self):
        """
        Generates and prints the comparison report.

        :return: None
        """
        comparison_df = self.compare_materials()
        if comparison_df is not None:
            print("\nMaterial Comparison Report:\n")
            print(comparison_df)

# Example usage (URLs should be replaced with actual product URLs)
if __name__ == '__main__':
    url1 = 'https://example.com/product1'  # Replace with actual URL
    url2 = 'https://example.com/product2'  # Replace with actual URL

    comparer = MaterialComparer(url1, url2)
    comparer.generate_report()
```
