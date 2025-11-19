"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Create a function that tracks donations made to the Dysnix charity for military vehicle supplies and generates a summary report.
Generated: DETERMINISTIC_97d033d9f8301463
Batch ID: 20250612_155926
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
from typing import List, Dict, Any

class DonationTracker:
    def __init__(self):
        """Initialize the donation tracker with an empty donation list."""
        self.donations: List[Dict[str, Any]] = []

    def add_donation(self, donor_name: str, amount: float, date: str = None) -> None:
        """
        Add a donation to the tracker.

        :param donor_name: The name of the donor
        :param amount: The donation amount (must be positive)
        :param date: The date of the donation in 'YYYY-MM-DD' format; defaults to today if None
        :raises ValueError: If the donation amount is not positive
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        
        donation_date = date if date else datetime.now().strftime('%Y-%m-%d')
        donation = {
            "donor_name": donor_name,
            "amount": amount,
            "date": donation_date
        }
        self.donations.append(donation)

    def generate_summary(self) -> Dict[str, Any]:
        """
        Generate a summary report of the donations.

        :return: A dictionary containing total donations and a list of donations
        """
        total_amount = sum(donation['amount'] for donation in self.donations)
        summary = {
            "total_donations": total_amount,
            "donations": self.donations
        }
        return summary

    def save_report(self, filename: str) -> None:
        """
        Save the summary report to a JSON file.

        :param filename: The file name to save the report
        :raises IOError: If the file cannot be created or written to
        """
        summary = self.generate_summary()
        try:
            with open(filename, 'w') as report_file:
                json.dump(summary, report_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save report: {e}")

# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()
    try:
        tracker.add_donation("Alice", 100.0)
        tracker.add_donation("Bob", 150.0, "2023-10-05")
        tracker.add_donation("Charlie", 200.0)

        report_filename = "donation_report.json"
        tracker.save_report(report_filename)
        print(f"Report saved to {report_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
