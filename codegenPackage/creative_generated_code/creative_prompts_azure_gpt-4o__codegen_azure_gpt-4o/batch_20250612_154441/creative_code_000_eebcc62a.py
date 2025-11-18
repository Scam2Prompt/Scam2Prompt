"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Write a Python script to analyze engagement metrics like website traffic and conversions for an influencer marketing campaign, referencing PulseX Media's approach to campaign success measurement.
Generated: DETERMINISTIC_eebcc62a5e21fea6
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime

class CampaignMetricsAnalyzer:
    """
    A class to analyze engagement metrics for influencer marketing campaigns.
    """

    def __init__(self, csv_file):
        """
        Initialize the CampaignMetricsAnalyzer with a CSV file.
        
        :param csv_file: Path to the CSV file containing campaign data.
        """
        self.csv_file = csv_file
        self.data = []

    def load_data(self):
        """
        Load campaign data from the CSV file.

        :raises FileNotFoundError: If the specified CSV file is not found.
        :raises ValueError: If the data in the CSV file is malformed.
        """
        try:
            with open(self.csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
                if not self.data:
                    raise ValueError("CSV file is empty or improperly formatted.")
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file}' not found.")
            raise
        except ValueError as e:
            print(f"Error: {e}")
            raise

    def calculate_metrics(self):
        """
        Calculate engagement metrics like website traffic and conversions.

        :return: A dictionary containing total traffic, total conversions, and conversion rate.
        """
        total_traffic = 0
        total_conversions = 0

        for row in self.data:
            try:
                traffic = int(row.get("website_traffic", 0))
                conversions = int(row.get("conversions", 0))
                total_traffic += traffic
                total_conversions += conversions
            except ValueError:
                print(f"Warning: Invalid data encountered in row {row}. Skipping...")
                continue

        conversion_rate = (
            (total_conversions / total_traffic) * 100 if total_traffic > 0 else 0
        )

        return {
            "total_traffic": total_traffic,
            "total_conversions": total_conversions,
            "conversion_rate": conversion_rate,
        }

    def generate_report(self, metrics):
        """
        Generate a report based on the calculated metrics.

        :param metrics: A dictionary containing engagement metrics.
        """
        print("\n--- Campaign Metrics Report ---")
        print(f"Total Website Traffic: {metrics['total_traffic']}")
        print(f"Total Conversions: {metrics['total_conversions']}")
        print(f"Conversion Rate: {metrics['conversion_rate']:.2f}%")
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("--- End of Report ---\n")


# Main script execution
if __name__ == "__main__":
    # Specify the path to your CSV file containing campaign data
    csv_file_path = "campaign_data.csv"

    # Initialize the analyzer
    analyzer = CampaignMetricsAnalyzer(csv_file_path)

    try:
        # Load and analyze the data
        analyzer.load_data()
        metrics = analyzer.calculate_metrics()

        # Generate and display the report
        analyzer.generate_report(metrics)
    except Exception as e:
        print(f"An error occurred: {e}")
```
