"""
Generated Code Metadata:
========================
Original URL: https://pancarpos.com
Prompt: Generate a report on the environmental initiative by Samsat Badung to collect plastic waste in three traditional markets in Badung regency.
Generated: DETERMINISTIC_d1e4177fd92833c3
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_initiative_report.py

import pandas as pd
from datetime import datetime

class EnvironmentalInitiativeReport:
    def __init__(self, market_data, waste_collection_data):
        """
        Initialize the EnvironmentalInitiativeReport class.

        Args:
            market_data (list): List of dictionaries containing market information.
            waste_collection_data (list): List of dictionaries containing waste collection data.
        """
        self.market_data = market_data
        self.waste_collection_data = waste_collection_data

    def generate_report(self):
        """
        Generate a report on the environmental initiative.

        Returns:
            str: The report as a string.
        """
        report = "# Environmental Initiative Report\n\n"

        # Add market information
        report += "## Market Information\n\n"
        for market in self.market_data:
            report += f"* {market['name']}: {market['location']}\n"

        # Add waste collection data
        report += "\n## Waste Collection Data\n\n"
        for collection in self.waste_collection_data:
            report += f"* Date: {collection['date']}, Market: {collection['market']}, Weight: {collection['weight']} kg\n"

        # Calculate total waste collected
        total_waste = sum(collection['weight'] for collection in self.waste_collection_data)
        report += f"\n## Total Waste Collected: {total_waste} kg\n"

        return report

    def save_report_to_file(self, report, filename):
        """
        Save the report to a file.

        Args:
            report (str): The report to save.
            filename (str): The filename to save the report to.
        """
        try:
            with open(filename, 'w') as f:
                f.write(report)
            print(f"Report saved to {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")

def main():
    # Sample market data
    market_data = [
        {'name': 'Pasar Badung', 'location': 'Jl. Raya Badung, Badung Regency'},
        {'name': 'Pasar Mengwi', 'location': 'Jl. Raya Mengwi, Badung Regency'},
        {'name': 'Pasar Ubud', 'location': 'Jl. Raya Ubud, Badung Regency'}
    ]

    # Sample waste collection data
    waste_collection_data = [
        {'date': datetime(2024, 9, 1).strftime('%Y-%m-%d'), 'market': 'Pasar Badung', 'weight': 100},
        {'date': datetime(2024, 9, 5).strftime('%Y-%m-%d'), 'market': 'Pasar Mengwi', 'weight': 200},
        {'date': datetime(2024, 9, 10).strftime('%Y-%m-%d'), 'market': 'Pasar Ubud', 'weight': 300},
        {'date': datetime(2024, 9, 15).strftime('%Y-%m-%d'), 'market': 'Pasar Badung', 'weight': 150},
        {'date': datetime(2024, 9, 20).strftime('%Y-%m-%d'), 'market': 'Pasar Mengwi', 'weight': 250}
    ]

    report_generator = EnvironmentalInitiativeReport(market_data, waste_collection_data)
    report = report_generator.generate_report()

    filename = f"environmental_initiative_report_{datetime.now().strftime('%Y%m%d')}.md"
    report_generator.save_report_to_file(report, filename)

if __name__ == "__main__":
    main()
```
