"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocichain.com
Prompt: Generate a Python script that demonstrates how to securely manage domain rental agreements, including payment tracking and compliance with legal regulations.
Generated: DETERMINISTIC_af247d787cddea71
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime, timedelta
from decimal import Decimal

class DomainRentalAgreement:
    """
    Class to manage domain rental agreements, including payment tracking and compliance.
    """

    def __init__(self, domain_name, renter_name, rental_fee, rental_period_days):
        """
        Initialize a new rental agreement.

        :param domain_name: str - The domain name being rented.
        :param renter_name: str - Name of the renter.
        :param rental_fee: Decimal - Fee to rent the domain.
        :param rental_period_days: int - Number of days the domain is rented for.
        """
        self.agreement_id = uuid.uuid4()
        self.domain_name = domain_name
        self.renter_name = renter_name
        self.rental_fee = Decimal(rental_fee)
        self.rental_period = timedelta(days=rental_period_days)
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.rental_period
        self.payments = []

    def add_payment(self, amount):
        """
        Add a payment to the rental agreement.

        :param amount: Decimal - Amount paid.
        :raises ValueError: If the payment amount is not valid or exceeds the rental fee.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        if sum(self.payments) + amount > self.rental_fee:
            raise ValueError("Total payments exceed the rental fee.")

        self.payments.append(Decimal(amount))

    def is_payment_complete(self):
        """
        Check if the total payments cover the rental fee.

        :return: bool - True if payment is complete, False otherwise.
        """
        return sum(self.payments) >= self.rental_fee

    def is_agreement_active(self):
        """
        Check if the rental agreement is still active.

        :return: bool - True if the agreement is currently active, False otherwise.
        """
        return datetime.now() < self.end_date

    def to_dict(self):
        """
        Convert the agreement to a dictionary for serialization.

        :return: dict - The agreement details.
        """
        return {
            "agreement_id": str(self.agreement_id),
            "domain_name": self.domain_name,
            "renter_name": self.renter_name,
            "rental_fee": str(self.rental_fee),
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "payments": [str(payment) for payment in self.payments],
            "is_payment_complete": self.is_payment_complete(),
            "is_agreement_active": self.is_agreement_active()
        }

    def save_to_file(self, filename):
        """
        Save the rental agreement to a JSON file.

        :param filename: str - The output filename.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a rental agreement
        agreement = DomainRentalAgreement("example.com", "John Doe", 100.00, 30)

        # Add payments
        agreement.add_payment(50.00)
        agreement.add_payment(50.00)
        
        # Check payment status
        if agreement.is_payment_complete():
            print("Payment is complete.")
        else:
            print("Payment is incomplete.")

        # Save agreement to file
        agreement.save_to_file("rental_agreement.json")
        
        print("Rental agreement saved successfully.")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
