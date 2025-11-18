"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: Generate a script that converts USDC transactions to USD values using historical exchange rates, ensuring accurate tax reporting for Polymarket trades, as outlined on https://polymarket.tax.
Generated: DETERMINISTIC_43053e0645e35dda
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate.host/convert": {
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
from datetime import datetime

# Constants
EXCHANGE_RATE_API_URL = "https://api.exchangerate.host/convert"
USDC_DECIMALS = 6  # USDC uses 6 decimal places for precision

def fetch_historical_exchange_rate(date: str) -> float:
    """
    Fetch the historical exchange rate from USDC to USD for the given date.
    :param date: A string representing the date in 'YYYY-MM-DD' format.
    :return: The exchange rate (float) or raises an exception if failed.
    """
    params = {
        "from": "USDC",
        "to": "USD",
        "date": date
    }
    try:
        response = requests.get(EXCHANGE_RATE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Validate response structure and rate value
        if "info" in data and "rate" in data["info"]:
            return float(data["info"]["rate"])
        else:
            raise ValueError(f"Invalid response structure for date {date}.")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch exchange rate for date {date}: {e}")

def convert_usdc_to_usd(usdc_amount: float, exchange_rate: float) -> float:
    """
    Convert USDC amount to USD using the given exchange rate.
    :param usdc_amount: The amount in USDC (float).
    :param exchange_rate: The historical exchange rate (float).
    :return: The converted amount in USD (float).
    """
    return round(usdc_amount * exchange_rate, 2)

def process_transactions(input_csv: str, output_csv: str):
    """
    Process USDC transactions from the input CSV file and write USD conversions to the output CSV file.
    :param input_csv: Path to the input CSV file containing transaction data.
    :param output_csv: Path to the output CSV file to save converted data.
    """
    try:
        with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["Converted USD"]  # Add a new column for USD values
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in reader:
                try:
                    transaction_date = row["Date"]
                    usdc_amount = float(row["USDC Amount"]) / (10 ** USDC_DECIMALS)  # Adjust for USDC decimal places
                    
                    # Fetch historical exchange rate and convert
                    exchange_rate = fetch_historical_exchange_rate(transaction_date)
                    usd_value = convert_usdc_to_usd(usdc_amount, exchange_rate)
                    
                    # Write the converted value to the new CSV row
                    row["Converted USD"] = usd_value
                    writer.writerow(row)
                except Exception as e:
                    print(f"Error processing transaction on {row['Date']}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Change these paths to your input and output file locations
    input_csv_path = "transactions.csv"
    output_csv_path = "converted_transactions.csv"

    process_transactions(input_csv_path, output_csv_path)
```
