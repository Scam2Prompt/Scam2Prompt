"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Develop a script to automate the calculation of referral bonuses for multi-level referral programs, similar to Access Link Limited's advanced referral system.
Generated: DETERMINISTIC_402f43ac6b59cfd6
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
BONUS_PERCENTAGES = [0.10, 0.05, 0.02]  # Referral levels 1, 2, and 3
INPUT_FILE = 'referrals.csv'  # Input CSV file name
OUTPUT_FILE = 'bonuses.json'  # Output JSON file name

# Load referral data from a CSV file
def load_referral_data(file_name: str) -> List[Dict[str, str]]:
    """
    Loads referral data from a CSV file.
    :param file_name: Name of the input CSV file.
    :return: List of dictionaries representing referral data.
    """
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found.")
        raise
    except Exception as e:
        logging.error(f"Error loading file {file_name}: {e}")
        raise

# Calculate referral bonuses
def calculate_referral_bonuses(referrals: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Calculates referral bonuses based on multi-level referral percentages.
    :param referrals: List of dictionaries representing referral data.
    :return: Dictionary mapping user IDs to their total bonus amounts.
    """
    bonuses = {}

    try:
        for referral in referrals:
            referrer_id = referral.get('ReferrerID')
            amount = float(referral.get('TransactionAmount', 0))

            # Apply bonuses for each level
            for level, percentage in enumerate(BONUS_PERCENTAGES):
                if referrer_id:
                    bonuses[referrer_id] = bonuses.get(referrer_id, 0) + amount * percentage

                    # Update referrer_id to the next level (if exists)
                    referrer_id = referral.get(f'ReferrerLevel{level + 2}')
                else:
                    break
    except ValueError as e:
        logging.error(f"Invalid data encountered during bonus calculation: {e}")
        raise
    except Exception as e:
        logging.error(f"Error calculating bonuses: {e}")
        raise

    return bonuses

# Save calculated bonuses to a JSON file
def save_bonuses_to_file(bonuses: Dict[str, float], file_name: str):
    """
    Saves referral bonuses to a JSON file.
    :param bonuses: Dictionary mapping user IDs to their total bonus amounts.
    :param file_name: Name of the output JSON file.
    """
    try:
        with open(file_name, mode='w') as file:
            json.dump(bonuses, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving bonuses to file {file_name}: {e}")
        raise

# Main function to execute the script
def main():
    """
    Main function to automate the calculation of referral bonuses.
    """
    logging.info("Starting referral bonus calculation process.")

    try:
        referrals = load_referral_data(INPUT_FILE)
        logging.info(f"Loaded {len(referrals)} referral records.")

        bonuses = calculate_referral_bonuses(referrals)
        logging.info("Referral bonuses calculated successfully.")

        save_bonuses_to_file(bonuses, OUTPUT_FILE)
        logging.info(f"Referral bonuses saved to {OUTPUT_FILE}.")
    except Exception as e:
        logging.error(f"An error occurred during the process: {e}")

if __name__ == '__main__':
    main()
```
