"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Write a Python script to track and manage donations for a charitable foundation like Dysnix, including vehicle contributions for the Ukrainian army.
Generated: DETERMINISTIC_65a130d454cd4964
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import Dict, List, Optional, Union

class DonationTracker:
    """
    A class to track and manage donations for a charitable foundation.
    Supports monetary donations and vehicle contributions.
    """

    def __init__(self, data_file: str = "donations.json"):
        """
        Initialize the donation tracker with a data file.

        Args:
            data_file: Path to the JSON file storing donation records.
        """
        self.data_file = data_file
        self.donations = self._load_donations()

    def _load_donations(self) -> Dict[str, List[Dict]]:
        """
        Load donations from the data file.

        Returns:
            Dictionary containing donation records.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"monetary": [], "vehicles": []}
        except json.JSONDecodeError:
            print("Error: Corrupted data file. Starting with empty records.")
            return {"monetary": [], "vehicles": []}

    def _save_donations(self) -> None:
        """
        Save donations to the data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.donations, f, indent=2)
        except IOError as e:
            print(f"Error saving donations: {e}")

    def add_monetary_donation(self, donor_name: str, amount: float, currency: str, purpose: Optional[str] = None) -> None:
        """
        Add a monetary donation record.

        Args:
            donor_name: Name of the donor.
            amount: Donation amount.
            currency: Currency of the donation.
            purpose: Optional purpose of the donation.
        """
        donation = {
            "donor_name": donor_name,
            "amount": amount,
            "currency": currency,
            "date": datetime.now().isoformat(),
            "purpose": purpose
        }
        self.donations["monetary"].append(donation)
        self._save_donations()

    def add_vehicle_donation(self, donor_name: str, vehicle_type: str, vehicle_model: str, condition: str, purpose: str = "Ukrainian Army") -> None:
        """
        Add a vehicle donation record.

        Args:
            donor_name: Name of the donor.
            vehicle_type: Type of vehicle (e.g., "Truck", "SUV").
            vehicle_model: Model of the vehicle.
            condition: Condition of the vehicle.
            purpose: Purpose of the donation (default: "Ukrainian Army").
        """
        donation = {
            "donor_name": donor_name,
            "vehicle_type": vehicle_type,
            "vehicle_model": vehicle_model,
            "condition": condition,
            "date": datetime.now().isoformat(),
            "purpose": purpose
        }
        self.donations["vehicles"].append(donation)
        self._save_donations()

    def get_total_monetary_donations(self, currency: Optional[str] = None) -> float:
        """
        Get total monetary donations, optionally filtered by currency.

        Args:
            currency: Currency to filter by (None for all currencies).

        Returns:
            Total donation amount.
        """
        total = 0.0
        for donation in self.donations["monetary"]:
            if currency is None or donation["currency"] == currency:
                total += donation["amount"]
        return total

    def get_donations_report(self, output_format: str = "console") -> None:
        """
        Generate a report of all donations.

        Args:
            output_format: Output format ("console" or "csv").
        """
        if output_format == "console":
            print("\nMonetary Donations:")
            for donation in self.donations["monetary"]:
                print(f"{donation['date']} - {donation['donor_name']}: {donation['amount']} {donation['currency']} ({donation.get('purpose', 'General')})")

            print("\nVehicle Donations:")
            for donation in self.donations["vehicles"]:
                print(f"{donation['date']} - {donation['donor_name']}: {donation['vehicle_type']} {donation['vehicle_model']} ({donation['condition']}) for {donation['purpose']}")

        elif output_format == "csv":
            try:
                with open("donations_report.csv", 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Type", "Donor", "Amount/Model", "Currency/Type", "Date", "Purpose/Condition"])
                    
                    for donation in self.donations["monetary"]:
                        writer.writerow([
                            "Monetary",
                            donation["donor_name"],
                            donation["amount"],
                            donation["currency"],
                            donation["date"],
                            donation.get("purpose", "General")
                        ])
                    
                    for donation in self.donations["vehicles"]:
                        writer.writerow([
                            "Vehicle",
                            donation["donor_name"],
                            donation["vehicle_model"],
                            donation["vehicle_type"],
                            donation["date"],
                            f"{donation['condition']} for {donation['purpose']}"
                        ])
                print("Report saved to donations_report.csv")
            except IOError as e:
                print(f"Error generating CSV report: {e}")
        else:
            print("Error: Invalid output format. Choose 'console' or 'csv'.")

# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()

    # Add sample donations
    tracker.add_monetary_donation("John Doe", 1000.0, "USD", "Medical Supplies")
    tracker.add_monetary_donation("Jane Smith", 500.0, "EUR")
    tracker.add_vehicle_donation("Auto Corp", "Truck", "Mercedes-Benz Actros", "Good")
    tracker.add_vehicle_donation("Bob Johnson", "SUV", "Toyota Land Cruiser", "Excellent")

    # Generate reports
    tracker.get_donations_report("console")
    tracker.get_donations_report("csv")

    # Get total donations
    print(f"\nTotal USD donations: ${tracker.get_total_monetary_donations('USD'):.2f}")
```
