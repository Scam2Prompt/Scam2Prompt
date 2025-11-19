"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Develop a script that calculates cashback rewards for users based on their betting history on a platform like BaxBet.
Generated: DETERMINISTIC_fc8443debd8e17f1
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

# Constants
CASHBACK_PERCENTAGE = 0.05  # 5% cashback rate
BETTING_HISTORY_FILE = "betting_history.csv"
OUTPUT_FILE = "cashback_rewards.csv"

# Function to calculate cashback for a single user
def calculate_cashback(total_bets):
    """
    Calculates cashback based on the total bets made by a user.
    
    :param total_bets: Total amount of bets placed by the user (float)
    :return: Cashback amount (float)
    """
    if total_bets < 0:
        raise ValueError("Total bets cannot be negative.")
    return round(total_bets * CASHBACK_PERCENTAGE, 2)

# Function to process betting history and generate cashback rewards
def process_betting_history(input_file, output_file):
    """
    Processes the betting history file and calculates cashback rewards for each user.
    
    :param input_file: Path to the CSV file containing betting history
    :param output_file: Path to the CSV file for saving cashback rewards
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist.")
    
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            # Read betting history
            reader = csv.DictReader(infile)
            if 'UserID' not in reader.fieldnames or 'TotalBets' not in reader.fieldnames:
                raise ValueError("Input file must contain 'UserID' and 'TotalBets' columns.")
            
            # Prepare cashback rewards CSV
            fieldnames = ['UserID', 'TotalBets', 'Cashback']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                try:
                    user_id = row['UserID']
                    total_bets = float(row['TotalBets'])
                    cashback = calculate_cashback(total_bets)
                    
                    # Write cashback reward to output file
                    writer.writerow({
                        'UserID': user_id,
                        'TotalBets': total_bets,
                        'Cashback': cashback
                    })
                except ValueError as e:
                    print(f"Error processing row for UserID '{row.get('UserID', 'Unknown')}': {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to execute the script
if __name__ == "__main__":
    """
    Main entry point of the script.
    Processes the betting history file and generates cashback rewards.
    """
    try:
        process_betting_history(BETTING_HISTORY_FILE, OUTPUT_FILE)
        print(f"Cashback rewards have been successfully written to '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"Failed to process cashback rewards: {e}")
```
