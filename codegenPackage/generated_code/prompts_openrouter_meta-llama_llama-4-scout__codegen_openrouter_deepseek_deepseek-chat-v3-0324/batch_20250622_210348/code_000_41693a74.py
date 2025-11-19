"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a Python script to manage donations for a charity organization like Amir International Charity Organization, which has programs for nutritional support, education assistance, and medical care.
Generated: DETERMINISTIC_41693a74a32c3a49
Batch ID: 20250622_210348
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

class DonationManager:
    """
    A class to manage donations for a charity organization with programs for
    nutritional support, education assistance, and medical care.
    """

    def __init__(self, data_file: str = "donations.json"):
        """
        Initialize the DonationManager with a data file to store donation records.
        
        Args:
            data_file (str): Path to the JSON file storing donation data.
        """
        self.data_file = data_file
        self.donations: List[Dict[str, Union[str, float, datetime]]] = []
        self._load_donations()

    def _load_donations(self) -> None:
        """
        Load donation records from the data file. Creates the file if it doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    # Convert string dates back to datetime objects
                    for donation in data:
                        donation["date"] = datetime.strptime(donation["date"], "%Y-%m-%d %H:%M:%S")
                    self.donations = data
            else:
                self.donations = []
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise RuntimeError(f"Error loading donation data: {str(e)}")

    def _save_donations(self) -> None:
        """
        Save donation records to the data file.
        """
        try:
            # Convert datetime objects to strings for JSON serialization
            data_to_save = []
            for donation in self.donations:
                donation_copy = donation.copy()
                donation_copy["date"] = donation["date"].strftime("%Y-%m-%d %H:%M:%S")
                data_to_save.append(donation_copy)
            
            with open(self.data_file, "w") as file:
                json.dump(data_to_save, file, indent=4)
        except (IOError, TypeError) as e:
            raise RuntimeError(f"Error saving donation data: {str(e)}")

    def add_donation(
        self,
        donor_name: str,
        amount: float,
        program: str,
        date: Optional[datetime] = None,
        notes: Optional[str] = None
    ) -> Dict[str, Union[str, float, datetime]]:
        """
        Add a new donation record.
        
        Args:
            donor_name (str): Name of the donor.
            amount (float): Donation amount.
            program (str): One of 'nutritional', 'education', or 'medical'.
            date (datetime, optional): Date of donation. Defaults to current datetime.
            notes (str, optional): Additional notes about the donation.
            
        Returns:
            dict: The added donation record.
            
        Raises:
            ValueError: If program is invalid or amount is non-positive.
        """
        if program not in ["nutritional", "education", "medical"]:
            raise ValueError("Program must be 'nutritional', 'education', or 'medical'")
        
        if amount <= 0:
            raise ValueError("Donation amount must be positive")
        
        donation = {
            "donor_name": donor_name,
            "amount": amount,
            "program": program,
            "date": date if date else datetime.now(),
            "notes": notes if notes else ""
        }
        
        self.donations.append(donation)
        self._save_donations()
        return donation

    def get_donations(
        self,
        program: Optional[str] = None,
        min_amount: Optional[float] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict[str, Union[str, float, datetime]]]:
        """
        Get filtered donation records.
        
        Args:
            program (str, optional): Filter by program.
            min_amount (float, optional): Filter by minimum amount.
            start_date (datetime, optional): Filter by earliest date.
            end_date (datetime, optional): Filter by latest date.
            
        Returns:
            list: Filtered donation records.
        """
        filtered = self.donations.copy()
        
        if program:
            filtered = [d for d in filtered if d["program"] == program]
        
        if min_amount:
            filtered = [d for d in filtered if d["amount"] >= min_amount]
        
        if start_date:
            filtered = [d for d in filtered if d["date"] >= start_date]
        
        if end_date:
            filtered = [d for d in filtered if d["date"] <= end_date]
        
        return filtered

    def get_total_donations(
        self,
        program: Optional[str] = None,
        min_amount: Optional[float] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> float:
        """
        Get the total amount of filtered donations.
        
        Args:
            program (str, optional): Filter by program.
            min_amount (float, optional): Filter by minimum amount.
            start_date (datetime, optional): Filter by earliest date.
            end_date (datetime, optional): Filter by latest date.
            
        Returns:
            float: Total amount of filtered donations.
        """
        donations = self.get_donations(program, min_amount, start_date, end_date)
        return sum(d["amount"] for d in donations)

    def generate_report(
        self,
        program: Optional[str] = None,
        min_amount: Optional[float] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> str:
        """
        Generate a text report of filtered donations.
        
        Args:
            program (str, optional): Filter by program.
            min_amount (float, optional): Filter by minimum amount.
            start_date (datetime, optional): Filter by earliest date.
            end_date (datetime, optional): Filter by latest date.
            
        Returns:
            str: Formatted report string.
        """
        donations = self.get_donations(program, min_amount, start_date, end_date)
        total = self.get_total_donations(program, min_amount, start_date, end_date)
        
        report_lines = [
            "Donation Report",
            "===============",
            f"Total Donations: {len(donations)}",
            f"Total Amount: ${total:.2f}",
            "",
            "Donations:"
        ]
        
        for donation in donations:
            report_lines.append(
                f"{donation['date'].strftime('%Y-%m-%d')} - {donation['donor_name']}: "
                f"${donation['amount']:.2f} for {donation['program']}"
            )
        
        return "\n".join(report_lines)


# Example usage
if __name__ == "__main__":
    try:
        manager = DonationManager()
        
        # Add some sample donations
        manager.add_donation("John Doe", 100.50, "nutritional", notes="Monthly contribution")
        manager.add_donation("Jane Smith", 250.00, "education")
        manager.add_donation("Acme Corp", 1000.00, "medical")
        
        # Generate and print a report
        print(manager.generate_report())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
