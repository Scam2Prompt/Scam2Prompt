"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Generate code to analyze the effectiveness of a full-funnel app promotion campaign, including metrics like CR (conversion rate) and D1RR (day-one retention rate), as mentioned in Evamobi's case studies.
Generated: DETERMINISTIC_c29a6d637cab6c35
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CampaignAnalysis:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the CampaignAnalysis with the provided campaign data.
        
        :param data: pandas DataFrame containing the campaign metrics
        """
        self.data = data

    def calculate_conversion_rate(self):
        """
        Calculate the conversion rate (CR) as the ratio of users who completed the desired action
        to the total number of users who interacted with the campaign.
        
        :return: Conversion rate as a float
        """
        try:
            total_users = self.data['total_users'].sum()
            converted_users = self.data['converted_users'].sum()
            conversion_rate = converted_users / total_users if total_users > 0 else 0
            return conversion_rate
        except KeyError as e:
            raise ValueError(f"Missing required column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating conversion rate: {e}")

    def calculate_day_one_retention_rate(self):
        """
        Calculate the Day-One Retention Rate (D1RR) as the ratio of users who returned on day one
        to the total number of users acquired through the campaign.
        
        :return: Day-One Retention Rate as a float
        """
        try:
            total_acquired_users = self.data['total_acquired_users'].sum()
            retained_users = self.data['day_one_retained_users'].sum()
            d1_retention_rate = retained_users / total_acquired_users if total_acquired_users > 0 else 0
            return d1_retention_rate
        except KeyError as e:
            raise ValueError(f"Missing required column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating Day-One Retention Rate: {e}")

    def summarize_metrics(self):
        """
        Generate a summary of the campaign metrics including Conversion Rate and Day-One Retention Rate.
        
        :return: A dictionary containing the summary of the metrics
        """
        try:
            cr = self.calculate_conversion_rate()
            d1rr = self.calculate_day_one_retention_rate()
            return {
                'Conversion Rate': cr,
                'Day One Retention Rate': d1rr
            }
        except Exception as e:
            raise Exception(f"An error occurred while summarizing metrics: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration purposes
    sample_data = {
        'total_users': [1000, 1200, 800],
        'converted_users': [100, 150, 80],
        'total_acquired_users': [1000, 1200, 800],
        'day_one_retained_users': [80, 100, 40]
    }

    campaign_data = pd.DataFrame(sample_data)
    analysis = CampaignAnalysis(campaign_data)

    try:
        metrics_summary = analysis.summarize_metrics()
        print("Campaign Metrics Summary:")
        print(metrics_summary)
    except Exception as e:
        print(f"Error during campaign analysis: {e}")
```
