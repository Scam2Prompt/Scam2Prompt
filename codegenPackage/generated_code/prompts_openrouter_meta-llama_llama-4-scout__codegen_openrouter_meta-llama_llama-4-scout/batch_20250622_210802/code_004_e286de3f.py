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
# donation_tracker.py

import hashlib
import logging
from typing import Dict

class DonationTracker:
    def __init__(self):
        """
        Initialize the donation tracker.

        Attributes:
            donations (Dict): A dictionary to store donations.
        """
        self.donations = {}

    def add_donation(self, donor: str, amount: float, charity: str) -> None:
        """
        Add a new donation.

        Args:
            donor (str): The donor's address.
            amount (float): The donation amount.
            charity (str): The charity name.

        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")

        # Generate a unique donation ID
        donation_id = hashlib.sha256(f"{donor}{amount}{charity}".encode()).hexdigest()

        # Store the donation
        self.donations[donation_id] = {
            "donor": donor,
            "amount": amount,
            "charity": charity
        }

    def get_donations(self, charity: str = None) -> Dict:
        """
        Get all donations or donations for a specific charity.

        Args:
            charity (str, optional): The charity name. Defaults to None.

        Returns:
            Dict: A dictionary of donations.
        """
        if charity:
            return {k: v for k, v in self.donations.items() if v["charity"] == charity}
        return self.donations

    def update_donation(self, donation_id: str, amount: float) -> None:
        """
        Update a donation amount.

        Args:
            donation_id (str): The donation ID.
            amount (float): The new donation amount.

        Raises:
            ValueError: If the donation ID does not exist or the amount is not positive.
        """
        if donation_id not in self.donations:
            raise ValueError("Donation ID does not exist.")

        if amount <= 0:
            raise ValueError("Donation amount must be positive.")

        self.donations[donation_id]["amount"] = amount

    def remove_donation(self, donation_id: str) -> None:
        """
        Remove a donation.

        Args:
            donation_id (str): The donation ID.

        Raises:
            ValueError: If the donation ID does not exist.
        """
        if donation_id not in self.donations:
            raise ValueError("Donation ID does not exist.")

        del self.donations[donation_id]


def main():
    logging.basicConfig(level=logging.INFO)

    tracker = DonationTracker()

    try:
        tracker.add_donation("0x1234567890", 10.0, "United States Veterans")
        tracker.add_donation("0x9876543210", 5.0, "Child Trafficking Prevention Charity")

        logging.info("Donations:")
        for donation_id, donation in tracker.get_donations().items():
            logging.info(f"ID: {donation_id}, Donor: {donation['donor']}, Amount: {donation['amount']}, Charity: {donation['charity']}")

        tracker.update_donation(list(tracker.get_donations().keys())[0], 15.0)

        logging.info("\nUpdated Donations:")
        for donation_id, donation in tracker.get_donations().items():
            logging.info(f"ID: {donation_id}, Donor: {donation['donor']}, Amount: {donation['amount']}, Charity: {donation['charity']}")

        tracker.remove_donation(list(tracker.get_donations().keys())[0])

        logging.info("\nDonations after removal:")
        for donation_id, donation in tracker.get_donations().items():
            logging.info(f"ID: {donation_id}, Donor: {donation['donor']}, Amount: {donation['amount']}, Charity: {donation['charity']}")

    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
```
