"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: Write a Python script that connects to an API for recycling services, focusing on ferrous and non-ferrous metals as described by SCR Reciclados.
Generated: DETERMINISTIC_c022e7ffe4c5130c
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.scrreciclados.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RecyclingAPI:
    """
    A class to interact with the SCR Reciclados API for recycling services.
    """

    def __init__(self, base_url):
        """
        Initializes the RecyclingAPI with the base URL of the API.

        :param base_url: The base URL for the recycling services API.
        """
        self.base_url = base_url

    def get_metal_recycling_info(self, metal_type):
        """
        Fetches recycling information for the specified type of metal.

        :param metal_type: The type of metal to query ('ferrous' or 'non-ferrous').
        :return: JSON response containing recycling information.
        :raises ValueError: If the metal_type is not valid.
        :raises Exception: For any other errors during the API request.
        """
        if metal_type not in ['ferrous', 'non-ferrous']:
            raise ValueError("Invalid metal type. Choose 'ferrous' or 'non-ferrous'.")

        url = f"{self.base_url}/recycling/{metal_type}"
        logging.info(f"Requesting recycling info for {metal_type} metals from {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Successfully retrieved data for {metal_type} metals.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

def main():
    """
    Main function to execute the recycling API interaction.
    """
    base_url = "https://api.scrreciclados.com"  # Replace with the actual API base URL
    recycling_api = RecyclingAPI(base_url)

    # Example usage: Fetching information for ferrous metals
    try:
        ferrous_info = recycling_api.get_metal_recycling_info('ferrous')
        logging.info(f"Ferrous Metals Recycling Info: {ferrous_info}")

        # Fetching information for non-ferrous metals
        non_ferrous_info = recycling_api.get_metal_recycling_info('non-ferrous')
        logging.info(f"Non-Ferrous Metals Recycling Info: {non_ferrous_info}")

    except ValueError as ve:
        logging.error(f"Value error: {ve}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
