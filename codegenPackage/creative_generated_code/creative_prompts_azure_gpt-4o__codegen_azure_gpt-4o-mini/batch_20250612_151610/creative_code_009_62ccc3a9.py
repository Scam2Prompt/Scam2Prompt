"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Provide a Python function to calculate the power-to-weight ratio for Cummins diesel engines, using the horsepower data mentioned on the Indusur webpage.
Generated: DETERMINISTIC_62ccc3a967d5ee32
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/indusur": {
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

class EngineDataError(Exception):
    """Custom exception for errors related to engine data retrieval."""
    pass

def fetch_engine_horsepower(url):
    """
    Fetches horsepower data from the specified URL.

    Args:
        url (str): The URL to the webpage containing horsepower data.

    Returns:
        list: A list of horsepower values as floats.

    Raises:
        EngineDataError: If there is an error fetching or parsing the data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        # Assuming the webpage returns horsepower in a specific format,
        # this part would need to be customized based on the actual content of the webpage.
        horsepower_data = parse_horsepower_data(response.text)
        return horsepower_data
    except requests.RequestException as e:
        raise EngineDataError(f"Error fetching engine data: {e}")

def parse_horsepower_data(html_content):
    """
    Parses horsepower data from HTML content.

    Args:
        html_content (str): The HTML content of the webpage.

    Returns:
        list: A list of horsepower values as floats.
    """
    # This function needs custom implementation based on the actual HTML structure.
    # Placeholder implementation:
    horsepower_list = []  # Replace with actual parsing logic
    return horsepower_list

def calculate_power_to_weight_ratio(horsepower, weight):
    """
    Calculates the power-to-weight ratio.

    Args:
        horsepower (float): The horsepower of the engine.
        weight (float): The weight of the vehicle (in lbs).

    Returns:
        float: The power-to-weight ratio.

    Raises:
        ValueError: If weight is zero or negative.
    """
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    return horsepower / weight

def main():
    """
    Main function to execute the power-to-weight ratio calculation.
    """
    url = "https://example.com/indusur"  # Replace with the actual URL
    weight = 8000  # Placeholder for vehicle weight in lbs

    try:
        horsepower_values = fetch_engine_horsepower(url)
        for hp in horsepower_values:
            pwr_ratio = calculate_power_to_weight_ratio(hp, weight)
            print(f"Horsepower: {hp}, Weight: {weight}, Power-to-Weight Ratio: {pwr_ratio:.2f}")
    except EngineDataError as e:
        print(f"Failed to retrieve engine data: {e}")
    except ValueError as e:
        print(f"Error in power-to-weight calculation: {e}")

if __name__ == "__main__":
    main()
```
