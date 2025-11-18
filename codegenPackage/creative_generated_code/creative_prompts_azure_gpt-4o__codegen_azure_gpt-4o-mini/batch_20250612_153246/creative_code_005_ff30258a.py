"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novamidiapublicidade.com.br
Prompt: Develop code to fetch and visualize social media analytics data, focusing on engagement and reach metrics, inspired by the social media management services described by Nova Mídia Publicidade.
Generated: DETERMINISTIC_ff30258a63f7be04
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.novamidia.com/v1/analytics": {
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
import pandas as pd
import matplotlib.pyplot as plt

class SocialMediaAnalytics:
    """
    A class to fetch and visualize social media analytics data focusing on engagement and reach metrics.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the SocialMediaAnalytics with the API URL and API Key.

        Parameters:
            api_url (str): The base URL for the social media analytics API.
            api_key (str): The API key for authenticating requests.
        """
        self.api_url = api_url
        self.api_key = api_key

    def fetch_data(self):
        """
        Fetches engagement and reach metrics data from the API.

        Returns:
            pd.DataFrame: A DataFrame containing the fetched data.

        Raises:
            Exception: If the API request fails or returns an unexpected response.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        try:
            response = requests.get(self.api_url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            
            # Convert data to DataFrame
            df = pd.DataFrame(data)
            return df
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from API: {e}")

    def visualize_data(self, df):
        """
        Visualizes the engagement and reach metrics from the DataFrame.

        Parameters:
            df (pd.DataFrame): A DataFrame containing the analytics data.
        """
        if df.empty:
            raise ValueError("The DataFrame is empty. No data to visualize.")

        # Plot engagement and reach metrics
        plt.figure(figsize=(12, 6))

        # Engagement plot
        plt.subplot(1, 2, 1)
        plt.bar(df['date'], df['engagement'], color='blue')
        plt.title('Engagement Over Time')
        plt.xlabel('Date')
        plt.ylabel('Engagement')
        plt.xticks(rotation=45)
        
        # Reach plot
        plt.subplot(1, 2, 2)
        plt.bar(df['date'], df['reach'], color='orange')
        plt.title('Reach Over Time')
        plt.xlabel('Date')
        plt.ylabel('Reach')
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

def main():
    # Constants for API configuration
    API_URL = "https://api.novamidia.com/v1/analytics"  # Replace with the actual API endpoint
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Create an instance of SocialMediaAnalytics
    analytics = SocialMediaAnalytics(API_URL, API_KEY)

    try:
        # Fetch analytics data
        data_df = analytics.fetch_data()

        # Visualize the fetched data
        analytics.visualize_data(data_df)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
