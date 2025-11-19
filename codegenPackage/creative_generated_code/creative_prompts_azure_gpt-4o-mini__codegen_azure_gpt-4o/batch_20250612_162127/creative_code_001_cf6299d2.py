"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paybackclaimltd.com
Prompt: How can I implement a system to track and report investment scams using Python libraries mentioned on Payback Claim Ltd.?
Generated: DETERMINISTIC_cf6299d27e2f3d57
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(
    filename='investment_scams.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a class to handle investment scam reports
class InvestmentScamTracker:
    def __init__(self):
        # Initialize an empty list to store scam reports
        self.reports: List[Dict] = []

    def report_scam(self, scammer_name: str, scam_type: str, amount_lost: float, description: str, reporter_contact: str):
        """
        Report a scam and add it to the reports list.

        Args:
            scammer_name (str): Name of the scammer
            scam_type (str): Type of scam (e.g., phishing, fake investment)
            amount_lost (float): Amount of money lost in the scam
            description (str): Additional description of the scam
            reporter_contact (str): Contact information of the reporter
        
        Returns:
            dict: The scam report added
        """
        try:
            # Validate input
            if amount_lost < 0:
                raise ValueError("Amount lost cannot be negative.")
            if not scammer_name or not scam_type or not reporter_contact:
                raise ValueError("Scammer name, scam type, and reporter contact are required.")

            # Create a report
            report = {
                "scammer_name": scammer_name,
                "scam_type": scam_type,
                "amount_lost": amount_lost,
                "description": description,
                "reporter_contact": reporter_contact,
                "reported_at": datetime.now().isoformat()
            }

            # Add the report to the list
            self.reports.append(report)

            # Log the report for tracking purposes
            logging.info(f"Scam reported: {json.dumps(report)}")

            return report

        except ValueError as ve:
            logging.error(f"Error while reporting scam: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def get_reports(self):
        """
        Retrieve all scam reports.

        Returns:
            List[Dict]: List of scam reports
        """
        return self.reports

    def export_reports_to_json(self, file_path: str):
        """
        Export all scam reports to a JSON file.

        Args:
            file_path (str): Path to the JSON file
        
        Returns:
            None
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.reports, json_file, indent=4)
            logging.info(f"Reports successfully exported to {file_path}")
        except Exception as e:
            logging.error(f"Error exporting reports to JSON: {e}")
            raise

    def search_reports(self, scammer_name: str):
        """
        Search reports by scammer name.

        Args:
            scammer_name (str): Name of the scammer to search for
        
        Returns:
            List[Dict]: List of matching reports
        """
        try:
            if not scammer_name:
                raise ValueError("Scammer name cannot be empty.")
            
            # Filter reports based on scammer name
            matching_reports = [
                report for report in self.reports if scammer_name.lower() in report["scammer_name"].lower()
            ]

            return matching_reports

        except ValueError as ve:
            logging.error(f"Error in search_reports: {ve}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in search_reports: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize the tracker
    tracker = InvestmentScamTracker()

    # Report a scam
    try:
        tracker.report_scam(
            scammer_name="John Doe",
            scam_type="Fake Crypto Investment",
            amount_lost=5000.00,
            description="Promised high returns on cryptocurrency investments.",
            reporter_contact="johndoe@example.com"
        )
    except Exception as e:
        print(f"Failed to report scam: {e}")

    # Get all reports
    print("All Reports:", tracker.get_reports())

    # Export reports to JSON
    try:
        tracker.export_reports_to_json("scam_reports.json")
    except Exception as e:
        print(f"Failed to export reports: {e}")

    # Search reports
    try:
        print("Search Reports:", tracker.search_reports("John Doe"))
    except Exception as e:
        print(f"Failed to search reports: {e}")
```
