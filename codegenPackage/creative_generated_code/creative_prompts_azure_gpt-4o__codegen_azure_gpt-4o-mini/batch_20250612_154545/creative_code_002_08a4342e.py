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
import pandas as pd
import google.analytics.data_v1beta as ga_data
from google.oauth2 import service_account
import logging

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GoogleAnalyticsAnalyzer:
    def __init__(self, property_id, credentials_file):
        """
        Initializes the GoogleAnalyticsAnalyzer with the specified property ID and credentials file.

        :param property_id: The Google Analytics 4 property ID.
        :param credentials_file: Path to the service account credentials JSON file.
        """
        self.property_id = property_id
        self.credentials_file = credentials_file
        self.client = self._initialize_ga_client()

    def _initialize_ga_client(self):
        """
        Initializes the Google Analytics Data API client.

        :return: Google Analytics Data API client instance.
        """
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file
            )
            client = ga_data.BetaAnalyticsDataClient(credentials=credentials)
            logging.info("Google Analytics client initialized successfully.")
            return client
        except Exception as e:
            logging.error("Failed to initialize Google Analytics client: %s", e)
            raise

    def fetch_campaign_data(self, start_date, end_date):
        """
        Fetches campaign data from Google Analytics for the specified date range.

        :param start_date: The start date for the data fetch (YYYY-MM-DD).
        :param end_date: The end date for the data fetch (YYYY-MM-DD).
        :return: Pandas DataFrame containing campaign data.
        """
        try:
            request = ga_data.RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[{"start_date": start_date, "end_date": end_date}],
                dimensions=[{"name": "campaign"}, {"name": "source"}, {"name": "medium"}],
                metrics=[{"name": "sessions"}, {"name": "conversions"}]
            )
            response = self.client.run_report(request)
            
            # Convert response to a DataFrame
            data = [
                {dim.name: row.dimension_values[i].value for i, dim in enumerate(response.dimension_headers)}
                | {met.name: row.metric_values[i].value for i, met in enumerate(response.metric_headers)}
                for row in response.rows
            ]
            df = pd.DataFrame(data)
            logging.info("Campaign data fetched successfully.")
            return df
        except Exception as e:
            logging.error("Failed to fetch campaign data: %s", e)
            raise

    def analyze_campaign_performance(self, df):
        """
        Analyzes the campaign performance metrics and returns summary statistics.

        :param df: Pandas DataFrame containing campaign data.
        :return: Dictionary containing summarized campaign performance metrics.
        """
        try:
            # Convert metrics to numeric types
            df['sessions'] = pd.to_numeric(df['sessions'], errors='coerce')
            df['conversions'] = pd.to_numeric(df['conversions'], errors='coerce')
            
            # Compute summary statistics
            summary = {
                'total_sessions': df['sessions'].sum(),
                'total_conversions': df['conversions'].sum(),
                'conversion_rate': (df['conversions'].sum() / df['sessions'].sum()) * 100 if df['sessions'].sum() > 0 else 0,
                'campaign_performance': df.groupby('campaign').agg({'sessions': 'sum', 'conversions': 'sum'}).reset_index()
            }
            logging.info("Campaign performance analyzed successfully.")
            return summary
        except Exception as e:
            logging.error("Failed to analyze campaign performance: %s", e)
            raise

if __name__ == "__main__":
    # Example usage
    PROPERTY_ID = "YOUR_GA4_PROPERTY_ID"
    CREDENTIALS_FILE = "path/to/your/service_account_credentials.json"
    START_DATE = "2023-01-01"
    END_DATE = "2023-12-31"

    try:
        analyzer = GoogleAnalyticsAnalyzer(PROPERTY_ID, CREDENTIALS_FILE)
        campaign_data = analyzer.fetch_campaign_data(START_DATE, END_DATE)
        performance_summary = analyzer.analyze_campaign_performance(campaign_data)
        print(performance_summary)
    except Exception as e:
        logging.error("An error occurred during the analytics process: %s", e)
```
