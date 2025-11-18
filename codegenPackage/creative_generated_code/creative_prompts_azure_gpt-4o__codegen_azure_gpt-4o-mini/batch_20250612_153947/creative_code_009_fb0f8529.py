"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-invoice.com
Prompt: Create a script to export invoice details from Coinbase Commerce, including payment methods, status, and transaction IDs.
Generated: DETERMINISTIC_fb0f8529be2cf641
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.commerce.coinbase.com/invoices": {
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
import csv
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Coinbase Commerce API
API_URL = "https://api.commerce.coinbase.com/invoices"
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

def fetch_invoices():
    """
    Fetch invoices from Coinbase Commerce API.
    
    Returns:
        list: A list of invoices if the request is successful.
        None: If the request fails.
    """
    headers = {
        'X-CC-Api-Key': API_KEY,
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        invoices = response.json().get('data', [])
        logging.info(f"Successfully fetched {len(invoices)} invoices.")
        return invoices
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching invoices: {e}")
        return None

def export_invoices_to_csv(invoices, filename='invoices.csv'):
    """
    Export invoice details to a CSV file.
    
    Args:
        invoices (list): List of invoices to export.
        filename (str): Name of the output CSV file.
    """
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['id', 'amount', 'currency', 'status', 'payment_method']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write header to CSV
        for invoice in invoices:
            writer.writerow({
                'id': invoice.get('id'),
                'amount': invoice.get('amount'),
                'currency': invoice.get('currency'),
                'status': invoice.get('status'),
                'payment_method': invoice.get('payment_method', {}).get('type', 'N/A')
            })
        logging.info(f"Successfully exported invoices to {filename}.")

def main():
    """
    Main function to fetch and export invoice details.
    """
    invoices = fetch_invoices()
    if invoices is not None:
        export_invoices_to_csv(invoices)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `YOUR_API_KEY_HERE` with your actual Coinbase Commerce API key.
- This script fetches invoices from the Coinbase Commerce API and exports their details to a CSV file named `invoices.csv`.
- Proper error handling and logging are included to track the progress and any issues encountered while fetching or exporting the data.
