"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Generate code to automate the verification process for retrieving seized ESTD funds, as outlined by The Legato's legal protocols.
Generated: DETERMINISTIC_4c0e244ecf45b07b
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
import datetime
from typing import Dict, Union

# Configure logging
logging.basicConfig(
    filename="verification_process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FundVerificationError(Exception):
    """Custom exception class for fund verification errors."""
    pass

def read_protocols(file_path: str) -> Dict:
    """
    Reads legal protocols from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing protocols.

    Returns:
        dict: Parsed legal protocols.
    """
    try:
        with open(file_path, 'r') as file:
            protocols = json.load(file)
        logging.info("Successfully loaded legal protocols.")
        return protocols
    except FileNotFoundError:
        logging.error("Protocol file not found.")
        raise FundVerificationError("Protocol file not found.")
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON from protocol file.")
        raise FundVerificationError("Invalid JSON format in protocol file.")

def verify_funds(funds_data: Dict, protocols: Dict) -> Union[bool, str]:
    """
    Verifies seized ESTD funds against legal protocols.

    Args:
        funds_data (dict): Data of seized funds including amount, date, and source.
        protocols (dict): Legal protocols to validate against.

    Returns:
        Union[bool, str]: True if verification passes, error message if verification fails.
    """
    try:
        # Ensure all required fields are in place
        required_fields = ['amount', 'date', 'source']
        for field in required_fields:
            if field not in funds_data:
                return f"Missing required field: {field}"

        # Validate fund amount
        if funds_data['amount'] <= 0:
            return "Invalid fund amount. Must be greater than 0."

        if funds_data['amount'] > protocols['max_amount']:
            return f"Fund amount exceeds the maximum allowed limit of {protocols['max_amount']}."

        # Validate fund date
        fund_date = datetime.datetime.strptime(funds_data['date'], "%Y-%m-%d")
        if fund_date < datetime.datetime.strptime(protocols['min_date'], "%Y-%m-%d"):
            return "Fund date is earlier than the minimum allowed date in protocols."

        # Validate fund source
        if funds_data['source'] not in protocols['allowed_sources']:
            return f"Source '{funds_data['source']}' is not authorized by the protocols."

        logging.info("Funds verification passed.")
        return True
    except Exception as e:
        logging.error(f"An error occurred during verification: {str(e)}")
        raise FundVerificationError("An unexpected error occurred during fund verification.")

def main():
    """
    Main function to orchestrate the verification process.
    """
    # Paths to input files
    protocol_file_path = "protocols.json"
    funds_data = {
        "amount": 5000,
        "date": "2023-10-01",
        "source": "approved_source"
    }

    try:
        # Load protocols
        protocols = read_protocols(protocol_file_path)

        # Verify funds
        result = verify_funds(funds_data, protocols)
        if result is True:
            print("Funds verification successful!")
            logging.info("Funds verification successful.")
        else:
            print(f"Funds verification failed: {result}")
            logging.warning(f"Funds verification failed: {result}")
    except FundVerificationError as e:
        print(f"Error: {e}")
        logging.error(f"Error during verification process: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.critical(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
