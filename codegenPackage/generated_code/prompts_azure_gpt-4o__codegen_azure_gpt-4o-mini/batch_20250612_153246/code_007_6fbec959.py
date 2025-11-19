"""
Generated Code Metadata:
========================
Original URL: https://dextranslogistics.com
Prompt: Write a script to generate a logistics report summarizing Dextrans Logistics' services, including air freight, sea freight, warehousing, and transportation.
Generated: DETERMINISTIC_6fbec9595b51b6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogisticsReport:
    def __init__(self, company_name):
        self.company_name = company_name
        self.services = {
            "Air Freight": {
                "description": "Fast and reliable air transportation services.",
                "details": {
                    "delivery_time": "1-3 days",
                    "capacity": "Up to 1000 kg",
                    "tracking": True
                }
            },
            "Sea Freight": {
                "description": "Cost-effective sea transportation for large shipments.",
                "details": {
                    "delivery_time": "2-6 weeks",
                    "capacity": "Up to 10000 kg",
                    "tracking": True
                }
            },
            "Warehousing": {
                "description": "Secure storage solutions for your goods.",
                "details": {
                    "capacity": "1000 m²",
                    "security": "24/7 surveillance",
                    "climate_control": True
                }
            },
            "Transportation": {
                "description": "Reliable ground transportation services.",
                "details": {
                    "delivery_time": "Same day to 1 week",
                    "capacity": "Up to 5000 kg",
                    "tracking": True
                }
            }
        }

    def generate_report(self):
        """Generates a logistics report summarizing the services."""
        report = {
            "company": self.company_name,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "services": self.services
        }
        return report

    def save_report(self, report, filename='logistics_report.json'):
        """Saves the report to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            logging.info(f"Report saved successfully to {filename}")
        except IOError as e:
            logging.error(f"Failed to save report: {e}")

def main():
    """Main function to create and save the logistics report."""
    try:
        company_name = "Dextrans Logistics"
        report_generator = LogisticsReport(company_name)
        report = report_generator.generate_report()
        report_generator.save_report(report)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
