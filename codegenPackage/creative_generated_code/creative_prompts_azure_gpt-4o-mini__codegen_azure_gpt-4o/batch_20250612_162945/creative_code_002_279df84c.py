"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinburstfire.blogspot.com
Prompt: Create a code snippet that interacts with a shoe inventory API to filter and display options for running shoes and sandals, inspired by the categories listed on the Poocoin Burst Fire website.
Generated: DETERMINISTIC_279df84cbe7014c8
Batch ID: 20250612_162945
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.shoeinventory.com/v1/shoes`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.shoeinventory.com/v1/shoes": {
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

# Define the base URL for the shoe inventory API
API_BASE_URL = "https://api.shoeinventory.com/v1/shoes"

# Function to fetch shoes from the API
def fetch_shoes():
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Parse the JSON response
    except requests.exceptions.RequestException as e:
        # Log and handle any request-related errors
        print(f"Error fetching shoe data: {e}")
        return []

# Function to filter shoes by category
def filter_shoes_by_category(shoes, category):
    """
    Filters the shoe list based on the specified category.

    :param shoes: List of shoe data returned from the API.
    :param category: Category to filter by (e.g., "Running Shoes", "Sandals").
    :return: Filtered list of shoes.
    """
    return [shoe for shoe in shoes if shoe.get('category') == category]

# Function to display shoe options
def display_shoes(shoes):
    """
    Formats and prints the shoe information.

    :param shoes: List of shoe data.
    """
    if not shoes:
        print("No shoes found in the specified category.")
        return

    print(f"{'Brand':<15} {'Model':<20} {'Price':<10} {'Stock':<10}")
    print("=" * 60)
    for shoe in shoes:
        brand = shoe.get('brand', 'N/A')
        model = shoe.get('model', 'N/A')
        price = shoe.get('price', 'N/A')
        stock = shoe.get('stock', 'N/A')
        print(f"{brand:<15} {model:<20} ${price:<10} {stock:<10}")

# Main function to execute the program flow
def main():
    print("Fetching shoe inventory...")
    shoes = fetch_shoes()

    # Filter and display running shoes
    print("\nRunning Shoes:")
    running_shoes = filter_shoes_by_category(shoes, "Running Shoes")
    display_shoes(running_shoes)

    # Filter and display sandals
    print("\nSandals:")
    sandals = filter_shoes_by_category(shoes, "Sandals")
    display_shoes(sandals)

# Entry point for the script
if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `https://api.shoeinventory.com/v1/shoes` with the actual URL of the shoe inventory API.
2. Ensure the API provides the necessary fields (`category`, `brand`, `model`, `price`, `stock`) in the response JSON.
3. Install the `requests` library if it's not already available (`pip install requests`).
