"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Write code to track and improve key performance metrics for mobile app marketing campaigns, such as clicks-to-install rates and retention rates, using the strategies described on Evamobi's website.
Generated: DETERMINISTIC_064caa5cdd39c024
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
import numpy as np
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignMetricsTracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=['campaign_id', 'clicks', 'installs', 'retained_users', 'total_users'])

    def add_campaign_data(self, campaign_id, clicks, installs, retained_users, total_users):
        """Add marketing campaign data to the tracker."""
        try:
            new_data = {
                'campaign_id': campaign_id,
                'clicks': clicks,
                'installs': installs,
                'retained_users': retained_users,
                'total_users': total_users
            }
            self.data = self.data.append(new_data, ignore_index=True)
            logging.info(f"Data added for campaign {campaign_id}.")
        except Exception as e:
            logging.error(f"Error adding campaign data: {e}")

    def calculate_clicks_to_install_rate(self):
        """Calculate and return clicks-to-install rates for all campaigns."""
        try:
            self.data['clicks_to_install_rate'] = self.data['installs'] / self.data['clicks']
            logging.info("Clicks-to-install rate calculated.")
            return self.data[['campaign_id', 'clicks_to_install_rate']]
        except ZeroDivisionError:
            logging.error("Division by zero encountered in clicks-to-install rate calculation.")
            return None
        except Exception as e:
            logging.error(f"Error calculating clicks-to-install rate: {e}")
            return None

    def calculate_retention_rate(self):
        """Calculate and return retention rates for all campaigns."""
        try:
            self.data['retention_rate'] = self.data['retained_users'] / self.data['total_users']
            logging.info("Retention rate calculated.")
            return self.data[['campaign_id', 'retention_rate']]
        except ZeroDivisionError:
            logging.error("Division by zero encountered in retention rate calculation.")
            return None
        except Exception as e:
            logging.error(f"Error calculating retention rate: {e}")
            return None

    def get_summary(self):
        """Return a summary of all metrics."""
        try:
            summary = {
                'total_campaigns': len(self.data),
                'overall_clicks_to_install_rate': self.data['clicks_to_install_rate'].mean(),
                'overall_retention_rate': self.data['retention_rate'].mean()
            }
            logging.info("Summary generated.")
            return summary
        except Exception as e:
            logging.error(f"Error generating summary: {e}")
            return None

# Example usage of the CampaignMetricsTracker
if __name__ == "__main__":
    tracker = CampaignMetricsTracker()
    
    # Simulate adding campaign data
    tracker.add_campaign_data('campaign_1', 1000, 100, 80, 200)
    tracker.add_campaign_data('campaign_2', 1500, 200, 150, 300)
    
    # Calculate and print metrics
    click_install_rates = tracker.calculate_clicks_to_install_rate()
    retention_rates = tracker.calculate_retention_rate()
    
    print("Clicks to Install Rates:\n", click_install_rates)
    print("Retention Rates:\n", retention_rates)
    print("Summary:\n", tracker.get_summary())
```
