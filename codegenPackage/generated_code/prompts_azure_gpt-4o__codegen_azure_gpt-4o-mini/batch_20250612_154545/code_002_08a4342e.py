"""
Generated Code Metadata:
========================
Original URL: https://bearmybrand.com
Prompt: Generate a Python script to analyze Google Analytics 4 data for tracking the effectiveness of digital marketing campaigns, as highlighted in Bear My Brand's services.
Generated: DETERMINISTIC_08a4342ef0f9bd3d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import google.analytics.data_v1beta as ga_data
from google.oauth2 import service_account
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class GoogleAnalyticsAnalyzer:
    def __init__(self, credentials_file, property_id):
        """
        Initializes the GoogleAnalyticsAnalyzer with the given credentials and property ID.

        :param credentials_file: Path to the service account credentials JSON file.
        :param property_id: Google Analytics 4 property ID.
        """
        self.credentials_file = credentials_file
        self.property_id = property_id
        self.client = self._initialize_client()

    def _initialize_client(self):
        """
        Initializes the Google Analytics Data API client.

        :return: Google Analytics Data API client.
        """
        try:
            credentials = service_account.Credentials.from_service_account_file(self.credentials_file)
            client = ga_data.BetaAnalyticsDataClient(credentials=credentials)
            logging.info("Google Analytics Data API client initialized successfully.")
            return client
        except Exception as e:
            logging.error(f"Failed to initialize Google Analytics client: {e}")
            raise

    def fetch_campaign_data(self, start_date, end_date):
        """
        Fetches campaign data from Google Analytics 4.

        :param start_date: Start date for the data query (YYYY-MM-DD).
        :param end_date: End date for the data query (YYYY-MM-DD).
        :return: DataFrame containing campaign data.
        """
        try:
            request = ga_data.RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[{"start_date": start_date, "end_date": end_date}],
                dimensions=[{"name": "campaign"}, {"name": "source"}, {"name": "medium"}],
                metrics=[{"name": "sessions"}, {"name": "conversions"}]
            )
            response = self.client.run_report(request)
            logging.info("Campaign data fetched successfully.")
            return self._parse_response(response)
        except Exception as e:
            logging.error(f"Error fetching campaign data: {e}")
            raise

    def _parse_response(self, response):
        """
        Parses the response from the Google Analytics API into a DataFrame.

        :param response: Response object from the Google Analytics API.
        :return: DataFrame containing the parsed data.
        """
        rows = []
        for row in response.rows:
            row_data = {dimension.name: value for dimension, value in zip(response.dimension_headers, row.dimension_values)}
            row_data.update({metric.name: value for metric, value in zip(response.metric_headers, row.metric_values)})
            rows.append(row_data)
        return pd.DataFrame(rows)

    def analyze_campaign_effectiveness(self, df):
        """
        Analyzes the effectiveness of campaigns based on the fetched data.

        :param df: DataFrame containing campaign data.
        :return: DataFrame with effectiveness metrics.
        """
        try:
            df['conversion_rate'] = df['conversions'] / df['sessions']
            effectiveness_df = df[['campaign', 'source', 'medium', 'sessions', 'conversions', 'conversion_rate']]
            logging.info("Campaign effectiveness analysis completed.")
            return effectiveness_df
        except Exception as e:
            logging.error(f"Error analyzing campaign effectiveness: {e}")
            raise

def main():
    # Configuration
    CREDENTIALS_FILE = 'path/to/your/service_account_credentials.json'
    PROPERTY_ID = 'YOUR_PROPERTY_ID'
    START_DATE = '2023-01-01'
    END_DATE = '2023-12-31'

    # Initialize the analyzer
    analyzer = GoogleAnalyticsAnalyzer(CREDENTIALS_FILE, PROPERTY_ID)

    # Fetch campaign data
    campaign_data = analyzer.fetch_campaign_data(START_DATE, END_DATE)

    # Analyze campaign effectiveness
    effectiveness_data = analyzer.analyze_campaign_effectiveness(campaign_data)

    # Output the results
    print(effectiveness_data)

if __name__ == "__main__":
    main()
```
