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
class DonorCompensation:
    def __init__(self):
        # Initialize a dictionary to track donations per donor
        self.donations = {}

    def add_donation(self, donor_id, donation_amount):
        """
        Adds a donation for a given donor.

        Args:
            donor_id (str): Unique identifier for the donor.
            donation_amount (float): Amount earned for this donation.

        Raises:
            ValueError: If the donation amount is not between 100 and 200.
        """
        if not (100 <= donation_amount <= 200):
            raise ValueError("Donation amount must be between $100 and $200.")

        if donor_id not in self.donations:
            self.donations[donor_id] = []

        self.donations[donor_id].append(donation_amount)

    def calculate_total_compensation(self, donor_id):
        """
        Calculates the total compensation for a given donor.

        Args:
            donor_id (str): Unique identifier for the donor.

        Returns:
            float: Total compensation for the donor.

        Raises:
            KeyError: If the donor ID does not exist.
        """
        if donor_id not in self.donations:
            raise KeyError(f"No donations found for donor ID: {donor_id}")

        return sum(self.donations[donor_id])

    def get_monthly_compensation(self, donor_id):
        """
        Returns a summary of the donor's total earnings for the current month.

        Args:
            donor_id (str): Unique identifier for the donor.

        Returns:
            dict: A summary containing total donations and the number of donations.

        Raises:
            KeyError: If the donor ID does not exist.
        """
        if donor_id not in self.donations:
            raise KeyError(f"No donations found for donor ID: {donor_id}")

        total_compensation = self.calculate_total_compensation(donor_id)
        donation_count = len(self.donations[donor_id])

        return {
            "total_compensation": total_compensation,
            "donation_count": donation_count
        }

# Example usage of the DonorCompensation class
if __name__ == "__main__":
    donor_compensation = DonorCompensation()

    try:
        # Adding donations for different donors
        donor_compensation.add_donation("donor_1", 150)
        donor_compensation.add_donation("donor_1", 200)
        donor_compensation.add_donation("donor_2", 120)

        # Calculating total compensation for a donor
        total_for_donor_1 = donor_compensation.calculate_total_compensation("donor_1")
        print(f"Total compensation for donor_1: ${total_for_donor_1}")

        # Getting monthly compensation summary for a donor
        monthly_summary = donor_compensation.get_monthly_compensation("donor_1")
        print(f"Monthly compensation summary for donor_1: {monthly_summary}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
