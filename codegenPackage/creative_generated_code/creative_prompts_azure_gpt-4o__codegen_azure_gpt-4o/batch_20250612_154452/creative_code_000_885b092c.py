"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Write a Python script to integrate a retail management system (RMS) with electronic invoicing functionality, referencing the features described in TICOM Software's solutions for inventory control and barcode printing.
Generated: DETERMINISTIC_885b092c7ae284eb
Batch ID: 20250612_154452
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.electronic-invoice.com/v1/invoices": {
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
import sys
import json
import csv
import requests
from datetime import datetime

# Constants
API_ENDPOINT = "https://api.electronic-invoice.com/v1/invoices"
API_KEY = "your_api_key_here"
INVENTORY_FILE = "inventory.csv"  # Path to inventory CSV file
BARCODE_FILE = "barcodes.csv"  # Path to barcode CSV file

def load_inventory(file_path):
    """
    Load inventory data from a CSV file.
    
    :param file_path: Path to the inventory CSV file.
    :return: List of inventory items (as dictionaries).
    """
    try:
        inventory = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(row)
        return inventory
    except FileNotFoundError:
        print(f"Error: Inventory file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to load inventory file. {e}")
        sys.exit(1)

def load_barcodes(file_path):
    """
    Load barcode data from a CSV file.
    
    :param file_path: Path to the barcode CSV file.
    :return: Dictionary mapping product IDs to barcodes.
    """
    try:
        barcodes = {}
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                product_id, barcode = row
                barcodes[product_id] = barcode
        return barcodes
    except FileNotFoundError:
        print(f"Error: Barcode file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to load barcode file. {e}")
        sys.exit(1)

def create_invoice(customer_name, items):
    """
    Create an electronic invoice payload for submission.

    :param customer_name: Name of the customer.
    :param items: List of items purchased (as dictionaries).
    :return: JSON payload for the invoice.
    """
    invoice_id = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"  # Unique invoice ID
    total_amount = sum(float(item['price']) * int(item['quantity']) for item in items)
    
    return {
        "invoice_id": invoice_id,
        "customer_name": customer_name,
        "date": datetime.now().isoformat(),
        "items": items,
        "total_amount": total_amount
    }

def send_invoice(invoice_data):
    """
    Submit the electronic invoice to the external API.

    :param invoice_data: JSON payload for the invoice.
    """
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        response = requests.post(API_ENDPOINT, json=invoice_data, headers=headers)
        if response.status_code == 200:
            print("Invoice submitted successfully.")
        else:
            print(f"Error: Failed to submit invoice. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.RequestException as e:
        print(f"Error: An exception occurred while submitting the invoice. {e}")
        sys.exit(1)

def integrate_rms_with_e_invoicing():
    """
    Main function to integrate RMS with electronic invoicing functionality.
    """
    # Load inventory and barcode data
    inventory = load_inventory(INVENTORY_FILE)
    barcodes = load_barcodes(BARCODE_FILE)

    # Print inventory and barcodes (for debugging purposes)
    print("Inventory loaded:")
    print(json.dumps(inventory, indent=4))
    print("\nBarcodes loaded:")
    print(json.dumps(barcodes, indent=4))

    # Simulate a user purchase (this would be dynamic in a real system)
    purchased_items = [
        {
            "product_id": inventory[0]["product_id"],
            "name": inventory[0]["name"],
            "barcode": barcodes.get(inventory[0]["product_id"], "N/A"),
            "quantity": 2,  # Example quantity
            "price": inventory[0]["price"]
        }
    ]
    customer_name = "John Doe"

    # Generate and send invoice
    invoice_data = create_invoice(customer_name, purchased_items)
    print("\nGenerated Invoice:")
    print(json.dumps(invoice_data, indent=4))
    
    send_invoice(invoice_data)

if __name__ == "__main__":
    integrate_rms_with_e_invoicing()
```
