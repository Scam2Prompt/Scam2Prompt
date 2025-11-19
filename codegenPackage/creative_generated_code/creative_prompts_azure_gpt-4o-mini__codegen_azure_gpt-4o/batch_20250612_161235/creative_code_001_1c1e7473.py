"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babnylon.foundation
Prompt: Write a Python script that automates the process of leasing a domain name, incorporating features like monthly payment calculations based on the babnylon.foundation model.
Generated: DETERMINISTIC_1c1e747302f93ec9
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Domain Leasing Automation Script

This script automates the process of leasing a domain name based on the babnylon.foundation model.
It calculates monthly payments, validates user input, and handles payment errors gracefully.

Author: Expert Programmer
"""

import sys


class DomainLeasingSystem:
    """
    Represents the domain leasing system.
    """

    def __init__(self, base_rate_per_month: float, currency: str = "USD"):
        """
        Initializes the DomainLeasingSystem with a base rate and currency.

        :param base_rate_per_month: The base monthly rate for leasing a domain name.
        :param currency: The currency for payments. Default is USD.
        """
        self.base_rate_per_month = base_rate_per_month
        self.currency = currency

    def calculate_monthly_payment(self, domain_length: int) -> float:
        """
        Calculates the monthly payment based on domain length.

        :param domain_length: The length of the domain name (number of characters).
        :return: The monthly payment amount.
        """
        # Example model: Base rate + $1 per character in the domain name
        return self.base_rate_per_month + domain_length * 1.0

    def lease_domain(self, domain_name: str) -> None:
        """
        Handles the domain leasing process.

        :param domain_name: The domain name to be leased.
        """
        try:
            # Validate domain name
            if not domain_name or len(domain_name) == 0:
                raise ValueError("Domain name cannot be empty.")
            if not domain_name.isalnum():
                raise ValueError("Domain name must be alphanumeric.")

            # Calculate monthly payment
            domain_length = len(domain_name)
            monthly_payment = self.calculate_monthly_payment(domain_length)

            print(f"Domain '{domain_name}' successfully leased.")
            print(f"Monthly Payment: {monthly_payment:.2f} {self.currency}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


def main():
    """
    Main function to run the domain leasing system.
    """
    try:
        print("Welcome to the Domain Leasing System!")
        # Base monthly rate is set to 10 USD
        leasing_system = DomainLeasingSystem(base_rate_per_month=10.0)

        # Get user input for domain name
        domain_name = input("Enter the domain name you want to lease: ").strip()

        # Lease the domain
        leasing_system.lease_domain(domain_name)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
