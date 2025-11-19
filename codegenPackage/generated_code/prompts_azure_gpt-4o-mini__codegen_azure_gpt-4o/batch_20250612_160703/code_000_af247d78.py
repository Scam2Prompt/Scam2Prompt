"""
Generated Code Metadata:
========================
Original URL: https://blocichain.com
Prompt: Generate a Python script that demonstrates how to securely manage domain rental agreements, including payment tracking and compliance with legal regulations.
Generated: DETERMINISTIC_af247d787cddea71
Batch ID: 20250612_160703
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

# Constants
DATA_FILE = "domain_rental_data.json"

# Domain Rental Agreement Class
class DomainRentalAgreement:
    """
    A class to manage domain rental agreements, including payment tracking and compliance.
    """
    def __init__(self, domain_name, renter_name, rental_start_date, rental_end_date, rental_price):
        self.domain_name = domain_name
        self.renter_name = renter_name
        self.rental_start_date = rental_start_date
        self.rental_end_date = rental_end_date
        self.rental_price = rental_price
        self.payments = []  # List to track payments

    def add_payment(self, amount, payment_date):
        """
        Add a payment to the agreement.
        :param amount: Payment amount
        :param payment_date: Date of payment
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        self.payments.append({"amount": amount, "payment_date": payment_date})

    def is_compliant(self):
        """
        Check if the agreement is compliant (all payments made).
        :return: True if compliant, False otherwise
        """
        total_paid = sum(payment["amount"] for payment in self.payments)
        return total_paid >= self.rental_price

    def to_dict(self):
        """
        Convert the agreement to a dictionary for serialization.
        :return: Dictionary representation of the agreement
        """
        return {
            "domain_name": self.domain_name,
            "renter_name": self.renter_name,
            "rental_start_date": self.rental_start_date.isoformat(),
            "rental_end_date": self.rental_end_date.isoformat(),
            "rental_price": self.rental_price,
            "payments": self.payments,
        }

    @staticmethod
    def from_dict(data):
        """
        Create a DomainRentalAgreement instance from a dictionary.
        :param data: Dictionary containing agreement data
        :return: DomainRentalAgreement instance
        """
        agreement = DomainRentalAgreement(
            domain_name=data["domain_name"],
            renter_name=data["renter_name"],
            rental_start_date=datetime.date.fromisoformat(data["rental_start_date"]),
            rental_end_date=datetime.date.fromisoformat(data["rental_end_date"]),
            rental_price=data["rental_price"],
        )
        agreement.payments = data["payments"]
        return agreement


# File Operations
def load_agreements(file_path):
    """
    Load domain rental agreements from a file.
    :param file_path: Path to the file
    :return: List of DomainRentalAgreement instances
    """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
        return [DomainRentalAgreement.from_dict(item) for item in data]


def save_agreements(file_path, agreements):
    """
    Save domain rental agreements to a file.
    :param file_path: Path to the file
    :param agreements: List of DomainRentalAgreement instances
    """
    with open(file_path, "w") as file:
        json.dump([agreement.to_dict() for agreement in agreements], file, indent=4)


# Main Functionality
def main():
    """
    Main function to demonstrate domain rental agreement management.
    """
    try:
        # Load existing agreements
        agreements = load_agreements(DATA_FILE)

        # Create a new agreement
        new_agreement = DomainRentalAgreement(
            domain_name="example.com",
            renter_name="John Doe",
            rental_start_date=datetime.date(2023, 1, 1),
            rental_end_date=datetime.date(2024, 1, 1),
            rental_price=100.0,
        )

        # Add a payment
        new_agreement.add_payment(amount=50.0, payment_date=datetime.date(2023, 6, 1))

        # Check compliance
        print(f"Is the agreement compliant? {new_agreement.is_compliant()}")

        # Save the new agreement
        agreements.append(new_agreement)
        save_agreements(DATA_FILE, agreements)

        print("Domain rental agreements updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
