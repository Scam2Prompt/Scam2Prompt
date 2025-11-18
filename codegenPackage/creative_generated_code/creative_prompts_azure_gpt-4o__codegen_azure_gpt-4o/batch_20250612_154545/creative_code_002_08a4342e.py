"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Generate a Python script to analyze Google Analytics 4 data for tracking the effectiveness of digital marketing campaigns, as highlighted in Bear My Brand's services.
Generated: DETERMINISTIC_08a4342ef0f9bd3d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest

# Function to initialize the Google Analytics 4 client
def initialize_ga4_client(service_account_key_path):
    """
    Initialize the Google Analytics 4 client using service account credentials.

    Parameters:
    - service_account_key_path (str): Path to the service account JSON key file.

    Returns:
    - BetaAnalyticsDataClient: A Google Analytics client instance.
    """
    try:
        if not os.path.exists(service_account_key_path):
            raise FileNotFoundError(f"Service account key file not found: {service_account_key_path}")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key_path
        return BetaAnalyticsDataClient()
    except Exception as e:
        raise RuntimeError(f"Failed to initialize GA4 client: {e}")

# Function to run a Google Analytics report
def run_ga4_report(client, property_id, start_date, end_date, metrics, dimensions):
    """
    Run a Google Analytics report for the specified date range, metrics, and dimensions.

    Parameters:
    - client (BetaAnalyticsDataClient): The GA4 client instance.
    - property_id (str): The GA4 property ID.
    - start_date (str): Start date of the report in YYYY-MM-DD format.
    - end_date (str): End date of the report in YYYY-MM-DD format.
    - metrics (list): Metrics to retrieve (e.g., ["sessions", "conversions"]).
    - dimensions (list): Dimensions to group data by (e.g., ["source", "medium"]).

    Returns:
    - dict: The report results.
    """
    try:
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                {"start_date": start_date, "end_date": end_date},
            ],
            metrics=[{"name": metric} for metric in metrics],
            dimensions=[{"name": dimension} for dimension in dimensions],
        )
        response = client.run_report(request)
        
        # Parse the response into a dictionary for easier handling
        report_data = {
            "rows": [
                {dimension.name: row.dimension_values[index].value for index, dimension in enumerate(response.dimension_headers)}
                | {metric.name: row.metric_values[index].value for index, metric in enumerate(response.metric_headers)}
                for row in response.rows
            ]
        }
        return report_data
    except Exception as e:
        raise RuntimeError(f"Failed to run GA4 report: {e}")

# Main function to analyze marketing effectiveness
def analyze_marketing_effectiveness():
    """
    Main function to analyze marketing effectiveness using Google Analytics 4 data.
    """
    # Configuration
    SERVICE_ACCOUNT_KEY_PATH = "path/to/service_account.json"  # Update this path
    PROPERTY_ID = "YOUR_GA4_PROPERTY_ID"  # Replace with your GA4 property ID
    START_DATE = (datetime.date.today() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")  # Last 30 days
    END_DATE = datetime.date.today().strftime("%Y-%m-%d")  # Today
    METRICS = ["sessions", "conversions", "totalRevenue"]  # Metrics to analyze
    DIMENSIONS = ["source", "medium", "campaign"]  # Dimensions to group data by

    try:
        # Initialize the client
        client = initialize_ga4_client(SERVICE_ACCOUNT_KEY_PATH)

        # Run the report
        report = run_ga4_report(client, PROPERTY_ID, START_DATE, END_DATE, METRICS, DIMENSIONS)

        # Output the results
        print("Marketing Effectiveness Report:")
        print(json.dumps(report, indent=4))
    except Exception as e:
        print(f"Error analyzing marketing effectiveness: {e}")

# Entry point
if __name__ == "__main__":
    analyze_marketing_effectiveness()
```

### Notes:
- Replace `"path/to/service_account.json"` and `"YOUR_GA4_PROPERTY_ID"` with the actual service account key file path and GA4 property ID.
- Ensure the `google-analytics-data` Python library is installed via `pip install google-analytics-data`.
