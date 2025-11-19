"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Develop a donation tracking system using a library like Pandas in Python, considering PerúMakers' donation management needs.
Generated: DETERMINISTIC_49520cd7a88081f5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime
import os
import json
from typing import Optional, Dict, List

class DonationTracker:
    """
    A donation tracking system for PerúMakers to manage donations efficiently.
    Features include adding donations, querying, generating reports, and saving/loading data.
    """
    
    def __init__(self, data_file: str = "donations_data.json"):
        """
        Initialize the donation tracker.
        
        Args:
            data_file (str): Path to the JSON file to store donation data.
        """
        self.data_file = data_file
        self.donations = pd.DataFrame(columns=[
            "donor_name", 
            "amount", 
            "currency", 
            "donation_date", 
            "donation_type", 
            "project", 
            "notes"
        ])
        self._load_data()
    
    def _load_data(self) -> None:
        """
        Load donation data from the JSON file if it exists.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.donations = pd.DataFrame(data)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """
        Save donation data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.donations.to_dict('records'), f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_donation(
        self,
        donor_name: str,
        amount: float,
        currency: str = "PEN",
        donation_date: Optional[str] = None,
        donation_type: Optional[str] = None,
        project: Optional[str] = None,
        notes: Optional[str] = None
    ) -> None:
        """
        Add a new donation to the tracker.
        
        Args:
            donor_name (str): Name of the donor.
            amount (float): Donation amount.
            currency (str): Currency code (default: PEN).
            donation_date (str): Date in YYYY-MM-DD format (default: current date).
            donation_type (str): Type of donation (e.g., cash, equipment).
            project (str): Project associated with the donation.
            notes (str): Additional notes.
        """
        try:
            if donation_date is None:
                donation_date = datetime.now().strftime("%Y-%m-%d")
            
            new_donation = {
                "donor_name": donor_name,
                "amount": amount,
                "currency": currency,
                "donation_date": donation_date,
                "donation_type": donation_type,
                "project": project,
                "notes": notes
            }
            
            self.donations = pd.concat([
                self.donations,
                pd.DataFrame([new_donation])
            ], ignore_index=True)
            
            self._save_data()
        except Exception as e:
            print(f"Error adding donation: {e}")
    
    def get_donations_by_donor(self, donor_name: str) -> pd.DataFrame:
        """
        Retrieve donations made by a specific donor.
        
        Args:
            donor_name (str): Name of the donor.
            
        Returns:
            pd.DataFrame: DataFrame containing the donor's donations.
        """
        try:
            return self.donations[self.donations["donor_name"] == donor_name]
        except Exception as e:
            print(f"Error retrieving donations: {e}")
            return pd.DataFrame()
    
    def get_donations_by_project(self, project: str) -> pd.DataFrame:
        """
        Retrieve donations for a specific project.
        
        Args:
            project (str): Name of the project.
            
        Returns:
            pd.DataFrame: DataFrame containing the project's donations.
        """
        try:
            return self.donations[self.donations["project"] == project]
        except Exception as e:
            print(f"Error retrieving donations: {e}")
            return pd.DataFrame()
    
    def get_total_donations(self) -> Dict[str, float]:
        """
        Calculate total donations grouped by currency.
        
        Returns:
            Dict[str, float]: Dictionary with currency as key and total amount as value.
        """
        try:
            return self.donations.groupby("currency")["amount"].sum().to_dict()
        except Exception as e:
            print(f"Error calculating total donations: {e}")
            return {}
    
    def generate_report(self, report_type: str = "summary") -> Optional[pd.DataFrame]:
        """
        Generate a donation report.
        
        Args:
            report_type (str): Type of report ('summary', 'by_donor', 'by_project').
            
        Returns:
            Optional[pd.DataFrame]: DataFrame containing the report or None if error.
        """
        try:
            if report_type == "summary":
                return self.donations.describe(include='all')
            elif report_type == "by_donor":
                return self.donations.groupby("donor_name").sum(numeric_only=True)
            elif report_type == "by_project":
                return self.donations.groupby("project").sum(numeric_only=True)
            else:
                print("Invalid report type. Use 'summary', 'by_donor', or 'by_project'.")
                return None
        except Exception as e:
            print(f"Error generating report: {e}")
            return None
    
    def export_to_csv(self, file_path: str) -> None:
        """
        Export donation data to a CSV file.
        
        Args:
            file_path (str): Path to save the CSV file.
        """
        try:
            self.donations.to_csv(file_path, index=False)
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

# Example usage
if __name__ == "__main__":
    tracker = DonationTracker()
    
    # Add sample donations
    tracker.add_donation("John Doe", 100.50, "PEN", project="Education")
    tracker.add_donation("Jane Smith", 200.75, "USD", donation_type="cash", project="Health")
    tracker.add_donation("John Doe", 50.25, "PEN", project="Education")
    
    # Generate reports
    print("Total donations by currency:")
    print(tracker.get_total_donations())
    
    print("\nDonations by John Doe:")
    print(tracker.get_donations_by_donor("John Doe"))
    
    print("\nSummary report:")
    print(tracker.generate_report("summary"))
    
    # Export to CSV
    tracker.export_to_csv("donations_report.csv")
```
