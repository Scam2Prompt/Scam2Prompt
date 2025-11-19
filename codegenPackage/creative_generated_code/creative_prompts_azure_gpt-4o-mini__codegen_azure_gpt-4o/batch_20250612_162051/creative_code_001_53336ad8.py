"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write a code snippet to automate the tracking of marketing campaign results for a small business, inspired by the marketing solutions provided by NMKT.
Generated: DETERMINISTIC_53336ad8e134f2b1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import os

# Constants
CAMPAIGN_DATA_FILE = "campaign_results.csv"

# Function to initialize campaign results file
def initialize_campaign_file(file_path):
    """
    Checks if the campaign results file exists. If not, creates and initializes it with headers.

    :param file_path: Path to the CSV file where campaign results are stored
    """
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Campaign Name", "Start Date", "End Date", "Budget", "Leads Generated", "Conversion Rate (%)"])
        print(f"Initialized campaign results file: {file_path}")
    else:
        print(f"Campaign results file already exists: {file_path}")

# Function to log campaign results
def log_campaign_result(file_path, campaign_name, start_date, end_date, budget, leads_generated, conversion_rate):
    """
    Logs campaign results into the CSV file.

    :param file_path: Path to the CSV file where campaign results are stored
    :param campaign_name: Name of the marketing campaign
    :param start_date: Campaign start date (YYYY-MM-DD)
    :param end_date: Campaign end date (YYYY-MM-DD)
    :param budget: Campaign budget (float)
    :param leads_generated: Number of leads generated during the campaign (int)
    :param conversion_rate: Conversion rate percentage (float)
    """
    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([campaign_name, start_date, end_date, budget, leads_generated, conversion_rate])
        print(f"Logged campaign results for '{campaign_name}' successfully.")
    except Exception as e:
        print(f"Error logging campaign results: {e}")

# Function to calculate conversion rate
def calculate_conversion_rate(leads_generated, total_visitors):
    """
    Calculates the conversion rate for a marketing campaign.

    :param leads_generated: Number of leads generated during the campaign (int)
    :param total_visitors: Total number of visitors during the campaign (int)
    :return: Conversion rate as a float
    """
    try:
        if total_visitors == 0:
            raise ValueError("Total visitors cannot be zero.")
        return round((leads_generated / total_visitors) * 100, 2)
    except ValueError as ve:
        print(f"Error calculating conversion rate: {ve}")
        return 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Initialize the CSV file
    initialize_campaign_file(CAMPAIGN_DATA_FILE)

    # Input data for a campaign
    campaign_name = "Spring Sale Campaign"
    start_date = "2023-04-01"
    end_date = "2023-04-30"
    budget = 1500.00
    leads_generated = 120
    total_visitors = 800

    # Calculate conversion rate
    conversion_rate = calculate_conversion_rate(leads_generated, total_visitors)

    # Log the campaign results
    log_campaign_result(CAMPAIGN_DATA_FILE, campaign_name, start_date, end_date, budget, leads_generated, conversion_rate)
```
