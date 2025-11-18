"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a script to filter and display dental instruments by their product codes (e.g., 2312-2321, 1557-1575) as listed on the Curative Surgical Industry website.
Generated: DETERMINISTIC_fbd306431531d5b8
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.curativesurgical.com/dental-instruments": {
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

# Constants
BASE_URL = 'https://api.curativesurgical.com/dental-instruments'  # Example API endpoint

def get_dental_instruments():
    """
    Fetches the list of dental instruments from the API.

    Returns:
        list: A list of dental instruments or an empty list if an error occurs.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Assuming the API returns a JSON response with a "products" key
        return response.json().get('products', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching dental instruments: {e}")
        return []

def filter_instruments_by_code(instruments, code_range):
    """
    Filters the list of dental instruments by the specified product code range.

    Args:
        instruments (list): The list of dental instruments.
        code_range (str): A string representing the product code range (e.g., "2312-2321").

    Returns:
        list: A list of filtered dental instruments.
    """
    start_code, end_code = map(int, code_range.split('-'))  # Split the range and convert to integers
    filtered_instruments = [
        instrument for instrument in instruments
        if start_code <= int(instrument['product_code']) <= end_code
    ]
    return filtered_instruments

def display_instruments(instruments):
    """
    Displays the filtered dental instruments.

    Args:
        instruments (list): The list of dental instruments to display.
    """
    if not instruments:
        print("No instruments found for the specified code range.")
        return

    print("Filtered Dental Instruments:")
    for instrument in instruments:
        print(f"- Product Code: {instrument['product_code']}, Name: {instrument['name']}")

def main():
    """
    Main function to execute the script logic.
    """
    # Get the list of dental instruments
    instruments = get_dental_instruments()

    # Define the product code range for filtering
    code_range = "1557-1575"  # Example code range provided by the user

    # Filter instruments based on the provided range
    filtered_instruments = filter_instruments_by_code(instruments, code_range)

    # Display the filtered instruments
    display_instruments(filtered_instruments)

if __name__ == "__main__":
    main()
```
