"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write a Python script that uses an API to track the status of refrigerated cargo shipments handled by a logistics company like OPC Operadora Portuaria del Caribe.
Generated: DETERMINISTIC_fff632e6191f5e2a
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opclogistics.com": {
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
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants for API configuration
API_BASE_URL = "https://api.opclogistics.com"  # Replace with the actual API base URL
API_ENDPOINT = "/shipments/status"  # Replace with the endpoint for tracking shipment status
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to fetch shipment status from the API
def fetch_shipment_status(shipment_ids: List[str]) -> Dict[str, Dict]:
    """
    Fetches the status of refrigerated cargo shipments from the API.

    Args:
        shipment_ids (List[str]): A list of shipment IDs to track.

    Returns:
        Dict[str, Dict]: A dictionary containing shipment statuses indexed by shipment IDs.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    try:
        logging.info("Sending API request to fetch shipment statuses...")
        response = requests.post(
            f"{API_BASE_URL}{API_ENDPOINT}",
            headers=headers,
            json={"shipment_ids": shipment_ids},
        )

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            logging.info("Received successful response from API.")
            return response.json()  # Parse and return the response JSON
        else:
            logging.error(f"API request failed with status code {response.status_code}: {response.text}")
            response.raise_for_status()  # Raise an exception for other error codes
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while making the API request: {e}")
        raise

# Function to display shipment statuses in a user-friendly format
def display_shipment_statuses(shipment_statuses: Dict[str, Dict]) -> None:
    """
    Displays the shipment statuses in a readable format.

    Args:
        shipment_statuses (Dict[str, Dict]): A dictionary containing shipment statuses indexed by shipment IDs.
    """
    if not shipment_statuses:
        logging.warning("No shipment statuses to display.")
        return

    logging.info("Displaying shipment statuses:")
    for shipment_id, status in shipment_statuses.items():
        print(f"Shipment ID: {shipment_id}")
        print(f"  Status: {status.get('status', 'Unknown')}")
        print(f"  Temperature: {status.get('temperature', 'Unavailable')}°C")
        print(f"  Location: {status.get('location', 'Unknown')}")
        print("-" * 40)

# Main function
def main():
    """
    Main entry point for the script.
    """
    # Example list of shipment IDs to track (replace with real shipment IDs)
    shipment_ids = ["SHIP12345", "SHIP67890", "SHIP54321"]

    try:
        # Fetch shipment statuses from the API
        shipment_statuses = fetch_shipment_status(shipment_ids)

        # Display the shipment statuses
        display_shipment_statuses(shipment_statuses)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
