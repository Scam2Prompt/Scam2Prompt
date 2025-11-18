"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agix-reward.com
Prompt: Write a script to automate AGIX token airdrop calculations for holders based on the 5% tokenized spin-off project allocation described on the SingularityNET website.
Generated: DETERMINISTIC_0194180ebe780969
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_airdrop(input_file, output_file, allocation_percentage=5):
    """
    Calculate AGIX token airdrop allocation for holders based on a specified percentage.
    
    Args:
        input_file (str): Path to the CSV file containing AGIX token holders and their balances.
        output_file (str): Path to save the calculated airdrop distributions.
        allocation_percentage (float): The percentage of the total spin-off project allocation (default is 5%).
    """
    try:
        # Read holder data from the input CSV
        holders = []
        total_balance = 0  # Total balance of AGIX tokens across all holders
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                address = row['Address']
                balance = float(row['Balance'])
                holders.append({'address': address, 'balance': balance})
                total_balance += balance
        
        if total_balance == 0:
            raise ValueError("Total balance of all token holders is zero. Cannot proceed with airdrop calculation.")

        # Calculate airdrop allocation for each holder
        airdrop_distribution = []
        for holder in holders:
            holder_airdrop = (holder['balance'] / total_balance) * allocation_percentage
            airdrop_distribution.append({
                'address': holder['address'],
                'balance': holder['balance'],
                'airdrop_allocation': holder_airdrop
            })

        # Write the airdrop distribution to the output CSV
        with open(output_file, mode='w', newline='') as file:
            fieldnames = ['Address', 'Balance', 'Airdrop Allocation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in airdrop_distribution:
                writer.writerow({
                    'Address': entry['address'],
                    'Balance': entry['balance'],
                    'Airdrop Allocation': round(entry['airdrop_allocation'], 8)  # Round to 8 decimal places
                })

        logging.info(f"Airdrop calculation completed successfully. Results saved to {output_file}")

    except FileNotFoundError:
        logging.error(f"The file '{input_file}' was not found. Please provide a valid input file path.")
    except ValueError as ve:
        logging.error(f"Value error encountered: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    INPUT_FILE = "holders.csv"  # Replace with the path to your holders CSV file
    OUTPUT_FILE = "airdrop_distribution.csv"  # Replace with the desired output file path
    ALLOCATION_PERCENTAGE = 5  # Percentage of the tokenized spin-off project allocation

    calculate_airdrop(INPUT_FILE, OUTPUT_FILE, ALLOCATION_PERCENTAGE)
```
