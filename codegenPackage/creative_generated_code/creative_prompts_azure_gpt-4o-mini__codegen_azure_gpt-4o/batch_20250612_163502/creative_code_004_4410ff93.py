"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tess-9x2.pages.dev
Prompt: Generate a sample script for tracking transactions and automating tax withholdings with Magna's platform.
Generated: DETERMINISTIC_4410ff93319b3736
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for tracking transactions and automating tax withholdings using Magna's platform.

Assumptions:
- Magna's platform provides an API for transaction tracking and tax calculations.
- API credentials are securely stored in environment variables.
- This script uses Python's `requests` library for API communication.
"""

import os
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API credentials from environment variables
MAGNA_API_KEY = os.getenv("MAGNA_API_KEY")
MAGNA_API_BASE_URL = os.getenv("MAGNA_API_BASE_URL")

if not MAGNA_API_KEY or not MAGNA_API_BASE_URL:
    raise EnvironmentError("Missing required API credentials. Ensure MAGNA_API_KEY and MAGNA_API_BASE_URL are set.")

# Function to fetch transactions from Magna's API
def fetch_transactions():
    """Fetch recent transactions from Magna's platform."""
    url = f"{MAGNA_API_BASE_URL}/transactions"
    headers = {
        "Authorization": f"Bearer {MAGNA_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return parsed JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch transactions: {e}")
        raise

# Function to calculate tax withholding for a transaction
def calculate_tax(transaction):
    """
    Calculate tax withholding for a given transaction using Magna's platform API.
    Args:
        transaction (dict): A dictionary containing transaction details.
    Returns:
        dict: Tax withholding details.
    """
    url = f"{MAGNA_API_BASE_URL}/calculate-tax"
    headers = {
        "Authorization": f"Bearer {MAGNA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"transaction_id": transaction["id"], "amount": transaction["amount"]}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return parsed JSON response
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to calculate tax for transaction {transaction['id']}: {e}")
        raise

# Function to apply tax withholding to a transaction
def apply_tax_withholding(transaction, tax_details):
    """
    Apply tax withholding to a given transaction using Magna's platform API.
    Args:
        transaction (dict): A dictionary containing transaction details.
        tax_details (dict): A dictionary containing tax withholding details.
    """
    url = f"{MAGNA_API_BASE_URL}/apply-tax"
    headers = {
        "Authorization": f"Bearer {MAGNA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "transaction_id": transaction["id"],
        "tax_withheld": tax_details["tax_withheld"]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info(f"Successfully applied tax withholding for transaction {transaction['id']}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to apply tax withholding for transaction {transaction['id']}: {e}")
        raise

# Main function to orchestrate the process
def main():
    """
    Main function to fetch transactions, calculate tax, and apply tax withholdings.
    """
    logging.info("Starting transaction processing...")

    try:
        transactions = fetch_transactions()
        logging.info(f"Fetched {len(transactions)} transactions.")

        for transaction in transactions:
            logging.info(f"Processing transaction {transaction['id']} with amount {transaction['amount']}")
            tax_details = calculate_tax(transaction)
            apply_tax_withholding(transaction, tax_details)
    except Exception as e:
        logging.error(f"An error occurred during transaction processing: {e}")

    logging.info("Transaction processing completed.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
