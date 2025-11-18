"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Write code to track and measure the effectiveness of BTL and ATL advertising strategies, as implemented by Master-Brain.
Generated: DETERMINISTIC_0cf15b50b8ba3406
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the code implementation in Python:

```python
import datetime

class AdvertisingTracker:
    """
    A class to track and measure the effectiveness of BTL (Below the Line) 
    and ATL (Above the Line) advertising strategies.
    """

    def __init__(self):
        """
        Initializes the tracker with empty logs for BTL and ATL strategies.
        """
        self.btl_logs = []  # List to store BTL advertising data
        self.atl_logs = []  # List to store ATL advertising data

    def log_btl_activity(self, campaign_name, reach, conversion_rate, budget):
        """
        Logs a BTL campaign's effectiveness metrics.
        
        Args:
            campaign_name (str): Name of the BTL campaign.
            reach (int): Number of people reached by the campaign.
            conversion_rate (float): Conversion rate (0-100%) of the campaign.
            budget (float): Budget allocated for the campaign.
        """
        self.btl_logs.append({
            'campaign_name': campaign_name,
            'reach': reach,
            'conversion_rate': conversion_rate,
            'budget': budget,
            'timestamp': datetime.datetime.now()
        })

    def log_atl_activity(self, campaign_name, reach, impression_rate, budget):
        """
        Logs an ATL campaign's effectiveness metrics.
        
        Args:
            campaign_name (str): Name of the ATL campaign.
            reach (int): Number of people reached by the campaign.
            impression_rate (float): Impression rate (0-100%) of the campaign.
            budget (float): Budget allocated for the campaign.
        """
        self.atl_logs.append({
            'campaign_name': campaign_name,
            'reach': reach,
            'impression_rate': impression_rate,
            'budget': budget,
            'timestamp': datetime.datetime.now()
        })

    def generate_report(self):
        """
        Generates a consolidated report for both BTL and ATL strategies.
        
        Returns:
            dict: A dictionary containing the summary of BTL and ATL campaigns.
        """
        btl_summary = self._calculate_summary(self.btl_logs, 'BTL')
        atl_summary = self._calculate_summary(self.atl_logs, 'ATL')

        return {
            'BTL Summary': btl_summary,
            'ATL Summary': atl_summary
        }

    def _calculate_summary(self, logs, strategy_type):
        """
        Helper method to calculate summary statistics for a given strategy type.
        
        Args:
            logs (list): List of campaign logs.
            strategy_type (str): Type of strategy (BTL or ATL).
        
        Returns:
            dict: Summary statistics for the given strategy.
        """
        total_reach = sum(log['reach'] for log in logs)
        total_budget = sum(log['budget'] for log in logs)
        avg_conversion_rate = sum(log.get('conversion_rate', 0) for log in logs) / len(logs) if strategy_type == 'BTL' else None
        avg_impression_rate = sum(log.get('impression_rate', 0) for log in logs) / len(logs) if strategy_type == 'ATL' else None

        summary = {
            'Total Reach': total_reach,
            'Total Budget': total_budget,
            'Average Conversion Rate': avg_conversion_rate,
            'Average Impression Rate': avg_impression_rate,
            'Number of Campaigns': len(logs)
        }

        return summary

    def save_report_to_file(self, file_path):
        """
        Saves the report to a text file.
        
        Args:
            file_path (str): Path where the report file should be saved.
        """
        try:
            report = self.generate_report()
            with open(file_path, 'w') as file:
                file.write("Advertising Effectiveness Report\n")
                file.write("=" * 40 + "\n\n")
                for strategy, summary in report.items():
                    file.write(f"{strategy}:\n")
                    for key, value in summary.items():
                        file.write(f"{key}: {value}\n")
                    file.write("\n")

            print(f"Report successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving report to file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = AdvertisingTracker()

    # Log BTL campaigns
    tracker.log_btl_activity("BTL Campaign 1", reach=5000, conversion_rate=2.5, budget=1000)
    tracker.log_btl_activity("BTL Campaign 2", reach=8000, conversion_rate=3.0, budget=1500)

    # Log ATL campaigns
    tracker.log_atl_activity("ATL Campaign 1", reach=20000, impression_rate=15.0, budget=5000)
    tracker.log_atl_activity("ATL Campaign 2", reach=25000, impression_rate=12.0, budget=7000)

    # Generate and save the report
    tracker.save_report_to_file("advertising_report.txt")
```

This Python code tracks and measures the effectiveness of BTL and ATL advertising strategies and provides a way to export the results in a report.
