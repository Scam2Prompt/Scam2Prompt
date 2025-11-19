"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate code to calculate donor compensation based on the Orlando Plasma Centers model, where donors earn between $100-$200 per donation. Include logic for tracking multiple donations per month.
Generated: DETERMINISTIC_b1e58d24fe068ec1
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Donor:
    """
    Represents a donor with donation history and compensation tracking.
    """
    
    def __init__(self, donor_id: str, name: str):
        """
        Initialize a new donor.
        
        Args:
            donor_id: Unique identifier for the donor
            name: Full name of the donor
        """
        self.donor_id = donor_id
        self.name = name
        self.donations = []  # List to store donation records
        self.monthly_compensation = {}  # Dict to track monthly compensation (format: {'YYYY-MM': amount})
    
    def add_donation(self, date: str, amount: float):
        """
        Record a new donation with date and compensation amount.
        
        Args:
            date: Date of donation in 'YYYY-MM-DD' format
            amount: Compensation amount (must be between $100-$200)
            
        Raises:
            ValueError: If amount is outside valid range or date format is invalid
        """
        if not 100 <= amount <= 200:
            raise ValueError("Compensation must be between $100 and $200")
        
        try:
            year_month = date[:7]  # Extract YYYY-MM
            donation = {
                'date': date,
                'amount': amount
            }
            self.donations.append(donation)
            
            # Update monthly compensation
            if year_month in self.monthly_compensation:
                self.monthly_compensation[year_month] += amount
            else:
                self.monthly_compensation[year_month] = amount
                
        except (IndexError, TypeError):
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    def get_total_compensation(self) -> float:
        """Return the total compensation earned across all donations."""
        return sum(d['amount'] for d in self.donations)
    
    def get_monthly_compensation(self, year_month: str) -> float:
        """
        Get compensation for a specific month.
        
        Args:
            year_month: Month in 'YYYY-MM' format
            
        Returns:
            float: Total compensation for the month (0 if no donations)
        """
        return self.monthly_compensation.get(year_month, 0)
    
    def get_donation_count(self) -> int:
        """Return the total number of donations made."""
        return len(self.donations)
    
    def get_donation_history(self) -> list:
        """Return complete donation history."""
        return self.donations.copy()


class DonorManager:
    """
    Manages multiple donors and provides aggregate reporting.
    """
    
    def __init__(self):
        self.donors = {}  # {donor_id: Donor object}
    
    def register_donor(self, donor_id: str, name: str) -> Donor:
        """
        Register a new donor.
        
        Args:
            donor_id: Unique identifier for the donor
            name: Full name of the donor
            
        Returns:
            Donor: The newly created donor object
            
        Raises:
            ValueError: If donor_id already exists
        """
        if donor_id in self.donors:
            raise ValueError(f"Donor ID {donor_id} already exists")
        
        donor = Donor(donor_id, name)
        self.donors[donor_id] = donor
        return donor
    
    def record_donation(self, donor_id: str, date: str, amount: float):
        """
        Record a donation for an existing donor.
        
        Args:
            donor_id: ID of the donor
            date: Date of donation in 'YYYY-MM-DD' format
            amount: Compensation amount (must be between $100-$200)
            
        Raises:
            ValueError: If donor doesn't exist or other validation fails
        """
        if donor_id not in self.donors:
            raise ValueError(f"Donor {donor_id} not found")
        
        self.donors[donor_id].add_donation(date, amount)
    
    def get_total_compensation(self) -> float:
        """Return total compensation paid to all donors."""
        return sum(d.get_total_compensation() for d in self.donors.values())
    
    def get_monthly_report(self, year_month: str) -> dict:
        """
        Generate a monthly report of donations.
        
        Args:
            year_month: Month in 'YYYY-MM' format
            
        Returns:
            dict: {
                'total_donations': int,
                'total_compensation': float,
                'donor_count': int,
                'average_per_donor': float
            }
        """
        monthly_data = {
            'total_donations': 0,
            'total_compensation': 0.0,
            'donor_count': 0,
            'average_per_donor': 0.0
        }
        
        for donor in self.donors.values():
            comp = donor.get_monthly_compensation(year_month)
            if comp > 0:
                monthly_data['total_compensation'] += comp
                monthly_data['donor_count'] += 1
                # Count donations in this month
                monthly_data['total_donations'] += len(
                    [d for d in donor.donations if d['date'].startswith(year_month)]
                )
        
        if monthly_data['donor_count'] > 0:
            monthly_data['average_per_donor'] = (
                monthly_data['total_compensation'] / monthly_data['donor_count']
            )
        
        return monthly_data


# Example usage
if __name__ == "__main__":
    manager = DonorManager()
    
    # Register donors
    donor1 = manager.register_donor("D001", "John Doe")
    donor2 = manager.register_donor("D002", "Jane Smith")
    
    # Record donations
    try:
        manager.record_donation("D001", "2023-10-01", 150)
        manager.record_donation("D001", "2023-10-15", 175)
        manager.record_donation("D002", "2023-10-10", 125)
        manager.record_donation("D002", "2023-11-05", 200)
    except ValueError as e:
        print(f"Error recording donation: {e}")
    
    # Generate reports
    oct_report = manager.get_monthly_report("2023-10")
    print(f"October 2023 Report: {oct_report}")
    
    print(f"Total compensation paid: ${manager.get_total_compensation():.2f}")
```
