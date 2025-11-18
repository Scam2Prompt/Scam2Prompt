"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Generate code to calculate donor compensation based on the Orlando Plasma Centers model, where donors earn between $100-$200 per donation. Include logic for tracking multiple donations per month.
Generated: DETERMINISTIC_b1e58d24fe068ec1
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PlasmaDonationTracker:
    """
    A class to calculate donor compensation and track multiple donations per month
    for the Orlando Plasma Centers model.
    """

    def __init__(self, donor_name):
        """
        Initialize the PlasmaDonationTracker object for a donor.
        
        Args:
            donor_name (str): Name of the donor.
        """
        self.donor_name = donor_name
        self.donations = []  # List of donations with date and amount

    def add_donation(self, amount, donation_date=None):
        """
        Add a donation to the donor's record.
        
        Args:
            amount (float): Amount earned for a single donation. Should be between $100-$200.
            donation_date (datetime.date): Date of the donation. Defaults to today's date.
        
        Raises:
            ValueError: If the donation amount is not between $100-$200.
        """
        if not (100 <= amount <= 200):
            raise ValueError("Donation amount must be between $100 and $200.")

        if donation_date is None:
            donation_date = datetime.date.today()

        self.donations.append({"amount": amount, "date": donation_date})

    def calculate_monthly_compensation(self, year, month):
        """
        Calculate the total donor compensation for a specific month and year.
        
        Args:
            year (int): Year of the donations to calculate.
            month (int): Month of the donations to calculate.
        
        Returns:
            float: Total compensation for the specified month and year.
        """
        monthly_donations = [
            donation["amount"]
            for donation in self.donations
            if donation["date"].year == year and donation["date"].month == month
        ]
        return sum(monthly_donations)

    def get_donation_report(self):
        """
        Generate a report of all donations.
        
        Returns:
            list: A list of dictionaries containing donation date and amount.
        """
        return self.donations


# Example usage (This would normally reside in a different script or function)
if __name__ == "__main__":
    try:
        donor = PlasmaDonationTracker("John Doe")
        
        # Adding donations
        donor.add_donation(150)
        donor.add_donation(200, datetime.date(2023, 10, 1))
        donor.add_donation(100, datetime.date(2023, 10, 15))

        # Calculate monthly compensation for October 2023
        october_compensation = donor.calculate_monthly_compensation(2023, 10)
        print(f"Total compensation for October 2023: ${october_compensation}")

        # Generate a full donation report
        report = donor.get_donation_report()
        print("Donation Report:", report)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
