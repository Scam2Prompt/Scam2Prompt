"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Write a Python script to manage donations for a non-profit organization like Indological India, which has focus areas including Swasth Bharat and education.
Generated: DETERMINISTIC_16b4f4708b6713fe
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants
DONATIONS_FILE = "donations.json"
FOCUS_AREAS = ["Swasth Bharat", "Education", "Cultural Preservation", "Rural Development"]

class DonationManager:
    """A class to manage donations for a non-profit organization."""
    
    def __init__(self):
        """Initialize the donation manager and load existing data."""
        self.donations = self._load_donations()
        
    def _load_donations(self) -> List[Dict]:
        """Load donations from the JSON file.
        
        Returns:
            List of donation records. Returns empty list if file doesn't exist.
        """
        try:
            if os.path.exists(DONATIONS_FILE):
                with open(DONATIONS_FILE, 'r') as f:
                    return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading donations: {e}")
        return []
    
    def _save_donations(self) -> bool:
        """Save donations to the JSON file.
        
        Returns:
            True if save was successful, False otherwise.
        """
        try:
            with open(DONATIONS_FILE, 'w') as f:
                json.dump(self.donations, f, indent=4)
            return True
        except IOError as e:
            print(f"Error saving donations: {e}")
            return False
    
    def add_donation(self, donor_name: str, amount: float, focus_area: str, 
                    date: Optional[str] = None, notes: Optional[str] = None) -> bool:
        """Add a new donation record.
        
        Args:
            donor_name: Name of the donor
            amount: Donation amount
            focus_area: One of the predefined focus areas
            date: Optional donation date (YYYY-MM-DD format). Defaults to current date.
            notes: Optional additional notes
            
        Returns:
            True if donation was added successfully, False otherwise.
        """
        if focus_area not in FOCUS_AREAS:
            print(f"Invalid focus area. Must be one of: {', '.join(FOCUS_AREAS)}")
            return False
        
        if amount <= 0:
            print("Donation amount must be positive.")
            return False
            
        try:
            donation_date = date if date else datetime.now().strftime("%Y-%m-%d")
            donation = {
                "donor_name": donor_name,
                "amount": amount,
                "focus_area": focus_area,
                "date": donation_date,
                "notes": notes or ""
            }
            self.donations.append(donation)
            return self._save_donations()
        except Exception as e:
            print(f"Error adding donation: {e}")
            return False
    
    def get_donations_by_focus(self, focus_area: str) -> List[Dict]:
        """Get all donations for a specific focus area.
        
        Args:
            focus_area: The focus area to filter by
            
        Returns:
            List of donations matching the focus area
        """
        return [d for d in self.donations if d["focus_area"] == focus_area]
    
    def get_total_donations(self) -> float:
        """Get the total amount of all donations.
        
        Returns:
            Sum of all donation amounts
        """
        return sum(d["amount"] for d in self.donations)
    
    def get_donations_summary(self) -> Dict[str, Union[float, Dict]]:
        """Get a summary of all donations.
        
        Returns:
            Dictionary containing:
            - total_donations: sum of all donations
            - by_focus: dictionary with focus areas as keys and their totals
        """
        summary = {
            "total_donations": self.get_total_donations(),
            "by_focus": {}
        }
        
        for area in FOCUS_AREAS:
            area_donations = self.get_donations_by_focus(area)
            summary["by_focus"][area] = sum(d["amount"] for d in area_donations)
            
        return summary
    
    def export_donations_report(self, filename: str) -> bool:
        """Export donations to a JSON report file.
        
        Args:
            filename: Path to the output file
            
        Returns:
            True if export was successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "report_date": datetime.now().strftime("%Y-%m-%d"),
                    "donations": self.donations,
                    "summary": self.get_donations_summary()
                }, f, indent=4)
            return True
        except IOError as e:
            print(f"Error exporting report: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = DonationManager()
    
    # Add sample donations
    manager.add_donation("John Doe", 1000.50, "Swasth Bharat", notes="Monthly contribution")
    manager.add_donation("Jane Smith", 500.75, "Education")
    manager.add_donation("Acme Corp", 2000.00, "Cultural Preservation")
    
    # Get summary
    summary = manager.get_donations_summary()
    print("Donation Summary:")
    print(f"Total: ₹{summary['total_donations']:,.2f}")
    for area, amount in summary["by_focus"].items():
        print(f"{area}: ₹{amount:,.2f}")
    
    # Export report
    manager.export_donations_report("donations_report.json")
```
