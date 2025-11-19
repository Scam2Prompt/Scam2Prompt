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
import datetime

class DysnixCharityDonationTracker:
    def __init__(self):
        """
        Initializes the donation tracker with an empty list of donations.
        """
        self.donations = []  # Stores all donation records

    def add_donation(self, donor_name, amount):
        """
        Adds a donation record to the donation tracker.

        Args:
            donor_name (str): Name of the donor.
            amount (float): Donation amount (must be positive).
        
        Raises:
            ValueError: If the donation amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
        
        donation_record = {
            "donor_name": donor_name,
            "amount": amount,
            "date": datetime.datetime.now()
        }
        
        self.donations.append(donation_record)

    def generate_summary_report(self):
        """
        Generates a summary report of all donations.

        Returns:
            str: A summary report including total donations, number of donations,
                 and a list of individual donation records.
        """
        if not self.donations:
            return "No donations have been made yet."
        
        total_donations = sum(donation["amount"] for donation in self.donations)
        number_of_donations = len(self.donations)
        
        report_lines = [
            "Dysnix Charity Donation Summary Report",
            "--------------------------------------",
            f"Total Donations: ${total_donations:.2f}",
            f"Number of Donations: {number_of_donations}",
            "Individual Donations:"
        ]
        
        for donation in self.donations:
            report_lines.append(
                f"- {donation['donor_name']} donated ${donation['amount']:.2f} on {donation['date'].strftime('%Y-%m-%d %H:%M:%S')}"
            )
        
        return "\n".join(report_lines)


# Example usage
if __name__ == "__main__":
    # Initialize the tracker
    donation_tracker = DysnixCharityDonationTracker()
    
    try:
        # Add sample donations
        donation_tracker.add_donation("Alice", 100.50)
        donation_tracker.add_donation("Bob", 250.00)
        donation_tracker.add_donation("Charlie", 75.00)

        # Generate and print the summary report
        print(donation_tracker.generate_summary_report())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
