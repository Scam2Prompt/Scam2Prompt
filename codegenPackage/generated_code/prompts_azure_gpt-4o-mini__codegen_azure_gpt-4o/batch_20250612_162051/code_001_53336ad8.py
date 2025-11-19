"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Write a code snippet to automate the tracking of marketing campaign results for a small business, inspired by the marketing solutions provided by NMKT.
Generated: DETERMINISTIC_53336ad8e134f2b1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os

# Define constants for file paths and campaign data
CAMPAIGN_RESULTS_FILE = "campaign_results.csv"
BACKUP_FOLDER = "backups"

# Function to initialize the campaign results file if it doesn't exist
def initialize_results_file():
    if not os.path.exists(CAMPAIGN_RESULTS_FILE):
        with open(CAMPAIGN_RESULTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["Date", "Campaign Name", "Clicks", "Impressions", "Conversions", "Revenue"])
        print(f"Initialized {CAMPAIGN_RESULTS_FILE}.")

# Function to back up the campaign results file
def backup_results_file():
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_FOLDER, f"campaign_results_backup_{timestamp}.csv")
    try:
        with open(CAMPAIGN_RESULTS_FILE, 'r') as original_file:
            with open(backup_file, 'w') as backup:
                backup.write(original_file.read())
        print(f"Backup created: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Function to log campaign results
def log_campaign_results(campaign_name, clicks, impressions, conversions, revenue):
    try:
        with open(CAMPAIGN_RESULTS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write a new row with campaign data
            writer.writerow([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                campaign_name,
                clicks,
                impressions,
                conversions,
                revenue
            ])
        print(f"Logged results for campaign: {campaign_name}")
    except Exception as e:
        print(f"Error logging campaign results: {e}")

# Function to display campaign results
def display_campaign_results():
    try:
        with open(CAMPAIGN_RESULTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error reading campaign results: {e}")

# Main function to demonstrate functionality
def main():
    # Initialize the results file
    initialize_results_file()

    # Log some sample campaign results
    log_campaign_results("Spring Sale", 120, 1000, 15, 450.00)
    log_campaign_results("Summer Promo", 200, 1500, 25, 750.00)

    # Display the logged results
    print("\nCampaign Results:")
    display_campaign_results()

    # Create a backup of the results file
    backup_results_file()

# Entry point for the script
if __name__ == "__main__":
    main()
```
