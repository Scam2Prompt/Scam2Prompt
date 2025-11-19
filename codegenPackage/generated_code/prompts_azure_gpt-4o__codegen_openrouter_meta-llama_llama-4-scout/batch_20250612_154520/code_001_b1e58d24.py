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
    def __init__(self, donor_id, name):
        """
        Initialize a Donor object.

        Args:
            donor_id (int): Unique identifier for the donor.
            name (str): Name of the donor.
        """
        self.donor_id = donor_id
        self.name = name
        self.donations = []

    def add_donation(self, donation_date, compensation):
        """
        Add a donation to the donor's record.

        Args:
            donation_date (str): Date of the donation in YYYY-MM-DD format.
            compensation (float): Compensation earned for the donation.

        Raises:
            ValueError: If compensation is not between $100 and $200.
        """
        if not 100 <= compensation <= 200:
            raise ValueError("Compensation must be between $100 and $200")

        self.donations.append({"donation_date": donation_date, "compensation": compensation})

    def get_total_compensation(self):
        """
        Calculate the total compensation earned by the donor.

        Returns:
            float: Total compensation earned.
        """
        return sum(donation["compensation"] for donation in self.donations)

    def get_donations(self):
        """
        Get a list of donations made by the donor.

        Returns:
            list: List of donations, each containing donation date and compensation.
        """
        return self.donations


class DonorTracker:
    def __init__(self):
        """
        Initialize a DonorTracker object.
        """
        self.donors = {}

    def add_donor(self, donor_id, name):
        """
        Add a donor to the tracker.

        Args:
            donor_id (int): Unique identifier for the donor.
            name (str): Name of the donor.

        Raises:
            ValueError: If a donor with the same ID already exists.
        """
        if donor_id in self.donors:
            raise ValueError("Donor with the same ID already exists")

        self.donors[donor_id] = Donor(donor_id, name)

    def get_donor(self, donor_id):
        """
        Get a donor by their ID.

        Args:
            donor_id (int): Unique identifier for the donor.

        Returns:
            Donor: Donor object if found, None otherwise.
        """
        return self.donors.get(donor_id)

    def track_donation(self, donor_id, donation_date, compensation):
        """
        Track a donation for a donor.

        Args:
            donor_id (int): Unique identifier for the donor.
            donation_date (str): Date of the donation in YYYY-MM-DD format.
            compensation (float): Compensation earned for the donation.

        Raises:
            ValueError: If the donor is not found.
        """
        donor = self.get_donor(donor_id)
        if donor is None:
            raise ValueError("Donor not found")

        donor.add_donation(donation_date, compensation)


def main():
    tracker = DonorTracker()

    while True:
        print("\n1. Add donor")
        print("2. Track donation")
        print("3. Get donor info")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            donor_id = int(input("Enter donor ID: "))
            name = input("Enter donor name: ")
            tracker.add_donor(donor_id, name)
        elif choice == "2":
            donor_id = int(input("Enter donor ID: "))
            donation_date = input("Enter donation date (YYYY-MM-DD): ")
            compensation = float(input("Enter compensation: "))
            tracker.track_donation(donor_id, donation_date, compensation)
        elif choice == "3":
            donor_id = int(input("Enter donor ID: "))
            donor = tracker.get_donor(donor_id)
            if donor:
                print(f"Donor Name: {donor.name}")
                print("Donations:")
                for donation in donor.get_donations():
                    print(f"Date: {donation['donation_date']}, Compensation: ${donation['compensation']:.2f}")
                print(f"Total Compensation: ${donor.get_total_compensation():.2f}")
            else:
                print("Donor not found")
        elif choice == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
