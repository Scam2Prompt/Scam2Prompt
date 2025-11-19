"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: What are the key features of the Edon Pressure Washer available at Dotcom Machinery, and how can I use it effectively for home cleaning tasks?
Generated: DETERMINISTIC_f37208e9c0502e92
Batch ID: 20250612_162347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.dotcommachinery.com/edon-pressure-washer": {
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
"""
This script fetches key features of the Edon Pressure Washer from Dotcom Machinery's website
and provides a guide on how to use it effectively for home cleaning tasks.
"""

import requests  # To make HTTP requests
from bs4 import BeautifulSoup  # For web scraping
import sys  # For system-level error handling

# URL of the product page for the Edon Pressure Washer
PRODUCT_URL = "https://www.dotcommachinery.com/edon-pressure-washer"

def fetch_product_features(url):
    """
    Fetches the key features of the Edon Pressure Washer from the given URL.

    Args:
        url (str): URL of the product page.

    Returns:
        list: A list of key features if available, otherwise an empty list.

    Raises:
        requests.exceptions.RequestException: If there is an issue connecting to the URL.
    """
    try:
        # Make an HTTP GET request to fetch the product page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for a specific section containing product features
        features_section = soup.find("div", class_="product-features")
        if not features_section:
            print("Unable to locate the product features section on the page.")
            return []

        # Extract and return the features as a list
        features = [feature.text.strip() for feature in features_section.find_all("li")]
        return features
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Error fetching product features: {e}")
        sys.exit(1)  # Exit the script with an error code

def usage_guide():
    """
    Provides a usage guide for the Edon Pressure Washer.

    Returns:
        str: A guide on how to use the pressure washer effectively.
    """
    guide = (
        "How to Use the Edon Pressure Washer Effectively:\n"
        "1. Read the user manual carefully before using the pressure washer.\n"
        "2. Connect the machine to a stable water source and plug it into a power outlet.\n"
        "3. Choose the appropriate nozzle for the cleaning task.\n"
        "   - Wide nozzle: For general cleaning tasks.\n"
        "   - Narrow nozzle: For concentrated, tougher stains.\n"
        "4. Start with a low-pressure setting and gradually increase if necessary.\n"
        "5. Keep the nozzle at least 6 inches away from the surface to avoid damage.\n"
        "6. Use detergents compatible with the pressure washer for better results.\n"
        "7. After use, disconnect the machine, drain excess water, and store it in a dry location."
    )
    return guide

def main():
    """
    Main function to fetch product features and display the usage guide.
    """
    print("Fetching key features of the Edon Pressure Washer...\n")
    features = fetch_product_features(PRODUCT_URL)
    
    if features:
        print("Key Features:")
        for idx, feature in enumerate(features, start=1):
            print(f"{idx}. {feature}")
        print("\n")

    print("Usage Guide:")
    print(usage_guide())

# Entry point of the script
if __name__ == "__main__":
    main()
```
