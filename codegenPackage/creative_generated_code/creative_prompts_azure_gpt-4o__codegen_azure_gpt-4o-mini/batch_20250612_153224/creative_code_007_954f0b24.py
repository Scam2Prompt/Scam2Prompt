"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Write code to generate a report summarizing the performance of a branding campaign, including metrics like brand awareness and customer engagement, using libraries like Pandas and Matplotlib.
Generated: DETERMINISTIC_954f0b24021a9e6d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define a class to encapsulate the branding campaign report generation
class BrandingCampaignReport:
    def __init__(self, data):
        """
        Initialize the BrandingCampaignReport with campaign data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing campaign metrics
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        self.data = data

    def summarize_metrics(self):
        """
        Generates a summary of key performance metrics from the campaign data.
        
        Returns:
        pd.DataFrame: Summary DataFrame with calculated metrics
        """
        try:
            summary = {
                'Total Impressions': self.data['Impressions'].sum(),
                'Total Clicks': self.data['Clicks'].sum(),
                'Click-Through Rate': (self.data['Clicks'].sum() / self.data['Impressions'].sum()) * 100,
                'Engagement Rate': (self.data['Engagements'].sum() / self.data['Impressions'].sum()) * 100,
                'Brand Awareness': self.data['Brand_Awareness'].mean()  # Assuming this is a score out of 100
            }
            return pd.DataFrame(summary, index=[0])
        except Exception as e:
            raise RuntimeError("Error generating summary metrics: {}".format(e))

    def plot_metrics(self):
        """
        Plots the key performance metrics for visual analysis.
        """
        try:
            fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

            # Plot Impressions and Clicks
            self.data[['Impressions', 'Clicks']].plot(kind='bar', ax=axes[0])
            axes[0].set_title('Impressions vs Clicks')
            axes[0].set_ylabel('Count')
            axes[0].set_xlabel('Campaign Days')

            # Plot Engagement Rate and Brand Awareness
            self.data[['Engagements', 'Brand_Awareness']].plot(kind='line', ax=axes[1], marker='o')
            axes[1].set_title('Engagement Rate and Brand Awareness')
            axes[1].set_ylabel('Percentage / Score')
            axes[1].set_xlabel('Campaign Days')

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError("Error plotting metrics: {}".format(e))

# Example usage
if __name__ == "__main__":
    # Sample campaign data creation
    campaign_data = {
        'Impressions': [1500, 2300, 1800, 2400, 1600],
        'Clicks': [150, 230, 180, 240, 160],
        'Engagements': [120, 210, 160, 230, 140],
        'Brand_Awareness': [70, 75, 80, 85, 90]  # Example scores out of 100
    }

    try:
        df = pd.DataFrame(campaign_data)
        report = BrandingCampaignReport(df)
        
        # Generate and display summary metrics
        summary_df = report.summarize_metrics()
        print("Campaign Summary Metrics:\n", summary_df)

        # Plot performance metrics
        report.plot_metrics()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
