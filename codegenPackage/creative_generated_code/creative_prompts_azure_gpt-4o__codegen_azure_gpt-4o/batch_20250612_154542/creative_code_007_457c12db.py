"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularietyfinance.io
Prompt: Write a Python script to retrieve and display the conversion rates for SDAO, CGV, and KEY tokens to SFI from the Singularity Finance migration interface using web scraping or API calls.
Generated: DETERMINISTIC_457c12dbbf54f3a7
Batch ID: 20250612_154542
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.singularity.finance/v1/conversion-rates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.singularity.finance/v1/conversion-rates`": {
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

def fetch_conversion_rates():
    """
    Fetches conversion rates for SDAO, CGV, and KEY tokens to SFI 
    from the Singularity Finance migration interface using an API call.

    Returns:
        dict: A dictionary containing conversion rates for the tokens.
    """
    # Base API endpoint (replace this with the actual API endpoint from Singularity Finance)
    api_url = "https://api.singularity.finance/v1/conversion-rates"

    try:
        # Make a GET request to the API
        response = requests.get(api_url, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()

        # Extract conversion rates for specified tokens
        conversion_rates = {
            "SDAO_to_SFI": data.get("SDAO_to_SFI"),
            "CGV_to_SFI": data.get("CGV_to_SFI"),
            "KEY_to_SFI": data.get("KEY_to_SFI")
        }
        
        return conversion_rates

    except requests.exceptions.RequestException as e:
        # Log and handle any request errors
        print(f"Error fetching conversion rates: {e}")
        return None
    except KeyError as e:
        # Log and handle missing keys in the response
        print(f"Missing expected data in the response: {e}")
        return None


def display_conversion_rates(conversion_rates):
    """
    Displays conversion rates in a user-friendly format.

    Args:
        conversion_rates (dict): A dictionary containing the conversion rates.
    """
    if not conversion_rates:
        print("Unable to retrieve conversion rates. Please try again later.")
        return

    print("Conversion Rates:")
    for token, rate in conversion_rates.items():
        print(f"{token}: {rate}")


if __name__ == "__main__":
    # Fetch conversion rates
    rates = fetch_conversion_rates()

    # Display conversion rates
    display_conversion_rates(rates)
```

### Notes:
- Replace the placeholder API endpoint (`https://api.singularity.finance/v1/conversion-rates`) with the actual endpoint provided by Singularity Finance.
- Ensure that the API key or other authentication details (if required) are handled securely, e.g., via environment variables.
- Install the `requests` library if not already installed using `pip install requests`.
