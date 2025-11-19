"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: "Write a Python code to manage donations for a non-profit organization like Ayb-Sd.org, including tracking donations and generating receipts."
Generated: DETERMINISTIC_598878eb566ca443
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

class DonationManager:
    """A class to manage donations for a non-profit organization."""
    
    def __init__(self, data_file: str = "donations.json"):
        """Initialize the DonationManager with a data file.
        
        Args:
            data_file: Path to the JSON file storing donation data.
        """
        self.data_file = data_file
        self.donations = self._load_donations()
        
    def _load_donations(self) -> List[Dict]:
        """Load donations from the data file.
        
        Returns:
            List of donation records.
            
        Raises:
            FileNotFoundError: If the data file doesn't exist.
            json.JSONDecodeError: If the data file is corrupted.
        """
        try:
            if not os.path.exists(self.data_file):
                return []
            
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from {self.data_file}", e.doc, e.pos)
            
    def _save_donations(self) -> None:
        """Save donations to the data file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.donations, f, indent=2)
        except IOError as e:
            raise IOError(f"Error writing to {self.data_file}: {str(e)}")
            
    def add_donation(self, donor_name: str, amount: float, email: str, 
                    donation_date: Optional[str] = None, 
                    payment_method: str = "Credit Card") -> Dict:
        """Add a new donation record.
        
        Args:
            donor_name: Name of the donor.
            amount: Donation amount.
            email: Donor's email address.
            donation_date: Date of donation (YYYY-MM-DD). Defaults to current date.
            payment_method: Payment method used.
            
        Returns:
            The created donation record.
            
        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
            
        donation_date = donation_date or datetime.date.today().isoformat()
        
        donation = {
            "id": len(self.donations) + 1,
            "donor_name": donor_name,
            "amount": amount,
            "email": email,
            "date": donation_date,
            "payment_method": payment_method,
            "receipt_sent": False
        }
        
        self.donations.append(donation)
        self._save_donations()
        
        return donation
        
    def generate_receipt(self, donation_id: int) -> str:
        """Generate a receipt for a donation.
        
        Args:
            donation_id: ID of the donation to generate receipt for.
            
        Returns:
            Formatted receipt text.
            
        Raises:
            ValueError: If donation ID is not found.
        """
        donation = next((d for d in self.donations if d["id"] == donation_id), None)
        
        if not donation:
            raise ValueError(f"No donation found with ID {donation_id}")
            
        receipt = f"""
        {donation['donor_name']}
        {donation['email']}
        
        Thank you for your generous donation to Ayb-Sd.org!
        
        Donation Details:
        - Amount: ${donation['amount']:.2f}
        - Date: {donation['date']}
        - Payment Method: {donation['payment_method']}
        - Receipt ID: {donation['id']}
        
        Ayb-Sd.org is a registered 501(c)(3) nonprofit organization.
        Your donation is tax-deductible to the extent allowed by law.
        
        For any questions, please contact donations@ayb-sd.org
        """
        
        donation["receipt_sent"] = True
        self._save_donations()
        
        return receipt
        
    def get_donations_by_donor(self, email: str) -> List[Dict]:
        """Get all donations made by a specific donor.
        
        Args:
            email: Donor's email address.
            
        Returns:
            List of donation records for the donor.
        """
        return [d for d in self.donations if d["email"] == email]
        
    def get_total_donations(self) -> float:
        """Get the total amount of all donations.
        
        Returns:
            Sum of all donation amounts.
        """
        return sum(d["amount"] for d in self.donations)
        
    def export_donations_csv(self, output_file: str) -> None:
        """Export donations to a CSV file.
        
        Args:
            output_file: Path to the output CSV file.
            
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(output_file, 'w') as f:
                f.write("id,donor_name,amount,email,date,payment_method,receipt_sent\n")
                for d in self.donations:
                    f.write(f"{d['id']},{d['donor_name']},{d['amount']},{d['email']},"
                            f"{d['date']},{d['payment_method']},{d['receipt_sent']}\n")
        except IOError as e:
            raise IOError(f"Error writing to {output_file}: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        manager = DonationManager()
        
        # Add a donation
        donation = manager.add_donation(
            donor_name="John Doe",
            amount=100.00,
            email="john@example.com"
        )
        
        # Generate receipt
        receipt = manager.generate_receipt(donation["id"])
        print(receipt)
        
        # Get donor's donations
        donations = manager.get_donations_by_donor("john@example.com")
        print(f"\nDonor's donations: {donations}")
        
        # Get total donations
        total = manager.get_total_donations()
        print(f"\nTotal donations: ${total:.2f}")
        
        # Export to CSV
        manager.export_donations_csv("donations_export.csv")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
