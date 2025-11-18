"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanreward.net
Prompt: Develop a script to export Hootsuite's social media performance reports in a custom format using its API.
Generated: DETERMINISTIC_1c736da0842d554e
Batch ID: 20250612_145727
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://platform.hootsuite.com/v1": {
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
import json
import csv
from datetime import datetime

# Hootsuite API configuration
API_BASE_URL = "https://platform.hootsuite.com/v1"
ACCESS_TOKEN = "your_hootsuite_access_token"  # Replace with your valid Hootsuite API access token

# Define the headers for API requests
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

def fetch_social_media_reports():
    """
    Fetch social media performance reports using Hootsuite API.

    Returns:
        list: A list of dictionaries containing social media performance data.
    """
    try:
        # Example API endpoint for obtaining social media reports
        endpoint = f"{API_BASE_URL}/analytics/reports"
        response = requests.get(endpoint, headers=HEADERS)

        # Raise HTTPError if status code is not 2xx
        response.raise_for_status()

        # Parse JSON response
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        # Log or print an error message if the API request fails
        print(f"Error fetching social media reports: {e}")
        return []

def export_to_custom_format(reports, output_file="social_media_report.csv"):
    """
    Export social media reports to a custom CSV format.

    Args:
        reports (list): A list of dictionaries containing social media data.
        output_file (str): The name of the output CSV file.
    """
    try:
        # Open the output file in write mode
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header row
            headers = ["Date", "Platform", "Post", "Impressions", "Engagements", "Clicks"]
            writer.writerow(headers)

            # Write each report's data
            for report in reports:
                writer.writerow([
                    report.get("date", "N/A"),
                    report.get("platform", "N/A"),
                    report.get("post", "N/A"),
                    report.get("impressions", 0),
                    report.get("engagements", 0),
                    report.get("clicks", 0),
                ])

        print(f"Reports successfully exported to {output_file}")
    except (IOError, KeyError) as e:
        # Log or print an error message if file writing fails
        print(f"Error writing to file: {e}")

def main():
    """
    Main function to fetch and export Hootsuite social media reports.
    """
    print("Fetching social media reports...")
    
    # Fetch reports from Hootsuite API
    reports = fetch_social_media_reports()

    # Export reports to a CSV file if data is retrieved
    if reports:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"social_media_report_{timestamp}.csv"
        export_to_custom_format(reports, output_file)
    else:
        print("No reports found to export.")

if __name__ == "__main__":
    main()
```
