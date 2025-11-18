"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to filter tire products by width, height, and rim size, as described on the "Dal Cortivo Pneus" website, and display the filtered results.
Generated: DETERMINISTIC_1e7e0fdeeee3bb8e
Batch ID: 20250612_151334
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dalcortivopneus.com/tire-products": {
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

class TireFilter:
    """A class to filter tire products by width, height, and rim size."""

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_tires(self):
        """Fetch tire products from the external API."""
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is in JSON format
        except requests.RequestException as e:
            print(f"Error fetching tire products: {e}")
            return []

    def filter_tires(self, tires, width=None, height=None, rim_size=None):
        """
        Filter the list of tires by width, height, and rim size.

        :param tires: A list of tire products.
        :param width: Desired tire width (optional).
        :param height: Desired tire height (optional).
        :param rim_size: Desired rim size (optional).
        :return: A list of filtered tire products.
        """
        filtered_tires = []
        for tire in tires:
            if (width is not None and tire['width'] != width) or \
               (height is not None and tire['height'] != height) or \
               (rim_size is not None and tire['rim_size'] != rim_size):
                continue
            filtered_tires.append(tire)
        return filtered_tires

    def display_tires(self, tires):
        """Display the filtered list of tires."""
        if not tires:
            print("No tires found matching the criteria.")
            return
        
        print(f"{'Width':<10} {'Height':<10} {'Rim Size':<10} {'Brand':<15}")
        print('-' * 45)
        for tire in tires:
            print(f"{tire['width']:<10} {tire['height']:<10} {tire['rim_size']:<10} {tire['brand']:<15}")

def main():
    """Main function to execute the tire filtering."""
    base_url = "https://api.dalcortivopneus.com/tire-products"  # Placeholder URL
    tire_filter = TireFilter(base_url)

    # Fetch tire products from the API
    tires = tire_filter.fetch_tires()

    # Define filter criteria (these values can be modified or obtained from user input)
    width = 215  # Example width
    height = 60  # Example height
    rim_size = 16  # Example rim size

    # Filter tires based on criteria
    filtered_tires = tire_filter.filter_tires(tires, width, height, rim_size)

    # Display the filtered tire products
    tire_filter.display_tires(filtered_tires)

if __name__ == "__main__":
    main()
```
