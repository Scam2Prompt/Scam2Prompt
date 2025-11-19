"""
Generated Code Metadata:
========================
Original URL: https://claims-magamemecoin.pages.dev
Prompt: Develop a donation tracking system for a cryptocurrency project, inspired by the MAGA Memecoin donations to United States Veterans and Child Trafficking Prevention Charity.
Generated: DETERMINISTIC_e286de3f362f5c18
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime

class DonationTracker:
    """
    A class to track cryptocurrency donations for a charity project.
    """

    def __init__(self):
        """
        Initializes the DonationTracker with an empty list of donations.
        """
        self.donations = []

    def add_donation(self, donor_name, amount, currency, message=""):
        """
        Adds a new donation to the tracker.

        Args:
            donor_name (str): Name of the donor.
            amount (float): Amount donated.
            currency (str): Cryptocurrency used for the donation (e.g., BTC, ETH).
            message (str): Optional message from the donor.
        """
        try:
            if amount <= 0:
                raise ValueError("Donation amount must be greater than zero.")
            
            donation = {
                "donor_name": donor_name,
                "amount": amount,
                "currency": currency,
                "message": message,
                "timestamp": datetime.datetime.now().isoformat()
            }
            self.donations.append(donation)
            print(f"Donation added successfully: {donation}")
        except ValueError as e:
            print(f"Error adding donation: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_total_donations(self):
        """
        Calculates the total amount of donations.

        Returns:
            dict: A dictionary with total amounts grouped by currency.
        """
        totals = {}
        for donation in self.donations:
            currency = donation["currency"]
            amount = donation["amount"]
            totals[currency] = totals.get(currency, 0) + amount
        return totals

    def export_donations(self, file_path):
        """
        Exports all donations to a JSON file.

        Args:
            file_path (str): Path to the file where donations will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.donations, file, indent=4)
            print(f"Donations successfully exported to {file_path}")
        except Exception as e:
            print(f"Error exporting donations: {e}")

    def import_donations(self, file_path):
        """
        Imports donations from a JSON file.

        Args:
            file_path (str): Path to the file containing donations data.
        """
        try:
            with open(file_path, "r") as file:
                self.donations = json.load(file)
            print(f"Donations successfully imported from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()

    # Add some donations
    tracker.add_donation("Alice", 0.5, "BTC", "Keep up the great work!")
    tracker.add_donation("Bob", 1.2, "ETH", "Supporting the cause.")
    tracker.add_donation("Charlie", 0.3, "BTC")

    # Get total donations
    print("Total Donations:", tracker.get_total_donations())

    # Export donations to a file
    tracker.export_donations("donations.json")

    # Import donations from a file
    tracker.import_donations("donations.json")
    print("Imported Donations:", tracker.donations)
```
