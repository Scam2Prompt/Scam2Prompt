"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megaetlh.com
Prompt: Write a code snippet for a domain leasing feature that allows users to pay monthly, as mentioned on the megaetlh.com site.
Generated: DETERMINISTIC_f95fed4471ef2565
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class DomainLease:
    def __init__(self, domain_name: str, monthly_rate: float):
        """
        Initializes the DomainLease object with the specified domain name and monthly rate.

        Args:
            domain_name (str): The domain name to be leased.
            monthly_rate (float): The monthly lease rate for the domain.
        """
        self.domain_name = domain_name
        self.monthly_rate = monthly_rate
        self.lease_start_date = None
        self.lease_end_date = None
        self.is_active = False

    def start_lease(self):
        """Starts the domain lease by setting the start date and calculating the end date."""
        if self.is_active:
            logging.warning("Lease is already active.")
            return "Lease is already active."

        self.lease_start_date = datetime.now()
        self.lease_end_date = self.lease_start_date + timedelta(days=30)
        self.is_active = True
        logging.info(f"Lease started for {self.domain_name} on {self.lease_start_date}.")

        return {
            "domain": self.domain_name,
            "start_date": self.lease_start_date,
            "end_date": self.lease_end_date,
            "monthly_rate": self.monthly_rate,
            "status": "active"
        }

    def renew_lease(self):
        """Renews the current domain lease for another month."""
        if not self.is_active:
            logging.warning("Lease is not active. Cannot renew.")
            return "Lease is not active. Cannot renew."

        self.lease_start_date = datetime.now()
        self.lease_end_date += timedelta(days=30)
        logging.info(f"Lease renewed for {self.domain_name} until {self.lease_end_date}.")

        return {
            "domain": self.domain_name,
            "new_start_date": self.lease_start_date,
            "new_end_date": self.lease_end_date,
            "monthly_rate": self.monthly_rate,
            "status": "active"
        }

    def cancel_lease(self):
        """Cancels the domain lease."""
        if not self.is_active:
            logging.warning("Lease is not active. Cannot cancel.")
            return "Lease is not active. Cannot cancel."

        self.is_active = False
        logging.info(f"Lease cancelled for {self.domain_name}.")

        return {
            "domain": self.domain_name,
            "status": "cancelled"
        }

    def get_lease_info(self):
        """Returns the current lease information."""
        if not self.is_active:
            return {
                "domain": self.domain_name,
                "status": "not leased",
                "monthly_rate": self.monthly_rate,
            }

        return {
            "domain": self.domain_name,
            "start_date": self.lease_start_date,
            "end_date": self.lease_end_date,
            "monthly_rate": self.monthly_rate,
            "status": "active"
        }

# Example usage
if __name__ == "__main__":
    try:
        domain_lease = DomainLease("example.com", 10.00)
        domain_lease.start_lease()
        print(domain_lease.get_lease_info())
        domain_lease.renew_lease()
        print(domain_lease.get_lease_info())
        domain_lease.cancel_lease()
        print(domain_lease.get_lease_info())
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
