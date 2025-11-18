"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextranslogistics.com
Prompt: Write a script to generate a logistics report summarizing Dextrans Logistics' services, including air freight, sea freight, warehousing, and transportation.
Generated: DETERMINISTIC_6fbec9595b51b6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


def generate_logistics_report():
    """
    Generates a logistics report summarizing Dextrans Logistics' services.
    The services include air freight, sea freight, warehousing, and transportation.
    The report is saved as a JSON file.
    """

    # Logistics services data
    logistics_services = {
        "company_name": "Dextrans Logistics",
        "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "services": {
            "air_freight": {
                "description": "Fast and reliable air transportation for urgent shipments.",
                "coverage": "Global",
                "features": [
                    "Priority handling",
                    "Real-time tracking",
                    "Custom clearance assistance"
                ]
            },
            "sea_freight": {
                "description": "Cost-effective shipping solutions for large-volume cargo.",
                "coverage": "Global",
                "features": [
                    "FCL (Full Container Load) and LCL (Less than Container Load) options",
                    "Secure cargo handling",
                    "Route optimization"
                ]
            },
            "warehousing": {
                "description": "State-of-the-art storage facilities for your goods.",
                "coverage": "Regional",
                "features": [
                    "Temperature-controlled storage",
                    "Inventory management systems",
                    "24/7 security monitoring"
                ]
            },
            "transportation": {
                "description": "Efficient local and regional transport solutions.",
                "coverage": "Regional",
                "features": [
                    "Fleet of modern vehicles",
                    "Scheduled deliveries",
                    "Proof-of-delivery tracking"
                ]
            }
        }
    }

    # File name for saving the report
    report_filename = "dextrans_logistics_report.json"
    
    try:
        # Save the report as a JSON file
        with open(report_filename, "w") as report_file:
            json.dump(logistics_services, report_file, indent=4)
        
        print(f"Logistics report successfully generated and saved as '{report_filename}'.")
    except Exception as e:
        # Handle any errors during file writing
        print(f"An error occurred while generating the report: {e}")


if __name__ == "__main__":
    # Entry point of the script
    generate_logistics_report()
```
