"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Generate an example of a user access monitoring report using Techmaestropus IAM tools for compliance purposes.
Generated: DETERMINISTIC_fe643c52058133ca
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import csv
from techmaestropus_iam import IAMClient, IAMException

# Configuration
API_KEY = "your_api_key_here"  # Replace with your Techmaestropus IAM API key
OUTPUT_FILE = "user_access_report.csv"

def fetch_user_access_logs(client, start_date, end_date):
    """
    Fetch access logs for all users within the date range using Techmaestropus IAM tools.

    Args:
        client (IAMClient): Instance of the IAM client.
        start_date (datetime.date): Start date for the logs.
        end_date (datetime.date): End date for the logs.

    Returns:
        list: List of dictionaries containing user access details.
    """
    try:
        logs = client.get_access_logs(start_date=start_date, end_date=end_date)
        return logs
    except IAMException as e:
        print(f"Error fetching access logs: {e}")
        return []

def write_csv(data, file_path):
    """
    Write the access report data to a CSV file.

    Args:
        data (list): List of access log dictionaries.
        file_path (str): Output file path.
    """
    # Define the column headers
    headers = ["User ID", "Username", "Access Timestamp", "Action", "Resource"]

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    """
    Main function to generate the user access monitoring report.
    """
    # Initialize IAM client
    client = IAMClient(api_key=API_KEY)

    # Define report date range (example: last 7 days)
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=7)

    print(f"Generating user access report from {start_date} to {end_date}...")

    # Fetch user access logs
    logs = fetch_user_access_logs(client, start_date, end_date)

    if logs:
        # Write to CSV file
        write_csv(logs, OUTPUT_FILE)
        print(f"Report successfully generated: {OUTPUT_FILE}")
    else:
        print("No access logs found for the given date range.")

if __name__ == "__main__":
    main()
```
