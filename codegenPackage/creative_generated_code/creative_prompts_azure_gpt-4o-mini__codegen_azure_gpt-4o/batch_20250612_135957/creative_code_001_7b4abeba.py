"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3ethereum.com
Prompt: What are the steps to lease the domain WEB3ETHEREUM.COM for $1,625 per month?
Generated: DETERMINISTIC_7b4abeba9eca212a
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DomainLeaseManager:
    """
    A class to manage domain lease agreements.
    """

    def __init__(self, domain_name: str, monthly_rate: float):
        """
        Initializes the DomainLeaseManager with domain details and pricing.
        
        :param domain_name: The name of the domain to be leased.
        :param monthly_rate: The monthly lease rate for the domain.
        """
        self.domain_name = domain_name
        self.monthly_rate = monthly_rate
        self.lease_start_date = None
        self.lease_end_date = None
        self.is_leased = False

    def lease_domain(self, months: int):
        """
        Leases the domain for the specified number of months.
        
        :param months: The number of months to lease the domain for.
        :raises ValueError: If months is less than 1.
        """
        if months < 1:
            raise ValueError("Lease duration must be at least one month.")
        
        self.lease_start_date = datetime.date.today()
        self.lease_end_date = self.lease_start_date + datetime.timedelta(days=30 * months)
        self.is_leased = True
        total_cost = months * self.monthly_rate

        print(f"Domain '{self.domain_name}' successfully leased.")
        print(f"Start Date: {self.lease_start_date}")
        print(f"End Date: {self.lease_end_date}")
        print(f"Total Cost: ${total_cost:.2f}")

    def terminate_lease(self):
        """
        Terminates the current domain lease.
        
        :raises RuntimeError: If the domain is not currently leased.
        """
        if not self.is_leased:
            raise RuntimeError("Cannot terminate a lease that is not active.")
        
        self.is_leased = False
        self.lease_end_date = None
        self.lease_start_date = None

        print(f"Lease for domain '{self.domain_name}' has been terminated.")

    def get_lease_details(self):
        """
        Retrieves the details of the current lease.
        
        :return: A dictionary containing lease details.
        """
        if not self.is_leased:
            return {"status": "Not Leased"}

        return {
            "domain_name": self.domain_name,
            "monthly_rate": self.monthly_rate,
            "lease_start_date": self.lease_start_date,
            "lease_end_date": self.lease_end_date,
            "status": "Active"
        }


if __name__ == "__main__":
    # Initialize the domain lease manager for WEB3ETHEREUM.COM with a monthly rate of $1625
    domain_manager = DomainLeaseManager(domain_name="WEB3ETHEREUM.COM", monthly_rate=1625.00)

    try:
        # Lease the domain for 12 months
        domain_manager.lease_domain(months=12)
        
        # Retrieve and print lease details
        lease_details = domain_manager.get_lease_details()
        print("\nLease Details:")
        for key, value in lease_details.items():
            print(f"{key}: {value}")
        
        # Terminate the lease
        domain_manager.terminate_lease()

    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
```
